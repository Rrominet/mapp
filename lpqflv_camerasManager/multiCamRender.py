import bpy 
import os

from lpqflv import fileTools as ft
from lpqflv import bl_events
from lpqflv_camerasManager import CameraManager as cm
from lpqflv_camerasManager import config as cfg

from lpqflv_camerasManager.renderFarm import RenderFarm as rf

class MultiCamRender : 
    WAITING = 0
    RENDERING = 1
    FINISHED = -1
    def __init__(self) : 
        #save cameras names, not pointers
        self.toRender = []
        self.all = []
        self.doned = []
        self.activeCamera = ""
        self.renderSettings = RenderSetings()
        self.status = MultiCamRender.FINISHED
        self.renderFarm = rf.RenderFarm()

    #TODO the disableMotionBlur don't work for now because it can't be included in the current systen (render in animation, need to render frame by frame)
    def preRender(self) : 
        self.renderSettings.get(bpy.context.scene)
        for c in cm.cams() : 
            for sed in c.data.cm.startEnds : 
                if sed.render and not sed.isRendered :
                    self.toRender.append({"name" : c.name, "start" : sed.start, "end" : sed.end, "step" : sed.step, "scene" : c.data.cm.scene, "disableMotionBlurFirstFrame" : sed.disableMotionBlurFirstFrame, "disableMotionBlurLastFrame" : sed.disableMotionBlurLastFrame})
            self.all.append(c.name)

    def hasSpecific(self) : 
        for c in cm.cams() : 
            #TODO : should add a render attribute here too.
            if c.data.isSpecificFrames : 
                return True 
        return False

    def startRender(self, modal=True) : 
        bpy.context.window_manager.isAutoUpdateCam = False
        self.preRender()
        if len(self.toRender) == 0 :
            self.status = MultiCamRender.FINISHED
            return
        self.render(self.toRender[0])
        if modal : 
            bl_events.add(MultiCamRender.onRenderEnd, bl_events.RENDER_COMPLETE)
            bl_events.add(MultiCamRender.onRenderCancelled, bl_events.RENDER_CANCEL)

    def overrideSettings(self, data) :
        cm = bpy.data.objects[data["name"]].data.cm
        if not cm.overrideResolution : 
            bpy.context.scene.render.resolution_x = self.renderSettings.resolution[0]
            bpy.context.scene.render.resolution_y = self.renderSettings.resolution[1]
            bpy.context.scene.render.resolution_percentage = self.renderSettings.resolutionPercentage
        else : 
            bpy.context.scene.render.resolution_x = cm.res.res[0]
            bpy.context.scene.render.resolution_y = cm.res.res[1]
            bpy.context.scene.render.resolution_percentage = cm.res.resPercentage

        if not cm.overrideSamples : 
            bpy.context.scene.cycles.use_adaptive_sampling = self.renderSettings.use_adaptive_threshold
            bpy.context.scene.cycles.adaptive_threshold = self.renderSettings.adaptive_threshold
            bpy.context.scene.cycles.samples = self.renderSettings.samples
            bpy.context.scene.cycles.use_animated_seed = self.renderSettings.use_seed
        else : 
            bpy.context.scene.cycles.use_adaptive_sampling = cm.samples.use_adaptive_threshold
            bpy.context.scene.cycles.adaptive_threshold = cm.samples.adaptive_threshold
            bpy.context.scene.cycles.samples = cm.samples.samples
            bpy.context.scene.cycles.use_animated_seed = cm.samples.use_seed
        
    def render(self, data, modal=True)  : 
        self.overrideSettings(data)
        c = bpy.data.objects[data["name"]].data
        sc = bpy.context.scene
        sc.frame_start = data["start"]
        sc.frame_end = data["end"]
        sc.frame_step = data["step"]
        sc.camera = bpy.data.objects[data["name"]]
        if (data["scene"] != "" and data["scene"] != sc.name) : 
            sc.background_set = bpy.data.scenes[data["scene"]]

        sc.render.filepath = self.renderSettings.filepath + os.sep + data["name"] + os.sep + data["name"] + "_"
        
        for fo in self.renderSettings.fileOutputs : 
            fo.node(sc).base_path = fo.filepath + os.sep + "compositing_" + data["name"] + os.sep + data["name"] + "_"

        if not c.isSpecificFrames : 
            if modal : 
                bpy.ops.render.render('INVOKE_DEFAULT', animation=True)
                self.toRender.remove(data)
            else : 
                bpy.ops.render.render(animation=True)
            self.activeCamera = data["name"]
            cfg.MCR.status = MultiCamRender.RENDERING
        else : 
            filepath = sc.render.filepath
            frames = MultiCamRender.specificFrames(c)
            frames = MultiCamRender.specificFramestoInt(frames)
            i = 0
            for f in frames : 
                sc.frame_start = f
                sc.frame_end = f
                sc.frame_current = f
                sc.render.filepath = filepath + str(sc.frame_current)
                bpy.ops.render.render(write_still=True)
                i+=1
               
                tot = len(frames)
                p = (i/tot) * 100.0
                p = round(p, 2)
                RENDER_STAT = ""
                if p>100 : 
                    RENDER_STAT = "Render for " + data["name"] + " is finished.\n"
                else : 
                    RENDER_STAT = "Render for " + data["name"] + " is at " + str(p) + "%."
                print (RENDER_STAT)

    def scene(self) : 
        return bpy.data.window_managers[0].windows[0].scene
    
    def window(self) : 
        return bpy.data.window_managers[0].windows[0]

    def window_manager(self) : 
        return bpy.data.window_managers[0]

    @staticmethod
    def onRenderEnd(dum1=None, dum2=None) : 
        if len(cfg.MCR.toRender) == 0 or cfg.MCR.status == MultiCamRender.FINISHED : 
            bl_events.remove(MultiCamRender.onRenderEnd, bl_events.RENDER_COMPLETE)
            bl_events.remove(MultiCamRender.onRenderCancelled, bl_events.RENDER_CANCEL)
            cfg.MCR.renderSettings.reset(cfg.MCR.scene())
            cfg.MCR.status = MultiCamRender.FINISHED
            return

        cfg.MCR.doned.append(cfg.MCR.activeCamera)
        cfg.MCR.activeCamera = ""
        cfg.MCR.status = MultiCamRender.WAITING

    @staticmethod
    def onRenderCancelled(dum1=None, dum2=None) : 
        bl_events.remove(MultiCamRender.onRenderEnd, bl_events.RENDER_COMPLETE)
        bl_events.remove(MultiCamRender.onRenderCancelled, bl_events.RENDER_CANCEL)
        cfg.MCR.status = MultiCamRender.FINISHED
        cfg.MCR.renderSettings.reset(cfg.MCR.scene())

    def onTimer(self) : 
        if self.status == MultiCamRender.WAITING : 
            self.render(self.toRender[0])

    @staticmethod
    def specificFrames (cameraData) :
        string = cameraData.specificFrames
        frames = string.split(",")

        i = 0 
        while i<len(frames) : 
            if frames[i] == "" : 
                frames.pop(i)
            i+=1

        return frames

    @staticmethod
    def removeSpecificFrame(cameraData, frame) : 
        frames = MultiCamRender.specificFrames(cameraData)
        newFrames = []
        for f in frames : 
            if f != frame : 
                newFrames.append(f)

        cameraData.specificFrames = ",".join(newFrames) + ","

    @staticmethod
    def specificFramestoInt (framesList) : 
        return list(map(int, framesList))

