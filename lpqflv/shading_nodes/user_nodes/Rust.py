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

class Rust (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Rust"
    bl_idname = "rust"

    def createTree (self) : 

        if Rust.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Rust', 'ShaderNodeTree')

            node = self.grp.nodes.new('NodeGroupOutput')
            self.grp.outputs.new('NodeSocketFloatFactor', 'Fac')
            node.inputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.is_active_output = True
            node.label = ''
            node.location[0] = 573.78955078125
            node.location[1] = -3.0651276111602783
            node.mute = False
            node.name = 'Group Output'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 80.0

            node = self.grp.nodes.new('ShaderNodeTexMusgrave')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 4.099999904632568
            node.inputs['Detail'].default_value = 7.799999713897705
            node.inputs['Dimension'].default_value = 1.5
            node.inputs['Lacunarity'].default_value = 2.0
            node.inputs['Offset'].default_value = 0.0
            node.inputs['Gain'].default_value = 1.0
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 135.58303833007812
            node.location[1] = 5.314731597900391
            node.musgrave_dimensions = '3D'
            node.musgrave_type = 'FBM'
            node.mute = False
            node.name = 'Musgrave Texture.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 150.0
            node.width_hidden = 120.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 0.5
            node.inputs['Color1'].default_value = (0.0,0.0,0.0,1.0)
            node.inputs['Color2'].default_value = (1.0,1.0,1.0,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MIX'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 361.1916809082031
            node.location[1] = 2.885072708129883
            node.mute = False
            node.name = 'Mix'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_alpha = False
            node.use_clamp = True
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexNoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 0.7000001668930054
            node.inputs['Detail'].default_value = 16.0
            node.inputs['Roughness'].default_value = 0.824999988079071
            node.inputs['Distortion'].default_value = 0.0
            node.outputs['Fac'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -66.16940307617188
            node.location[1] = -2.323153495788574
            node.mute = False
            node.name = 'Noise Texture.002'
            node.noise_dimensions = '3D'
            node.show_options = True
            node.show_preview = False
            node.show_texture = True
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 100.0

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketFloat', 'Scale')
            self.grp.inputs['Scale'].default_value = 0.7000001668930054
            self.grp.inputs['Scale'].min_value = -1000.0
            self.grp.inputs['Scale'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketFloat', 'Detail')
            self.grp.inputs['Detail'].default_value = 16.0
            self.grp.inputs['Detail'].min_value = 0.0
            self.grp.inputs['Detail'].max_value = 16.0
            self.grp.inputs.new('NodeSocketFloatFactor', 'Roughness')
            self.grp.inputs['Roughness'].default_value = 0.824999988079071
            self.grp.inputs['Roughness'].min_value = 0.0
            self.grp.inputs['Roughness'].max_value = 1.0
            self.grp.inputs.new('NodeSocketVector', 'Coord')
            self.grp.inputs['Coord'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['Coord'].min_value = -10000.0
            self.grp.inputs['Coord'].max_value = 10000.0
            node.outputs['Scale'].default_value = 0.7000001668930054
            node.outputs['Detail'].default_value = 16.0
            node.outputs['Roughness'].default_value = 0.824999988079071
            node.outputs['Coord'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -368.35821533203125
            node.location[1] = -85.87791442871094
            node.mute = False
            node.name = 'Group Input'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 80.0

            links = self.grp.links
            links.new(self.grp.nodes["Noise Texture.002"].outputs[1], self.grp.nodes["Musgrave Texture.001"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Noise Texture.002"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Noise Texture.002"].inputs[3])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Noise Texture.002"].inputs[4])
            links.new(self.grp.nodes["Mix"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Musgrave Texture.001"].outputs[0], self.grp.nodes["Mix"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Noise Texture.002"].inputs[0])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Rust"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Rust" : 
                return True

        return False







