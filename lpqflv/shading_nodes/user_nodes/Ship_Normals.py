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

class Ship_Normals (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Ship Normals"
    bl_idname = "shipnormals"

    def createTree (self) : 

        if Ship_Normals.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Ship Normals', 'ShaderNodeTree')

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketFloat', 'Scale')
            self.grp.inputs['Scale'].default_value = 1.0
            self.grp.inputs['Scale'].min_value = -10000.0
            self.grp.inputs['Scale'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketVector', 'Vector')
            self.grp.inputs['Vector'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['Vector'].min_value = -3.4028234663852886e+38
            self.grp.inputs['Vector'].max_value = 3.4028234663852886e+38
            self.grp.inputs.new('NodeSocketFloatFactor', 'Strength')
            self.grp.inputs['Strength'].default_value = 1.0
            self.grp.inputs['Strength'].min_value = 0.0
            self.grp.inputs['Strength'].max_value = 1.0
            self.grp.inputs.new('NodeSocketFloat', 'Distance')
            self.grp.inputs['Distance'].default_value = 1.0
            self.grp.inputs['Distance'].min_value = 0.0
            self.grp.inputs['Distance'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketVector', 'Normal')
            self.grp.inputs['Normal'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['Normal'].min_value = -1.0
            self.grp.inputs['Normal'].max_value = 1.0
            node.outputs['Scale'].default_value = 1.0
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.outputs['Strength'].default_value = 1.0
            node.outputs['Distance'].default_value = 1.0
            node.outputs['Normal'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1314.5416259765625
            node.location[1] = -118.06291198730469
            node.mute = False
            node.name = 'Group Input'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('brick3d')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Color1'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            node.inputs['Color2'].default_value = (0.03698683902621269,0.03698683902621269,0.03698683902621269,1.0)
            node.inputs['Mortar'].default_value = (0.0,0.0,0.0,1.0)
            node.inputs['Scale'].default_value = 16.299999237060547
            node.inputs['Mortar Size'].default_value = 0.009999999776482582
            node.inputs['Mortar Smooth'].default_value = 0.10000000149011612
            node.inputs['Bias'].default_value = 0.0
            node.inputs['Brick Width'].default_value = 0.30000001192092896
            node.inputs['Row Height'].default_value = 1.25
            node.outputs['Color'].default_value = (0.0,0.0,0.0,1.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 259.746826171875
            node.location[1] = 294.6636657714844
            node.mute = False
            node.name = 'Brick 3D'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 649.657958984375
            node.location[1] = 202.26974487304688
            node.mute = False
            node.name = 'Math'
            node.operation = 'MULTIPLY'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeValToRGB')
            node.inputs['Fac'].default_value = 0.5
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.outputs['Alpha'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.color_ramp.color_mode = 'RGB'
            node.color_ramp.hue_interpolation = 'NEAR'
            node.color_ramp.interpolation = 'LINEAR'
            element = node.color_ramp.elements.new(0.0)
            element.color = (0.0,0.0,0.0,1.0)
            element.alpha = 1.0
            element.position = 0.0
            element = node.color_ramp.elements.new(1.0)
            element.color = (1.0,1.0,1.0,1.0)
            element.alpha = 1.0
            element.position = 1.0
            node.hide = False
            node.label = ''
            node.location[0] = 472.38623046875
            node.location[1] = -286.3913879394531
            node.mute = False
            node.name = 'ColorRamp'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 905.23046875
            node.location[1] = 7.98516845703125
            node.mute = False
            node.name = 'Math.001'
            node.operation = 'MULTIPLY'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupOutput')
            self.grp.outputs.new('NodeSocketVector', 'Normal')
            self.grp.outputs.new('NodeSocketFloat', 'Value')
            node.inputs['Normal'].default_value = (0.0,0.0,0.0)
            node.inputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.is_active_output = True
            node.label = ''
            node.location[0] = 1357.714599609375
            node.location[1] = 0.0
            node.mute = False
            node.name = 'Group Output'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('brick3d')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Color1'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            node.inputs['Color2'].default_value = (0.10300524532794952,0.10300524532794952,0.10300524532794952,1.0)
            node.inputs['Mortar'].default_value = (0.0,0.0,0.0,1.0)
            node.inputs['Scale'].default_value = 10.199999809265137
            node.inputs['Mortar Size'].default_value = 0.009999999776482582
            node.inputs['Mortar Smooth'].default_value = 0.10000000149011612
            node.inputs['Bias'].default_value = 0.09999999403953552
            node.inputs['Brick Width'].default_value = 0.8999999761581421
            node.inputs['Row Height'].default_value = 1.25
            node.outputs['Color'].default_value = (0.0,0.0,0.0,1.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 252.35107421875
            node.location[1] = -10.950103759765625
            node.mute = False
            node.name = 'Brick 3D.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeBump')
            node.inputs['Strength'].default_value = 1.0
            node.inputs['Distance'].default_value = 1.0
            node.inputs['Height'].default_value = 1.0
            node.inputs['Height_dx'].default_value = 1.0
            node.inputs['Height_dy'].default_value = 1.0
            node.inputs['Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Normal'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.invert = False
            node.label = ''
            node.location[0] = 1157.714599609375
            node.location[1] = -142.53114318847656
            node.mute = False
            node.name = 'Bump'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexVoronoi')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 2.3500001430511475
            node.inputs['Smoothness'].default_value = 1.0
            node.inputs['Exponent'].default_value = 0.5
            node.inputs['Randomness'].default_value = 0.09166663885116577
            node.outputs['Distance'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.outputs['Position'].default_value = (0.0,0.0,0.0)
            node.outputs['W'].default_value = 0.0
            node.outputs['Radius'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.distance = 'EUCLIDEAN'
            node.feature = 'F1'
            node.hide = False
            node.label = ''
            node.location[0] = 252.38623046875
            node.location[1] = -294.6636657714844
            node.mute = False
            node.name = 'Voronoi Texture'
            node.show_options = True
            node.show_preview = False
            node.show_texture = True
            node.use_custom_color = False
            node.voronoi_dimensions = '3D'
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 80.16311645507812
            node.location[1] = -115.47309112548828
            node.mute = False
            node.name = 'Reroute'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 1.0
            node.inputs['Value'].default_value = 2.3499999046325684
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -232.80279541015625
            node.location[1] = -311.5643615722656
            node.mute = False
            node.name = 'Math.005'
            node.operation = 'MULTIPLY'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -652.4853515625
            node.location[1] = -116.71839141845703
            node.mute = False
            node.name = 'Reroute.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 1.0
            node.inputs['Value'].default_value = 10.199999809265137
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -271.0848388671875
            node.location[1] = 28.498247146606445
            node.mute = False
            node.name = 'Math.004'
            node.operation = 'MULTIPLY'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 1.0
            node.inputs['Value'].default_value = 16.299999237060547
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -69.23126220703125
            node.location[1] = 405.0591735839844
            node.mute = False
            node.name = 'Math.002'
            node.operation = 'MULTIPLY'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 1.0
            node.inputs['Value'].default_value = 0.009999999776482582
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -107.96986389160156
            node.location[1] = 173.52493286132812
            node.mute = False
            node.name = 'Math.003'
            node.operation = 'MULTIPLY'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            links = self.grp.links
            links.new(self.grp.nodes["Reroute"].outputs[0], self.grp.nodes["Brick 3D"].inputs[0])
            links.new(self.grp.nodes["Voronoi Texture"].outputs[1], self.grp.nodes["ColorRamp"].inputs[0])
            links.new(self.grp.nodes["Brick 3D"].outputs[0], self.grp.nodes["Math"].inputs[0])
            links.new(self.grp.nodes["Brick 3D.001"].outputs[0], self.grp.nodes["Math"].inputs[1])
            links.new(self.grp.nodes["Math"].outputs[0], self.grp.nodes["Math.001"].inputs[0])
            links.new(self.grp.nodes["ColorRamp"].outputs[0], self.grp.nodes["Math.001"].inputs[1])
            links.new(self.grp.nodes["Math.001"].outputs[0], self.grp.nodes["Bump"].inputs[2])
            links.new(self.grp.nodes["Bump"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Reroute"].outputs[0], self.grp.nodes["Brick 3D.001"].inputs[0])
            links.new(self.grp.nodes["Math.001"].outputs[0], self.grp.nodes["Group Output"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Bump"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Bump"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Bump"].inputs[5])
            links.new(self.grp.nodes["Reroute.001"].outputs[0], self.grp.nodes["Math.002"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Reroute"].inputs[0])
            links.new(self.grp.nodes["Reroute"].outputs[0], self.grp.nodes["Voronoi Texture"].inputs[0])
            links.new(self.grp.nodes["Reroute.001"].outputs[0], self.grp.nodes["Math.003"].inputs[0])
            links.new(self.grp.nodes["Reroute.001"].outputs[0], self.grp.nodes["Math.004"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Reroute.001"].inputs[0])
            links.new(self.grp.nodes["Reroute.001"].outputs[0], self.grp.nodes["Math.005"].inputs[0])
            links.new(self.grp.nodes["Math.002"].outputs[0], self.grp.nodes["Brick 3D"].inputs[4])
            links.new(self.grp.nodes["Math.003"].outputs[0], self.grp.nodes["Brick 3D"].inputs[5])
            links.new(self.grp.nodes["Math.003"].outputs[0], self.grp.nodes["Brick 3D.001"].inputs[5])
            links.new(self.grp.nodes["Math.004"].outputs[0], self.grp.nodes["Brick 3D.001"].inputs[4])
            links.new(self.grp.nodes["Math.005"].outputs[0], self.grp.nodes["Voronoi Texture"].inputs[2])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Ship Normals"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Ship Normals" : 
                return True

        return False







