# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import sys
import os

from lpqflv_camerasManager import prefs as prefsm
from lpqflv_camerasManager import menus 
from lpqflv_camerasManager import config as cfg
from lpqflv import bl_utils 
from lpqflv import log
from lpqflv import bl_ops
from lpqflv_camerasManager import Pipeline as p 
from lpqflv_camerasManager import PipelineNodeTree as pnt 
from lpqflv_camerasManager.nodes import SceneNode as sn 
from lpqflv_camerasManager import pipelineFiles
from lpqflv_camerasManager import panels
from lpqflv_camerasManager import pipelineRead
from lpqflv_camerasManager import multiCamRender as mcr
from lpqflv_camerasManager import CameraManager as cm
from lpqflv import fileTools as ft
from lpqflv import bl_anim
from lpqflv import bl_ui

    
import bpy

class MkActiveCamera (bpy.types.Operator) : 
    """Make this Camera the active One"""
    
    bl_idname = "lpqflv_camera_manager.mk_active_camera"
    bl_label = "Active strip as active Camera"
    
    cameraName : bpy.props.StringProperty()
    
    def execute(self, context) : 
        context.scene.camera = bpy.data.objects[self.cameraName]
        return {'FINISHED'}
        
class SelectCamera (bpy.types.Operator) : 
    """Select the Camera"""
    
    bl_idname = "lpqflv_camera_manager.select_camera"
    bl_label = ""
    
    cameraName : bpy.props.StringProperty()
    
    def execute(self, context) : 
        context.scene.objects[self.cameraName].select_set(True)
        bpy.context.view_layer.objects.active = context.scene.objects[self.cameraName]
        
        return {'FINISHED'}

class CameraFramesAsRange (bpy.types.Operator) : 
    bl_idname = "lpqflv_camera_manager.frames_as_range"
    bl_label = ""
    bl_description = "Set the timeline range of this scene from this camera"
    
    cameraName : bpy.props.StringProperty()
    index : bpy.props.IntProperty(default=0)
    
    def execute(self, context) : 
        cam = bpy.data.objects[self.cameraName]
        context.scene.frame_preview_start = cam.data.cm.startEnds[self.index].start
        context.scene.frame_preview_end = cam.data.cm.startEnds[self.index].end 
        context.scene.use_preview_range = True
        return {'FINISHED'}

class SelectAllCameras (bpy.types.Operator) : 
    """Select all cameras"""

    bl_idname = "lpqflv_camera_manager.select_all_cameras"
    bl_label = "Select All"
    
    def execute(self, context) : 
        for o in context.scene.objects : 
            o.select_set(False)

        for o in context.scene.objects : 
            if o.type == "CAMERA" : 
                o.select_set(True)
        
        return {'FINISHED'}

class CameraRangeFromKeyframes (bpy.types.Operator) : 
    bl_idname = "lpqflv_cameras_manager.set_range_from_keyframes"
    bl_label = "Set Frame Range"

    bl_description = "Set actie camera frame range from selected keyframes"

    @classmethod
    def poll(cls, ctx) : 
        c = ctx.object
        if not c : 
            return False
        if not c.type == "CAMERA" : 
            return False
        if not c.animation_data : 
            return False

        action = c.animation_data.action
        if not action : 
            return False
        return True

    def execute (self, ctx) : 
        keyframes = bl_anim.selectedKeyframes(ctx.object)
        start = 1000000000000
        end = -1000000000000

        for k in keyframes : 
            if k.co[0]< start : 
                start = k.co[0]
            if k.co[0]> end : 
                end = k.co[0]

        ctx.object.data.cm.startEnds[0].start = int(start)
        ctx.object.data.cm.startEnds[0].end = int(end)
        return {'FINISHED'}

        
class DOFSetUp (bpy.types.Operator) : 
    """ Create a DOF set up for your selected camera
Select the target object AND NEXT your camera."""
    
    bl_idname = "lpqflv_pipeline.dof_camera"
    bl_label = "DOF Set Up"
    
    def execute(self, context) : 
        camera = context.object
        centerObject = ""
        for obj in context.selected_objects : 
            if obj.type != "CAMERA" : 
                centerObject = obj
        
        if camera.type == "CAMERA" : 
            if centerObject.type != "CAMERA" : 
                bpy.ops.object.empty_add(location=(centerObject.location[0], centerObject.location[1], centerObject.location[2]))
                empty = context.object
                bpy.ops.mesh.primitive_plane_add(location=(0,0,0))
                plane = context.object
                plane.parent = empty
                empty.rotation_euler = camera.rotation_euler
                empty.parent = camera
                empty.matrix_parent_inverse = camera.matrix_world.inverted()
                camera.data.dof.focus_object = plane
                plane.hide_render = True
                
                plane.lock_location[0] = True 
                plane.lock_location[1] = True
                
                plane.cycles_visibility.camera = False
                plane.cycles_visibility.diffuse = False
                plane.cycles_visibility.glossy = False
                plane.cycles_visibility.transmission = False
                plane.cycles_visibility.scatter = False
                plane.cycles_visibility.shadow = False

        return {'FINISHED'}
    
class CameraPresetOperator(bpy.types.Operator) :
    """Create camera with default attributes values"""

    bl_idname = "lpqflv.create_camera"
    bl_label = "Camera"

    lens : bpy.props.FloatProperty(name="Focal Length")
    
    def execute(self, context) : 
        self.addCamera(context)
        self.cam.data.lens = self.lens

        return {'FINISHED'}

    @staticmethod
    def drawMenu (self, context) : 
        l = self.layout
        l.separator() 
        r = l.row() 
        r.menu(menus.CamerasMenu.bl_idname, text="Cameras", icon="OUTLINER_OB_CAMERA")

    def createCamsCollection(self) :
        col = None
        if not "cameras" in bpy.data.collections : 
            col = bpy.data.collections.new("cameras")
        else : 
            col = bpy.data.collections["cameras"]
        try :
            bpy.context.scene.collection.children.link(col)
        except : 
            pass

        return col

    def addCamera(self, ctx) : 
        cname, last = cm.nameToNew()
        bpy.ops.object.camera_add() 
        self.cam = ctx.view_layer.objects.active
        self.cam.name = cname

        self.cam.rotation_euler[2] = 1.5708
        self.cam.rotation_euler[0] = 1.5708

        prefs = ctx.preferences.addons[prefsm.Prefs.bl_idname].preferences

        self.cam.data.passepartout_alpha = prefs.defaultCameraAlpha
        self.cam.data.clip_start = prefs.defaultClipStart
        self.cam.data.clip_end = prefs.defaultClipEnd
        self.cam.data.cm.startEnds.add()

        if last != "" : 
            try : 
                self.cam.data.cm.startEnds[0].start = bpy.data.objects[last].data.cm.startEnds[0].end + 1
                self.cam.data.cm.startEnds[0].end = self.cam.data.cm.startEnds[0].start + 100
            except : pass

        col = self.createCamsCollection()
        for c in self.cam.users_collection : 
            c.objects.unlink(self.cam)
        col.objects.link(self.cam)

class LinkCamsAndSeqs(bpy.types.Operator) : 
    bl_idname = "lpqfl.modal_camera_events_handler"
    bl_label = "Modal Camera Event Handler"
    
    @classmethod
    def poll(cls, context) : 
        return True 
    
    def __init__ (self) : 
        cfg.CM.running = True
        print("Camera Manager - Modal Event Handler : Started.")
        
    def __del__(self) : 
        cfg.CM.running = False
    
    def modal(self, context, e) : 
        if not cfg.CM.running : 
            print("Camera Manager - Modal Event Handler : Stopped.")
            return {'CANCELLED'}
        area = bl_utils.focusedArea(e)
        
        #Link selection 
        cfg.CM.linkSelections(area.type)
        
        if area.type == "VIEW_3D" : 
            cfg.CM.updateFrom3DView()
            
        elif area.type == "SEQUENCE_EDITOR" : 
            cfg.CM.updateFromSequencer()
        
        return {'PASS_THROUGH'}
        
    def invoke(self, context, e) : 
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
    
