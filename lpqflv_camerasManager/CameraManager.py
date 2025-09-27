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


from . import Camera as cam
from . import config as cfg


import bpy 
from bpy.app.handlers import persistent

class CameraManager : 
    def __init__(self) : 
        self.seqCameras = [] 
        self.running = False
        
    def updateSeqCameras(self) : 
        self.updateFrom3DView() 
        
    def updateFrom3DView(self) : 
        seqs = cam.sequences_all()
        for s in seqs : 
            if s.cm.isCamera : 
                if s.name in bpy.context.scene.objects and bpy.context.scene.objects[s.name].type == "CAMERA" : 
                    pass #all is good the seq and the cmaera exists
                else : 
                    cam.sequences().remove(s)
                    
        for c in cams() : 
            if c.cm.hasStrip : 
                cam.createStrip(c)
            else : 
                cam.removeStrip(c)
                    
    def updateFromSequencer(self) : 
        s = cam.activeStrip() 
        if not s : 
            return 
        camera = cam.cameraFromStrip(s.name) 
        if not camera : 
            return
        camera.data.cm.start = s.frame_final_start
        camera.data.cm.end = s.frame_final_end
                
    @staticmethod
    def linkSelections(view) : 
        if view == "VIEW_3D" : 
            active = bpy.context.view_layer.objects.active
            if active and active.type == "CAMERA" :
                if active.data.cm.strip in cam.sequences() :
                    bpy.context.scene.sequence_editor.active_strip = cam.sequences()[active.data.cm.strip]
            for c in cams() : 
                if c.data.cm.strip in cam.sequences() : 
                    cam.sequences()[c.data.cm.strip].select = c.select_get()
        
        elif view == "SEQUENCE_EDITOR" : 
            if bpy.context.mode != "OBJECT" : 
                return

            oneSelected = False
            for seq in bpy.context.scene.sequence_editor.sequences : 
                if seq.select : 
                    oneSelected = True 
                    break

            if not oneSelected : 
                return

            if cam.activeStrip() : 
                camera = cam.cameraFromStrip(cam.activeStrip().name)
                if camera : 
                    bpy.context.view_layer.objects.active = camera
            
            for strip in cam.sequences() : 
                if strip.cm.isCamera : 
                    camera = cam.cameraFromStrip(strip.name)
                    if camera : 
                        camera.select_set(strip.select)
    
    @staticmethod
    def updateActiveCam (scene) : 
        for camera in cams() : 
            if CameraManager.isActive(camera, scene.frame_current) : 
                scene.camera = camera
                return

    @staticmethod
    def isActive(camera, currentFrame) : 
        inTime = CameraManager.isInTime(camera, currentFrame)
        if not inTime: 
            return False
        seq = cam.strip(camera)
        if not seq : 
            return inTime
        else : 
            for s in cam.sequences() : 
                if s.cm.isCamera : 
                    if s.channel > seq.channel and (CameraManager.isInTime(cam.cameraFromStrip(s.name), currentFrame)) : 
                        return False
            return True
    
    @staticmethod
    def isInTime(camera, frame) :
        if not camera : 
            return False
        for se in camera.data.cm.startEnds :
            if se.start <= frame and frame < se.end : 
                return True
        return False

    @staticmethod
    def onAutoCameraChangeUpdate(self, context) : 
        wm = context.window_manager
        if self.isAutoUpdateCam == True : 
            if CameraManager.updateActiveCam not in bpy.app.handlers.frame_change_pre :
                bpy.app.handlers.frame_change_pre.append(CameraManager.updateActiveCam)
        else : 
            if CameraManager.updateActiveCam in bpy.app.handlers.frame_change_pre :
                bpy.app.handlers.frame_change_pre.remove(CameraManager.updateActiveCam)
        
    @persistent
    def startCameraLink(scene) : 
        if not hasStrips() : 
            return
        if not bpy.context.scene.sequence_editor : 
            bpy.context.scene.sequence_editor_create()
        
        cfg.CM.updateFrom3DView()
        if not cfg.CM.running : 
            bpy.ops.lpqfl.modal_camera_events_handler('INVOKE_DEFAULT')
            
    def register(self) : 
        if CameraManager.startCameraLink not in bpy.app.handlers.load_post : 
            bpy.app.handlers.load_post.append(CameraManager.startCameraLink)
    
    def unregister(self) : 
        if self.running : 
            self.running = False
            
        if CameraManager.startCameraLink in bpy.app.handlers.load_post : 
            bpy.app.handlers.load_post.remove(CameraManager.startCameraLink)
            
        if CameraManager.updateActiveCam in bpy.app.handlers.frame_change_pre : 
            bpy.app.handlers.frame_change_pre.remove(CameraManager.updateActiveCam)


def cams() : 
    cams = []
    scene = bpy.context.scene
    if scene.cm.local : 
        for o in scene.objects : 
            if o.type == "CAMERA" : 
                cams.append(o)
    else : 
        for o in bpy.data.objects : 
            if o.type == "CAMERA" : 
                cams.append(o)
    return sorted(cams, key=lambda cam: cam.name)

def hasStrips() : 
    for c in cams() : 
        if c.cm.hasStrip : 
            return True

    return False

def imagesToRender(camera) : 
    cm = camera.data.cm
    inter = cm.end - cm.start
    return inter + 1

# ls is a list of name from existing cameras in scene
# if ls empty, all cameras in scene are used
def nameToNew(ls=[], padding=2) : 
    if not ls : 
        ls = []
        cms = cams()
        for c in cms : 
            ls.append(c.name)

    ls.sort()
    lastIndex = 0
    numberOfZero = padding

    for c in ls : 
        if not "plan" in c : 
            continue
        number = c.split("-")[-1]
        number = number.split("_")[-1]
        try : 
            lastIndex = int(number)
        except :
            continue

    if lastIndex + 1 >= 10 : 
        numberOfZero = 1
    if lastIndex +1 >=100 : 
        numberOfZero = 0

    last = ""
    if len(ls) > 0 :
        last = ls[-1]
    return "plan-"+str(lastIndex+1).zfill(numberOfZero +1), last
