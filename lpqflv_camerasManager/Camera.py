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

import bpy
if ("Strip" in bpy.types.__dict__):
    bpy.types.Sequence = bpy.types.Strip

from lpqflv_camerasManager import CameraManager as cm
from lpqflv_camerasManager import config  as cf
from lpqflv import bl_events as ev

def sequences() : 
    if not bpy.context.scene.sequence_editor : 
        bpy.context.scene.sequence_editor_create()
    return bpy.context.scene.sequence_editor.sequences

def sequences_all() : 
    if not bpy.context.scene.sequence_editor : 
        bpy.context.scene.sequence_editor_create()
    return bpy.context.scene.sequence_editor.sequences_all

def strip(camera) : 
    if camera.name != camera.data.cm.strip : 
        camera.data.cm.strip = camera.name
    data = camera.data
    return stripFromData(data)

def stripFromData(data) : 
    if data.cm.strip not in sequences_all() : 
        return None
    
    return sequences_all()[data.cm.strip]

def availableChannel() : 
    r_channel = 1
    channels = []
    for seq in sequences() : 
        channels.append(seq.channel)
        
    while r_channel in channels : 
        r_channel += 1
        
    return r_channel

def cameraFromStrip(stripName) : 
    for c in cm.cams() : 
        if c.name == stripName : 
            return c

def activeStrip() : 
    return bpy.context.scene.sequence_editor.active_strip

def isStartEndOk(start, end) : 
    if start <= end : 
        return True  
    else : 
        return False

def createStrip(camera) : 
    if not strip(camera) : 
        ch = availableChannel()
        camStrip = sequences().new_effect(camera.name,
                                       'ADJUSTMENT', 
                                       ch, 
                                       bpy.context.scene.frame_start,
                                       frame_end=bpy.context.scene.frame_end)
        camStrip.cm.isCamera = True
        camStrip.frame_final_start = camera.data.cm.start
        camStrip.frame_final_end = camera.data.cm.end
        camera.data.cm.strip = camStrip.name
        
    else : 
        return
    
def removeStrip(camera) : 
    camStrip = strip(camera)
    if not camStrip : 
        return 
    else : 
        sequences().remove(camStrip)
        camera.data.cm.strip = ""

# on change functions # 
        
def onStartChange (self, ctx) : 
    s = stripFromData(self.id_data)
    if s : 
        s.frame_final_start = self.start

def onEndChange (self, ctx) : 
    s = stripFromData(self.id_data)
    if s : 
        s.frame_final_end = self.end

def onHasStripChange (self, ctx) : 
    if cm.hasStrips() : 
        cm.CameraManager.startCameraLink(ctx.scene)
    else : 
       cf.CM.running = False 

class CameraManagerSeqProps(bpy.types.PropertyGroup) : 
    isCamera : bpy.props.BoolProperty(name="Camera", description="Does this Strip reference a Camera ?", default=False, update=None)

class Resolution(bpy.types.PropertyGroup) :
    res : bpy.props.IntVectorProperty(name="Resolution", default=(0, 0), size=2, options={"LIBRARY_EDITABLE"})
    resPercentage : bpy.props.IntProperty(name="%", default=100, options={"LIBRARY_EDITABLE"}, min=0, max=100, subtype="PERCENTAGE")

class Samples(bpy.types.PropertyGroup) :
    use_adaptive_threshold : bpy.props.BoolProperty(name="Use Adaptive Threshold", default=True, options={"LIBRARY_EDITABLE"})
    adaptive_threshold : bpy.props.FloatProperty(name="Noise Threshold", default=0.01, min = 0.0, options={"LIBRARY_EDITABLE"})
    samples : bpy.props.IntProperty(name="Samples", default=256, min=0, options={"LIBRARY_EDITABLE"})
    use_seed : bpy.props.BoolProperty(name="Use Seed", default=True, options={"LIBRARY_EDITABLE"})
