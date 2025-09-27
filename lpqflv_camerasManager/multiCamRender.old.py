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


from lpqflv_camerasManager import config as cf
from lpqflv_camerasManager import CameraManager as cm
from lpqflv import fileTools as ft
from lpqflv import log


import bpy
from threading import Thread
import time
import os
import sys
import shutil
import platform

# Globals
# [(identifier, name, description, icon, number), ...].

# items available for preview render a animation
# reference in WindowManager.viewportQuality
items = [
('BOUNDBOX', "Bounding Box", "", 'PIVOT_BOUNDBOX', 0),
('WIREFRAME', "Wireframe", "", 'SHADING_WIRE', 1),
('SOLID', "Solid", "", 'SHADING_SOLID', 2),
]

RENDER_STAT = "Render not started"
FILE_PATH = ""

DEBUG = False

#classes

class MultiCamRender : 
    def render (self, filepath) : 
        log.replace("render(self, filepath) start.\n", DEBUG)
        oldSequencer = bpy.context.scene.render.use_sequencer
        bpy.context.scene.render.use_sequencer = False
        global RENDER_STAT
    
        for cam in cm.cams() :  
            if not cam.data.cm.render : 
                continue

            for o in bpy.context.scene.objects : 
                for c in o.camerasToExclude : 
                    if c.camera == cam : 
                        if (o.hide_render == False) : 
                            o.hide_render = True
                            o.isHideFromCamera = True
            
            RENDER_STAT = "Render for " + cam.name + " is started."
            
            bpy.context.scene.camera = cam

            if cam.data.isSpecificFrames : 
                frames = MultiCamRender.specificFrames(cam.data)
                frames = MultiCamRender.specificFramestoInt(frames)
                i = 0
                for f in frames : 
                    bpy.context.scene.frame_start = f
                    bpy.context.scene.frame_end = f
                    bpy.context.scene.frame_current = f
                    bpy.context.scene.render.filepath = filepath + cam.name + "/" + cam.name + "_" + str(bpy.context.scene.frame_current)
                    
                    if bpy.context.scene.use_nodes : 
                        for node in bpy.context.scene.node_tree.nodes : 
                            if node.type=="OUTPUT_FILE" : 
                                node.base_path = filepath + node.name + "/" + cam.name + "/"

                    bpy.ops.render.render(write_still=True)

                    tot = len(frames)

                    p = (i/tot) * 100.0
                    if p>100 : 
                        RENDER_STAT = "Render for " + cam.name + " is finished.\n"
                        RENDER_STAT += "The images are in the folder : " + filepath + cam.name + "/"
                    else : 
                    
                        RENDER_STAT = "Render for " + cam.name + " is at " + str(p) + "%."
                    print (RENDER_STAT)
                    i+=1

            else : 
                bpy.context.scene.frame_start = cam.data.cm.start
                bpy.context.scene.frame_end = cam.data.cm.end
                bpy.context.scene.render.filepath = filepath + cam.name + "/"
                
                if bpy.context.scene.use_nodes : 
                    for node in bpy.context.scene.node_tree.nodes : 
                        if node.type=="OUTPUT_FILE" : 
                            node.base_path = filepath + node.name + "/" + cam.name + "/"
                
                tot = bpy.context.scene.frame_end - bpy.context.scene.frame_start + 1
                bpy.context.scene.frame_current = bpy.context.scene.frame_start
                i=0
                while bpy.context.scene.frame_current <= bpy.context.scene.frame_end :
                    bpy.context.scene.render.filepath = filepath + cam.name + "/" + cam.name + "_" + str(bpy.context.scene.frame_current)
                    bpy.ops.render.render(write_still=True)
                    MultiCamRender.writeFramesInfos(cam.name)
                    i+=1
                    bpy.context.scene.frame_current += bpy.context.scene.frame_step

                    p = (i/tot) * 100.0
                    if p>100 : 
                        RENDER_STAT = "Render for " + cam.name + " is finished.\n"
                        RENDER_STAT += "The images are in the folder : " + filepath + cam.name + "/"
                    else : 
                    
                        RENDER_STAT = "Render for " + cam.name + " is at " + str(p) + "%."
                    print (RENDER_STAT)
                
            RENDER_STAT = "Render for " + cam.name + " is finished."
            
            for o in bpy.data.objects : 
                if o.isHideFromCamera : 
                    o.hide_render = False
                    o.isHideFromCamera = False
            
        bpy.context.scene.render.filepath = filepath
        bpy.context.scene.render.use_sequencer = oldSequencer

    def launchQtProgram (self) :
        pass

    @staticmethod
    def writeFramesInfos(currentCamName) : 
        path = cf.ROOT + os.sep 
        if not os.path.exists(path) : 
            return 

        s = ""
        for cam in cm.cams() : 
            if cam.select_get() == True :
                if cam.name == currentCamName : 
                    s += cam.name + "::" + str(bpy.context.scene.frame_current + 1) + ";" + str(cam.data.cm.end) + "##"
                else : 
                    s += cam.name + "::" + str(cam.data.cm.start) + ";" + str(cam.data.cm.end) + "##"

        ft.writeInFile(path + "frames", s)

    @staticmethod
    def readFramesInfos() : 
        if not os.path.exists(cf.ROOT + os.sep + "/frames") : 
            return 
        s = ft.readFileContent(cf.ROOT + os.sep + "/frames")

        tmp = s.split ("##")
        tmp.pop()

        for line in tmp : 
            tmp2 = line.split ("::")
            name = tmp2[0]
            tmp3 = tmp2[1].split (";")
            start = int (tmp3[0])
            end = int (tmp3[1])

            for cam in cm.cams() :
                if cam.name == name : 
                    cam.data.cm.start = start
                    cam.data.cm.end = end

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

