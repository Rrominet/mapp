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

class Random_Color (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Random Color"
    bl_idname = "randomcolor"

    def createTree (self) : 

        if Random_Color.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Random Color', 'ShaderNodeTree')

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
            element = node.color_ramp.elements[0]
            element.color = (0.0,0.0,0.0,1.0)
            element.alpha = 1.0
            element.position = 0.0
            element = node.color_ramp.elements[1]
            element.color = (1.0,0.0,0.0,1.0)
            element.alpha = 1.0
            element.position = 1.0
            node.hide = False
            node.label = ''
            node.location[0] = -263.32489013671875
            node.location[1] = 245.02645874023438
            node.mute = False
            node.name = 'ColorRamp'
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
            element = node.color_ramp.elements[0]
            element.color = (0.0,0.0,1.0,1.0)
            element.alpha = 1.0
            element.position = 0.0
            element = node.color_ramp.elements[1]
            element.color = (0.0,0.0,0.0,1.0)
            element.alpha = 1.0
            element.position = 1
            node.hide = False
            node.label = ''
            node.location[0] = -264.13446044921875
            node.location[1] = 10.3592529296875
            node.mute = False
            node.name = 'ColorRamp.001'
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
            element = node.color_ramp.elements[0]
            element.color = (0.0,0.0,0.0,1.0)
            element.alpha = 1.0
            element.position = 0.0
            element = node.color_ramp.elements[1]
            element.color = (0.0,0.0,0.0,1.0)
            element.alpha = 1.0
            element.position = 1
            element = node.color_ramp.elements.new(0.5)
            element.color = (0.0,1.0,0.0,1.0)
            element.alpha = 1.0
            element.position = 0.5
            node.hide = False
            node.label = ''
            node.location[0] = -261.11260986328125
            node.location[1] = -221.68997192382812
            node.mute = False
            node.name = 'ColorRamp.002'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 1.0
            node.inputs['Color1'].default_value = (0.5,0.5,0.5,1.0)
            node.inputs['Color2'].default_value = (0.0,0.0,0.0,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MULTIPLY'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 30.6722412109375
            node.location[1] = 6.92333984375
            node.mute = False
            node.name = 'Mix.003'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_alpha = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 1.0
            node.inputs['Color1'].default_value = (0.5,0.5,0.5,1.0)
            node.inputs['Color2'].default_value = (0.5,0.5,0.5,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'ADD'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 330.2105712890625
            node.location[1] = 49.689727783203125
            node.mute = False
            node.name = 'Mix'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_alpha = False
            node.use_clamp = False
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
            node.location[0] = 779.1317749023438
            node.location[1] = -0.0
            node.mute = False
            node.name = 'Group Output'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 1.0
            node.inputs['Color1'].default_value = (0.5,0.5,0.5,1.0)
            node.inputs['Color2'].default_value = (0.5,0.5,0.5,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'ADD'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 579.1317749023438
            node.location[1] = -120.09071350097656
            node.mute = False
            node.name = 'Mix.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_alpha = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeObjectInfo')
            node.outputs['Location'].default_value = (0.0,0.0,0.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.outputs['Object Index'].default_value = 0.0
            node.outputs['Material Index'].default_value = 0.0
            node.outputs['Random'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -588.9149780273438
            node.location[1] = 159.33468627929688
            node.mute = False
            node.name = 'Object Info'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 1.0
            node.inputs['Color1'].default_value = (0.5,0.5,0.5,1.0)
            node.inputs['Color2'].default_value = (0.0,0.0,0.0,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MULTIPLY'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 79.2509765625
            node.location[1] = -238.03585815429688
            node.mute = False
            node.name = 'Mix.004'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_alpha = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 1.0
            node.inputs['Color1'].default_value = (0.5,0.5,0.5,1.0)
            node.inputs['Color2'].default_value = (0.0,0.0,0.0,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MULTIPLY'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 39.58990478515625
            node.location[1] = 241.95870971679688
            node.mute = False
            node.name = 'Mix.002'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_alpha = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketFloat', 'Red')
            self.grp.inputs['Red'].default_value = 0.0
            self.grp.inputs['Red'].min_value = 0.0
            self.grp.inputs['Red'].max_value = 10.0
            self.grp.inputs.new('NodeSocketFloat', 'Green')
            self.grp.inputs['Green'].default_value = 0.0
            self.grp.inputs['Green'].min_value = 0.0
            self.grp.inputs['Green'].max_value = 10.0
            self.grp.inputs.new('NodeSocketFloat', 'Blue')
            self.grp.inputs['Blue'].default_value = 0.0
            self.grp.inputs['Blue'].min_value = 0.0
            self.grp.inputs['Blue'].max_value = 10.0
            node.outputs['Red'].default_value = 0.0
            node.outputs['Green'].default_value = 0.0
            node.outputs['Blue'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -734.40869140625
            node.location[1] = -233.48568725585938
            node.mute = False
            node.name = 'Group Input'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            links = self.grp.links
            links.new(self.grp.nodes["Object Info"].outputs[4], self.grp.nodes["ColorRamp"].inputs[0])
            links.new(self.grp.nodes["Object Info"].outputs[4], self.grp.nodes["ColorRamp.001"].inputs[0])
            links.new(self.grp.nodes["Object Info"].outputs[4], self.grp.nodes["ColorRamp.002"].inputs[0])
            links.new(self.grp.nodes["ColorRamp.001"].outputs[0], self.grp.nodes["Mix.003"].inputs[1])
            links.new(self.grp.nodes["Mix"].outputs[0], self.grp.nodes["Mix.001"].inputs[1])
            links.new(self.grp.nodes["ColorRamp.002"].outputs[0], self.grp.nodes["Mix.004"].inputs[1])
            links.new(self.grp.nodes["ColorRamp"].outputs[0], self.grp.nodes["Mix.002"].inputs[1])
            links.new(self.grp.nodes["Mix.001"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Mix.002"].outputs[0], self.grp.nodes["Mix"].inputs[1])
            links.new(self.grp.nodes["Mix.003"].outputs[0], self.grp.nodes["Mix"].inputs[2])
            links.new(self.grp.nodes["Mix.004"].outputs[0], self.grp.nodes["Mix.001"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Mix.002"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Mix.003"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Mix.004"].inputs[2])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Random Color"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Random Color" : 
                return True

        return False