#Start or stop manually the camera and strips link handler
class StartStopCameraHandler(bpy.types.Operator) :
    bl_description = "Manage the Modal operator used for handle the cameras and the strips link.\nDon't touh unless you know how work modal operators in Blender"

    bl_idname = "pqflv.start_stop_camera_handler"
    bl_label = "Manage cameras and strip link handler"
    
    def invoke(self, context, event) : 
        if cfg.CM.running : 
            cfg.CM.running = False
        else : 
            cfg.CM.updateFrom3DView()
            bpy.ops.lpqfl.modal_camera_events_handler('INVOKE_DEFAULT')

        return {'FINISHED'}

class PIPE_CreatePipeline(bpy.types.Operator) : 
    bl_description = "Get the existing Pipeline as nodes"

    bl_idname = "pqflv_pipeline.create_pipeline"
    bl_label = "Get Pipeline"
    
    def execute(self, context) : 
        cfg.PipelineTree = pnt.PipelineNodeTree.create()
        try : 
            context.area.spaces[0].node_tree = cfg.PipelineTree
            bpy.ops.pqflv_pipeline.update_pipeline_nodes('INVOKE_DEFAULT')
        except : pass
        return {'FINISHED'}
    
    @staticmethod
    def draw(self, context) : 
        if context.area.ui_type == "PipelineNodeTree" : 
            self.layout.operator(PIPE_CreatePipeline.bl_idname, icon="WINDOW")

class PIPE_OpenScene(bpy.types.Operator) : 
    bl_description = "Open this scene"

    bl_idname = "pqflv_pipeline.open_scene"
    bl_label = "Open"
    
    nodeName : bpy.props.StringProperty()
    filepath : bpy.props.StringProperty(default="")
    
    def execute(self, context) : 
        if self.filepath != "" : 
            dir = ft.folder(self.filepath) 
            bpy.ops.wm.save_mainfile('INVOKE_DEFAULT')
            bpy.ops.wm.open_mainfile(filepath = pipelineFiles.lastIncrement(dir, True))
            return {'FINISHED'}
        
        tree = pnt.PipelineNodeTree.get()
        node = tree.nodes[self.nodeName]
        
        node.open()
        
        return {'FINISHED'}
    
class PIPE_ExportAsAbc(bpy.types.Operator) : 
    bl_description = "Export selected objects as alembic format."

    bl_idname = "pqflv_pipeline.export_abc"
    bl_label = "Export to Alembic"
    
    nodeName : bpy.props.StringProperty()
    
    def execute(self, context) : 
        tree = pnt.PipelineNodeTree.get()
        node = tree.nodes[self.nodeName]
        node.exportAsAbc() 
        return {'FINISHED'}
 
    
class PIPE_GenerateScene(bpy.types.Operator) : 
    bl_description = "Generate the files for this scene"

    bl_idname = "pqflv_pipeline.generate_scene"
    bl_label = "Generate"

    GENERATE = 0
    COPY = 1
    
    nodeName : bpy.props.StringProperty()
    
    def execute(self, context) : 
        tree = pnt.PipelineNodeTree.get()
        node = tree.nodes[self.nodeName]
        
        node.generate()
        
        return {'FINISHED'}


class PIPE_PanelShowDirContent(bpy.types.Operator) : 
    bl_description = "Open this scene"

    bl_idname = "pqflv_pipeline.show_panel_dir_content"
    bl_label = "Show"
    
    path : bpy.props.StringProperty(default="")
    
    def execute(self, context) : 
        dir = panels.PanelDir.getByPath(self.path)
        dir.closed = not dir.closed
        return {'FINISHED'}