class CmdLine (Thread) : 
    def __init__(self, path) : 
        Thread.__init__(self)
        self.path = path

    def run (self) : 
        os.system(self.path)


#onChange funcs
def onTmpCameraChange (self, context) : 
    ok = False
    try : 
        if context.scene.tmpCamera.type != "CAMERA" : 
            for o in bpy.data.objects : 
                if o.type == "CAMERA" : 
                    context.scene.tmpCamera = o
                    ok = True
                if (ok == False) : 
                    context.scene.tmpCamera = None
    except : 
        pass

            
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


class CameraToExcludeItem(bpy.types.PropertyGroup) : 
    camera : bpy.props.PointerProperty(name="camera", type=bpy.types.Object)

def register () : 
    cf.MCR = MultiCamRender ()

    bpy.types.WindowManager.secondsPerFrame = bpy.props.IntProperty(name="Seconds Per Frame", min=0)

    bpy.types.Object.cameraToExcludeIndex = bpy.props.IntProperty(name="Camera to exclude index")
    bpy.types.Scene.tmpCamera = bpy.props.PointerProperty(name="Choose Camera", type=bpy.types.Object, update=onTmpCameraChange)

    bpy.utils.register_class(CameraToExcludeItem)

    bpy.types.Object.camerasToExclude = bpy.props.CollectionProperty(type=CameraToExcludeItem, name="Cameras to exclude", description="Exclude this object from several cameras")
    bpy.types.Object.isHideFromCamera = bpy.props.BoolProperty(default = False)

    
    bpy.types.WindowManager.viewportQuality = bpy.props.EnumProperty(items = items, name="Quality", description="Quality for your preview", default='SOLID')
    bpy.types.WindowManager.previewFilepath = bpy.props.StringProperty(name="Preview output path", description="Path to export your preview", subtype='DIR_PATH')

    bpy.types.Camera.isSpecificFrames = bpy.props.BoolProperty(default = False, options={"LIBRARY_EDITABLE"}, name="Specific Frames", description="Render only specific frames not a frame range.")
    bpy.types.Camera.specificFrames = bpy.props.StringProperty(default = "", options={"LIBRARY_EDITABLE"}, name="Specific Frames to render", description="Render only thes specific frames not a frame range. The synthax is 1,35,68,458,9,35,15,\nThe number followed by a coma.")
    bpy.types.Camera.specificFrame = bpy.props.StringProperty(default ="", options={"LIBRARY_EDITABLE"}, name="Frame", description="Add a new frame to render")

def unregister() : 
    bpy.utils.unregister_class(CameraToExcludeItem)
    del bpy.types.Object.camerasToExclude
