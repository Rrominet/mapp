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

class Military (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Military"
    bl_idname = "military"

    def createTree (self) : 

        if Military.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Military', 'ShaderNodeTree')

            node = self.grp.nodes.new('ShaderNodeTexMusgrave')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 0.46000009775161743
            node.inputs['Detail'].default_value = 16.0
            node.inputs['Dimension'].default_value = 0.7300000190734863
            node.inputs['Lacunarity'].default_value = 2.8999996185302734
            node.inputs['Offset'].default_value = 0.0
            node.inputs['Gain'].default_value = 1.0
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -513.000732421875
            node.location[1] = 275.625244140625
            node.musgrave_dimensions = '3D'
            node.musgrave_type = 'FBM'
            node.mute = False
            node.name = 'Musgrave Texture'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 150.0
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
            element = node.color_ramp.elements.new(0.290909081697464)
            element.color = (0.0,0.0,0.0,1.0)
            element.alpha = 1.0
            element.position = 0.290909081697464
            element = node.color_ramp.elements.new(0.3409092426300049)
            element.color = (1.0,1.0,1.0,1.0)
            element.alpha = 1.0
            element.position = 0.3409092426300049
            node.hide = False
            node.label = ''
            node.location[0] = -229.12779235839844
            node.location[1] = 279.93896484375
            node.mute = False
            node.name = 'ColorRamp.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexMusgrave')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 0.28000009059906006
            node.inputs['Detail'].default_value = 16.0
            node.inputs['Dimension'].default_value = 0.7300000190734863
            node.inputs['Lacunarity'].default_value = 2.8999996185302734
            node.inputs['Offset'].default_value = 0.0
            node.inputs['Gain'].default_value = 1.0
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -517.468505859375
            node.location[1] = 45.95994567871094
            node.musgrave_dimensions = '3D'
            node.musgrave_type = 'FBM'
            node.mute = False
            node.name = 'Musgrave Texture.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 150.0
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
            element = node.color_ramp.elements.new(0.290909081697464)
            element.color = (0.0,0.0,0.0,1.0)
            element.alpha = 1.0
            element.position = 0.290909081697464
            element = node.color_ramp.elements.new(0.3409092426300049)
            element.color = (1.0,1.0,1.0,1.0)
            element.alpha = 1.0
            element.position = 0.3409092426300049
            node.hide = False
            node.label = ''
            node.location[0] = -242.53099060058594
            node.location[1] = 33.86888122558594
            node.mute = False
            node.name = 'ColorRamp.002'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 240.0
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
            element = node.color_ramp.elements.new(0.290909081697464)
            element.color = (0.0,0.0,0.0,1.0)
            element.alpha = 1.0
            element.position = 0.290909081697464
            element = node.color_ramp.elements.new(0.3409092426300049)
            element.color = (1.0,1.0,1.0,1.0)
            element.alpha = 1.0
            element.position = 0.3409092426300049
            node.hide = False
            node.label = ''
            node.location[0] = -251.32762145996094
            node.location[1] = -210.58106994628906
            node.mute = False
            node.name = 'ColorRamp.003'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexMusgrave')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 0.5600000023841858
            node.inputs['Detail'].default_value = 16.0
            node.inputs['Dimension'].default_value = 0.7300000190734863
            node.inputs['Lacunarity'].default_value = 2.8999996185302734
            node.inputs['Offset'].default_value = 0.0
            node.inputs['Gain'].default_value = 1.0
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -514.35107421875
            node.location[1] = -201.47267150878906
            node.musgrave_dimensions = '3D'
            node.musgrave_type = 'FBM'
            node.mute = False
            node.name = 'Musgrave Texture.002'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 150.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 0.5
            node.inputs['Color1'].default_value = (0.002899122890084982,0.005784939508885145,0.003068947698920965,1.0)
            node.inputs['Color2'].default_value = (0.007555999793112278,0.06900399923324585,0.004575999919325113,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MIX'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 84.81752014160156
            node.location[1] = 174.70994567871094
            node.mute = False
            node.name = 'Mix.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_alpha = False
            node.use_clamp = True
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 0.5
            node.inputs['Color1'].default_value = (0.0,0.0,0.0,1.0)
            node.inputs['Color2'].default_value = (0.03485799953341484,0.01604899950325489,0.005133000202476978,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MIX'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 319.9915771484375
            node.location[1] = 24.947494506835938
            node.mute = False
            node.name = 'Mix.002'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_alpha = False
            node.use_clamp = True
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 0.5
            node.inputs['Color1'].default_value = (0.0,0.0,0.0,1.0)
            node.inputs['Color2'].default_value = (0.3600679934024811,0.23512400686740875,0.07914700359106064,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MIX'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 520.716796875
            node.location[1] = -155.44532775878906
            node.mute = False
            node.name = 'Mix.003'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_alpha = False
            node.use_clamp = True
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeVectorMath')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Vector'].default_value = (0.0,-1.2999999523162842,0.0)
            node.inputs['Scale'].default_value = 1.0
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -728.532958984375
            node.location[1] = 209.95213317871094
            node.mute = False
            node.name = 'Vector Math.002'
            node.operation = 'ADD'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeVectorMath')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Vector'].default_value = (0.0,4.899999618530273,0.0)
            node.inputs['Scale'].default_value = 1.0
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -730.022216796875
            node.location[1] = -36.12184143066406
            node.mute = False
            node.name = 'Vector Math.001'
            node.operation = 'ADD'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeVectorMath')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Vector'].default_value = (0.0,1.5999999046325684,0.0)
            node.inputs['Scale'].default_value = 1.0
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -728.39404296875
            node.location[1] = -270.2650146484375
            node.mute = False
            node.name = 'Vector Math'
            node.operation = 'ADD'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketColor', 'Base Color')
            self.grp.inputs['Base Color'].default_value = (0.002899122890084982,0.005784939508885145,0.003068947698920965,1.0)
            self.grp.inputs.new('NodeSocketColor', 'Color 1')
            self.grp.inputs['Color 1'].default_value = (0.007555999793112278,0.06900399923324585,0.004575999919325113,1.0)
            self.grp.inputs.new('NodeSocketColor', 'Color 2')
            self.grp.inputs['Color 2'].default_value = (0.03485799953341484,0.01604899950325489,0.005133000202476978,1.0)
            self.grp.inputs.new('NodeSocketColor', 'Color 3')
            self.grp.inputs['Color 3'].default_value = (0.3600679934024811,0.23512400686740875,0.07914700359106064,1.0)
            self.grp.inputs.new('NodeSocketVector', 'Vector')
            self.grp.inputs['Vector'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['Vector'].min_value = -10000.0
            self.grp.inputs['Vector'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketVector', 'Offset 1')
            self.grp.inputs['Offset 1'].default_value = (0.0,-1.2999999523162842,0.0)
            self.grp.inputs['Offset 1'].min_value = -10000.0
            self.grp.inputs['Offset 1'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketVector', 'Offset 2')
            self.grp.inputs['Offset 2'].default_value = (0.0,4.899999618530273,0.0)
            self.grp.inputs['Offset 2'].min_value = -10000.0
            self.grp.inputs['Offset 2'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketVector', 'Offset 3')
            self.grp.inputs['Offset 3'].default_value = (0.0,1.5999999046325684,0.0)
            self.grp.inputs['Offset 3'].min_value = -10000.0
            self.grp.inputs['Offset 3'].max_value = 10000.0
            node.outputs['Base Color'].default_value = (0.002899122890084982,0.005784939508885145,0.003068947698920965,1.0)
            node.outputs['Color 1'].default_value = (0.007555999793112278,0.06900399923324585,0.004575999919325113,1.0)
            node.outputs['Color 2'].default_value = (0.03485799953341484,0.01604899950325489,0.005133000202476978,1.0)
            node.outputs['Color 3'].default_value = (0.3600679934024811,0.23512400686740875,0.07914700359106064,1.0)
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.outputs['Offset 1'].default_value = (0.0,-1.2999999523162842,0.0)
            node.outputs['Offset 2'].default_value = (0.0,4.899999618530273,0.0)
            node.outputs['Offset 3'].default_value = (0.0,1.5999999046325684,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1165.1544189453125
            node.location[1] = 90.94194030761719
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
            node.location[0] = 800.1060791015625
            node.location[1] = -198.23765563964844
            node.mute = False
            node.name = 'Group Output'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            links = self.grp.links
            links.new(self.grp.nodes["Musgrave Texture"].outputs[0], self.grp.nodes["ColorRamp.001"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Vector Math.002"].inputs[0])
            links.new(self.grp.nodes["Musgrave Texture.001"].outputs[0], self.grp.nodes["ColorRamp.002"].inputs[0])
            links.new(self.grp.nodes["Musgrave Texture.002"].outputs[0], self.grp.nodes["ColorRamp.003"].inputs[0])
            links.new(self.grp.nodes["ColorRamp.001"].outputs[0], self.grp.nodes["Mix.001"].inputs[0])
            links.new(self.grp.nodes["ColorRamp.002"].outputs[0], self.grp.nodes["Mix.002"].inputs[0])
            links.new(self.grp.nodes["ColorRamp.003"].outputs[0], self.grp.nodes["Mix.003"].inputs[0])
            links.new(self.grp.nodes["Mix.001"].outputs[0], self.grp.nodes["Mix.002"].inputs[1])
            links.new(self.grp.nodes["Mix.002"].outputs[0], self.grp.nodes["Mix.003"].inputs[1])
            links.new(self.grp.nodes["Vector Math"].outputs[0], self.grp.nodes["Musgrave Texture.002"].inputs[0])
            links.new(self.grp.nodes["Vector Math.001"].outputs[0], self.grp.nodes["Musgrave Texture.001"].inputs[0])
            links.new(self.grp.nodes["Vector Math.002"].outputs[0], self.grp.nodes["Musgrave Texture"].inputs[0])
            links.new(self.grp.nodes["Mix.003"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Vector Math.001"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Vector Math"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Mix.001"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Mix.001"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Mix.002"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Mix.003"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[5], self.grp.nodes["Vector Math.002"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[6], self.grp.nodes["Vector Math.001"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[7], self.grp.nodes["Vector Math"].inputs[1])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Military"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Military" : 
                return True

        return False







