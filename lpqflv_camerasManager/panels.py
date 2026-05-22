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



from lpqflv_camerasManager import ops
from lpqflv_camerasManager import config as cf
from lpqflv_camerasManager import Pipeline as p
from lpqflv_camerasManager import multiCamRender as mcr
from lpqflv_camerasManager import Camera as Cam
from lpqflv_camerasManager import CameraManager as cm
from lpqflv_camerasManager.renderFarm import ops as rfops
from lpqflv_camerasManager.renderFarm.RenderFarm import RenderFarm
from lpqflv import bl_utils

import bpy
import os 
import sys

class CamerasToolPanel(bpy.types.Panel):
    """Panel for the Cameras Manager"""
    bl_label = "Cameras Manager"
    bl_idname = "LPQFLV_PT_Cameras_tool"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        r = layout.row()
        r.alignment = "EXPAND"
        r.prop(context.scene.cm, "search", icon="VIEWZOOM")
        r.prop(context.scene.cm, "local", icon="SCENE_DATA", text="")
        r.prop(context.window_manager, "isAutoUpdateCam", icon="PLAY", text="")
        for cam in cm.cams() : 
            if context.scene.cm.search == "" or context.scene.cm.search.lower() in cam.name.lower() : 
                self.drawCam(context, cam)

    def drawCam(self, ctx, cam) : 
        row = self.layout.row(align=True)
        row.prop(cam.data.cm, "expand", text="", icon="TRIA_DOWN")
        row.separator()
        if cam == ctx.scene.camera : 
            row.label(text=cam.name, icon="VIEW_CAMERA")
        else : 
            row.label(text=cam.name, icon="CAMERA_DATA")
        row.separator()
        c = row.column(align=True)
        if Cam.needUpdate(cam.data) : 
            r = c.row(align=True)
            r.prop(cam.data.cm, "start", text="")
            r.prop(cam.data.cm, "end", text="")
        for i in range(len(cam.data.cm.startEnds)) : 
            se = cam.data.cm.startEnds[i]
            r = c.row(align=True)
            if se.isRendered : 
                r.label(text="Rendered.")
            else :
                r.prop(se, "start", text="")
                r.prop(se, "end", text="")
                _set = r.operator(ops.CameraFramesAsRange.bl_idname, icon="PREVIEW_RANGE")
                _set.cameraName = cam.name
                _set.index = i
        row.separator()
        row.prop(cam.cm, "hasStrip", text="", icon="FILE_MOVIE")
        row.separator()
        
        if ctx.scene.objects.get(cam.name) : 
            row.operator (ops.SelectCamera.bl_idname, icon="RESTRICT_SELECT_OFF").cameraName = cam.name ## select Camera)
        row.operator (ops.MkActiveCamera.bl_idname, icon="OUTLINER_OB_CAMERA", text="").cameraName = cam.name ## mk active camera 

        if cam.data.cm.expand : 
            box = self.layout.box()
            r = box.row(align=True)
            r.prop(cam, "name")
            self.layout.separator()
            r = box.row()
            r.prop(cam.data, "lens", icon="RESTRICT_RENDER_OFF")
            r = box.row(align=True)
            r.label(text="Clip : ")
            r.prop(cam.data, "clip_start", text="")
            r.prop(cam.data, "clip_end", text="")
            r = box.row(align=True)
            r.prop(cam.data.dof, "use_dof")
            if cam.data.dof.use_dof : 
                r.prop(cam.data.dof, "focus_object", text="Object")
                r = box.row(align=True)
                r.label(text="Aperture : ")
                r.prop(cam.data.dof, "aperture_fstop", text="")
                r.prop(cam.data.dof, "aperture_ratio", text="")

            r = box.row(align=True)
            r.prop_search(cam.data.cm, "scene", bpy.data, "scenes")

