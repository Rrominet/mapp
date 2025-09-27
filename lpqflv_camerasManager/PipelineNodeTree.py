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
import bpy.utils.previews
from bpy.app.handlers import persistent
import os
import json
from concurrent.futures import ThreadPoolExecutor
from functools import cmp_to_key

from lpqflv import lpqflv_popup as pp
from lpqflv import fileTools as ft
from lpqflv import bl_utils
from lpqflv_camerasManager import config as cfg
from lpqflv_camerasManager.nodes import PipelineNode as pn
from lpqflv_camerasManager import icons as ic
from lpqflv_camerasManager import Pipeline
from lpqflv_camerasManager.PipelineUpdater import PipelineUpdater

pipelineIcons = None 

class PipelineNodeTree (bpy.types.NodeTree) : 
    '''Manage your pipeline with Nodes ! '''
    bl_idname = 'PipelineNodeTree'
    bl_label = 'Pipeline Editor'
    bl_icon = 'NODE_SEL'
    
    assets = None 
    characters = None 
    animations = None 
    lightings = None 
    renderSettings = None
    
    sceneNodes = []
    
    assetNodes = []
    characterNodes = []
    animationNodes = []
    lightingNodes = []
    renderSettingsNodes = []
    
    deleteEmptyDataSocket : bpy.props.BoolProperty(default=True)
    deleteEmptySockets : bpy.props.BoolProperty(default=True)
    
    updating : bpy.props.BoolProperty(default=False)
    
    handlerRunning : bpy.props.BoolProperty(default = False)
    
    saving : bpy.props.BoolProperty(default = False)
    reading : bpy.props.BoolProperty(default = False)
    copying : bpy.props.BoolProperty(default = False)

    updater = None
    
    @classmethod
    def poll(cls, context):
        return True
    
    @staticmethod
    def create() : 
        for nt in bpy.data.node_groups : 
            if nt.bl_idname == "PipelineNodeTree" : 
                return nt
            
        if not os.path.exists(bpy.context.scene.projectPath) : 
            pp.popup("You must set your project first ! ", "ERROR")
            return False
        
        pipe = bpy.data.node_groups.new("Pipeline", PipelineNodeTree.bl_idname)
        pipe.updater = PipelineUpdater()
        pipe.updater.pnt = pipe
        return pipe
    
    @staticmethod
    def get() : 
        pipes = []
        
        for nt in bpy.data.node_groups : 
            if nt.bl_idname == "PipelineNodeTree" : 
                pipes.append(nt)
        
        if len(pipes) == 0 : 
            return None
                
        i=1
        while i < len(pipes) : 
            bpy.data.node_groups.remove(pipes[i])
            i+=1
            
        return pipes[0]
    
    @staticmethod
    def root() : 
        return Pipeline.project()
    
    def clear(self) : 
        self.updating = True
        self.nodes.clear()
        self.clearInternalMemory()
        self.updating = False
        
    def clearInternalMemory(self) : 
        self.sceneNodes = []
        self.assetNodes = []
        self.characterNodes = []
        self.animationNodes = []
        self.lightingNodes = []
        self.renderSettingsNodes = []
    
    def read(self, scenes) : 
        self.updater = PipelineUpdater()
        self.clear()
        for s in scenes : 
            if s.nodeType == "None" : 
                continue
            node = self.nodes.new(s.nodeType)
            node.name = s.filename.replace(".blend", "")
            node.content = s.content
            try : 
                node.seq = s.seq
            except : 
                pass
    def updateInternalMemory(self) :
        self.clearInternalMemory()
        
        nodesType = (
            ("AssetSceneNode", "assetNodes"),
            ("CharModSceneNode", "characterNodes"),
            ("CharRigSceneNode", "characterNodes"),
            ("AnimSceneNode", "animationNodes"),
            ("LightingSceneNode", "lightingNodes"),
            ("RenderSceneNode", "renderSettingsNodes")
        )
        
        for n in self.nodes : 
            for nt in nodesType : 
                if n.bl_idname == nt[0] : 
                    tmp = getattr(self, nt[1])
                    tmp.append(n)
                    setattr(self, nt[1], tmp)
                    self.sceneNodes.append(n)

    @staticmethod
    def placeNodes(nodes, marge = 25): 
        xMarge = marge*4
        sortedNodes = []
        for n in nodes : 
            sortedNodes.append(n)
        sortedNodes.sort(key=cmp_to_key(pn.isLeft))
        
        x = 0 
        y = 0
        for i in range(len( sortedNodes)) :
            if i == 0 : 
                sortedNodes[i].location = (x,y)

            if i<len(sortedNodes) - 1 : 
                if sortedNodes[i+1] in sortedNodes[i].toNodes() : 
                    x += xMarge + sortedNodes[i].dimensions[0]
                else : 
                    y += marge + sortedNodes[i].dimensions[1]
                sortedNodes[i+1].location = (x,y)
        
        for sc in bpy.data.screens : 
            for a in sc.areas : 
                if a.ui_type == "PipelineNodeTree" : 
                    a.tag_redraw()    

    def setDefaultPos(self, readJson=False) : 
        self.icons().clear()
        
        for n in self.nodes : 
            n.location = (0,0)

        PipelineNodeTree.placeNodes(self.nodes)
        
        read = False
        if readJson : 
            read = self.readJson()
                
    def serialize(self) : 
        nodes = []
        for n in self.nodes : 
            if n.bl_idname != "NodeFrame" and n.bl_idname != "NodeReroute" : 
                nodes.append(n.serialize())
            else : 
                nodes.append(pn.PipelineNode.staticSerialize(n))
            
        links = []
        for l in self.links : 
            sl = {
                    "fromSocketType"   : l.from_socket.bl_idname, 
                    "fromSocketName"   : l.from_socket.name, 
                    "toSocketType"     : l.to_socket.bl_idname,
                    "toSocketName"     : l.to_socket.name,
                    "fromNode"         : l.from_node.name,
                    "toNode"           : l.to_node.name,
                    "toSocketDataType" : ""
                  }
            
            if hasattr(l.to_socket, "dataType") : 
                sl["toSocketDataType"] = l.to_socket.dataType
            
            links.append(sl)
            
        return {
                    "nodes" : nodes, 
                    "links" : links
                }
    
    def deserialize(self, dict) : 
        self.deleteEmptySockets = False
        self.saving = True
        self.reading = True
        for nd in dict["nodes"] : 
            if self.nodes.find (nd["name"]) == -1 : 
                n = self.nodes.new(nd["type"])
                n.name = nd["name"]
                
            if nd["type"] == "NodeFrame" or nd["type"] == "NodeReroute" : 
                pn.PipelineNode.staticDeserialize(self.nodes[nd["name"]], nd)
            else : 
                self.nodes[nd["name"]].deserialize(nd)
            
        for ld in dict["links"] : 
            fromSocket = self.nodes[ld["fromNode"]].outputs.find(ld["fromSocketName"])
            if fromSocket == -1 : 
                fromSocket = self.nodes[ld["fromNode"]].outputs.new(ld["fromSocketType"], ld["fromSocketName"]) 
            else : 
                fromSocket =  self.nodes[ld["fromNode"]].outputs[ld["fromSocketName"]]
            
            toNode = self.nodes[ld["toNode"]]
            if toNode.type == "REROUTE" : 
                toSocket = toNode.inputs[0]
            else : 
                toSocket = toNode.inputs.new(ld["toSocketType"], ld["toSocketName"]) 

            try : toSocket.dataType = ld["toSocketDataType"]
            except : pass
            
            self.links.new(fromSocket, toSocket)
        
        self.deleteEmptySockets = True
        self.saving = False
        self.reading = False
        
    def savedJson(self) : 
        return json.dumps(self.serialize(), indent=2)
    
    @staticmethod
    def write() : 
        pipe = PipelineNodeTree.get()
        pipe.saving = True
        print("Pipeline saving..")
        ft.writeInFile(cfg.pipelineFile(), pipe.savedJson()) 
        pipe.saving = False
        print("Pipeline saved. ")
    
    def save(self) : 
        if self.saving : 
            return
        exec = ThreadPoolExecutor(max_workers=1) 
        exec.submit(PipelineNodeTree.write)
        
    @persistent
    def saveHandler(scene) : 
        pipe = PipelineNodeTree.get()
        if pipe : 
            pipe.save()
        
    def readJson(self) : 
        if not os.path.exists(cfg.pipelineFile()) : 
            return False
        
        s = ft.readFileContent(cfg.pipelineFile())
        dict = json.loads(s)
        self.deserialize(dict)
        return True
    
    def update(self) : 
        pass
