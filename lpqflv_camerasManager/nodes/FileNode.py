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

from lpqflv_camerasManager.nodes import PipelineNode as pn
import mathutils


import bpy 
import os

class FileBaseNode(pn.PipelineNode, pn.PipelineNodeBaseProps) : 
    
    bl_idname = "FileNode"
    bl_label = "File"
    bl_icon = "FILE"
    
    def init(self, context) : 
        self.outputs.new("FileSocket", "File")
    
    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.prop(self, "path", icon="FILE_TICK")
        if not self.exists() : 
            layout.label(text="File not found", icon="ERROR")

 
    def onPathChange(self, context) : 
        self.setColor()
        tmp = self.path.replace("\\", "/").split("/")
        self.label = tmp[len(tmp)-1]

    def setColor(self) : 
        if not self.exists() : 
            self.use_custom_color = True 
            self.color = (0.6,0,0)
        elif self.color == mathutils.Color((0.6, 0, 0)) :
            self.color = (0.34, 0.34, 0.34)

    def exists(self) : 
        return os.path.exists(self.absPath())

    def absPath(self) : 
        return bpy.path.abspath(self.path)

    def serialize(self) : 
        dict = super().serialize()
        dict["path"] = self.path
        return dict

    def deserialize(self, dict) : 
        super().deserialize(dict)
        if "path" in dict :
            self.path = dict["path"]


class FileProps (pn.PipelineNodeBaseProps) : 
    path : bpy.props.StringProperty(name="path", subtype="FILE_PATH", description="File location on the hard drive", update=FileBaseNode.onPathChange)

      
class FileNode (FileBaseNode, FileProps) : 
    
    bl_label = "File"
        
        
def register() : 
    bpy.utils.register_class (FileNode) 
    
def unregister () : 
    bpy.utils.unregister_class (FileNode) 