class PIPE_Link(bpy.types.Operator) : 
    bl_description = "Link a file to a scene"

    bl_idname = "pqflv_pipeline.link"
    bl_label = "Link"
    
    newScene: bpy.props.BoolProperty(name="Create a new Scene", description="Create a new scene in the file with the data linked")
    
    showCollections : bpy.props.BoolProperty()
    showObjects     : bpy.props.BoolProperty()
    showScenes      : bpy.props.BoolProperty()
    showWorlds      : bpy.props.BoolProperty()
    showActions     : bpy.props.BoolProperty()
    showCameras     : bpy.props.BoolProperty()
    showMeshes      : bpy.props.BoolProperty()
    showLights      : bpy.props.BoolProperty()
    showMovies      : bpy.props.BoolProperty()
    showMaterials   : bpy.props.BoolProperty()
    showTextures    : bpy.props.BoolProperty()
    showData        : bpy.props.BoolProperty()
    
    fromNodeName : bpy.props.StringProperty()
    toNodeName : bpy.props.StringProperty()
    
    libPaths = []
    
    elmts = {}
    pipe = None
    node = None
    toNode = None
    lastLink = None
    fromNodeSocketUsed = None
    reroutes = []
    
    types = ("collections", 
             "objects",
             "meshes",
             "scenes",
             "worlds",
             "materials", 
             "lights", 
             "cameras",
             "textures", 
             "actions", 
             "movies", 
             "data")
    
    linkCollectionToNewScene : bpy.props.BoolProperty(name="New Scene", description="Create a new scene for the linked collections. If not, the collections will be linked in the active scene.", default=False)
    
    linkObjectToNewScene : bpy.props.BoolProperty(name="New Scene", description="Create a new scene for the linked Objects. If not, the objetcs will be linked in the active collection.", default=False)
    
    @classmethod
    def poll(cls, context) : 
        if (context.area.ui_type == "PipelineNodeTree" and 
            os.path.exists(context.scene.projectPath)
            and len(bpy.data.node_groups)>0) : 
                return True

    def isSmartLink(self, socket) : 
        return False

    def execute(self, context):
        if self.node.bl_idname == "AlembicNode" : 
            self.toNode.importAbc(self.node.absPath())
            return {"FINISHED"}
        
        self.toNode.updating = True
        self.lastLink = self.pipe.links[-1]
        self.fromNodeSocketUsed = self.lastLink.from_socket
        for s in self.toNode.linkedInSocket() : 
            if s.links and self.lastLink == s.links[0] : 
                self.lastLink = None
                self.toNode.inputs.remove(s)
                break
        
        for t in self.types : 
            for e in getattr(self.node.sceneElmts, t) : 
                if e.selected : 
                    self.createLinkSocket(t)
                    break

        if self.isSmartLink(self.fromNodeSocketUsed) : 
            self.createSmartLinkScene()

        self.toNode.updating = False
        name = self.toNode.name
        self.toNode = None
        self.fromNodeSocketUsed = None
        self.elmts = self.node.sceneElmts
        self.node_prefix = self.node.prefix()
        self.node = None
        self.pipe = None

        bpy.ops.pqflv_pipeline.open_scene(nodeName=name)
        # forbidden to use object variable

        for p in self.libPaths : 
            self.linkFromLib(p)

        return {'FINISHED'}

    def linkFromLib (self, path) : 
        isCollection = False 
        isObjects = False
        
        with bpy.data.libraries.load(path, link=True) as (data_from, data_to):
            for t in self.types :
                for elmt in getattr(self.elmts, t) : 
                    if elmt.selected : 
                        getattr(data_to, elmt.type).append(elmt.name)
                        if elmt.type == "collections" : 
                            isCollection = True
                        elif elmt.type == "objects" : 
                            isObjects = True
                        
        sc = None
        if self.linkCollectionToNewScene or self.linkObjectToNewScene : 
            scenes = bpy.data.scenes
            if scenes.find(self.fromNodeName) != -1 : 
                sc = scenes[self.fromNodeName]
            else : 
                sc = scenes.new(self.fromNodeName)
        else : 
            sc = bpy.context.scene
        
        if isCollection : 
            for col in data_to.collections : 
                try : 
                    bl_utils.newCollectionInstanceToScene(col, sc, self.node_prefix, True)
                except : pass
        
        if isObjects : 
            for o in data_to.objects : 
                try : 
                    sc.collection.objects.link(o)
                except : pass

    #create the smartlink scene and update self.libPath
    def createSmartLinkScene(self) : 
        self.node.createSmartLinkFile()
        self.libPaths = [self.node.smartLinks()[-1]]
    
    def createLinkSocket(self, type) : 
        linkSocket = self.toNode.inputs.new("LinkSocket", type)
        linkSocket.dataType = type[:-1]
        output = None
        if self.isSmartLink(self.fromNodeSocketUsed) : 
            output = self.node.outputs[1]
        else :
            output = self.node.outputs[0]
        if not self.reroutes : 
            self.pipe.links.new(output, linkSocket)
        else : 
            for i in range(len( self.reroutes)) :
                if i == 0 : 
                    self.pipe.links.new(self.reroutes[i].outputs[0], linkSocket)
                elif i < len(self.reroutes) - 1 : 
                    self.pipe.links.new(self.reroutes[i+1].outputs[0], self.reroutes[i].inputs[0])
                elif i == len(self.reroutes) - 1 : 
                    self.pipe.links.new(output, self.reroutes[i].inputs[0])
                
        return linkSocket
    
    def invoke(self, context, event) : 
        self.pipe = pnt.PipelineNodeTree.get()
        self.node = self.pipe.nodes[self.fromNodeName]
        self.reroutes = []
        while self.node.type == "REROUTE" : 
            self.reroutes.append(self.node)
            self.node = self.node.inputs[0].links[0].from_node
        self.toNode = self.pipe.nodes[self.toNodeName]
        
        if self.node.bl_idname == "AlembicNode" : 
            return self.execute(context)
         
        if not self.node.getMaster() : 
            self.node.createMaster()

        self.libPaths = [self.node.getMasterPath()]
        self.elmts = self.node.sceneContent()
        if not self.elmts : 
            return {"CANCELLED"}
        
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    
    def draw(self, context):
        layout = self.layout
        r = layout.row() 
        r.label(text="Link scene content from file : ")
        r = layout.row() 
        r.label(text=self.node.content, icon="BLENDER")
        self.drawSubType("collections", layout, "OUTLINER_OB_GROUP_INSTANCE")
        self.drawSubType("objects", layout, "MESH_CUBE")
        self.drawSubType("meshes", layout, "MESH_DATA")
        self.drawSubType("materials", layout, "MATERIAL_DATA")
        self.drawSubType("lights", layout, "LIGHT")
        self.drawSubType("cameras", layout, "CAMERA_DATA")
        self.drawSubType("scenes", layout, "SCENE_DATA")
        self.drawSubType("worlds", layout, "WORLD")
        self.drawSubType("textures", layout, "TEXTURE")
        self.drawSubType("actions", layout, "DECORATE_KEYFRAME")
        self.drawSubType("movies", layout, "FILE_MOVIE")
        self.drawSubType("data", layout, "PRESET")
        
    def drawSubType(self, elmtType, layout, icon="NONE") : 
        box = layout.box()
        propName = "show" + elmtType.capitalize()
        r = box.row(align=True)
        r.prop(self, propName, text="", icon=icon)
        selAll = r.operator(PIPE_SelectFileElmts.bl_idname, text="", icon="RESTRICT_SELECT_OFF")
        selAll.nodeName = self.node.name
        selAll.elmtType = elmtType
        deselAll = r.operator(PIPE_DeselectFileElmts.bl_idname, text="", icon="RESTRICT_SELECT_ON")
        deselAll.nodeName = self.node.name
        deselAll.elmtType = elmtType
        if elmtType == "collections" : 
            r.prop(self, "linkCollectionToNewScene", icon="SCENE_DATA")
        elif elmtType == "objects" : 
            r.prop(self, "linkObjectToNewScene", icon="SCENE_DATA") 
        c = box.column(align=True)
        if  getattr(self, propName) : 
            for e in getattr(self.elmts, elmtType) : 
                self.drawElmt(e, c)
    
   
    def drawElmt(self, elmt, layout, textToAdd="") : 
        if elmt.selected : 
            ope = layout.operator(PIPE_SelectFileElmt.bl_idname, text= textToAdd + elmt.name, icon="RESTRICT_SELECT_OFF")
        else : 
            ope = layout.operator(PIPE_SelectFileElmt.bl_idname, text= textToAdd + elmt.name, emboss=False)
        ope.elmtName = elmt.name 
        ope.elmtType = elmt.type
        ope.nodeName = self.node.name
        

class PIPE_SelectFileElmt(bpy.types.Operator) : 
    bl_description = "Select this element to link"

    bl_idname = "pqflv_pipeline.select_pipeline_file_elmt"
    bl_label = "Select"
    
    elmtName : bpy.props.StringProperty() 
    elmtType : bpy.props.StringProperty()
    nodeName : bpy.props.StringProperty()
        
    def invoke(self, context, event) : 
        pipe = pnt.PipelineNodeTree.get() 
        node = pipe.nodes[self.nodeName] 
        
        elmt = node.sceneElmts.find(self.elmtName, self.elmtType)
        elmt.selected = not elmt.selected
        
        return {'FINISHED'}


class PIPE_SelectFileElmts(bpy.types.Operator) : 
    bl_description = "Select all emts in this section"

    bl_idname = "pqflv_pipeline.select_pipeline_file_elmts"
    bl_label = "Select All"
    
    elmtType : bpy.props.StringProperty()
    nodeName : bpy.props.StringProperty()
        
    def invoke(self, context, event) : 
        pipe = pnt.PipelineNodeTree.get() 
        node = pipe.nodes[self.nodeName] 
        
        for e in node.sceneElmts.getByType(self.elmtType) : 
            e.selected = True
        
        return {'FINISHED'}


class PIPE_DeselectFileElmts(bpy.types.Operator) : 
    bl_description = "Deselect all emts in this section"

    bl_idname = "pqflv_pipeline.deselect_pipeline_file_elmts"
    bl_label = "Deselect All"
    
    elmtType : bpy.props.StringProperty()
    nodeName : bpy.props.StringProperty()
        
    def invoke(self, context, event) : 
        pipe = pnt.PipelineNodeTree.get() 
        node = pipe.nodes[self.nodeName] 
        
        for e in node.sceneElmts.getByType(self.elmtType) : 
            e.selected = False
        
        return {'FINISHED'}
    
class PIPE_ReadPipeline(bpy.types.Operator) : 
    bl_description = "Update pipeline nodes from your project files"

    bl_idname = "pqflv_pipeline.update_pipeline_nodes"
    bl_label = "Update Pipeline nodes"
    
    @classmethod
    def poll(cls, context) : 
        if (os.path.exists(context.scene.projectPath)
            and len(bpy.data.node_groups)>0) : 
                return True
    
    def invoke(self, context, event) : 
        scenes = pipelineRead.scenesFromFiles() 
        pipe = pnt.PipelineNodeTree.get() 
        pipe.read(scenes)
        pipe.setDefaultPos(True)
        return {'FINISHED'}
    
    
class PIPE_ArrangeNodes(bpy.types.Operator) : 
    bl_description = "Re-arrange your nodes in the Pipelines"

    bl_idname = "pqflv_pipeline.arrange_pipeline_nodes"
    bl_label = "Arrange nodes"
    
    @classmethod
    def poll(cls, context) : 
        if (context.area.ui_type == "PipelineNodeTree" and 
            os.path.exists(context.scene.projectPath)
            and len(bpy.data.node_groups)>0) : 
                return True
    
    def invoke(self, context, event) : 
        pipe = pnt.PipelineNodeTree.get()
        pipe.updateInternalMemory()
        pipe.setDefaultPos()
        return {'FINISHED'}
    