class ProjectPanel(bpy.types.Panel): 
    bl_label = "Project"
    bl_idname = "LPQFLV_PT_Pipeline_node_editor"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Pipeline"
    
    def draw_header(self, context) : 
        layout = self.layout
        layout.label(icon="LOCKVIEW_ON")
    
    @classmethod
    def poll(cls, context) : 
        return context.area.ui_type == "PipelineNodeTree"

    def draw(self, context):
        layout = self.layout

        row = layout.row() 
        row.prop(context.scene, "projectPath")
        row = layout.row()
        row.prop(context.scene, "previousProject")
        row.operator(ops.PIPE_UpdateInfos.bl_idname, icon="FILE_REFRESH", text="")

        ## path conflicts ## 
        row = layout.row() 
        row.prop(context.window_manager, "showPath", text="", icon="TRIA_DOWN")
        row.label (text="Path replacement & conflicts", icon="LIBRARY_DATA_BROKEN")
        if context.window_manager.showPath : 
            box = layout.box()
            row = box.row() 
            row.prop(context.scene, "pathToReplace")
            row = box.row() 
            row.prop(context.scene, "pathFromReplace")
            row= box.row(align=True)
            row.operator (ops.PIPE_ReplacePath.bl_idname, icon="FILE_TICK")
            row.operator (ops.PIPE_InvertPaths.bl_idname, icon="AUTOMERGE_OFF", text="")
            row = box.row()
            row.label(text="Libraries", icon="LIBRARY_DATA_DIRECT")

            activeDir = os.path.dirname(bpy.data.filepath)

            for lib in bpy.data.libraries : 
                row = box.row(align=True) 
                row.prop(lib, "filepath")
                op = row.operator(ops.PIPE_ReloadLib.bl_idname, icon="FILE_REFRESH", text="")
                op.name = lib.name
                if ("//" in lib.filepath): 
                    path = activeDir + lib.filepath.replace("//", "/")
                    # print (path)
                else : 
                    path = lib.filepath
                if os.path.exists(path) : 
                    row.label(text="", icon="FILE_TICK")
                else : 
                    row.label(text="", icon="CANCEL")

#panel File Tree props # 

class FileTreeProps(bpy.types.PropertyGroup):
    onlyBlends : bpy.props.BoolProperty(name="Blend Files", description="Filter only the blend files", default=True)
    onlyMaster : bpy.props.BoolProperty(name="Master Files", description="Filter only the Master files", default=False)
    
class PanelDir : 
    def __init__(self, path, closed=True):
        self.path = path
        self.closed = closed
        
    @staticmethod
    def getByPath(path) : 
        for d in cf.panelDirs : 
            if d.path == path : 
                return d
            
        dir = PanelDir(path)
        cf.panelDirs.append(dir) 
        return dir
        