#        self.updater.getNodes()
    
    def updateNodes(self) : 
        self.updateInternalMemory() 
        for n in self.sceneNodes : 
            n.setColor()
            self.reloadIcon(n)
            
    @persistent
    def onOpenningScene(scene) : 
        pip = PipelineNodeTree.get()
        if pip : 
            pip.handlerRunning = False
            bpy.ops.pqflv_pipeline.update_pipeline_nodes('INVOKE_DEFAULT')
            bpy.ops.pqflv.start_stop_pipe_handler('INVOKE_DEFAULT')
            
    def icons(self) : 
        return cfg.icons
    
    def reloadIcon(self, node) : 
        name = node.getSceneFileName()
        path = node.getImagePath()
        if not os.path.exists(path) : 
            return
        img = self.icons().pipeline.get(name)
        if not img : 
            self.icons().newIcon("pipeline", name, path)
            return 
        
        if self.icons().getInfos("pipeline", name).hasChanged() : 
            self.icons().remove("pipeline", name)
            self.icons().newIcon("pipeline", name, path)
            
def register () : 
    bl_utils.addHandler(PipelineNodeTree.saveHandler, bpy.app.handlers.save_post)
    bl_utils.addHandler(PipelineNodeTree.onOpenningScene, bpy.app.handlers.load_post)
    
    global pipelineIcons
    pipelineIcons = bpy.utils.previews.new()

def unregister () : 
    bl_utils.removeHandler(PipelineNodeTree.saveHandler, bpy.app.handlers.save_post)
    bl_utils.removeHandler(PipelineNodeTree.onOpenningScene, bpy.app.handlers.load_post)
    
    cfg.icons.pipeline.close()
