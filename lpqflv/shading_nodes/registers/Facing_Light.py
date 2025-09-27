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

class Facing_LightOperator(bpy.types.Operator):
    bl_idname = "shading_nodes.facinglight_operator"
    bl_label = "Facing Light"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'ShaderNodeTree'

    def execute(self, context):
        bpy.ops.node.add_node(type="facinglight")
        return {"FINISHED"}

def drawFacing_LightMenu(self, context) : 
    col = self.layout.column(align=True)
    col.operator(Facing_LightOperator.bl_idname)

#register#

bpy.utils.register_class(Facing_Light)
bpy.utils.register_class(Facing_LightOperator)
bpy.types.NODE_MT_category_shader_input.append (drawFacing_LightMenu)