class FileTree(bpy.types.Panel):
    bl_label = "Files"
    bl_idname = "LPQFLV_PT_pipeline_files"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Pipeline"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw_header(self, context) : 
        layout = self.layout
        layout.label(icon="FILE_FOLDER")
    
    @classmethod
    def poll(cls, context) : 
        if (context.area.ui_type == "PipelineNodeTree" and 
            os.path.exists(context.scene.projectPath)) : 
                return True
            
        return False

    def draw(self, context):
        layout = self.layout
        props = context.window_manager.lpqflv_pipelineFiles
        
        r = layout.row(align=True) 
        r.prop(props, "onlyBlends", icon="BLENDER", text="") 
        r.prop(props, "onlyMaster", icon="MONKEY", text="")
        
        self.drawHiearchie(context.scene.projectPath)
    
        
    def drawSplit(self, text, icon, fac, type="file", filepath="") : 
        c = self.layout.column()
        row = c.row(align=True)
        split = row.split(factor=fac, align=True)
        c = split.column()
        c.label(text="")
        split = split.split(factor = 0.9)
        c = split.column()
        c.label(text=text, icon=icon)
        if type == "folder" : 
            split = split.split()
            c = split.column()
            c.operator(ops.PIPE_PanelShowDirContent.bl_idname, icon="TRIA_DOWN", text="", emboss=False).path=filepath
            
        if type == "file" and "MASTER" in text : 
            split = split.split()
            c = split.column()
            c.operator(ops.PIPE_OpenScene.bl_idname, icon="FILEBROWSER", text="").filepath = filepath
    
    def addFolder(self, folder, fac, filepath) : 
        if "__trash__" in filepath : 
            self.drawSplit(folder, "TRASH", fac, "folder", filepath)
        else : 
            self.drawSplit(folder, "FILE_FOLDER", fac, "folder", filepath)
        dir = PanelDir.getByPath(filepath)
        return not dir.closed
    
    def addFile(self, file, fac, filepath) : 
        props = bpy.context.window_manager.lpqflv_pipelineFiles
        icon = "NONE"
        
        if "blend1" in file : 
            return 
        
        if "MASTER" in file and "blend" in file : 
            icon="MONKEY"
            self.drawSplit(file, icon, fac, "file", filepath)
        
        elif "blend" in file and not props.onlyMaster: 
            icon="FILE_BACKUP"
            self.drawSplit(file, icon, fac, "file", filepath)
            
        elif not props.onlyBlends and not props.onlyMaster : 
            icon="FILE"
            self.drawSplit(file, icon, fac, "file", filepath)
            
    def drawHiearchie(self, root) : 
        if root[-1] == "/" : 
            root = root[:-1]
        files = os.listdir(root)
        
        i=0
        max = len(files)
        while i< max : 
            if os.path.isdir(root + "/" + files[i]) : 
                if self.addFolder(files[i], self.getIncrement(root + "/" + files[i]), 
                                root + "/" + files[i]) : 
                    self.drawHiearchie(root + "/" + files[i])
            else : 
                self.addFile(files[i], self.getIncrement(root + "/" + files[i]), root + "/" + files[i])
            
            i+=1
            
    def getIncrement(self, path) : 
        path = path.replace(bpy.context.scene.projectPath, "")
        path.replace("\\", "/")
        return float(len(path.split("/"))/20)

class Pipeline(bpy.types.Panel):
    bl_label = "Pipeline"
    bl_idname = "LPQFLV_PT_pipeline_infos_panel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Pipeline"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw_header(self, context) : 
        layout = self.layout
        layout.label(icon="OUTLINER_OB_GREASEPENCIL")
    
    @classmethod
    def poll(cls, context) : 
        if (context.area.ui_type == "PipelineNodeTree" and 
            os.path.exists(context.scene.projectPath)) : 
                return True
            
        return False

    def draw(self, context):
        layout = self.layout
        c = layout.column(align=True) 
        c.operator(ops.PIPE_ReadPipeline.bl_idname, icon="FILE_REFRESH")
        c.operator(ops.PIPE_ArrangeNodes.bl_idname, icon="SHADERFX")
        
        