class PIPE_SaveIncrement(bpy.types.Operator):
    """Save one increment of your scene"""
    bl_idname = "lpqflv_pipeline.save_increment"
    bl_label = "Save scene as increment"
    
    @classmethod
    def poll(self, context) : 
        if context.scene.sceneContent == "" : 
            return False
        return True

    def execute(self, context):
        pipeline = p.Pipeline(bpy.context.scene.projectPath, bpy.context.scene.sceneContent, bpy.context.scene.sceneType, bpy.context.scene.charType, bpy.context.scene.seq)
        scenePath = pipeline.saveIncrementScene()
        
        self.report({'INFO'}, "File Saved : " + scenePath)
        return {'FINISHED'}

class PIPE_ResetPipeSettings(bpy.types.Operator) : 
    """Reset all pipeline settings to default"""
    bl_idname = "lpqflv_pipeline.reset_pipe"
    bl_label = "Reset"
    
    def execute(self, context) : 
        bpy.context.scene.projectPath = "yourScenesPath"
        bpy.context.scene.sceneContent = ""
        bpy.context.scene.sceneType="assets"
        bpy.context.scene.charType = "modeling"
        bpy.context.scene.seq = 0 
        
        return {'FINISHED'}

class PIPE_SaveMaster(bpy.types.Operator):
    """Save your scene as Master scene for reference"""
    bl_idname = "lpqflv_pipeline.save_master"
    bl_label = "Save as Master"

    @classmethod
    def poll(self, context) : 
        if context.scene.sceneContent == "" : 
            return False
        return True    

    def execute(self, context):
        pipeline = p.Pipeline(bpy.context.scene.projectPath, bpy.context.scene.sceneContent, bpy.context.scene.sceneType, bpy.context.scene.charType, bpy.context.scene.seq)
        scenePath = pipeline.saveMasterScene()
        
        self.report({'INFO'}, "Master file Saved : " + scenePath)
        return {'FINISHED'}
    

class PIPE_NewScene(bpy.types.Operator):
    """Create a new scene with the pipeline tool's settings"""
    bl_idname = "lpqflv_pipeline.new_scene"
    bl_label = "New Scene"

    @classmethod
    def poll(self, context) : 
        if context.scene.sceneContent == "" : 
            return False
        return True

    def invoke (self, context, event) : 
        pip = p.Pipeline(context.scene.projectPath, context.scene.sceneContent, context.scene.sceneType, context.scene.charType, context.scene.seq)
        path = pip.getScenePath()

        if  os.path.exists(path): 
            return context.window_manager.invoke_props_dialog(self)
        else : 
            return self.execute(context)

    def draw(self, context) : 
        l = self.layout
        r = l.row()
        r.label(text="The file already exist.", icon="ERROR")
        r = l.row()
        r.label(text="Are you sure to create an empty increment ?")
        r = l.row()
        r.label(text="It can lead to errors.")

    def execute(self, context):
        for obj in bpy.data.objects : 
            obj.select_set(False)
            #context.view_layer.objects.unlink(obj)
            bpy.data.objects.remove (obj)
            
        for grp in bpy.data.collections : 
            bpy.data.collections.remove (grp)
            
        for cam in bpy.data.cameras : 
            bpy.data.cameras.remove (cam)
            
        for action in bpy.data.actions : 
            bpy.data.actions.remove (action)
            
        for crv in bpy.data.curves : 
            bpy.data.curves.remove (crv)
            
        for msh in bpy.data.meshes : 
            bpy.data.meshes.remove (msh)
            
        for meta in bpy.data.metaballs : 
            bpy.data.metaballs.remove(meta)
            
        for arma in bpy.data.armatures : 
            if bpy.ops.object.mode_set.poll():
                bpy.ops.object.mode_set("INVOKE_DEFAULT", mode = 'OBJECT')
            bpy.data.armatures.remove (arma)
            
        for mat in bpy.data.materials : 
            bpy.data.materials.remove (mat, do_unlink=True)
            
        for part in bpy.data.particles : 
            bpy.data.particles.remove (part)
            
        for img in bpy.data.images : 
            bpy.data.images.remove (img)
            
        for tex in bpy.data.textures : 
            bpy.data.textures.remove (tex)
            
        for sc in bpy.data.scenes : 
            if sc.library : 
                bpy.data.scenes.remove(sc)
            
        pipeline = p.Pipeline(bpy.context.scene.projectPath, bpy.context.scene.sceneContent, bpy.context.scene.sceneType, bpy.context.scene.charType, bpy.context.scene.seq)
        scenePath = pipeline.saveIncrementScene()
        
        self.report({'INFO'}, "New scene saved : " + scenePath)
        return {'FINISHED'}


class PIPE_OpenSeq(bpy.types.Operator):
    """Ouvrir la sequence selectionnée"""
    bl_idname = "lpqflv_pipeline.open_seq"
    bl_label = "Open"

   # EXISTING_SEQS

    @classmethod
    def poll (self, context) : 
        if len(cfg.EXISTING_SEQS) > 0 or context.scene.existingScenes != "" : 
            return True
        else : 
            return False

    def execute(self, context):
        currentDir = context.scene.projectPath.replace("\\", "/") + context.scene.sceneType + "/" + context.scene.existingScenes
        files = os.listdir(currentDir)
        blends = []
        nb = []
        fileName = ""

        for f in files : 
            tmp = f.split (".")
            if tmp[len(tmp) - 1] == "blend" : 
                blends.append(f)
                
        for b in blends : 
            tmp = b.split (".")
            id = tmp[len(tmp) - 2]
            if (id == "MASTER") : 
                continue
            id = int(id)
            fileName = tmp[0]
            nb.append (id)
            
        maxId = max(nb)
        
        fileToOpen = currentDir + "/" + fileName + "." + str(maxId) + ".blend"
        
        bpy.ops.wm.open_mainfile(filepath=fileToOpen)

        self.report({'INFO'}, "project openned : " + fileToOpen)
        return {'FINISHED'}

class PIPE_ReplacePath(bpy.types.Operator):
    """Replace in all Path in the scene file and reload all. 
Useful when your project directorie has changed."""
    bl_idname = "path.replace_path_conflicts"
    bl_label = "Replace All"

    def execute (self, context) : 
        PIPE_ReplacePath.replace(PIPE_ReplacePath.getAllPath(context), context)
        return {'FINISHED'}

    @classmethod
    def getAllPath (cls, context) : 
        #libs 
        #images
        #sounds
        #caches
        #movie clips 
        #

        filepaths = []

        for lib in bpy.data.libraries : 
            filepaths.append(lib)

        for img in bpy.data.images : 
            filepaths.append(img)
        
        for s in bpy.data.sounds : 
            filepaths.append(s)
        
        for m in bpy.data.movieclips : 
            filepaths.append(m)
        
        for c in bpy.data.cache_files : 
            filepaths.append(c)

        return filepaths

    @classmethod
    def replace(cls, list, context) : 
        for p in list : 
            p.filepath = p.filepath.replace(context.scene.pathToReplace, context.scene.pathFromReplace)
            p.filepath = p.filepath.replace("\\", "/")
            context.scene.projectPath = bpy.context.scene.projectPath.replace(context.scene.pathToReplace, context.scene.pathFromReplace)
            context.scene.projectPath = bpy.context.scene.projectPath.replace("\\", "/")

        for lib in bpy.data.libraries : 
            lib.reload()

class PIPE_InvertPaths (bpy.types.Operator) : 
    """Invert path TO and path FROM"""
    bl_idname = "path.invert_path_conflicts"
    bl_label = "Invert"

    def execute (self, context) : 
        sc = context.scene

        tmpTo = sc.pathToReplace
        sc.pathToReplace = sc.pathFromReplace
        sc.pathFromReplace = tmpTo 

        return {'FINISHED'}
        

class PIPE_SetRenderOutput (bpy.types.Operator) :
    """Set Render path output from the pipeline settings"""
    bl_idname = "pipeline.set_render_output"
    bl_label = "Set Render Output"

    def execute (self, context) :
        renderPath = context.scene.projectPath.replace ("\\", "/")
        if renderPath[len(renderPath) -1] == "/" : 
            pass
        else :
            renderPath += "/"

        renderPath += "renders/seq_" + str(context.scene.seq) + "_" + context.scene.sceneContent + "/" 

        context.scene.render.filepath = renderPath

        return {'FINISHED'}

