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

class Incoming_Normals (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Incoming Normals"
    bl_idname = "incomingnormals"

    def createTree (self) : 

        if Incoming_Normals.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Incoming Normals', 'ShaderNodeTree')

            node = self.grp.nodes.new('ShaderNodeNewGeometry')
            node.name = 'Geometry'
            node.location = [-165.89959716796875, -165.89959716796875]
            node.outputs['Position'].default_value = (0.0,0.0,0.0)
            node.outputs['Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Tangent'].default_value = (0.0,0.0,0.0)
            node.outputs['True Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Incoming'].default_value = (0.0,0.0,0.0)
            node.outputs['Parametric'].default_value = (0.0,0.0,0.0)
            node.outputs['Backfacing'].default_value = 0.0
            node.outputs['Pointiness'].default_value = 0.0

            node = self.grp.nodes.new('ShaderNodeNewGeometry')
            node.name = 'Geometry.001'
            node.location = [-175.86135864257812, -175.86135864257812]
            node.outputs['Position'].default_value = (0.0,0.0,0.0)
            node.outputs['Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Tangent'].default_value = (0.0,0.0,0.0)
            node.outputs['True Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Incoming'].default_value = (0.0,0.0,0.0)
            node.outputs['Parametric'].default_value = (0.0,0.0,0.0)
            node.outputs['Backfacing'].default_value = 0.0
            node.outputs['Pointiness'].default_value = 0.0

            node = self.grp.nodes.new('ShaderNodeVectorMath')
            node.name = 'Vector Math'
            node.location = [105.39939880371094, 105.39939880371094]
            node.inputs['Vector'].default_value = (0.5,0.5,0.5)
            node.inputs['Vector'].default_value = (0.5,0.5,0.5)
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.outputs['Value'].default_value = 0.0
            node.operation = 'DOT_PRODUCT'

            node = self.grp.nodes.new('NodeGroupOutput')
            node.name = 'Group Output'
            node.location = [332.5952453613281, 332.5952453613281]
            self.grp.outputs.new('NodeSocketFloat', 'Value')
            node.inputs['Value'].default_value = 0.0
            node.is_active_output = True

            links = self.grp.links
            links.new(self.grp.nodes["Geometry"].outputs[1], self.grp.nodes["Vector Math"].inputs[0])
            links.new(self.grp.nodes["Geometry.001"].outputs[4], self.grp.nodes["Vector Math"].inputs[1])
            links.new(self.grp.nodes["Vector Math"].outputs[1], self.grp.nodes["Group Output"].inputs[0])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Incoming Normals"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Incoming Normals" : 
                return True

        return False