class MCR_MultiCamRenderPanelOK(bpy.types.Panel):
    """Creates the multi cam render updated panel in the render propertires"""
    
    bl_label = "Multi Camera Render"
    bl_idname = "LPQFLV_PT_Multicam_render_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "output"
    bl_options = {'DEFAULT_CLOSED'}
    
    def isCamera (self) : 
        if cm.cams() : 
            return True

    def calculProgress (self) : 
        tot = bpy.context.scene.frame_end - bpy.context.scene.frame_start + 1
        doned = bpy.context.scene.frame_current - bpy.context.scene.frame_start + 1
        bpy.context.window_manager.mcr_progress = (doned * 1.0)/tot
        bpy.context.window_manager.mcr_progress*=100

        alltot = 0
        allDoned = 0
        for c in cf.MCR.doned : 
            cm = bpy.data.objects[c].data.cm
            allDoned += (cm.end - cm.start + 1)
        for c in cf.MCR.all : 
            cm = bpy.data.objects[c].data.cm
            alltot += (cm.end - cm.start + 1)

        allDoned += doned
        bpy.context.window_manager.mcr_totalProgress = (allDoned*1.0)/alltot
        bpy.context.window_manager.mcr_totalProgress*= 100

    def draw(self, context):
        layout = self.layout
        mcrPanel = context.window_manager.lpqflv_mcr
        cams = cm.cams()

        if cf.MCR.status == mcr.MultiCamRender.FINISHED  : 
            if not cams : 
                r = layout.row()
                r.label(text="You have to create a camera first.", icon="OUTLINER_OB_CAMERA")
                return

            r = layout.row()
            r.prop(context.window_manager, "mcr_toggleRenderCameras", text="Check all to Render")
            for cam in cams :
                row = layout.row(align=True)
                row.label(text=cam.name, icon="CAMERA_DATA")
                if cam.data.isSpecificFrames : 
                    row.prop(cam.data, "isSpecificFrames", text="", icon="RENDERLAYERS")
                    b = layout.box() 
                    for frame in mcr.MultiCamRender.specificFrames(cam.data) : 
                        r = b.row() 
                        r.label(text="Frame : " + frame, icon='IMAGE_DATA')
                        rm = r.operator(ops.MCR_Remove_Specific_Frame.bl_idname, icon='X', text="")
                        rm.frameToRemove = frame
                        rm.cameraName = cam.name
                    r = b.row()
                    r.prop(cam.data, "specificFrame")
                    r.operator(ops.MCR_Add_Specific_Frame.bl_idname, icon='ADD').cameraName = cam.name
                else : 
                    if Cam.needUpdate(cam.data) : 
                        row.prop(cam.data.cm, "start", text="")
                        row.prop(cam.data.cm, "end", text="")
                    else : 
                        c = row.column(align=True)
                        for se in cam.data.cm.startEnds : 
                            r = c.row(align=True)
                            c1 = r.column(align=True)
                            r = c1.row(align=True)
                            r.prop(se, "render", text="")

                            c2 = r.column(align=True)
                            r = c2.row(align=True)
                            if not se.render : 
                                r.enabled = False

                            if se.isRendered :
                                r.label(text="Rendered.")
                            else : 
                                r.prop(se, "start", text="")
                                r.prop(se, "end", text="")
#                                r.prop(se, "disableMotionBlurFirstFrame", text="", icon="RENDERLAYERS")
#                                r.prop(se, "disableMotionBlurLastFrame", text="", icon="RENDERLAYERS")
                            r.prop(se, "isRendered", icon="RENDER_STILL" ,text="")

                    row.separator()
                    row.prop(cam.data, "isSpecificFrames", text="", icon="RENDERLAYERS")
                
            r = layout.row(align=True)
            r.prop(context.scene.cm, "useSampleOverride")
            if (context.scene.cm.useSampleOverride) : 
                r.prop(context.scene.cm, "samples")
            row = layout.row(align=True)
            if bl_utils.isOperatorRegistered("lpqflv.bake_tensions_color_attr") : 
                _set = row.operator("lpqflv.bake_tensions_color_attr", text="Bake Dynamics & Render Animation (MCR)", icon="RENDER_ANIMATION")
                _set.action = "Bake"
                _set.start = context.scene.frame_start
                _set.end = context.scene.frame_end
                _set.ls = "All"
                _set.after = "RenderMulticam"
            else : 
                row.operator(ops.MCR_MkRender.bl_idname, text="Render Animation", icon="RENDER_ANIMATION")
            r = layout.row(align=True)
            r.prop(context.scene, "mcr_outputDir")
            r.operator(ops.MCR_ExportToAe.bl_idname, text="After Effects", icon="EXPORT")
