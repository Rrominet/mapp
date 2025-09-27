import bpy 
from lpqflv import json2 as json
import json as JSON 
from lpqflv import bl_addons
from lpqflv import thread
from lpqflv_camerasManager import CameraManager as cm
import os

ROOT = bl_addons.addonsPath() + os.sep + "lpqflv_camerasManager" + os.sep + "renderFarm"

class RenderFarm : 
    STOPPED = 1; 
    RENDRING = 2;
    def __init__(self, project = "") : 
        self.computers = []
        self.project = project
        self.state = RenderFarm.STOPPED

    def serialize(self)  : 
        d = {}
        d["project"] = self.project
        d["computers"] = []

        for c in self.computers : 
            d["computers"].append(c.serialize())
        return JSON.dumps(d)

    def save(self) : 
        if len(self.computers)<1 : 
            return
        bpy.context.scene.lpqflv_renderFarm.jsonStr = self.serialize()

    def read(self) : 
        self.deserialize(bpy.context.scene.lpqflv_renderFarm.jsonStr)

    def deserialize(self, string) : 
        if string == "" : 
            return
        js = JSON.loads(string)
        self.project = js["project"]
        self.computers = []
        for c in js["computers"] : 
            com = Computer()
            com.deserialize(c)
            self.computers.append(com)

    def computerFromIp(self, ip) : 
        for c in self.computers : 
            if c.ip == ip : 
                return c

        return None

    def sort(self) : 
        sorted(self.computers, key=lambda computer: computer.power)

    def createCamerasFromScene(self) : 
        if len(self.computers) == 0 : 
            return 

        self.updatePowers(self.masterComputer())

        # reinitialise all
        for c in self.computers : 
            c.files[0].cameras = []

        toRender = []
        for o in bpy.data.objects : 
            if o.type == "CAMERA" and o.data.cm.render : 
                toRender.append(o)

        cameras = []
        for c in toRender : 
            cameras.append(Camera(c.name, c.data.cm.start, c.data.cm.end))

        self.sort()
        sorted(cameras, key=lambda camera : camera.imagesNumber())

        for cam in cameras : 
            start = cam.start
            for c in self.computers : 
                if c == self.computers[-1] : 
                    c.files[0].cameras.append(Camera(cam.name, start, cam.end))
                else : 
                    toCalcul = int(c.ratio() * cam.imagesNumber())
                    c.files[0].cameras.append(Camera(cam.name,
                        start,
                        toCalcul + start))
                    start += toCalcul + 1

    #freeze is the coputer that the power will not move
    def updatePowers(self, master=None) : 
        tot = 0
        for c in self.computers : 
            tot += c.power

        dif = 100 - tot

        if not master : 
            self.computers[0].power += dif
        else : 
            for c in self.computers : 
                if c == master : 
                    c.power += dif
                    return

    def masterComputer(self) : 
        for c in self.computers : 
            if c.master : 
                return c

        return None

    def removeComputer(self, c) : 
        for com in self.computers : 
            if com == c : 
                self.computers.remove(c)
                return True

        return False

    def render(self) : 
        cmd = ROOT + os.sep + "client" + os.sep + "render-farm-client '" + self.serialize() + "'"
        os.system(cmd)
        self.state = RenderFarm.STOPPED

    def startRender(self) : 
        # stuff to prevent bugs
        bpy.ops.file.make_paths_relative()
        bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath.replace(".blend", "_render.blend"))
        self.updateComputersFiles()

        #start the command on thread
        self.state = RenderFarm.RENDRING
        thread.startOnObj(RenderFarm.render, self)

    def getProgress(self) : 
        doned = 0
        tot = 0
        for cam in cm.cams() : 
            output = bpy.path.abspath(bpy.context.scene.render.filepath) + os.sep + cam.name + os.sep
            output = output.replace(os.sep + os.sep, os.sep)
            if os.path.exists(output) : 
                doned += len(os.listdir(output))

        for c in cm.cams() : 
            tot += cm.imagesToRender(c)
            #reprendre ICI

        pg = doned*1.0/tot
        return round(pg*100, 2)

    def updateComputersFiles(self) : 
        for c in self.computers : 
            c.files[0].path = bpy.data.filepath

class Computer : 
    def __init__(self, name="", ip="", power = 10, master = False) : 
        self.name = name
        self.ip = ip 

        #The Master computer is the one where the files will be written
        self.master = master

        #Time to start the render
        self.start = 0

        #Time to end the render if it's not finished
        self.end = 0

        self.power = power

        self.files = []
        self.files.append(File(bpy.data.filepath))

    def serialize(self) : 
        d = json.classToDict(self)
        d["files"] = []
        for f in self.files : 
            d["files"].append(f.serialize())

        return d

    def deserialize(self, js) : 
        self.name = js["name"]
        self.ip = js["ip"]
        self.master = js["master"]
        self.start = js["start"]
        self.end = js["end"]
        self.power = js["power"]
        self.files = []

        for f in js["files"] : 
            fi = File()
            fi.deserialize(f)
            self.files.append(fi)

    def ratio(self) : 
        return self.power*0.01

class File : 
    def __init__(self, path="") : 
        if path : 
            self.path = path
        else : 
            self.path = bpy.data.filepath
        self.cameras = []

    def serialize(self) : 
        d = {}
        d["path"] = bpy.data.filepath
        d["cameras"] = []
        for c in self.cameras : 
            d["cameras"].append(c.serialize())

        return d

    def deserialize(self, js) : 
        self.path = bpy.data.filepath
        self.cameras = []
        for c in js["cameras"] : 
            cam = Camera("dum")
            cam.deserialize(c)
            self.cameras.append(cam)

    def cameraByName(self, name) : 
        for c in self.cameras : 
            if c == name : 
                return c
        return None

class Camera : 
    def __init__(self, name, start=-1, end=-1) : 
        self.name = name
        self.start = start
        self.end = end

    def serialize(self) : 
        return json.classToDict(self)
    
    def deserialize(self, js) : 
        self.name = js["name"]
        self.start = js["start"]
        self.end = js["end"]

    def imagesNumber(self) : 
        return self.end - self.start