#
#    diffuse_bounces : bpy.props.IntProperty(name="Diffuse", default=0, min=0, options={"LIBRARY_EDITABLE"})
#    glossy_bounces : bpy.props.IntProperty(name="Glossy", default=2, min=0, options={"LIBRARY_EDITABLE"})
#    trans_bounces : bpy.props.IntProperty(name="Transmission", default=24, min=0, options={"LIBRARY_EDITABLE"})
#    volume_bounces : bpy.props.IntProperty(name="Volume", default=0, min=0, options={"LIBRARY_EDITABLE"})
#    transparent_bounces : bpy.props.IntProperty(name="Transparent", default=24, min=0, options={"LIBRARY_EDITABLE"})
#    
#    clamp_direct : bpy.props.FloatProperty(name="Clamp Direct", default=10, min = 0.0, options={"LIBRARY_EDITABLE"})
#    clamp_indirect : bpy.props.FloatProperty(name="Clamp Indirect", default=1, min = 0.0, options={"LIBRARY_EDITABLE"})
#    filter_glossy : bpy.props.FloatProperty(name="Filter Glossy", default=1, min = 0.0, options={"LIBRARY_EDITABLE"})
#    caustics_reflective : bpy.props.BoolProperty(name="Reflective Caustics", default=False, options={"LIBRARY_EDITABLE"})
#    caustics_refractice : bpy.props.BoolProperty(name="Refractive Caustics", default=False, options={"LIBRARY_EDITABLE"})
#    volume_step : bpy.props.FloatProperty(name="Volume Step Rate", default=1, min = 0.0, options={"LIBRARY_EDITABLE"})
#    use_motion_blur : bpy.props.BoolProperty(name="Motion Blur", default=True, options={"LIBRARY_EDITABLE"})
#    shutter : bpy.props.FloatProperty(name="Shutter", default=0.33, min = 0.0, options={"LIBRARY_EDITABLE"})
#    exposure : bpy.props.FloatProperty(name="Exposure", default=1, min = 0.0, options={"LIBRARY_EDITABLE"})
#    use_tiling : bpy.props.BoolProperty(name="Tiling", default=False, options={"LIBRARY_EDITABLE"})
#    use_persistent_data : bpy.props.BoolProperty(name="Persistent Data", default=True, options={"LIBRARY_EDITABLE"})



class StartEndProps(bpy.types.PropertyGroup) :
    start : bpy.props.IntProperty(name="Start", description="Start frame", options={"LIBRARY_EDITABLE"}, update=onStartChange)
    end : bpy.props.IntProperty(name="End", description="End frame", default=250, options={"LIBRARY_EDITABLE"}, update=onEndChange)
    step : bpy.props.IntProperty(name="Step", default=1, options={"LIBRARY_EDITABLE"})
    render : bpy.props.BoolProperty(name="Render", description="Check it if you want to render this camera with the Multi Cam Render", options={"LIBRARY_EDITABLE"},  default=True)
    isRendered : bpy.props.BoolProperty(name="Rendered", description="Check if this camera is already rendered", default=False)
    disableMotionBlurFirstFrame : bpy.props.BoolProperty(name="No Motion Blur 1st frame", description="Disable motion blur on the first frame", options={"LIBRARY_EDITABLE"},  default=False)
    disableMotionBlurLastFrame : bpy.props.BoolProperty(name="No Motion Blur last frame", description="Disable motion blur on the last frame", options={"LIBRARY_EDITABLE"},  default=False)

def onOverrideResolutionChange (self, ctx) :
    self.res.res[0] = ctx.scene.render.resolution_x
    self.res.res[1] = ctx.scene.render.resolution_y
    self.res.resPercentage = ctx.scene.render.resolution_percentage

def onOverrideSamplesChange (self, ctx) :
    self.samples.use_adaptive_threshold = ctx.scene.cycles.use_adaptive_sampling
    self.samples.adaptive_threshold = ctx.scene.cycles.adaptive_threshold
    self.samples.samples = ctx.scene.cycles.samples
    self.samples.use_seed = ctx.scene.cycles.use_animated_seed

