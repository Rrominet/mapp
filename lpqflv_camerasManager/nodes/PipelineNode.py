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
import os
import mathutils
from lpqflv import lpqflv_popup as pp
from lpqflv import utils
from lpqflv import log
from lpqflv_camerasManager import SeqCamera as sc
from lpqflv_camerasManager import PipelineNodeTree as pnt

 
class SavePipelineNode : 
    def serialize(self) : 
        dict =  SavePipelineNode.staticSerialize(self)
        dict["id"] = self.id
        return dict
    
    def deserialize(self, dict) : 
        SavePipelineNode.staticDeserialize(self, dict)
        
    @staticmethod
    def staticSerialize(Node) : 
        js = {
            "name" : Node.name, 
            "label" : Node.label,
            "height" : Node.dimensions[1], 
            "width" : Node.dimensions[0], 
            "x" : Node.location[0], 
            "y" : Node.location[1],
            "type" : Node.bl_idname,
            "useColor" : Node.use_custom_color,
            "colorR" : Node.color[0],
            "colorG" : Node.color[1],
            "colorB" : Node.color[2],
            "hide" : Node.hide,
        }
        if Node.parent : 
            js["parent"] = Node.parent.name
        
        if Node.bl_idname == "NodeFrame" : 
            js["label_size"] = Node.label_size
            js["shrink"] = Node.shrink

            if Node.text : 
                js["textName"] = Node.text.name
        
        return js
    
    @staticmethod
    def staticDeserialize(Node, dict) : 
        Node.name          = dict["name"]
        Node.height        = dict["height"]
        Node.width         = dict["width"]
        Node.location[0]   = dict["x"]
        Node.location[1]   = dict["y"]
        if "id" in dict : 
            Node.id = dict["id"]
        if "label" in dict : 
            Node.label = dict["label"]
        if "useColor" in dict : 
            Node.use_custom_color = dict["useColor"]
        if "colorR" in dict : 
            Node.color = mathutils.Color((dict["colorR"], dict["colorG"], dict["colorB"]))
        if "hide" in dict : 
            Node.hide = dict["hide"]
        if "parent" in dict : 
            Node.parent = pnt.PipelineNodeTree.get().nodes[dict["parent"]]
            if Node.type == "REROUTE" : 
                Node.location[0] += Node.parent.location[0]
                Node.location[1] += Node.parent.location[1]

        if Node.bl_idname == "NodeFrame" : 
            Node.label_size = dict["label_size"]
            Node.shrink = dict["shrink"]
            txt = bpy.data.texts.get(dict["textName"])
            if txt : 
                Node.text = txt

class PipelineNode (bpy.types.Node, SavePipelineNode) : 
    bl_icon = "NONE"
    
    @classmethod
    def poll(cls, ntree) : 
        can = True
        can = ntree.bl_idname == "PipelineNodeTree"
        
        if not can : 
            return can
        
        can = os.path.exists(bpy.context.scene.projectPath)
        
        if not can :
            pp.popup("You must set your project first ! ", "ERROR")
            return can 
        
        return can
    
    def socket_value_update(self, context) : 
        pass

    def update(self) : 
        updater = self.updater()
        if not updater : 
            self.onUpdate()
            return
        madeSocket = updater.connectionMade()
        if madeSocket : 
            self.onConnectionMade(madeSocket)

        brokeSocket = updater.connectionBroke()
        if brokeSocket : 
            self.onConnectionBroke(brokeSocket)
        self.onUpdate()

    def updater(self) : 
        try : 
            for u in pnt.PipelineNodeTree.get().updater.nodeUpdaters : 
                if u.node.id == self.id : 
                    return u 
        except : return None
        return None

    def onConnectionMade(self, socket) : 
        pass

    def onConnectionBroke(self, socket) : 
        pass

    """You must override this method to fire function on update"""
    def onUpdate(self) : 
        pass
    
    def draw_buttons(self, context, layout):
        layout.label(text="", icon =self.bl_icon)
    
    def pipeline(self) : 
        pipe = pnt.PipelineNodeTree.get() 
        return pipe
        
    def init(self, context) : 
        self.id = utils.uniqId()
        self.pipeline().updater.new(self)

    def free(self) : 
        up = self.updater()
        if up : 
            self.pipeline().updater.nodeUpdaters.remove(self.updater())

    def fromNodes(self) : 
        nodes = []
        for inp in self.inputs : 
            if not inp.links : 
                continue
            nodes.append(inp.links[0].from_node)
        return nodes

    def toNodes(self) : 
        nodes = []
        for out in self.outputs : 
            for l in out.links : 
                nodes.append(l.to_node)
        return nodes

    def linkedInSocket(self) : 
        _ret = []
        for s in self.inputs : 
            if s.is_linked : 
                _ret.append(s)
        return _ret
    
    def prefix(self) : 
        return "Pipe : "

class PipelineNodeBaseProps :
    id : bpy.props.StringProperty()
    updating : bpy.props.BoolProperty()
    working : bpy.props.BoolProperty()

def register () : 
    pass

def unregister () : 
    pass

def isLeft(n1, n2) : 
    if n1 in n2.fromNodes() : 
        return -1
    return 1