class PIPE_ReloadLib(bpy.types.Operator) : 
    """Reload the librarie's data"""

    bl_idname = "pipeline.reload_lib"
    bl_label = "Reload"
    name : bpy.props.StringProperty(name="lib name", description="lib name to reload")

    def execute (self, context) :
        bpy.data.libraries[self.name].reload() 

        return {'FINISHED'}

class PIPE_GoToProjectDir(bpy.types.Operator) : 
    """Navigate to the project directory"""

    bl_idname = "pipeline.go_to_project_dir"
    bl_label = "Project Dir"

    folder : bpy.props.StringProperty()

    def execute (self, context) :
        fb = context.area.spaces.active
        fb.params.directory = context.scene.projectPath + self.folder

        return {'FINISHED'}

class PIPE_UpdateInfos(bpy.types.Operator) : 
    """Update the Pipeline Panel Infos"""

    bl_idname = "pipeline.update"
    bl_label = "Update"

    def execute (self, context) :
        p.Pipeline.setExistingSeqs(self, context)
        p.Pipeline.readPreviousProjects()
        return {'FINISHED'}
    
class PIPE_UpdatePipelineNodes(bpy.types.Operator) : 
    bl_idname = "lpqflv.modal_update_pipeline_nodes"
    bl_label = "Modal Pipeline nodes event handler"
    
    @classmethod
    def poll(cls, context) : 
        return True 
    
    def modal(self, context, e) : 
        pipe = pnt.PipelineNodeTree.get()
        if not pipe or not pipe.handlerRunning : 
            print("Pipeline Node Tree - Modal Event Handler : Stopped.")
            return {'CANCELLED'}
        area = bl_utils.focusedArea(e)
        if area.type == "NODE_EDITOR" : 
            pipe.updateNodes()
        
        return {'PASS_THROUGH'}
        
    def invoke(self, context, e) : 
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
    
#Start or stop manually the pipeline and strips link handler
class PIPE_StartStopPipelineHandler(bpy.types.Operator) :
    bl_description = "Manage the Modal operator used for handle the nodes update in the Pipeline Node Tree."

    bl_idname = "pqflv.start_stop_pipe_handler"
    bl_label = "Manage Pipeline Node Tree Events Handler"
    
    def invoke(self, context, event) :
        pipe = pnt.PipelineNodeTree.get()
        if not pipe : 
            return {'CANCELLED'}
        
        if pipe.handlerRunning: 
            pipe.handlerRunning = False
        else : 
            pipe.handlerRunning = True
            print("Pipeline Node Tree - Modal Event Handler : Started.")
            #bpy.ops.lpqflv.modal_update_pipeline_nodes('INVOKE_DEFAULT')

        return {'FINISHED'}
    
class PIPE_LinkFromDataObjects(bpy.types.Operator) : 
    bl_description = "Add Object from other linked scenes/collections"

    bl_idname = "pqflv_pipeline.link_from_blenddata_objects"
    bl_label = "Blend data objects"
    
    object : bpy.props.StringProperty(name = "Object to link")
    
    def invoke(self, context, event) :
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    
    def draw(self, context) : 
        l = self.layout
        l.prop_search(self, "object", bpy.data, "objects")
    
    def execute(self, context) : 
        context.collection.objects.link(bpy.data.objects[self.object])
        return {'FINISHED'}
    
class PIPE_LinkFromDataData(bpy.types.Operator) : 
    bl_description = "Add Mesh from other linked scenes/collections"

    bl_idname = "pqflv_pipeline.link_from_blenddata_objects_data"
    bl_label = "Blend data meshes"
    
    data : bpy.props.StringProperty(name="Mesh to link")
    useObjectName : bpy.props.BoolProperty(default=True, name="Use Objects Name")
    
    def draw(self, context) : 
        l = self.layout
        r = l.row() 
        r.prop(self, "useObjectName")
        r = l.row()
        if self.useObjectName : 
            r.prop_search(self, "data", bpy.data, "objects")
        else : 
            r.prop_search(self, "data", bpy.data, "meshes")
        
    
    def invoke(self, context, event) :
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    
    def execute(self, context) : 
        obj = None
        D = bpy.data
        if self.useObjectName :
            if D.objects[self.data].type == "MESH" : 
                obj = D.objects.new(self.data, D.objects[self.data].data)
                
        else : 
            obj = D.objects.new(self.data, D.meshes[self.data])
            
        if obj : 
            context.collection.objects.link(obj)
        return {'FINISHED'}
    
class PIPE_LinkObjectsFromCollection(bpy.types.Operator) : 
    bl_description = "Add all objects from a collection"

    bl_idname = "pqflv_pipeline.link_all_from_collection"
    bl_label = "Objects from collection"
    
    collection : bpy.props.StringProperty(name="Collection")
    
    def draw(self, context) : 
        l = self.layout
        l.prop_search(self, "collection", bpy.data, "collections")
        
    def invoke(self, context, event) :
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    
    def execute(self, context) : 
        bl_utils.linkAllFromCollection(bpy.data.collections[self.collection], 
                                          bpy.context.collection)
            
        return {'FINISHED'}


class PIPE_LinkObjectsFromScene(bpy.types.Operator) : 
    bl_description = "Add all objects from a scene"

    bl_idname = "pqflv_pipeline.link_all_from_scene"
    bl_label = "Objects from scene"
    
    scene : bpy.props.StringProperty(name="Scene")
    
    def draw(self, context) : 
        l = self.layout
        l.prop_search(self, "scene", bpy.data, "scenes")
        
    def invoke(self, context, event) :
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    
    def execute(self, context) : 
        bl_utils.linkAllFromScene(bpy.data.scenes[self.scene])
        return {'FINISHED'}


class PIPE_DuplicateCurrentScene(bl_ops.Operator) : 
    bl_description = "Duplicate the current scene in the Pipeline"
    bl_idname = "pqflv_pipeline.duplicate_current_scene"
    bl_label = "Duplicate current Scene"

    newName : bpy.props.StringProperty(name="New Name", description="Name of the new scene (duplicate from this one)")
    
    @classmethod
    def poll(cls, context) : 
        if context.scene.projectPath == "" :
            return False
        if context.scene.sceneContent == "" : 
            return False
        return True

    def overInvoke(self, ctx, e) :
        self.newName = ctx.scene.sceneContent

    def draw(self, context) : 
        self.layout.prop(self, "newName")

    def execute(self, context) : 
        p.Pipeline.duplicate(self.newName)
        self.report({'INFO'}, "Scene duplicated.")
        return {'FINISHED'}
        

class MCR_Remove_Specific_Frame (bpy.types.Operator):
    bl_idname = "lpqflv_multicam_render.remove_specific_frame"
    bl_label = "Remove Specific Frame"
    bl_description = "Remove this Specific Frame to render from this camera"
    bl_options = {'REGISTER'}

    cameraName : bpy.props.StringProperty(name="camera name")
    frameToRemove : bpy.props.StringProperty(name="Frame to Remove")

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        mcr.MultiCamRender.removeSpecificFrame(bpy.data.objects[self.cameraName].data, self.frameToRemove)
        return {"FINISHED"}

class MCR_Add_Specific_Frame (bpy.types.Operator):
    bl_idname = "lpqflv_multicam_render.add_specific_frame"
    bl_label = "Add Specific Frame"
    bl_description = "Add this Specific Frame to render from this camera"
    bl_options = {'REGISTER'}
    
    cameraName : bpy.props.StringProperty(name="camera name")
    
    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        data = bpy.data.objects[self.cameraName].data
        try : 
            int(data.specificFrame)
            data.specificFrames += data.specificFrame + ","
            return {"FINISHED"}
        except :
            self.report({"INFO"}, "Can't convert '" + data.specificFrame + "' in a frame number.")
            return {"CANCELLED"} 

    @staticmethod
    def cameraByName(name) : 
        objects = bpy.context.scene.objects
        for o in objects : 
            if o.type == "CAMERA" and o.name == name :
                return o 

