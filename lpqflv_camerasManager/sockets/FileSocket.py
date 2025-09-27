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

class FileSocket(bpy.types.NodeSocket) : 
    '''File Socket''' 
    
    bl_idname = "FileSocket"
    bl_label = "File"
    
    def draw(self, context, layout, node, text) : 
        layout.label(text=text)
    
    def draw_color(self, context, node) : 
        return (.6, .6, .6, 1)
    
    
def register () : 
    bpy.utils.register_class(FileSocket)
    
def unregister() : 
    bpy.utils.unregister_class(FileSocket)
