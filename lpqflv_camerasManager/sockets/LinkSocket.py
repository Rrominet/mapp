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

class LinkSocket(bpy.types.NodeSocket) : 
    '''Blend Socket''' 
    
    bl_idname = "LinkSocket"
    bl_label = "Blend"
    
    dataType : bpy.props.StringProperty()
    
    def draw(self, context, layout, node, text) : 
        layout.label(text=text)
    
    def draw_color(self, context, node) : 
        if self.dataType == "collection" : 
            return (.8, .2, .35, 1)
    
        elif self.dataType == "world" : 
            return (0, 0, .5, 1)
    
        elif self.dataType == "scene" : 
            return (.5, .7, .2, 1)
    
        elif self.dataType == "object" : 
            return (1, .8, 0, 1)
    
        elif self.dataType == "action" : 
            return (1, .7, 0, 1)
    
        elif self.dataType == "camera" : 
            return (.218, .007, .4623, 1)
    
        elif self.dataType == "mesh" or self.dataType == "meshe" : 
            return (0, .455, .60, 1)
    
        elif self.dataType == "light" : 
            return (1, 1, 0, 1)
    
        elif self.dataType == "movie" : 
            return (0.393, 0, .25, 1)
        
        elif self.dataType == "material" : 
            return (0, 0.729, 0.01, 1)
    
        elif self.dataType == "texture" : 
            return (.393, .0033, 0, 1)
    
        elif self.dataType == "data" : 
            return (.1, .4, 1, 1)
        
        return (0,0,0,1)
    
    
    
def register () : 
    bpy.utils.register_class(LinkSocket)
    
def unregister() : 
    bpy.utils.unregister_class(LinkSocket)