class MCR_MkRender (bl_ops.Operator) : 
    """Make a render with all your active cameras"""
    bl_idname = "lpqflv_multicam_render.render_animation"
    bl_label = "Make Render with Multi Cameras"

    _timer = None

    def overInvoke(self, ctx, e) : 
        if cfg.MCR.hasSpecific() : 
            cfg.MCR.preRender()
            ctx.window_manager.isAutoUpdateCam = False
            for c in cfg.MCR.toRender : 
                cfg.MCR.render(c, False)

        else :
            cfg.MCR.startRender()
            wm = ctx.window_manager
            self._timer = wm.event_timer_add(1, window=ctx.window)

    def modal (self, ctx, e) : 
        if not self._timer : 
            return {'FINISHED'}

        if e.type == "TIMER" : 
            cfg.MCR.onTimer()
            if cfg.MCR.status == mcr.MultiCamRender.FINISHED : 
                ctx.window_manager.event_timer_remove(self._timer)
                return {'FINISHED'}

        return {'PASS_THROUGH'}
    
    def execute(self, context) : 
        return self.invoke(self, context, None)        

class MCR_MkPreview (bpy.types.Operator) : 
    """Make a play blast with all your active cameras"""
    bl_idname = "lpqflv_multicam_render.render_preview"
    bl_label = "Make PlayBlast with Multi Cameras"
    
    def execute(self, context) : 
        context.window_manager.isAutoUpdateCam = False
        filePath = context.window_manager.previewFilepath
        sceneName = bpy.data.filepath.split("/")[-1].replace(".blend", "")
        if filePath == "" :  
            self.report({'ERROR'}, 'The output path is empty.')
            return {"CANCELLED"}


        o_file_format = context.scene.render.image_settings.file_format
        o_color_mode = context.scene.render.image_settings.color_mode
        o_color_depth = context.scene.render.image_settings.color_depth
        o_ffmpeg_preset = context.scene.render.ffmpeg.ffmpeg_preset
        o_gopsize = context.scene.render.ffmpeg.gopsize
        o_codec = context.scene.render.ffmpeg.codec

        o_format = context.scene.render.ffmpeg.format
        o_constant_rate_factor = context.scene.render.ffmpeg.constant_rate_factor
        o_resolution = (context.scene.render.resolution_x, context.scene.render.resolution_y, context.scene.render.resolution_percentage)
        o_bgScene = context.scene.background_set

        use_preview_range = context.scene.use_preview_range

        context.scene.use_preview_range = False
        context.scene.render.image_settings.file_format = 'FFMPEG'
        context.scene.render.ffmpeg.constant_rate_factor = 'MEDIUM'
        context.scene.render.ffmpeg.ffmpeg_preset = 'GOOD'
        context.scene.render.ffmpeg.gopsize = 1
        context.scene.render.image_settings.color_mode = 'RGB'
        context.scene.render.ffmpeg.format = 'MPEG4'
        context.scene.render.ffmpeg.codec = 'H264'

        prevType = context.area.type
        context.area.type = "VIEW_3D"
        context.area.spaces[0].region_3d.view_perspective = 'CAMERA'
        context.space_data.shading.type = context.window_manager.viewportQuality
        context.space_data.overlay.show_overlays = False

        toPreview = []
        for c in cm.cams() : 
            for sed in c.data.cm.startEnds : 
                if sed.render and not sed.isRendered : 
                    toPreview.append({"name" : c.name, "start" : sed.start, "end" : sed.end, "step" : sed.step, "scene" : c.data.cm.scene})

        for d in toPreview : 
            cmp = bpy.data.objects[d["name"]].data.cm
            context.scene.camera = bpy.data.objects[d["name"]]
            context.scene.frame_start = d["start"]
            context.scene.frame_end = d["end"]
            if (d["scene"] != "") :
                context.scene.background_set = bpy.data.scenes[d["scene"]]
            context.scene.render.filepath = filePath + sceneName + "_" + d["name"] + "_"
            bpy.ops.render.opengl(animation=True, view_context=True)
        
        context.scene.render.filepath = filePath
        context.area.type = prevType

        context.scene.render.image_settings.file_format = o_file_format
        context.scene.render.image_settings.color_mode = o_color_mode
        context.scene.render.image_settings.color_depth = o_color_depth

        context.scene.render.ffmpeg.constant_rate_factor = o_constant_rate_factor
        context.scene.render.ffmpeg.ffmpeg_preset = o_ffmpeg_preset
        context.scene.render.ffmpeg.gopsize = o_gopsize
        context.scene.render.image_settings.file_format = o_file_format

        context.scene.render.ffmpeg.format = o_format
        context.scene.render.ffmpeg.codec = o_codec
        context.scene.render.ffmpeg.constant_rate_factor = o_constant_rate_factor
        context.scene.background_set = o_bgScene

        context.scene.render.resolution_x = o_resolution[0]
        context.scene.render.resolution_y = o_resolution[1]
        context.scene.render.resolution_percentage = o_resolution[2]

        context.scene.use_preview_range = use_preview_range

        self.report({'INFO'}, 'Your Preview is finished.')
        return {'FINISHED'}
    
class MCR_AddCameraToExclude (bpy.types.Operator) : 
    """Add Camera to exclude for the selected object"""
    bl_idname = "lpqflv_multicam_render.add_exclude_camera"
    bl_label = ""
    
    def execute(self, context) : 
    
        for c in context.object.camerasToExclude : 
            if context.scene.tmpCamera == c.camera : 
                return {'FINISHED'}  
        camToExclude = context.object.camerasToExclude.add()
        camToExclude.camera = context.scene.tmpCamera
        return {'FINISHED'}
        
class MCR_RemoveCameraToExclude (bpy.types.Operator) : 
    """Remove Camera to exclude for the selected object"""
    bl_idname = "lpqflv_multicam_render.remove_exclude_camera"
    bl_label = ""
    
    def execute(self, context) : 
    
        context.object.camerasToExclude.remove (context.object.cameraToExcludeIndex)
        return {'FINISHED'}  

class MCR_ClearAllCamerasToExclude (bpy.types.Operator) : 
    """Remove All Cameras to exclude for the selected object"""
    bl_idname = "lpqflv_multicam_render.clear_exclude_camera"
    bl_label = ""
    
    def execute(self, context) : 
    
        context.object.camerasToExclude.clear()
        return {'FINISHED'}

class MCR_ReadFramesInfos (bpy.types.Operator) : 
    """Update frames infos from previous render of this scene\n
    Very useful if you had to interupt your previous render"""
    bl_idname = "lpqflv_multicam_render.read_frames_infos"
    bl_label = ""
    
    def execute(self, context) : 
        mcr.MultiCamRender.readFramesInfos()
        return {'FINISHED'}

class MCR_CreateBatchRenderFiles (bpy.types.Operator) : 
    """Separate this file in several files (one foreach selected camera)
and create a command line file to render all the scenes.
Development in the future..."""
    bl_idname = "lpqflv_multicam_render.create_batch_render_files"
    bl_label = "Create Files"
    
    def execute(self, context) : 
        return {'FINISHED'}