class CameraManagerCamProps(bpy.types.PropertyGroup) : 
    bpy.utils.register_class(StartEndProps)
    startEnds : bpy.props.CollectionProperty(type=StartEndProps)

    #for old files compatibility
    start : bpy.props.IntProperty(name="Start", description="Start frame", options={"LIBRARY_EDITABLE"}, update=onStartChange)
    end : bpy.props.IntProperty(name="End", description="End frame", default=250, options={"LIBRARY_EDITABLE"}, update=onEndChange)
    step : bpy.props.IntProperty(name="Step", default=1, options={"LIBRARY_EDITABLE"})
    #

    strip : bpy.props.StringProperty(name="Sequence Strip Name")
    expand : bpy.props.BoolProperty(name="", options={"LIBRARY_EDITABLE"})
    overrideResolution : bpy.props.BoolProperty(name="Override Resolution", options={"LIBRARY_EDITABLE"}, default=False, update=onOverrideResolutionChange)
    bpy.utils.register_class(Resolution)
    res: bpy.props.PointerProperty(type=Resolution)

    overrideSamples : bpy.props.BoolProperty(name="Override Samples", options={"LIBRARY_EDITABLE"}, default=False, update=onOverrideSamplesChange)
    bpy.utils.register_class(Samples)
    samples: bpy.props.PointerProperty(type=Samples)
    scene : bpy.props.StringProperty(name="Background Scene", options={"LIBRARY_EDITABLE"})

class CameraManagerObjectProps(bpy.types.PropertyGroup) : 
    hasStrip : bpy.props.BoolProperty(name="Has a Strip", description="Has a Strip to manage the start and the end frame", update=onHasStripChange)

class CameraManagerSceneProps(bpy.types.PropertyGroup) : 
    local : bpy.props.BoolProperty(name="Only display locals", description="Only display the cameras in the active scene.\nIf off, all the cameras in the blend data will be displayed", default=True)
    search : bpy.props.StringProperty(name="Search", description="Only display the cameras that contains the text")
    disableMotionBlurFrames : bpy.props.StringProperty(name="No Motion Blur Frames", description="Disable motion blur on specefic frames, separated by comma", default="")

    useSampleOverride : bpy.props.BoolProperty(name="Override Samples", options={"LIBRARY_EDITABLE"}, default=False)
    samples : bpy.props.IntProperty(name="Samples", default=256, min=0, options={"LIBRARY_EDITABLE"})

def needUpdate(c) : 
    return (len(c.cm.startEnds) == 0)

def updateOldCamera(c) : 
    if len(c.cm.startEnds) == 0 : 
        prop = c.cm.startEnds.add()
        prop.start = c.cm.start
        prop.end = c.cm.end
        prop.step = c.cm.step

from bpy.app.handlers import persistent
@persistent
def initOldCameras(dum=None, dum2=None) : 
    for c in bpy.data.cameras : 
        updateOldCamera(c)

def register () : 
    bpy.utils.register_class(CameraManagerSeqProps)
    bpy.utils.register_class(CameraManagerCamProps)
    bpy.utils.register_class(CameraManagerObjectProps)
    bpy.utils.register_class(CameraManagerSceneProps)

    bpy.types.Sequence.cm = bpy.props.PointerProperty(type=CameraManagerSeqProps)
    bpy.types.Camera.cm = bpy.props.PointerProperty(type=CameraManagerCamProps)
    bpy.types.Object.cm = bpy.props.PointerProperty(type=CameraManagerObjectProps)
    bpy.types.Scene.cm = bpy.props.PointerProperty(type=CameraManagerSceneProps)

    ev.add(initOldCameras, ev.LOAD)
    ev.add(initOldCameras, ev.SAVE_PRE)

def unregister () :
    bpy.utils.unregister_class(CameraManagerSeqProps)
    bpy.utils.unregister_class(CameraManagerCamProps)
    bpy.utils.unregister_class(CameraManagerObjectProps)
    bpy.utils.unregister_class(CameraManagerSceneProps)
    bpy.utils.unregister_class(Resolution)

    del bpy.types.Sequence.cm
    del bpy.types.Camera.cm
    del bpy.types.Object.cm
    del bpy.types.Scene.cm
