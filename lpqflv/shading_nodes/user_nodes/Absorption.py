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

class Absorption (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Absorption"
    bl_idname = "absorption"

    def createTree (self) : 

        if Absorption.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Absorption', 'ShaderNodeTree')

            node = self.grp.nodes.new('ShaderNodeMath')
            node.name = 'Math.003'
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.5
            node.outputs['Value'].default_value = 0.0
            node.operation = 'MULTIPLY'
            node.use_clamp = False

            node = self.grp.nodes.new('ShaderNodeMath')
            node.name = 'Math.001'
            node.inputs['Value'].default_value = 10.0
            node.inputs['Value'].default_value = 1.7300024032592773
            node.outputs['Value'].default_value = 0.0
            node.operation = 'MULTIPLY'
            node.use_clamp = False

            node = self.grp.nodes.new('ShaderNodeMath')
            node.name = 'Math'
            node.inputs['Value'].default_value = 2.7182817459106445
            node.inputs['Value'].default_value = 2.7182817459106445
            node.outputs['Value'].default_value = 0.0
            node.operation = 'POWER'
            node.use_clamp = False

            node = self.grp.nodes.new('ShaderNodeLightPath')
            node.name = 'Light Path'
            node.outputs['Is Camera Ray'].default_value = 0.0
            node.outputs['Is Shadow Ray'].default_value = 0.0
            node.outputs['Is Diffuse Ray'].default_value = 0.0
            node.outputs['Is Glossy Ray'].default_value = 0.0
            node.outputs['Is Singular Ray'].default_value = 0.0
            node.outputs['Is Reflection Ray'].default_value = 0.0
            node.outputs['Is Transmission Ray'].default_value = 0.0
            node.outputs['Ray Length'].default_value = 0.0
            node.outputs['Ray Depth'].default_value = 0.0
            node.outputs['Diffuse Depth'].default_value = 0.0
            node.outputs['Glossy Depth'].default_value = 0.0
            node.outputs['Transparent Depth'].default_value = 0.0
            node.outputs['Transmission Depth'].default_value = 0.0

            node = self.grp.nodes.new('NodeGroupOutput')
            node.name = 'Group Output'
            self.grp.outputs.new('NodeSocketColor', 'Color')
            node.inputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.is_active_output = True

            node = self.grp.nodes.new('ShaderNodeNewGeometry')
            node.name = 'Geometry'
            node.outputs['Position'].default_value = (0.0,0.0,0.0)
            node.outputs['Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Tangent'].default_value = (0.0,0.0,0.0)
            node.outputs['True Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Incoming'].default_value = (0.0,0.0,0.0)
            node.outputs['Parametric'].default_value = (0.0,0.0,0.0)
            node.outputs['Backfacing'].default_value = 0.0
            node.outputs['Pointiness'].default_value = 0.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.name = 'Mix'
            node.inputs['Fac'].default_value = 0.5
            node.inputs['Color1'].default_value = (1.0,0.7594030499458313,0.4953795075416565,1.0)
            node.inputs['Color2'].default_value = (0.0,0.0,0.0,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MIX'
            node.use_alpha = False
            node.use_clamp = False

            node = self.grp.nodes.new('NodeGroupInput')
            node.name = 'Group Input'
            self.grp.inputs.new('NodeSocketFloat', 'Factor')
            self.grp.inputs.new('NodeSocketColor', 'Color1')
            self.grp.inputs.new('NodeSocketColor', 'Color2')
            node.outputs['Factor'].default_value = 1.7300024032592773
            node.outputs['Color1'].default_value = (1.0,0.7594030499458313,0.4953795075416565,1.0)
            node.outputs['Color2'].default_value = (0.0,0.0,0.0,1.0)

            links = self.grp.links
            links.new(self.grp.nodes['Light Path'].outputs['Ray Length'], self.grp.nodes['Math.003'].inputs['Value'])
            links.new(self.grp.nodes['Geometry'].outputs['Backfacing'], self.grp.nodes['Math.003'].inputs[1])
            links.new(self.grp.nodes['Math.003'].outputs['Value'], self.grp.nodes['Math.001'].inputs['Value'])
            links.new(self.grp.nodes['Math'].outputs['Value'], self.grp.nodes['Mix'].inputs['Fac'])
            links.new(self.grp.nodes['Math.001'].outputs['Value'], self.grp.nodes['Math'].inputs['Value'])
            links.new(self.grp.nodes['Mix'].outputs['Color'], self.grp.nodes['Group Output'].inputs['Color'])
            links.new(self.grp.nodes['Group Input'].outputs['Factor'], self.grp.nodes['Math.001'].inputs[1])
            links.new(self.grp.nodes['Group Input'].outputs['Color1'], self.grp.nodes['Mix'].inputs['Color1'])
            links.new(self.grp.nodes['Group Input'].outputs['Color2'], self.grp.nodes['Mix'].inputs['Color2'])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Absorption"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Absorption" : 
                return True

        return False