#            row = layout.row() 
#            row.operator (ops.MCR_ReadFramesInfos.bl_idname, text="Update Frames Infos", icon="FILE_REFRESH")
            row = layout.row()
            row.operator(ops.MCR_MkPreview.bl_idname, text="Render Preview", icon="RENDER_ANIMATION")
            row.prop(context.window_manager, "viewportQuality")
            row = layout.row()
            row.prop(context.window_manager, "previewFilepath")
            try : 
                if context.scene.projectPath != "" and context.window_manager.previewFilepath == "" : 
                    context.window_manager.previewFilepath = context.scene.projectPath + "/renders/previews/" 
            except : pass
        
        else : 
            self.calculProgress()
            col = layout.column()
            col.label(text="Rendering : " + cf.MCR.activeCamera + "...")
            col.prop(context.window_manager, "mcr_progress")
            col.prop(context.window_manager, "mcr_totalProgress")
            
        layout.separator()
        row = layout.row() 
        row.prop (mcrPanel, "showTime", text="", icon="TRIA_DOWN")
        row.label (text="Render Time", icon="TIME")
        if mcrPanel.showTime : 
            box = layout.box()
            row = box.row() 
            row.prop (context.window_manager, "secondsPerFrame")
            row = box.row() 
            renderTime = mcr.RenderTime (cf.CM.seqCameras , context.window_manager.secondsPerFrame)
            if self.isCamera() : 
                row.label(text="Render Time Estimation : " + renderTime.getTimeFromCameras())
            else : 
                row.label(text="Render Time Estimation : " + renderTime.getTimeFromScene())

        row = layout.row()
        row.prop(mcrPanel, "showRenderFarm", text="", icon="TRIA_DOWN")
        row.label(text="Render Farm", icon="RENDERLAYERS")
        if mcrPanel.showRenderFarm : 
            if cf.MCR.renderFarm.state == RenderFarm.STOPPED : 
                r = layout.row()
                r.label(text="Computers : ")
                r.operator(rfops.AddComputer.bl_idname, text="", icon="ADD").action = rfops.AddComputer.CREATE
                if len(cf.MCR.renderFarm.computers)>0 : 
                    r.operator(rfops.UpdateCamerasFromFile.bl_idname, text="", icon="FILE_REFRESH")
                for c in cf.MCR.renderFarm.computers : 
                    self.drawComputer(c)
                r = layout.row()
                r.operator(rfops.LaunchRender.bl_idname, icon="RENDER_ANIMATION")
            elif cf.MCR.renderFarm.state == RenderFarm.RENDRING : 
                
                r = layout.row()
                r.label(text="Render Progress : " + str(cf.MCR.renderFarm.getProgress()) + "%")

    def drawComputer(self, c) : 
        b = self.layout.box()
        r = b.row()
        if c.master : 
            r.label(text=c.name, icon="HOME")
        else : 
            r.label(text=c.name, icon="RESTRICT_VIEW_OFF")
        r.separator()
        r.label(text=c.ip)
        r.label(text="(" + str(c.power) + ")")
        op = r.operator(rfops.AddComputer.bl_idname, text="", icon="GREASEPENCIL", emboss=False)
        op.action = rfops.AddComputer.MODIFY
        op.ip = c.ip
        op = r.operator(rfops.AddComputer.bl_idname, text="", icon="X", emboss=False)
        op.action = rfops.AddComputer.REMOVE
        op.ip = c.ip
        r = b.row()
        r.label(text="Cameras : ")
        r.operator(rfops.AddCamera.bl_idname, text="", icon="ADD").computerIp = c.ip
        for cam in c.files[0].cameras : 
            r = b.row()
            r.label(text = cam.name, icon="CAMERA_DATA")
            r.label(text=str(cam.start) + " - " + str(cam.end), icon="MOD_TIME")

