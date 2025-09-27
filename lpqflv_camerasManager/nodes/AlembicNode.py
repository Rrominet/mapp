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
from lpqflv_camerasManager.nodes import FileNode as fn


import os
import bpy 

class AlembicProps (fn.FileProps) : 
    pass
class AlembicBaseNode(fn.FileBaseNode, pn.PipelineNodeBaseProps) : 
    
    bl_idname = "AlembicNode"
    bl_label = "Alembic"
    bl_icon = "FILE_CACHE"
    
    def init(self, context) : 
        self.outputs.new("FileSocket", "Alembic")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "path", icon="FILE_TICK")
        if not self.exists() : 
            layout.label(text="Alembic not found", icon="ERROR")

class AlembicNode (AlembicBaseNode, AlembicProps) : 
    
    bl_label = "Alembic"
        
        
def register() : 
    bpy.utils.register_class (AlembicNode) 
    
def unregister () : 
    bpy.utils.unregister_class (AlembicNode) 
