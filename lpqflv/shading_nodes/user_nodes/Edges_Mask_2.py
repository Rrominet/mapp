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

class Edges_Mask_2 (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Edges Mask 2"
    bl_idname = "edgesmask2"

    def createTree (self) : 

        if Edges_Mask_2.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Edges Mask 2', 'ShaderNodeTree')

            node = self.grp.nodes.new('ShaderNodeNewGeometry')
            node.outputs['Position'].default_value = (0.0,0.0,0.0)
            node.outputs['Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Tangent'].default_value = (0.0,0.0,0.0)
            node.outputs['True Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Incoming'].default_value = (0.0,0.0,0.0)
            node.outputs['Parametric'].default_value = (0.0,0.0,0.0)
            node.outputs['Backfacing'].default_value = 0.0
            node.outputs['Pointiness'].default_value = 0.0
            node.outputs['Random Per Island'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -215.21771240234375
            node.location[1] = -69.68142700195312
            node.mute = False
            node.name = 'Geometry'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeBevel')
            node.inputs['Radius'].default_value = 0.06999988853931427
            node.inputs['Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Normal'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -217.56475830078125
            node.location[1] = 69.68141174316406
            node.mute = False
            node.name = 'Bevel'
            node.samples = 4
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeVectorMath')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Scale'].default_value = 1.0
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 16.62152099609375
            node.location[1] = 25.767745971679688
            node.mute = False
            node.name = 'Vector Math'
            node.operation = 'DOT_PRODUCT'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketFloat', 'Radius')
            self.grp.inputs['Radius'].default_value = 0.06999988853931427
            self.grp.inputs['Radius'].min_value = 0.0
            self.grp.inputs['Radius'].max_value = 1000.0
            node.outputs['Radius'].default_value = 0.06999988853931427
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -417.56475830078125
            node.location[1] = -0.0
            node.mute = False
            node.name = 'Group Input'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupOutput')
            self.grp.outputs.new('NodeSocketColor', 'Color')
            node.inputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.is_active_output = True
            node.label = ''
            node.location[0] = 407.56475830078125
            node.location[1] = -0.0
            node.mute = False
            node.name = 'Group Output'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeInvert')
            node.inputs['Fac'].default_value = 1.0
            node.inputs['Color'].default_value = (0.0,0.0,0.0,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 217.56475830078125
            node.location[1] = 13.336807250976562
            node.mute = False
            node.name = 'Invert'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            links = self.grp.links
            links.new(self.grp.nodes["Invert"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Bevel"].outputs[0], self.grp.nodes["Vector Math"].inputs[0])
            links.new(self.grp.nodes["Geometry"].outputs[1], self.grp.nodes["Vector Math"].inputs[1])
            links.new(self.grp.nodes["Vector Math"].outputs[1], self.grp.nodes["Invert"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Bevel"].inputs[0])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Edges Mask 2"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Edges Mask 2" : 
                return True

        return False