class RenderSetings : 
    def __init__(self) : 
        self.filepath = ""
        self.frame_start = 0
        self.frame_end = 0
        self.activeCamera = ""
        self.activeBgScene = ""
        self.resolution = []
        self.resolutionPercentage = 100
        self.use_adaptive_threshold = True
        self.adaptive_threshold = 0.01
        self.samples = 256
        self.use_seed = True

        self.fileOutputs = []

    def get(self, sc) : 
        self.filepath = sc.render.filepath
        self.frame_start = sc.frame_start
        self.frame_end = sc.frame_end
        if sc.camera : 
            self.activeCamera = sc.camera.name
        
        if sc.background_set : 
            self.activeBgScene = sc.background_set.name

        self.fileOutputs = FileOutput.all(sc)
        self.resolution = [sc.render.resolution_x, sc.render.resolution_y]
        self.resolutionPercentage = sc.render.resolution_percentage
        self.use_adaptive_threshold = sc.cycles.use_adaptive_sampling
        self.adaptive_threshold = sc.cycles.adaptive_threshold
        if sc.cm.useSampleOverride :
            self.samples = sc.cm.samples
        else :
            self.samples = sc.cycles.samples
        self.use_seed = sc.cycles.use_animated_seed

    def reset(self, sc) : 
        sc.render.filepath = self.filepath
        sc.frame_start = self.frame_start 
        sc.frame_end = self.frame_end
        if self.activeCamera != "" :
            sc.camera = bpy.data.objects[self.activeCamera]
        if self.activeBgScene != "" :
            sc.background_set = bpy.data.scenes[self.activeBgScene]

        for fo in self.fileOutputs : 
            fo.node(sc).base_path = fo.filepath

        sc.render.resolution_x = self.resolution[0]
        sc.render.resolution_y = self.resolution[1]
        sc.render.resolution_percentage = self.resolutionPercentage

        sc.cycles.use_adaptive_sampling = self.use_adaptive_threshold 
        sc.cycles.adaptive_threshold = self.adaptive_threshold
        sc.cycles.samples = self.samples
        sc.cycles.use_animated_seed = self.use_seed