class ActiveCameraOptions (bl_ops.Operator) : 
    bl_idname = "lpqflv_cameras_manager.active_camera_options"
    bl_label = "Active Camera Options..."
    bl_description = "Change active camera settings"

    option : bpy.props.StringProperty()
    value : bpy.props.FloatProperty(name="Value", default=0.0)
    slow : bpy.props.BoolProperty()

    @classmethod
    def poll(cls, ctx) : 
        if ctx.workspace.name == "Viewport Compositing" : 
            return False
        if not ctx.scene.camera : 
            return False
        if ctx.scene.camera.type != "CAMERA" : 
            return False
        if not ctx.area : 
            return False
        return ctx.area.type == "VIEW_3D"

    def overInvoke(self, ctx, e) : 
        self.option = "none"

    def modal(self, ctx, e) : 
        camera = ctx.scene.camera.data
        if e.shift : 
            self.slow = True
        else : 
            self.slow = False

        if e.type == "RIGHTMOUSE" or e.type =="ESC" : 
            ctx.area.header_text_set(None)
            return {'FINISHED'}
        elif e.type == "F" : 
            self.option = "lens"
            self.value = camera.lens
        elif e.type == "C" and not e.ctrl : 
            self.option = "clipEnd"
            self.value = camera.clip_end
        elif e.type == "C" and e.ctrl and not e.shift: 
            self.option = "clipStart"
            self.value = camera.clip_start
        elif e.type == "P" : 
            self.option = "passepartout"
            self.value = camera.passepartout_alpha
        elif e.type == "B" : 
            camera.dof.use_dof = True
            self.value = camera.dof.aperture_fstop
            self.option = "blur"

        elif e.type == "LEFTMOUSE" : 
            ctx.area.header_text_set(None)
            return self.execute(ctx)
        
        self.setValue(e)
        self.drawHeader(ctx, e)
        self.execute(ctx)
        return {'RUNNING_MODAL'}

    def setValue (self, e) : 
        offset = e.mouse_x - e.mouse_prev_x
        if self.option == "lens" : 
            offset *= 0.2
        elif self.option == "clipStart" : 
            offset *= 0.05
        elif self.option == "clipEnd" : 
            offset *= 10
        elif self.option == "blur" : 
            offset *= 0.05
        elif self.option == "passepartout" : 
            offset *= 0.01

        if self.slow : 
            offset *= 0.1

        self.value += offset 
        self.value = abs(self.value)

    def drawHeader(self, ctx, e) : 
        end = "Keys : F -> Lens   |   P -> Passepartout Opacity   |   C -> End Clip, Ctrl + C -> Start Clip   |   B -> Depth of Field Apperture"
        start = "Current Option : "
        if self.option == "lens" : 
            start += "Focal Lens"
        elif self.option == "clipStart" : 
            start += "Clip Start"
        elif self.option == "clipEnd" : 
            start += "Clip End"
        elif self.option == "passepartout" : 
            start += "Passepartout Opacity"
        elif self.option == "blur" : 
            start += "Depth of Field Apperture"
        else : start = "Chosse an option"

        if self.option != "none" : 
            start += " - " + str(round(self.value, 2))

        separator = "         "
        
        st = start + separator + end
        ctx.area.header_text_set(st)

    def execute(self, ctx) : 
        if self.option == "non" : 
            return {'CANCELLED'}

        camera = ctx.scene.camera.data
        if self.option == "lens" : 
            camera.lens = self.value    
        elif self.option == "clipStart" : 
            camera.clip_start = self.value
        elif self.option == "clipEnd" : 
            camera.clip_end = self.value
        elif self.option == "passepartout" : 
            if (self.value>1) : 
                self.value = 1
            camera.passepartout_alpha = self.value
        elif self.option == "blur" : 
            camera.dof.aperture_fstop = self.value
        return {'FINISHED'}

class CreateDOFTarget (bl_ops.Operator) : 
    bl_idname = "lpqflv_cameras_manager.create_dof_target"
    bl_label = "Create DOF Target"
    bl_description = "Create a dof target for the active camera\n(the dof object will be created at the 3D cursor location)"

    camera = None
    empty = None
    old = {}

    @classmethod
    def poll(cls, ctx) : 
        if not ctx.object : 
            return False
        return ctx.object == ctx.scene.camera

    def overInvoke(self, ctx, event) : 
        if ctx.scene.camera.data.dof.focus_object : 
            bpy.data.objects.remove(ctx.scene.camera.data.dof.focus_object)
        bpy.ops.object.empty_add(type='PLAIN_AXES')
        CreateDOFTarget.empty = bpy.data.objects[ctx.object.name]
        CreateDOFTarget.camera = ctx.scene.camera
        CreateDOFTarget.empty.name = "focus_" + CreateDOFTarget.camera.name
        CreateDOFTarget.camera.data.dof.use_dof = True 
        CreateDOFTarget.camera.data.dof.focus_object = CreateDOFTarget.empty
        CreateDOFTarget.camera.data.dof.aperture_ratio = 2
        CreateDOFTarget.old["dof"] = ctx.area.spaces.active.shading.use_dof 

        ctx.area.spaces.active.shading.use_dof = True

    def modal(self, ctx, event) : 
        offset = event.mouse_x - event.mouse_prev_x
        if not event.shift : 
            CreateDOFTarget.camera.data.dof.aperture_fstop += offset * 0.01
        else : 
            CreateDOFTarget.camera.data.dof.aperture_fstop += offset * 0.001
        if event.type == "WHEELUPMOUSE" : 
            CreateDOFTarget.camera.data.dof.aperture_ratio += 0.5
        elif event.type == "WHEELDOWNMOUSE" : 
            CreateDOFTarget.camera.data.dof.aperture_ratio += -0.5

        ctx.area.header_text_set("Aperture : " + str(round(CreateDOFTarget.camera.data.dof.aperture_fstop, 4)) + " - Blur Ratio : " + str(round(CreateDOFTarget.camera.data.dof.aperture_ratio, 2)))
        if event.type == "LEFTMOUSE" : 
            return self.execute(ctx)
        return {'RUNNING_MODAL'}

    def execute(self, ctx) : 
        ctx.area.header_text_set(None)
        ctx.area.spaces.active.shading.use_dof = CreateDOFTarget.old["dof"]
        return {"FINISHED"}

class MCR_ExportToAe (bpy.types.Operator) : 
    bl_idname = "lpqflv_multicam_render.export_to_ae"
    bl_label = "Export to After Effects"
    bl_description = "Export the selected to .jsx file to be readed in After Effects"

    @classmethod
    def poll(cls, ctx) : 
        if not ctx.scene.mcr_outputDir : 
            return False
        return os.path.exists(bpy.path.abspath(ctx.scene.mcr_outputDir))
    
    def execute(self, context) : 
        ostart = context.scene.frame_start
        oend = context.scene.frame_end
        oName = context.scene.camera.name
        for c in cm.cams() : 
            if not c.data.cm.render : 
                continue
            context.scene.frame_start = c.data.cm.start
            context.scene.frame_end = c.data.cm.end
            context.scene.camera = c
            bpy.ops.export.jsx(filepath = context.scene.mcr_outputDir + os.sep + c.name + ".jsx", 
                    include_active_cam=True, 
                    include_animation=True, 
                    include_selected_objects=True)
        context.scene.frame_start = ostart
        context.scene.frame_end = oend
        context.scene.camera = bpy.data.objects[oName]
        return {'FINISHED'}

class MCR_ManageCamSE(bpy.types.Operator) :
    bl_idname = "lpqflv_multicam_render.mange_cam_se"
    bl_label = ""
    bl_description = "Add, remove or clear all cameras start end couples"
    ADD = 1
    REMOVE = 2
    CLEAR = 3
    action : bpy.props.IntProperty(default=ADD)
    idx : bpy.props.IntProperty()
    
    def execute(self, context) : 
        if self.action == self.ADD :
            context.object.data.cm.startEnds.add()
        elif self.action == self.REMOVE :
            context.object.data.cm.startEnds.remove(self.idx)
        elif self.action == self.CLEAR :
            context.object.data.cm.startEnds.clear()
        return {'FINISHED'}

