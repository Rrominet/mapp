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

class Facing_Light (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Facing Light"
    bl_idname = "facinglight"

    def createTree (self) : 

        if Facing_Light.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Facing Light', 'ShaderNodeTree')

            node = self.grp.nodes.new('ShaderNodeMixShader')
            node.inputs['Fac'].default_value = 0.5
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 287.30633544921875
            node.location[1] = -10.328536987304688
            node.mute = False
            node.name = 'Mix Shader'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupOutput')
            self.grp.outputs.new('NodeSocketShader', 'Shader')
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.is_active_output = True
            node.label = ''
            node.location[0] = 487.30633544921875
            node.location[1] = -0.0
            node.mute = False
            node.name = 'Group Output'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeEmission')
            node.inputs['Color'].default_value = (1.0,1.0,1.0,1.0)
            node.inputs['Strength'].default_value = 1.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 20.106918334960938
            node.location[1] = -7.5907440185546875
            node.mute = False
            node.name = 'Emission'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketFloat', 'Strength')
            self.grp.inputs['Strength'].default_value = 1.0
            self.grp.inputs['Strength'].min_value = 0.0
            self.grp.inputs['Strength'].max_value = 1000000.0
            self.grp.inputs.new('NodeSocketColor', 'In Color')
            self.grp.inputs['In Color'].default_value = (1.0,1.0,1.0,1.0)
            self.grp.inputs.new('NodeSocketColor', 'Out Color')
            self.grp.inputs['Out Color'].default_value = (0.0,0.032268185168504715,1.0,1.0)
            self.grp.inputs.new('NodeSocketFloat', 'Blend')
            self.grp.inputs['Blend'].default_value = 0.9799999594688416
            self.grp.inputs['Blend'].min_value = 0.0
            self.grp.inputs['Blend'].max_value = 1.0
            self.grp.inputs.new('NodeSocketVector', 'Normal')
            self.grp.inputs['Normal'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['Normal'].min_value = -1.0
            self.grp.inputs['Normal'].max_value = 1.0
            node.outputs['Strength'].default_value = 1.0
            node.outputs['In Color'].default_value = (1.0,1.0,1.0,1.0)
            node.outputs['Out Color'].default_value = (0.0,0.032268185168504715,1.0,1.0)
            node.outputs['Blend'].default_value = 0.9799999594688416
            node.outputs['Normal'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -515.0623168945312
            node.location[1] = -29.878549575805664
            node.mute = False
            node.name = 'Group Input'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeValue')
            node.outputs['Value'].default_value = 77.30000305175781
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -757.1016845703125
            node.location[1] = -143.47238159179688
            node.mute = False
            node.name = 'Value'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeEmission')
            node.inputs['Color'].default_value = (0.0,0.032268185168504715,1.0,1.0)
            node.inputs['Strength'].default_value = 1.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 34.524383544921875
            node.location[1] = -152.0875244140625
            node.mute = False
            node.name = 'Emission.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeLayerWeight')
            node.inputs['Blend'].default_value = 0.9799999594688416
            node.inputs['Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Fresnel'].default_value = 0.0
            node.outputs['Facing'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -30.901641845703125
            node.location[1] = 152.0875244140625
            node.mute = False
            node.name = 'Layer Weight'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            links = self.grp.links
            links.new(self.grp.nodes["Layer Weight"].outputs[0], self.grp.nodes["Mix Shader"].inputs[0])
            links.new(self.grp.nodes["Emission"].outputs[0], self.grp.nodes["Mix Shader"].inputs[1])
            links.new(self.grp.nodes["Emission.001"].outputs[0], self.grp.nodes["Mix Shader"].inputs[2])
            links.new(self.grp.nodes["Mix Shader"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Emission"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Emission.001"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Emission"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Emission.001"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Layer Weight"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Layer Weight"].inputs[1])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Facing Light"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Facing Light" : 
                return True

        return False







