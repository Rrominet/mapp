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

import mathutils
from lpqflv_camerasManager.nodes import PipelineNode as pn
from lpqflv_camerasManager import ops
from lpqflv_camerasManager import PipelineNodeTree as pnt
from lpqflv_camerasManager import Pipeline as p
from lpqflv_camerasManager import pipelineFiles
from lpqflv_camerasManager import config as cfg
from lpqflv import fileTools as ft
from lpqflv_camerasManager.sockets import sockets
from lpqflv import log
from lpqflv import process
from lpqflv import thread
from lpqflv import bl_utils
from lpqflv import lpqflv_popup as pp


import bpy
import bpy.utils.previews 
import os
import shutil
import time
from threading import Thread

        
class SceneElmts : 
    collections = []
    objects = []
    scenes = [] 
    worlds = []
    meshes = []
    materials = []
    lights  = []
    cameras = []
    textures = []
    actions = []
    movies = []
    data = []
    
    def find(self, name, type="") : 
        elmts = (self.collections +
                 self.objects +
                 self.meshes + 
                 self.materials + 
                 self.lights + 
                 self.cameras + 
                 self.textures + 
                 self.actions + 
                 self.movies +
                 self.scenes + 
                 self.worlds + 
                 self.data)
        
        if type == "" : 
            for e in elmts : 
                if e.name == name : 
                    return e 
                    
        for e in elmts : 
            if e.name == name and e.type == type : 
                return e
            
    def getByType(self, type) :
        return getattr(self, type)
    
    def clear(self) : 
        self.collections  = []
        self.objects      = []
        self.meshes       = []
        self.materials    = []
        self.lights       = []
        self.cameras      = []
        self.textures     = []
        self.actions      = []
        self.movies       = []
        self.scenes       = []
        self.worlds       = []
        self.data         = []