class MCR_OffsetCams(bl_ops.Operator) :
    bl_idname = "lpqflv_multicam_render.offset_cameras"
    bl_label = "Offset Cameras"
    bl_description = "Offset cameras start and end from a specific frame"
    
    selection : bpy.props.EnumProperty(items=bl_ui.items("All", "Selected"), default="All", name="Selection")

    frame : bpy.props.IntProperty(name="from Frame", description="the offset will be done only after the frame. (frame included.)")
    offset : bpy.props.IntProperty(name="Offset")

    def overInvoke(self, ctx, e) : 
        self.frame = ctx.scene.frame_current

    def draw(self, context) : 
        self.layout.prop(self, "selection")
        self.layout.prop(self, "frame")
        self.layout.prop(self, "offset")
    
    def execute(self, context) : 
        cameras = []
        if (self.selection == "Selected") : 
            for o in context.selected_objects : 
                if o.type == "CAMERA" : 
                    cameras.append(o)
        elif self.selection == "All" : 
            cameras = cm.cams()

        for c in cameras : 
            for se in c.data.cm.startEnds :
                if se.start >= self.frame : 
                    se.start += self.offset
                if se.end >= self.frame : 
                    se.end += self.offset

        return {'FINISHED'}

def register () : 
    bpy.utils.register_class(MkActiveCamera)
    bpy.utils.register_class(SelectCamera)
    bpy.utils.register_class(DOFSetUp)
    bpy.utils.register_class(SelectAllCameras)
    bpy.utils.register_class(CameraPresetOperator)
    bpy.utils.register_class(LinkCamsAndSeqs)
    bpy.utils.register_class(StartStopCameraHandler)
    bpy.utils.register_class(CameraFramesAsRange)
    
    bpy.utils.register_class(PIPE_CreatePipeline)
    bpy.types.NODE_HT_header.append(PIPE_CreatePipeline.draw)
    bpy.utils.register_class(PIPE_OpenScene)
    bpy.utils.register_class(PIPE_ExportAsAbc)
    bpy.utils.register_class(PIPE_GenerateScene)
    bpy.utils.register_class(PIPE_PanelShowDirContent)
    bpy.utils.register_class(PIPE_ReadPipeline)
    bpy.utils.register_class(PIPE_ArrangeNodes)
    bpy.utils.register_class(PIPE_Link)
    bpy.utils.register_class(PIPE_SelectFileElmt)
    bpy.utils.register_class(PIPE_SelectFileElmts)
    bpy.utils.register_class(PIPE_DeselectFileElmts)

    bpy.utils.register_class(PIPE_SaveIncrement)
    bpy.utils.register_class(PIPE_ResetPipeSettings)
    bpy.utils.register_class(PIPE_SaveMaster)
    bpy.utils.register_class(PIPE_NewScene)
    bpy.utils.register_class(PIPE_OpenSeq)
    bpy.utils.register_class(PIPE_ReplacePath)
    bpy.utils.register_class(PIPE_InvertPaths)
    bpy.utils.register_class(PIPE_SetRenderOutput)
    bpy.utils.register_class(PIPE_ReloadLib)
    bpy.utils.register_class(PIPE_GoToProjectDir)
    bpy.utils.register_class(PIPE_UpdateInfos)
    bpy.utils.register_class(PIPE_UpdatePipelineNodes)
    bpy.utils.register_class(PIPE_StartStopPipelineHandler)
    bpy.utils.register_class(PIPE_LinkFromDataObjects)
    bpy.utils.register_class(PIPE_LinkFromDataData)
    bpy.utils.register_class(PIPE_LinkObjectsFromCollection)
    bpy.utils.register_class(PIPE_LinkObjectsFromScene)
    
    bpy.utils.register_class(MCR_Remove_Specific_Frame)
    bpy.utils.register_class(MCR_Add_Specific_Frame)
    bpy.utils.register_class(MCR_MkRender)
    bpy.utils.register_class(MCR_MkPreview)
    bpy.utils.register_class(MCR_AddCameraToExclude)
    bpy.utils.register_class(MCR_RemoveCameraToExclude)
    bpy.utils.register_class(MCR_ClearAllCamerasToExclude)
    bpy.utils.register_class(MCR_ReadFramesInfos)
    bpy.utils.register_class(MCR_CreateBatchRenderFiles)

    bpy.utils.register_class(ActiveCameraOptions)
    bpy.utils.register_class(MCR_ExportToAe)
    bpy.utils.register_class(CameraRangeFromKeyframes)
    bpy.utils.register_class(CreateDOFTarget)
    bpy.utils.register_class(MCR_ManageCamSE)
    bpy.utils.register_class(MCR_OffsetCams)

    bpy.utils.register_class(PIPE_DuplicateCurrentScene)

    def updatePipelinePaths() : 
        bpy.ops.pipeline.update()
        return None
    bpy.app.timers.register(updatePipelinePaths, first_interval=1)

def unregister () : 
    bpy.utils.unregister_class(MkActiveCamera)
    bpy.utils.unregister_class(SelectCamera)
    bpy.utils.unregister_class(DOFSetUp)
    bpy.utils.unregister_class(SelectAllCameras)
    bpy.utils.unregister_class(CameraPresetOperator)
    bpy.utils.unregister_class(LinkCamsAndSeqs)
    bpy.utils.unregister_class(StartStopCameraHandler)
    bpy.utils.unregister_class(CameraFramesAsRange)

    bpy.utils.unregister_class(PIPE_CreatePipeline)    
    bpy.types.NODE_HT_header.remove(PIPE_CreatePipeline.draw)
    bpy.utils.unregister_class(PIPE_OpenScene)
    bpy.utils.unregister_class(PIPE_ExportAsAbc)
    bpy.utils.unregister_class(PIPE_GenerateScene)
    bpy.utils.unregister_class(PIPE_PanelShowDirContent)
    bpy.utils.unregister_class(PIPE_ReadPipeline)
    bpy.utils.unregister_class(PIPE_ArrangeNodes)
    bpy.utils.unregister_class(PIPE_Link)
    bpy.utils.unregister_class(PIPE_SelectFileElmt)
    bpy.utils.unregister_class(PIPE_SelectFileElmts)
    bpy.utils.unregister_class(PIPE_DeselectFileElmts)
    
    bpy.utils.unregister_class(PIPE_SaveIncrement)
    bpy.utils.unregister_class(PIPE_ResetPipeSettings)
    bpy.utils.unregister_class(PIPE_SaveMaster)
    bpy.utils.unregister_class(PIPE_NewScene)
    bpy.utils.unregister_class(PIPE_OpenSeq)
    bpy.utils.unregister_class(PIPE_ReplacePath)
    bpy.utils.unregister_class(PIPE_InvertPaths)
    bpy.utils.unregister_class(PIPE_SetRenderOutput)
    bpy.utils.unregister_class(PIPE_ReloadLib)
    bpy.utils.unregister_class(PIPE_GoToProjectDir)
    bpy.utils.unregister_class(PIPE_UpdateInfos)
    bpy.utils.unregister_class(PIPE_UpdatePipelineNodes)
    bpy.utils.unregister_class(PIPE_StartStopPipelineHandler)
    bpy.utils.unregister_class(PIPE_LinkFromDataObjects)
    bpy.utils.unregister_class(PIPE_LinkFromDataData)
    bpy.utils.unregister_class(PIPE_LinkObjectsFromCollection)
    bpy.utils.unregister_class(PIPE_LinkObjectsFromScene)
    
    bpy.utils.unregister_class(MCR_Remove_Specific_Frame)
    bpy.utils.unregister_class(MCR_Add_Specific_Frame)
    bpy.utils.unregister_class(MCR_MkRender)
    bpy.utils.unregister_class(MCR_MkPreview)
    bpy.utils.unregister_class(MCR_AddCameraToExclude)
    bpy.utils.unregister_class(MCR_RemoveCameraToExclude)
    bpy.utils.unregister_class(MCR_ClearAllCamerasToExclude)
    bpy.utils.unregister_class(MCR_ReadFramesInfos)
    bpy.utils.unregister_class(MCR_CreateBatchRenderFiles)

    bpy.utils.unregister_class(ActiveCameraOptions)
    bpy.utils.unregister_class(MCR_ExportToAe)

    bpy.utils.unregister_class(CameraRangeFromKeyframes)
    bpy.utils.unregister_class(CreateDOFTarget)
    bpy.utils.unregister_class(MCR_ManageCamSE)

    bpy.utils.unregister_class(PIPE_DuplicateCurrentScene)
    bpy.utils.unregister_class(MCR_OffsetCams)
