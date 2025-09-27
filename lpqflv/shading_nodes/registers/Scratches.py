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

class ScratchesOperator(bpy.types.Operator):
    bl_idname = "shading_nodes.scratches_operator"
    bl_label = "Scratches"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'ShaderNodeTree'

    def execute(self, context):
        bpy.ops.node.add_node(type="scratches")
        return {"FINISHED"}

def drawScratchesMenu(self, context) : 
    col = self.layout.column(align=True)
    col.operator(ScratchesOperator.bl_idname)

#register#

bpy.utils.register_class(Scratches)
bpy.utils.register_class(ScratchesOperator)
bpy.types.NODE_MT_category_texture_input.append (drawScratchesMenu)









