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

class Rust_ShaderOperator(bpy.types.Operator):
    bl_idname = "shading_nodes.rustshader_operator"
    bl_label = "Rust Shader"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'ShaderNodeTree'

    def execute(self, context):
        bpy.ops.node.add_node(type="rustshader")
        return {"FINISHED"}

def drawRust_ShaderMenu(self, context) : 
    col = self.layout.column(align=True)
    col.operator(Rust_ShaderOperator.bl_idname)

#register#

bpy.utils.register_class(Rust_Shader)
bpy.utils.register_class(Rust_ShaderOperator)
bpy.types.NODE_MT_category_shader_input.append (drawRust_ShaderMenu)









