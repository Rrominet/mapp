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

class Realistic_Color (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Realistic Color"
    bl_idname = "realisticcolor"

    def createTree (self) : 

        if Realistic_Color.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Realistic Color', 'ShaderNodeTree')

            node = self.grp.nodes.new('NodeGroupOutput')
            self.grp.outputs.new('NodeSocketColor', 'Color')
            node.inputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.is_active_output = True
            node.label = ''
            node.location[0] = 430.0376281738281
            node.location[1] = 73.452880859375
            node.mute = False
            node.name = 'Group Output'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 80.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 0.5
            node.inputs['Color1'].default_value = (0.5,0.5,0.5,1.0)
            node.inputs['Color2'].default_value = (0.5,0.5,0.5,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MIX'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 230.03762817382812
            node.location[1] = 78.45281982421875
            node.mute = False
            node.name = 'Mix'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_alpha = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 100.0

            node = self.grp.nodes.new('ShaderNodeTexNoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 5.0
            node.inputs['Detail'].default_value = 2.0
            node.inputs['Roughness'].default_value = 0.5
            node.inputs['Distortion'].default_value = 0.0
            node.outputs['Fac'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 34.467098236083984
            node.location[1] = 68.45294189453125
            node.mute = False
            node.name = 'Noise Texture'
            node.noise_dimensions = '3D'
            node.show_options = True
            node.show_preview = False
            node.show_texture = True
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 100.0

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketFloat', 'Scale')
            self.grp.inputs['Scale'].default_value = 5.0
            self.grp.inputs['Scale'].min_value = -1000.0
            self.grp.inputs['Scale'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketFloat', 'Detail')
            self.grp.inputs['Detail'].default_value = 2.0
            self.grp.inputs['Detail'].min_value = 0.0
            self.grp.inputs['Detail'].max_value = 16.0
            self.grp.inputs.new('NodeSocketFloatFactor', 'Roughness')
            self.grp.inputs['Roughness'].default_value = 0.5
            self.grp.inputs['Roughness'].min_value = 0.0
            self.grp.inputs['Roughness'].max_value = 1.0
            self.grp.inputs.new('NodeSocketFloat', 'Distortion')
            self.grp.inputs['Distortion'].default_value = 0.0
            self.grp.inputs['Distortion'].min_value = -1000.0
            self.grp.inputs['Distortion'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketColor', 'Color1')
            self.grp.inputs['Color1'].default_value = (0.5,0.5,0.5,1.0)
            self.grp.inputs.new('NodeSocketColor', 'Color2')
            self.grp.inputs['Color2'].default_value = (0.5,0.5,0.5,1.0)
            self.grp.inputs.new('NodeSocketVector', 'Coord')
            self.grp.inputs['Coord'].default_value = (1.0,1.0,1.0)
            self.grp.inputs['Coord'].min_value = -10000.0
            self.grp.inputs['Coord'].max_value = 10000.0
            node.outputs['Scale'].default_value = 5.0
            node.outputs['Detail'].default_value = 2.0
            node.outputs['Roughness'].default_value = 0.5
            node.outputs['Distortion'].default_value = 0.0
            node.outputs['Color1'].default_value = (0.5,0.5,0.5,1.0)
            node.outputs['Color2'].default_value = (0.5,0.5,0.5,1.0)
            node.outputs['Coord'].default_value = (1.0,1.0,1.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -285.4435119628906
            node.location[1] = 42.64739227294922
            node.mute = False
            node.name = 'Group Input'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 80.0

            links = self.grp.links
            links.new(self.grp.nodes["Noise Texture"].outputs[0], self.grp.nodes["Mix"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Noise Texture"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Noise Texture"].inputs[3])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Noise Texture"].inputs[4])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Noise Texture"].inputs[5])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Mix"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[5], self.grp.nodes["Mix"].inputs[2])
            links.new(self.grp.nodes["Mix"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[6], self.grp.nodes["Noise Texture"].inputs[0])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Realistic Color"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Realistic Color" : 
                return True

        return False







