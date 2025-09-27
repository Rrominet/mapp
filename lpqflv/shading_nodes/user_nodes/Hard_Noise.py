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

class Hard_Noise (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Hard Noise"
    bl_idname = "hardnoise"

    def createTree (self) : 

        if Hard_Noise.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Hard Noise', 'ShaderNodeTree')

            node = self.grp.nodes.new('NodeGroupOutput')
            self.grp.outputs.new('NodeSocketFloatFactor', 'Fac')
            node.inputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.is_active_output = True
            node.label = ''
            node.location[0] = 294.831298828125
            node.location[1] = -0.0
            node.mute = False
            node.name = 'Group Output'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexNoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 7.100000381469727
            node.inputs['Detail'].default_value = 2.0
            node.inputs['Roughness'].default_value = 0.5833333134651184
            node.inputs['Distortion'].default_value = 1.0799999237060547
            node.outputs['Fac'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 94.831298828125
            node.location[1] = 1.241119384765625
            node.mute = False
            node.name = 'Noise Texture'
            node.noise_dimensions = '3D'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexNoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 6.400000095367432
            node.inputs['Detail'].default_value = 16.0
            node.inputs['Roughness'].default_value = 0.699999988079071
            node.inputs['Distortion'].default_value = 0.0
            node.outputs['Fac'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -94.831298828125
            node.location[1] = -1.241119384765625
            node.mute = False
            node.name = 'Noise Texture.001'
            node.noise_dimensions = '3D'
            node.show_options = True
            node.show_preview = False
            node.show_texture = True
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketVector', 'Vector')
            self.grp.inputs['Vector'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['Vector'].min_value = 0.0
            self.grp.inputs['Vector'].max_value = 1.0
            self.grp.inputs.new('NodeSocketFloat', 'Scale')
            self.grp.inputs['Scale'].default_value = 6.400000095367432
            self.grp.inputs['Scale'].min_value = -1000.0
            self.grp.inputs['Scale'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketFloatFactor', 'Roughness')
            self.grp.inputs['Roughness'].default_value = 0.699999988079071
            self.grp.inputs['Roughness'].min_value = 0.0
            self.grp.inputs['Roughness'].max_value = 1.0
            self.grp.inputs.new('NodeSocketFloat', 'Distortion')
            self.grp.inputs['Distortion'].default_value = 0.0
            self.grp.inputs['Distortion'].min_value = -1000.0
            self.grp.inputs['Distortion'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketFloat', 'Details')
            self.grp.inputs['Details'].default_value = 7.100000381469727
            self.grp.inputs['Details'].min_value = -1000.0
            self.grp.inputs['Details'].max_value = 1000.0
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.outputs['Scale'].default_value = 6.400000095367432
            node.outputs['Roughness'].default_value = 0.699999988079071
            node.outputs['Distortion'].default_value = 0.0
            node.outputs['Details'].default_value = 7.100000381469727
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -398.28900146484375
            node.location[1] = -106.30850982666016
            node.mute = False
            node.name = 'Group Input'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            links = self.grp.links
            links.new(self.grp.nodes["Noise Texture.001"].outputs[1], self.grp.nodes["Noise Texture"].inputs[0])
            links.new(self.grp.nodes["Noise Texture"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Noise Texture.001"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Noise Texture.001"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Noise Texture.001"].inputs[4])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Noise Texture.001"].inputs[5])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Noise Texture"].inputs[2])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Hard Noise"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Hard Noise" : 
                return True

        return False