class SceneBaseNode (pn.PipelineNode) : 
    bl_idname = "SceneNode"
    bl_label = "Scene Blender"
    bl_icon = "FILE_BLEND" 
    
    sceneType = "NONE"
    sceneTypeIcon = "NONE"
    charType = "modeling"

    sceneElmts = SceneElmts()

    def init(self, context) : 
        super().init(context)
        self.getDirPath()
        self.inputs.new("SceneSocket", "Blend")
        self.inputs.new("FileSocket", "Alembic")
        self.outputs.new("SceneSocket", "Blend")
        
        pnt.PipelineNodeTree.get().sceneNodes.append(self)

    def copy(self, node) : 
        super().init(bpy.context)

        self.content += "_copy"
        self.isCopy = True
        self.copySrc = node.getSceneFullPath()
        self.srcName = node.getSceneFileName()

        ptree =self.pipeline()
        ptree.copying = True
        other_node = ptree.nodes[node.name]
        for _in in other_node.inputs : 
            if not _in.links : 
                continue
            sk = _in.links[0].from_socket
            _input = self.inputs.new(_in.bl_idname, _in.name)
            _input.dataType = _in.dataType
            pnt.PipelineNodeTree.get().links.new(_input, sk)

        ptree.sceneNodes.append(self)
        ptree.copying = False

    def getDirPath(self) : 
        self.dirPath = pnt.PipelineNodeTree.root() + os.sep + self.getSceneType()
        if not os.path.isdir(self.dirPath) : 
            os.makedirs(self.dirPath)
            
    def exists(self) : 
        if self.getLastIncrement() : 
            return True 
        return False
        
    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        self.drawBeforeOpen(context, layout)
        if not self.exists() : 
            if self.isCopy : 
                layout.label(text="File not copied yet.", icon="ERROR")
                layout.operator(ops.PIPE_GenerateScene.bl_idname, icon="COPYDOWN", text="Copy").nodeName = self.name
            else : 
                layout.label(text="File not generated yet.", icon="ERROR")
                layout.operator(ops.PIPE_GenerateScene.bl_idname, icon="FILE_NEW").nodeName = self.name
        else : 
            if self.isCurrent() : 
                r = layout.row(align=True)
                r.operator(ops.PIPE_ExportAsAbc.bl_idname, icon="FILE_CACHE").nodeName = self.name
                r.prop(self, "showAbcSettings", text="", icon="SETTINGS")
                if self.showAbcSettings : 
                    box = layout.box()
                    c = box.column(align=True)
                    c.prop(self, "abcSamples")
                    c.prop(self, "abcSelected")
                    c.prop(self, "abcRenderabe_only")
                    c.prop(self, "abcVisible_objects_only")
                    c.prop(self, "abcExport_hair")
                    c.prop(self, "abcExport_particles")
            else : 
                layout.operator(ops.PIPE_OpenScene.bl_idname, icon="FILE_FOLDER").nodeName = self.name
        if self.working : 
            layout.enabled = False 
        else: 
            layout.enabled = True
        
    def drawBeforeOpen(self, context, layout) : 
        name = self.getSceneFileName()
        img = self.pipeline().icons().pipeline.get(name)
        if img : 
            layout.template_icon(img.icon_id, scale=6)
        layout.label(text="Type : " + self.sceneType, icon=self.sceneTypeIcon)
        
        layout.prop(self, "content", icon="MONKEY")

    def setColor(self) : 
        if not self.exists() : 
            self.use_custom_color = True 
            self.color = (0.6,0,0)
        elif self.color == mathutils.Color((0.6, 0, 0)) :
            self.color = (0.34, 0.34, 0.34)
    
    def sceneContent(self) : 
        self.sceneElmts.clear()
        path = self.getMasterPath()
        if not os.path.exists(path) : 
            pp.popup("You need to create a MASTER file first !", "ERROR")
            return None
        with bpy.data.libraries.load(path) as (data_from, data_to) :
            for bl_type in dir(data_from) : 
                if len ( getattr(data_from, bl_type) ) >0 : 
                    for obj in getattr(data_from, bl_type) : 
                        elmt = SceneElmt(bl_type, obj)
                        try : 
                            l = getattr(self.sceneElmts, elmt.type)
                            l.append(elmt)
                        except : 
                            self.sceneElmts.data.append(elmt)
        return self.sceneElmts
    
    @staticmethod
    def link (filepath, type, name) : 
        with bpy.data.libraries.load(filepath, link=True) as (data_from, data_to): 
            for o in getattr(data_from, type) : 
                if o == name : 
                    getattr(data_to, type).append(o)
            
    def hasUnlinkedBlend(self) : 
        for inp in self.inputs : 
            if inp.name == "Blend" and not inp.is_linked : 
                return True 
        return False

    def hasUnlinkedAbc(self) : 
        for inp in self.inputs : 
            if inp.name == "Alembic" and not inp.is_linked : 
                return True
        return False

    def onUpdate(self) : 
        if not self.pipeline() : 
            return
        if self.pipeline().reading : 
            return
        self.setColor()

    def onConnectionMade(self, socket) : 
        if not self.pipeline() : 
            return
        if self.pipeline().reading or self.pipeline().copying : 
            return
        if self.updating : 
            return

        self.updating = True

        if socket.name == "Blend" : 
            self.inputs.new("SceneSocket", "Blend")
        elif socket.name == "Alembic" : 
            self.inputs.new("FileSocket", "Alembic")
        bpy.ops.pqflv_pipeline.link('INVOKE_DEFAULT', fromNodeName=self.pipeline().links[-1].from_node.name, 
                                            toNodeName = self.name)
        self.updating = False

    def onConnectionBroke(self, sockets) : 
        if self.pipeline().reading : 
            return
        if self.updating : 
            return
        for s in sockets : 
            self.inputs.remove(s)
        if not self.hasUnlinkedBlend() : 
            self.inputs.new("SceneSocket", "Blend")
        if not self.hasUnlinkedAbc() : 
            self.inputs.new("FileSocket", "Alembic")

    def scenes (self, includeMaster=True, includeSmartLinks=False) : 
        blends = pipelineFiles.blendScenes(self.getSceneFullPath(), False, True)
        if not blends : 
            return []

        if not includeMaster :
            for s in blends : 
                if "MASTER" in s : 
                    blends.remove(s)

        if not includeSmartLinks : 
            badBlends = []
            for f in blends : 
                if ".MASTER_smart-link" in f : 
                    badBlends.append(f)
            for f in badBlends : 
                blends.remove(f)
                
        return blends
    
    def getMaster(self) : 
        blends = self.scenes(True)
        master = None
        
        for sc in blends : 
            if "MASTER" in sc : 
                master = sc
                return master
            
        return master
    
    def isMaster (self) : 
        if self.getMaster() : 
            return True
        else : 
            return False
    
    def getLastIncrement(self) : 
        return pipelineFiles.lastIncrementFromScenesList(self.scenes(False))
    
    def getSceneType(self) : 
        scType = self.sceneType.lower().replace(" ", "-").replace("/", "-")
        if scType == "asset" or scType == "character" or scType == "animation" : 
            scType += "s"
        
        return scType
    
    def getSceneFullPath(self) : 
        fullPath = self.dirPath
            
        if self.getSceneType() == "assets" or self.getSceneType() == "characters" :
            fullPath += os.sep + self.content
            
        else : 
            fullPath += os.sep + "seq" + str(self.seq) + "_" + self.content
            
        return fullPath
    
    def getSceneFileName(self) : 
        r_name = self.getSceneType() + "_" + self.content
        return r_name
    
    def getMasterName(self) : 
        return self.getSceneFileName() + ".MASTER.blend"
            
    def createMaster (self) : 
        self.createScene()
        lastIncrement = self.getLastIncrement()
        master = self.getMaster()
        
        if master : 
            f1 = ft.File(self.getSceneFullPath() + "/" + str(lastIncrement)) 
            f2 = ft.File(self.getSceneFullPath() + "/" + master)
            
            if not f1.idem(f2) : 
                shutil.copyfile(f1.path, f2.path)
        
        else : 
            if os.path.exists(self.getMasterPath()) : 
                shutil.copyfile(self.getSceneFullPath() + "/" + str(lastIncrement), 
                            self.getMasterPath())
        
    def getMasterPath(self) : 
        return self.getSceneFullPath() + "/" + self.getMasterName()
    
    def getImagePath(self) : 
        path = self.getMasterPath()
        path = path.replace("MASTER", "MASTER_img")
        path = path.replace(".blend", ".jpg")
        return path
    
    def createScene(self) : 
        if self.sceneExists() : 
            return False
        
        scene = bpy.context.scene
        scene.sceneContent = self.content
        scene.sceneType = self.getSceneType()
        scene.charType = self.charType
        scene.seq = self.getSeq()
        
        bpy.ops.lpqflv_pipeline.new_scene()
        
    def getSeq(self) : 
        try : 
            return self.seq
        except : 
            return 0
    
    def sceneExists(self) : 
        if len(self.scenes())>0 : 
            return True
        else : 
            return False
        
    def generate (self) : 
        if self.content == "" : 
            return
        
        if (self.getSceneType() == "animations" or 
            self.getSceneType() == "lighting-shading" or 
            self.getSceneType() == "render-settings") : 
            if self.seq == 0 : 
                return 
        try : 
            bpy.ops.wm.save_mainfile()
            self.currentScenePath = bpy.data.filepath
        except : pass
        if not self.isCopy : 
            self.createMaster()
        else : 
            self.mkCopy()
        self.setColor()
        try : 
            self.pipeline().updater.terminate()
            bpy.ops.wm.open_mainfile(filepath=self.currentScenePath)
        except : pass

    def mkCopy(self) : 
        shutil.copytree(self.copySrc, self.getSceneFullPath())
        for f in os.listdir(self.getSceneFullPath()) : 
            os.rename(self.getSceneFullPath() + os.sep + f,
                    self.getSceneFullPath() + os.sep + f.replace(self.srcName, self.getSceneFileName()))
        self.isCopy = False
        
    def isCurrent(self) : 
        if bpy.data.filepath == self.getSceneFullPath()  + "/" + self.getLastIncrement(): 
            return True 
        else : 
            return False
    
    def open(self) : 
        try : 
            self.pipeline().updater.terminate()
        except : pass
        self.pipeline().updater = None
        try : 
            bpy.ops.wm.save_mainfile()
        except : 
            pass
        
        path = self.getSceneFullPath()  + os.sep + self.getLastIncrement()
        bpy.ops.wm.open_mainfile(filepath=path)
        
    def openOnProcess(self, pyFile) : 
        """the pyFile if exist will be executed in the scene after opening"""
        args = []
        args.append(bl_utils.blenderExecPath())
        args.append("-b")
        args.append(self.getSceneFullPath() + "/" + self.getLastIncrement())
        args.append("-P")
        args.append(pyFile)
        self.py["working"] = True
        process.launch(args)
        self.py["working"] = False
   
    def importAbc(self, abcPath) : 
        if not self.isCurrent(): 
            basicScript = ft.readFileContent(cfg.ROOT + "/scripts/importAlembic.py")
            goodScript = basicScript.replace("*path*", abcPath)
            tmpScriptPath = cfg.ROOT + "/tmp/importAlembic.py"
            ft.writeInFile(tmpScriptPath, goodScript)
            def dum() : 
                self.openOnProcess(tmpScriptPath)
            t = Thread(target=dum)
            t.start()
        else : 
            bpy.ops.wm.alembic_import(filepath=abcPath)

    def exportAsAbc(self) : 
        path = bpy.data.filepath
        path = path.split(".")
        path = path[:-2]
        path = ".".join(path)
        path += ".abc"
        bpy.ops.wm.alembic_export(filepath=path,
                xsamples = self.abcSamples,
                gsamples = self.abcSamples, 
                selected = self.abcSelected,
                renderable_only = self.abcRenderabe_only,
                visible_objects_only = self.abcVisible_objects_only,
                export_hair = self.abcExport_hair,
                export_particles = self.abcExport_particles,
                uvs=True
                )
        pipe = pnt.PipelineNodeTree.get()
        node = pipe.nodes.new("AlembicNode")
        node.path = path
        node.location.x = self.location.x 
        node.location.y = self.location.y - self.dimensions[1] - 35
        node.width = self.dimensions[0]

    def onContentChange(self, context) : 
        if ("_" in self.content) : 
            self.content = self.content.replace("_", "-")
        self.setColor()
        pn.PipelineNode.socket_value_update(self, context)
        self.name = self.getSceneType() + "_" + self.content
        self.label = self.content
        
    def removeScene(self) : 
        if not self.exists() or pnt.PipelineNodeTree.get().updating: 
            return
        
        shutil.move(self.getSceneFullPath(), p.trash())
        
    def free(self) : 
        self.removeScene()
        try : 
            bpy.utils.previews.remove(self.pcoll)
        except : 
            pass

    def updateSmartLinks(self) : 
        pass

    def createSmartLinkFile(self) : 
        pass

    def smartLinkPath(self, index=0) : 
        return ""

    def smartLinks(self) : 
        r = []
        return r

    def numberOfSmartlinks(self) : 
        return 0

    def smartLinkExists(self, index=0) :
        return False

    @staticmethod
    def increment(path) : 
        tmp = path.replace(".blend", "")
        tmpL = tmp.split(".")
        inc = 0
        try : 
            inc = int(tmpL[-1])
            inc += 1
            path = ".".join(tmpL[:-1]) + "." + str(inc) + ".blend"
            return path
        except : 
            return tmp + ".1.blend"
        
