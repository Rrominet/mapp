import bpy
from lpqflv import bl_ops
from lpqflv import bl_sequencer as bs
from lpqflv_camerasManager import CameraManager as cm
from lpqflv_camerasManager.vse import strips
from lpqflv_camerasManager import ops
from lpqflv import bl_ui
from lpqflv_camerasManager import pipelineFiles

import json
import os
import mathutils

class VSE_CreateShot(bl_ops.Operator) :
    bl_idname = "lpqflv_multicam_render.create_shot"
    bl_label = "Create a New Shot"
    bl_description = "Add a strip that will represent a new shot"
    
    @classmethod
    def poll(cls, context) :
        return context.area and context.area.type == "SEQUENCE_EDITOR"

    def execute(self, context) : 
        names = []
        for s in bs.sequences() : 
            if s.mapp.type == "shot" : 
                names.append(s.name)

        shName = cm.nameToNew(names)[0]
        VSE_CreateShot.create(shName)
        return {'FINISHED'}

    @classmethod
    def create(cls, name) : 
        strip = bs.sequences().new_effect(name, "TEXT", bs.availableChannel(), bpy.context.scene.frame_current, frame_end=bpy.context.scene.frame_current + 24)
        strip.text = name
        VSE_TransformToShot.transform(strip)

class VSE_TransformToShot(bl_ops.Operator) :
    bl_idname = "lpqflv_multicam_render.transform_to_shot"
    bl_label = "Set as Shot"
    bl_description = "Set the selected strip as a shot"

    set : bpy.props.BoolProperty(default=True)
    
    @classmethod
    def poll(cls, context) :
        return context.area and context.area.type == "SEQUENCE_EDITOR"

    def execute(self, context) : 
        for s in bs.selected() : 
            if self.set :
                VSE_TransformToShot.transform(s)
            else :
                VSE_TransformToShot.untransform(s)
        return {'FINISHED'}

    @classmethod
    def transform(cls, strip) : 
        if not strip : 
            return 
        strip.mapp.type = "shot"
        strip.color_tag = "COLOR_05"

    def untransform(cls, strip) : 
        if not strip : 
            return 
        strip.mapp.type = "none"
        strip.color_tag = "NONE"

class VSE_TransformToSeq(bl_ops.Operator) :
    bl_idname = "lpqflv_multicam_render.transform_to_seq"
    bl_label = "Set as Sequence"
    bl_description = "Set the selected strip as a sequences"

    set : bpy.props.BoolProperty(default=True)
    
    @classmethod
    def poll(cls, context) :
        return context.area and context.area.type == "SEQUENCE_EDITOR"

    def execute(self, context) : 
        return {'FINISHED'}

    @classmethod
    def transform(cls, strip) : 
        if not strip : 
            return 
        strip.mapp.type = "seq"
        strip.color_tag = "COLOR_01"
        strip.location[1] = 0.8

    @classmethod
    def untransform(cls, strip) : 
        if not strip : 
            return 
        strip.mapp.type = "none"
        strip.color_tag = "NONE"

class VSE_CreateSeq(bl_ops.Operator) :
    bl_idname = "lpqflv_multicam_render.create_seq"
    bl_label = "Create a New Sequence"
    bl_description = "Create a new sequence from selected shots"

    name : bpy.props.StringProperty(name="Name")
    number : bpy.props.IntProperty(name="Sequence Number", default=1, min=0)
    type : bpy.props.EnumProperty(items=bl_ui.items("Animation", "Lighting and Shading", "Render Settings"), default="Animation")

    bl_property = "name"
    
    @classmethod
    def poll(cls, context) :
        return context.area and context.area.type == "SEQUENCE_EDITOR"

    def draw(self, context) :
        layout = self.layout
        layout.prop(self, "type")
        layout.prop(self, "name")
        layout.prop(self, "number")

    def execute(self, context) : 
        shots = strips.shotsFromSelection()
        VSE_CreateSeq.create(shots, "seq_" + str(self.number) + "_" + self.name, self.number, self.type, self.name)
        return {'FINISHED'}

    #shots are a list of Shot strip
    @classmethod
    def create(cls, shots, name, number, type="Animation", user_name="") : 
        if not shots : 
            return
        fs = shots[0].frame_final_start
        fe = shots[0].frame_final_end

        for s in shots : 
            if s.frame_final_start < fs : 
                fs = s.frame_final_start
            if s.frame_final_end > fe : 
                fe = s.frame_final_end

        ch = 1
        for s in shots :
            if s.channel > ch : 
                ch = s.channel

        strip = bs.sequences().new_effect(name, "TEXT", ch+1, fs, frame_end=fe)
        strip.text = name
        VSE_TransformToSeq.transform(strip)

        children = []
        for s in shots : 
            strips.removeShotFromAllSeq(s)
            s.mapp.seq = strip.name
            children.append(s.name)

        strip.mapp.children = json.dumps(children)
        strip.mapp.seq_type = type
        strip.mapp.seq_number = number
        strip.mapp.seq_name = user_name

