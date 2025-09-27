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

class Veins (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Veins"
    bl_idname = "veins"

    def createTree (self) : 

        if Veins.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Veins', 'ShaderNodeTree')

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 0.46666669845581055
            node.inputs['Color1'].default_value = (0.5,0.5,0.5,1.0)
            node.inputs['Color2'].default_value = (0.5,0.5,0.5,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MIX'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -299.073486328125
            node.location[1] = -73.55291748046875
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
            node.location[0] = 476.44921875
            node.location[1] = 53.888519287109375
            node.mute = False
            node.name = 'Math'
            node.operation = 'ADD'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = True
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexWave')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Scale'].default_value = 4.5
            node.inputs['Distortion'].default_value = 0.0
            node.inputs['Detail'].default_value = 2.0
            node.inputs['Detail Scale'].default_value = 0.0
            node.inputs['Detail Roughness'].default_value = 0.5
            node.inputs['Phase Offset'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.outputs['Fac'].default_value = 0.0
            node.bands_direction = 'X'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -67.150634765625
            node.location[1] = -102.73052978515625
            node.mute = False
            node.name = 'Wave Texture'
            node.rings_direction = 'X'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.wave_profile = 'SIN'
            node.wave_type = 'BANDS'
            node.width = 150.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMapRange')
            node.inputs['Value'].default_value = 1.0
            node.inputs['From Min'].default_value = 0.0
            node.inputs['From Max'].default_value = 0.05000000074505806
            node.inputs['To Min'].default_value = 0.0
            node.inputs['To Max'].default_value = 1.0
            node.inputs['Steps'].default_value = 4.0
            node.outputs['Result'].default_value = 0.0
            node.clamp = True
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.interpolation_type = 'LINEAR'
            node.label = ''
            node.location[0] = 234.0357666015625
            node.location[1] = -56.585113525390625
            node.mute = False
            node.name = 'Map Range'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
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
            element = node.color_ramp.elements.new(0.00909090880304575)
            element.color = (0.0,0.0,0.0,1.0)
            element.alpha = 1.0
            element.position = 0.00909090880304575
            element = node.color_ramp.elements.new(0.04090911149978638)
            element.color = (1.0,1.0,1.0,1.0)
            element.alpha = 1.0
            element.position = 0.04090911149978638
            node.hide = False
            node.label = ''
            node.location[0] = 132.74755859375
            node.location[1] = 210.57675170898438
            node.mute = False
            node.name = 'ColorRamp.002'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('rust')
            node.inputs['Scale'].default_value = 7.299999237060547
            node.inputs['Detail'].default_value = 14.5
            node.inputs['Roughness'].default_value = 0.3333333432674408
            node.inputs['Additional Coord'].default_value = (0.0,0.0,0.0)
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -128.221923828125
            node.location[1] = 210.34242248535156
            node.mute = False
            node.name = 'Rust'
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
            node.location[0] = 912.13525390625
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
            node.location[0] = 712.13525390625
            node.location[1] = 28.561126708984375
            node.mute = False
            node.name = 'Invert'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexCoord')
            node.outputs['Generated'].default_value = (0.0,0.0,0.0)
            node.outputs['Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['UV'].default_value = (0.0,0.0,0.0)
            node.outputs['Object'].default_value = (0.0,0.0,0.0)
            node.outputs['Camera'].default_value = (0.0,0.0,0.0)
            node.outputs['Window'].default_value = (0.0,0.0,0.0)
            node.outputs['Reflection'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.from_instancer = False
            node.hide = False
            node.label = ''
            node.location[0] = -1603.9320068359375
            node.location[1] = -128.6394805908203
            node.mute = False
            node.name = 'Texture Coordinate.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
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
            node.location[0] = -1046.0616455078125
            node.location[1] = -165.91259765625
            node.mute = False
            node.name = 'Reroute'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeVectorMath')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Vector'].default_value = (1.0,1.0,1.0)
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Scale'].default_value = 1.0
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1302.2203369140625
            node.location[1] = -116.73191833496094
            node.mute = False
            node.name = 'Vector Math'
            node.operation = 'MULTIPLY'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexNoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 6.59999942779541
            node.inputs['Detail'].default_value = 4.0
            node.inputs['Roughness'].default_value = 0.8916666507720947
            node.inputs['Distortion'].default_value = 0.0
            node.outputs['Fac'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -805.826904296875
            node.location[1] = -316.79266357421875
            node.mute = False
            node.name = 'Noise Texture'
            node.noise_dimensions = '3D'
            node.show_options = True
            node.show_preview = False
            node.show_texture = True
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketVector', 'Add Coord')
            self.grp.inputs['Add Coord'].default_value = (1.0,1.0,1.0)
            self.grp.inputs['Add Coord'].min_value = -10000.0
            self.grp.inputs['Add Coord'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketFloat', 'Scale')
            self.grp.inputs['Scale'].default_value = 6.59999942779541
            self.grp.inputs['Scale'].min_value = -1000.0
            self.grp.inputs['Scale'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketFloat', 'Width')
            self.grp.inputs['Width'].default_value = 0.05000000074505806
            self.grp.inputs['Width'].min_value = -10000.0
            self.grp.inputs['Width'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketFloat', 'Detail')
            self.grp.inputs['Detail'].default_value = 4.0
            self.grp.inputs['Detail'].min_value = 0.0
            self.grp.inputs['Detail'].max_value = 16.0
            self.grp.inputs.new('NodeSocketFloatFactor', 'Roughness')
            self.grp.inputs['Roughness'].default_value = 0.8916666507720947
            self.grp.inputs['Roughness'].min_value = 0.0
            self.grp.inputs['Roughness'].max_value = 1.0
            node.outputs['Add Coord'].default_value = (1.0,1.0,1.0)
            node.outputs['Scale'].default_value = 6.59999942779541
            node.outputs['Width'].default_value = 0.05000000074505806
            node.outputs['Detail'].default_value = 4.0
            node.outputs['Roughness'].default_value = 0.8916666507720947
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1611.9683837890625
            node.location[1] = -390.5640563964844
            node.mute = False
            node.name = 'Group Input'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            links = self.grp.links
            links.new(self.grp.nodes["Noise Texture"].outputs[1], self.grp.nodes["Mix"].inputs[2])
            links.new(self.grp.nodes["Mix"].outputs[0], self.grp.nodes["Wave Texture"].inputs[0])
            links.new(self.grp.nodes["Rust"].outputs[0], self.grp.nodes["ColorRamp.002"].inputs[0])
            links.new(self.grp.nodes["ColorRamp.002"].outputs[0], self.grp.nodes["Math"].inputs[0])
            links.new(self.grp.nodes["Math"].outputs[0], self.grp.nodes["Invert"].inputs[1])
            links.new(self.grp.nodes["Invert"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Wave Texture"].outputs[0], self.grp.nodes["Map Range"].inputs[0])
            links.new(self.grp.nodes["Map Range"].outputs[0], self.grp.nodes["Math"].inputs[1])
            links.new(self.grp.nodes["Reroute"].outputs[0], self.grp.nodes["Mix"].inputs[1])
            links.new(self.grp.nodes["Reroute"].outputs[0], self.grp.nodes["Noise Texture"].inputs[0])
            links.new(self.grp.nodes["Texture Coordinate.001"].outputs[3], self.grp.nodes["Vector Math"].inputs[0])
            links.new(self.grp.nodes["Vector Math"].outputs[0], self.grp.nodes["Reroute"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Vector Math"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Noise Texture"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Noise Texture"].inputs[3])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Noise Texture"].inputs[4])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Rust"].inputs[3])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Map Range"].inputs[2])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Veins"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Veins" : 
                return True

        return False