class SceneBaseProps (pn.PipelineNodeBaseProps) : 
    content : bpy.props.StringProperty(default="", description="Content of the scene", update=SceneBaseNode.onContentChange)
    isCopy : bpy.props.BoolProperty()
    copySrc : bpy.props.StringProperty()
    srcName : bpy.props.StringProperty()
    dirPath : bpy.props.StringProperty(default="", description="Path to the scene dir")
    currentScenePath : bpy.props.StringProperty()
    showAbcSettings : bpy.props.BoolProperty(default=False)
    abcSamples : bpy.props.IntProperty(default=1, description="Number of times per frame the animation is exported", name="Samples")
    abcSelected : bpy.props.BoolProperty(default=True, description="Export only selected objects", name="Export only selected")
    abcRenderabe_only : bpy.props.BoolProperty(default=True, description="Export only renderable objects", name="Export only renderable")
    abcVisible_objects_only : bpy.props.BoolProperty(default=False, description="Export only visible layers", name="Export only visible")
    abcExport_hair : bpy.props.BoolProperty(default=True, description="Export hair particles in the alembic", name="Export hair")
    abcExport_particles : bpy.props.BoolProperty(default=True, description="Export particles in the alembic", name="Export particles")
    
class SceneElmt : 
    selected = False
    type = "NONE"
    name = ""
    
    def __init__(self, type, name):
        self.type = type
        self.name = name