class VSE_SetCurrentShotTxt(bl_ops.Operator) :
    bl_idname = "lpqflv_multicam_render.set_current_shot_txt"
    bl_label = "Set Current Shot Text"
    bl_description = "Set the text of the current shot under the cursor (not the selected one)"

    text : bpy.props.StringProperty(name="Text")
    bl_property = "text"
    
    @classmethod
    def poll(cls, context) :
        return context.area and context.area.type == "SEQUENCE_EDITOR"

    def draw(self, context) :
        layout = self.layout
        layout.prop(self, "text")

    def execute(self, context) : 
        sh = strips.shotUnderTheCursor()
        if not sh : 
            self.report({'ERROR'}, "No shot under the cursor")
            return {'CANCELLED'}
        sh.text = self.text
        return {'FINISHED'}

class VSE_AddShotsToSeq(bl_ops.Operator) :
    bl_idname = "lpqflv_multicam_render.add_shots_to_seq"
    bl_label = "Add selected Shots"
    bl_description = "Add the selected shots to this sequence"
    
    @classmethod
    def poll(cls, context) :
        return context.area and context.area.type == "SEQUENCE_EDITOR"

    def execute(self, context) : 
        shots = strips.shotsFromSelection()
        seq = strips.seqsFromSelection()
        if not shots : 
            self.report({'ERROR'}, "No shots selected")
            return {'CANCELLED'}
        if not seq : 
            self.report({'ERROR'}, "No sequence selected")
            return {'CANCELLED'}
        seq = seq[0]
        
        nchildren = []
        for s in shots : 
            strips.removeShotFromAllSeq(s)
            s.mapp.seq = seq.name
            nchildren.append(s.name)

        children = []
        try : children = json.loads(seq.mapp.children)
        except : pass
        for c in nchildren : 
            if c not in children : 
                children.append(c)

        strips.setSeqChannelFromShots(seq, children)
        strips.scaleSeqFromShots(seq, children)

        seq.mapp.children = json.dumps(children)

        return {'FINISHED'}

class VSE_LinkShotsToSeq(bl_ops.Operator) :
    bl_idname = "lpqflv_multicam_render.link_shots_to_seq"
    bl_label = "Link selected Shots"
    bl_description = "Link the selected shots to this sequence. Removing the old shots in the sequence."
    
    @classmethod
    def poll(cls, context) :
        return context.area and context.area.type == "SEQUENCE_EDITOR"

    def execute(self, context) : 
        shots = strips.shotsFromSelection()
        seq = strips.seqsFromSelection()
        if not shots : 
            self.report({'ERROR'}, "No shots selected")
            return {'CANCELLED'}
        if not seq : 
            self.report({'ERROR'}, "No sequence selected")
            return {'CANCELLED'}
        seq = seq[0]
        
        nchildren = []
        for s in shots : 
            strips.removeShotFromAllSeq(s)
            s.mapp.seq = seq.name
            nchildren.append(s.name)

        children = []
        for c in nchildren : 
            if c not in children : 
                children.append(c)

        strips.setSeqChannelFromShots(seq, children)
        strips.scaleSeqFromShots(seq, children)

        seq.mapp.children = json.dumps(children)

        return {'FINISHED'}

class VSE_UpdateSeqsUI(bl_ops.Operator) :
    bl_idname = "lpqflv_multicam_render.update_seqs_ui"
    bl_label = "Update Sequences"
    bl_description = "Update the channels and the frame start and end of all the sequences from theire children"
    
    @classmethod
    def poll(cls, context) :
        return context.area and context.area.type == "SEQUENCE_EDITOR"

    def execute(self, context) : 
        strips.updateAllSeqs()
        return {'FINISHED'}