class MCR_CameraSettingsPanel(bpy.types.Panel):
    bl_label = "Render Settings"
    bl_idname = "LPQFLV_PT_per_camera_render_settings"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"
    bl_options = {'DEFAULT_CLOSED'}
     
    def drawStartEnd(self, startEnds, idx, layout) : 
        startEnd = startEnds[idx]
        r = layout.row()
        c = r.row(align=True)
        c.prop(startEnd, "start")
        c.prop(startEnd, "end")
        c.prop(startEnd, "step")
        sett = c.operator(ops.MCR_ManageCamSE.bl_idname, text="", icon="X", emboss=False)
        sett.action = ops.MCR_ManageCamSE.REMOVE
        sett.idx = idx

    def draw(self, context) : 
        if context.object.type != 'CAMERA' : 
            return
        cam = context.object.data.cm
        r = self.layout.row(align=True)
        r.label(text="Start & Ends", icon = "TIME")
        if Cam.needUpdate(context.object.data) :
            r = self.layout.row()
            r.label(text="You need to save your scene to see this.", icon = "ERROR")
        else : 
            r.operator(ops.MCR_ManageCamSE.bl_idname, text="", icon="ADD").action = ops.MCR_ManageCamSE.ADD
            r.operator(ops.MCR_ManageCamSE.bl_idname, text="", icon="X").action = ops.MCR_ManageCamSE.CLEAR
            sebox = self.layout.box()
            for i in range(len(cam.startEnds)) :
                self.drawStartEnd(cam.startEnds, i, sebox)
        c = self.layout.column(align=True)
        c.prop(cam, "overrideResolution")
        if cam.overrideResolution : 
            c.prop(cam.res, "res")
            c.prop(cam.res, "resPercentage")
            c.operator(ops.MCR_SetResolutionFromActiveCamera.bl_idname)
        c.prop(cam, "overrideSamples")
        if cam.overrideSamples : 
            c.prop(cam.samples, "use_adaptive_threshold")
            c.prop(cam.samples, "adaptive_threshold")
            c.prop(cam.samples, "samples")
            c.prop(cam.samples, "use_seed", icon="TIME")
#            c.label(text="Bounces : ")
#            bb = c.box()
#            c2 = bb.column(align=True)
#            c2.prop(cam.renderSettings, "diffuse_bounces") 
#            c2.prop(cam.renderSettings, "glossy_bounces") 
#            c2.prop(cam.renderSettings, "trans_bounces") 
#            c2.prop(cam.renderSettings, "volume_bounces") 
#            c2.prop(cam.renderSettings, "transparent_bounces") 
#            c.separator()
#            c.prop(cam.renderSettings, "clamp_direct") 
#            c.prop(cam.renderSettings, "clamp_indirect") 
#            c.prop(cam.renderSettings, "filter_glossy") 
#            c.prop(cam.renderSettings, "caustics_reflective") 
#            c.prop(cam.renderSettings, "caustics_refractice") 
#            c.prop(cam.renderSettings, "volume_step") 
#            c.prop(cam.renderSettings, "use_motion_blur") 
#            c.prop(cam.renderSettings, "shutter") 
#            c.separator()
#            c.prop(cam.renderSettings, "exposure") 
#            c.prop(cam.renderSettings, "use_tiling") 
#            c.prop(cam.renderSettings, "use_persistent_data") 

def drawAutoRenderOutputButton (self, context) : 
    l = self.layout
    r = l.row()
    l.operator(ops.PIPE_SetRenderOutput.bl_idname)
         
class MCR_PanelProps(bpy.types.PropertyGroup) : 
    showTime : bpy.props.BoolProperty(default=False)
    showBatch : bpy.props.BoolProperty(default=False)
    showRenderFarm : bpy.props.BoolProperty(default=False)
                    
def register () : 
    bpy.utils.register_class(CamerasToolPanel)
    bpy.utils.register_class(ProjectPanel)
    bpy.utils.register_class(FileTreeProps)
    bpy.utils.register_class(MCR_PanelProps)
    
    bpy.types.WindowManager.lpqflv_pipelineFiles = bpy.props.PointerProperty(type=FileTreeProps)
    bpy.types.WindowManager.lpqflv_mcr = bpy.props.PointerProperty(type=MCR_PanelProps)
    
    bpy.utils.register_class(FileTree)
    bpy.utils.register_class(Pipeline)
    
    bpy.utils.register_class(MCR_MultiCamRenderPanelOK)
    bpy.utils.register_class(MCR_CameraSettingsPanel)
    bpy.types.RENDER_PT_output.append(drawAutoRenderOutputButton)
    
def unregister () : 
    bpy.utils.unregister_class(FileTreeProps)
    bpy.utils.unregister_class(MCR_PanelProps)
    bpy.utils.unregister_class(FileTree)
    bpy.utils.unregister_class(Pipeline)
    
    bpy.utils.unregister_class(MCR_MultiCamRenderPanelOK)
    bpy.utils.unregister_class(MCR_CameraSettingsPanel)

    bpy.types.RENDER_PT_output.remove(drawAutoRenderOutputButton)