class FileOutput : 
    def __init__(self, name, filepath) : 
        self.name = name
        self.filepath = filepath

    def node(self, sc) : 
        return sc.node_tree.nodes[self.name]

    @staticmethod
    def all(sc) : 
        fileOutputs = []
        if not sc.node_tree :
            return fileOutputs
        for n in sc.node_tree.nodes : 
            if n.bl_idname == "CompositorNodeOutputFile" : 
                fo = FileOutput (n.name, n.base_path)
                fileOutputs.append(fo)

        return fileOutputs

class RenderTime : 
    def __init__ (self, seqCams, pSecondsPerFrame) : 
        self.seqCams = seqCams
        self.secondsPerFrame = pSecondsPerFrame
        self.totalSeconds = 0
        
    def getTimeFromScene (self) : 
        totalFrames = bpy.context.scene.frame_end - bpy.context.scene.frame_start
        self.totalSeconds = totalFrames*self.secondsPerFrame
        heureString = self.getTime(self.totalSeconds)
        return heureString
        
    def getTime (self, pSeconds) : 
        m, s = divmod(pSeconds, 60)
        h, m = divmod(m, 60)
        heureString = str(h) + " houres, " + str(m) + " minutes " + str(s) + " seconds"
        return heureString
        
    def getTimeFromCameras (self) : 
        self.totalSeconds = 0
        for cam in cm.cams() : 
            if not cam.data.cm.render : 
                continue 

            difference = cam.data.cm.end - cam.data.cm.start
            self.totalSeconds += difference
            
        self.totalSeconds =  self.totalSeconds * self.secondsPerFrame            
        heureString = self.getTime(self.totalSeconds)
        return heureString

def onRenderCamerasUpdate(self, context) : 
    for c in cm.cams() : 
        for se in c.data.cm.startEnds :
            if not se.isRendered or (se.isRendered and context.window_manager.mcr_seeRendered) : 
                se.render = self.mcr_toggleRenderCameras

def register() : 
    cfg.MCR = MultiCamRender()
    bpy.types.WindowManager.secondsPerFrame = bpy.props.IntProperty(name="Seconds Per Frame", min=0)
    
    items = [
    ('BOUNDBOX', "Bounding Box", "", 'PIVOT_BOUNDBOX', 0),
    ('WIREFRAME', "Wireframe", "", 'SHADING_WIRE', 1),
    ('SOLID', "Solid", "", 'SHADING_SOLID', 2),
    ('MATERIAL', "EEVEE", "", 'NODE_MATERIAL', 3),
    ]
    bpy.types.WindowManager.viewportQuality = bpy.props.EnumProperty(items = items, name="Quality", description="Quality for your preview", default='SOLID')
    bpy.types.WindowManager.previewFilepath = bpy.props.StringProperty(name="Preview output path", description="Path to export your preview", subtype='DIR_PATH')

    bpy.types.Camera.isSpecificFrames = bpy.props.BoolProperty(default = False, options={"LIBRARY_EDITABLE"}, name="Specific Frames", description="Render only specific frames not a frame range.")
    bpy.types.Camera.specificFrames = bpy.props.StringProperty(default = "", options={"LIBRARY_EDITABLE"}, name="Specific Frames to render", description="Render only thes specific frames not a frame range. The synthax is 1,35,68,458,9,35,15,\nThe number followed by a coma.")
    bpy.types.Camera.specificFrame = bpy.props.StringProperty(default ="", options={"LIBRARY_EDITABLE"}, name="Frame", description="Add a new frame to render")

    bpy.types.WindowManager.mcr_progress = bpy.props.FloatProperty(name="Camera Progress", default = 0.0, max=100.0, subtype="PERCENTAGE")
    bpy.types.WindowManager.mcr_totalProgress = bpy.props.FloatProperty(name="Total Progress", default = 0.0, max=100.0, subtype="PERCENTAGE")
    bpy.types.WindowManager.mcr_toggleRenderCameras = bpy.props.BoolProperty(name="Render cameras", description="Desactivate/activate render propertie for each cameras", update=onRenderCamerasUpdate)
    bpy.types.WindowManager.mcr_seeRendered = bpy.props.BoolProperty(name="Rendered", default=False)
    bpy.types.Scene.mcr_outputDir = bpy.props.StringProperty(name="AE Path", subtype='DIR_PATH')

def unregister() : 
    pass