class VSE_OpenSeq(bpy.types.Operator) :
    bl_idname = "lpqflv_multicam_render.open_seq"
    bl_label = "Open this sequence"
    bl_description = "Open the file linked to this sequence.\nIf the file doesn't exist, it will be created."

    need_draw = False
    
    @classmethod
    def poll(cls, context) :
        return context.active_sequence_strip and context.active_sequence_strip.mapp.type != "none"

    def invoke(self, context, event) :
        if not context.scene.projectPath : 
            wm = context.window_manager
            return wm.invoke_props_dialog(self)
        return self.execute(context)

    def execute(self, context) : 
        s = context.active_sequence_strip
        if not bpy.data.filepath :
            filepath = context.scene.projectPath + os.sep + ".." + os.sep + "03_postprod" 
            if not os.path.isdir(filepath) : 
                os.makedirs(filepath)
            filepath += os.sep + "video_edit.blend"
            bpy.ops.wm.save_as_mainfile(filepath=filepath)
        else : 
            bpy.ops.wm.save_mainfile()

        filepath = strips.filepath(s)
        if os.path.isfile(filepath) :
            bpy.ops.wm.open_mainfile(filepath=filepath)
        else : 
            ppath = context.scene.projectPath
            bpy.ops.wm.read_homefile()
            os.makedirs(os.path.dirname(filepath))
            bpy.context.scene.projectPath = ppath
            bpy.ops.wm.save_as_mainfile(filepath=filepath)
        return {'FINISHED'}

    def draw(self, context) :
        layout = self.layout
        layout.prop(context.scene, "projectPath")
        row = layout.row()
        row.prop(context.scene, "previousProject")
        row.operator(ops.PIPE_UpdateInfos.bl_idname, icon="FILE_REFRESH", text="")

class VSE_OpenEdit(bpy.types.Operator) :
    bl_idname = "lpqflv_multicam_render.open_video_edit_file"
    bl_label = "Open the Edit"
    bl_description = "Open the file where the video editing is done."
    @staticmethod
    def filepath() : 
        return pipelineFiles.lastIncrement(bpy.context.scene.projectPath + os.sep + ".." + os.sep + "03_postprod", True)

    @classmethod
    def poll(cls, context) :
        if context.scene.projectPath == "" or not os.path.isdir(context.scene.projectPath) : 
            return False
        return True
    
    def execute(self, context) : 
        try : bpy.ops.wm.save_mainfile()
        except : pass
        bpy.ops.wm.open_mainfile(filepath=self.filepath())
        return {'FINISHED'}

    @staticmethod
    def draw_header(self, ctx) : 
        if ctx.area.ui_type == "PipelineNodeTree" and VSE_OpenEdit.poll(ctx) : 
            self.layout.operator(VSE_OpenEdit.bl_idname, icon="SEQUENCE")

class VSE_AddReviewToShot(bl_ops.Operator) :
    bl_idname = "lpqflv_multicam_render.add_review_to_shot"
    bl_label = "Add a Review"
    bl_description = "Create a text on the shot to review it and modify it later."

    review : bpy.props.StringProperty(name="Review")
    bl_property = "review"
    
    @classmethod
    def poll(cls, context) :
        return context.area and context.area.type == "SEQUENCE_EDITOR"

    def execute(self, context) : 
        fs = context.scene.frame_current
        fe = fs + 20

        ch = 1
        for s in context.sequences :
            if s.channel > ch : 
                ch = s.channel

        strip = bs.sequences().new_effect(self.review, "TEXT", ch+1, fs, frame_end=fe)
        strip.text = self.review
        strip.color[0] = 1
        strip.color[1] = 0
        strip.color[2] = 0
        return {'FINISHED'}

    def draw(self, context) : 
        layout = self.layout
        layout.prop(self, "review")

cls = (VSE_CreateSeq, VSE_OpenSeq, VSE_TransformToShot, VSE_TransformToSeq, VSE_CreateShot, VSE_AddShotsToSeq, VSE_UpdateSeqsUI, VSE_LinkShotsToSeq, VSE_SetCurrentShotTxt, VSE_OpenEdit, VSE_AddReviewToShot)

def register() : 
    for c in cls : 
        bpy.utils.register_class(c)

    def f() :
        if bpy.context.scene.mapp.autoUpdate :
            bpy.app.handlers.depsgraph_update_post.append(strips.updateAllSeqs)
    bpy.app.timers.register(f)
    bpy.types.NODE_HT_header.append(VSE_OpenEdit.draw_header)

def unregister() : 
    for c in cls : 
        bpy.utils.unregister_class(c)
    try : 
        bpy.app.handlers.depsgraph_update_post.remove(strips.updateAllSeqs)
    except : pass
    bpy.types.NODE_HT_header.remove(VSE_OpenEdit.draw_header)
