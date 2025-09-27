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

class Dirt (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Dirt"
    bl_idname = "dirt"

    def createTree (self) : 

        if Dirt.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Dirt', 'ShaderNodeTree')

            node = self.grp.nodes.new('ShaderNodeBsdfPrincipled')
            node.inputs['Base Color'].default_value = (0.0,0.0,0.0,1.0)
            node.inputs['Subsurface'].default_value = 0.0
            node.inputs['Subsurface Radius'].default_value = (1.0,0.20000000298023224,0.10000000149011612)
            node.inputs['Subsurface Color'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            node.inputs['Metallic'].default_value = 0.0
            node.inputs['Specular'].default_value = 0.15890538692474365
            node.inputs['Specular Tint'].default_value = 0.0
            node.inputs['Roughness'].default_value = 0.6961966753005981
            node.inputs['Anisotropic'].default_value = 0.0
            node.inputs['Anisotropic Rotation'].default_value = 0.0
            node.inputs['Sheen'].default_value = 0.0
            node.inputs['Sheen Tint'].default_value = 0.5
            node.inputs['Clearcoat'].default_value = 0.0
            node.inputs['Clearcoat Roughness'].default_value = 0.029999999329447746
            node.inputs['IOR'].default_value = 1.4500000476837158
            node.inputs['Transmission'].default_value = 0.0
            node.inputs['Transmission Roughness'].default_value = 0.0
            node.inputs['Emission'].default_value = (0.0,0.0,0.0,1.0)
            node.inputs['Alpha'].default_value = 1.0
            node.inputs['Normal'].default_value = (0.0,0.0,0.0)
            node.inputs['Clearcoat Normal'].default_value = (0.0,0.0,0.0)
            node.inputs['Tangent'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.distribution = 'GGX'
            node.hide = False
            node.label = ''
            node.location[0] = 483.66046142578125
            node.location[1] = 206.699462890625
            node.mute = False
            node.name = 'Principled BSDF.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.subsurface_method = 'BURLEY'
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 140.0

            node = self.grp.nodes.new('NodeGroupOutput')
            self.grp.outputs.new('NodeSocketShader', 'BSDF')
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.is_active_output = True
            node.label = ''
            node.location[0] = 843.4547729492188
            node.location[1] = 109.37725830078125
            node.mute = False
            node.name = 'Group Output'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 80.0

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
            element = node.color_ramp.elements.new(0.0)
            element.color = (0.24946600198745728,0.07309000194072723,0.017016999423503876,1.0)
            element.alpha = 1.0
            element.position = 0.0
            element = node.color_ramp.elements.new(0.2931821942329407)
            element.color = (0.1677473485469818,0.04469519481062889,0.005574079696089029,1.0)
            element.alpha = 1.0
            element.position = 0.2931821942329407
            element = node.color_ramp.elements.new(0.5818185806274414)
            element.color = (0.037480998784303665,0.015684999525547028,0.008860999718308449,1.0)
            element.alpha = 1.0
            element.position = 0.5818185806274414
            element = node.color_ramp.elements.new(0.7772728800773621)
            element.color = (0.017172111198306084,0.05505158007144928,0.0015423598233610392,1.0)
            element.alpha = 1.0
            element.position = 0.7772728800773621
            element = node.color_ramp.elements.new(1.0)
            element.color = (1.0,1.0,1.0,1.0)
            element.alpha = 1.0
            element.position = 1.0
            node.hide = False
            node.label = ''
            node.location[0] = -126.02626037597656
            node.location[1] = 160.22821044921875
            node.mute = False
            node.name = 'ColorRamp.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 140.0

            node = self.grp.nodes.new('ShaderNodeHueSaturation')
            node.inputs['Hue'].default_value = 0.5
            node.inputs['Saturation'].default_value = 1.0
            node.inputs['Value'].default_value = 1.0
            node.inputs['Fac'].default_value = 1.0
            node.inputs['Color'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 231.63507080078125
            node.location[1] = 177.07110595703125
            node.mute = False
            node.name = 'Hue Saturation Value'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 150.0
            node.width_hidden = 120.0

            node = self.grp.nodes.new('ShaderNodeBump')
            node.inputs['Strength'].default_value = 0.2749999761581421
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
            node.location[0] = -48.41767883300781
            node.location[1] = -175.68203735351562
            node.mute = False
            node.name = 'Bump'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 100.0

            node = self.grp.nodes.new('ShaderNodeMapRange')
            node.inputs['Value'].default_value = 1.0
            node.inputs['From Min'].default_value = -0.44999998807907104
            node.inputs['From Max'].default_value = 1.0
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
            node.location[0] = -349.13677978515625
            node.location[1] = 134.93215942382812
            node.mute = False
            node.name = 'Map Range'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 100.0

            node = self.grp.nodes.new('rust')
            node.inputs['Scale'].default_value = 0.8400001525878906
            node.inputs['Detail'].default_value = 16.0
            node.inputs['Roughness'].default_value = 0.7583333253860474
            node.inputs['Coord'].default_value = (0.0,8.59999942779541,0.0)
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -709.8222045898438
            node.location[1] = -253.6796875
            node.mute = False
            node.name = 'Rust.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 100.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.0
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 224.89547729492188
            node.location[1] = -6.973949432373047
            node.mute = False
            node.name = 'Math'
            node.operation = 'MULTIPLY'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 100.0

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketFloat', 'Scale')
            self.grp.inputs['Scale'].default_value = 0.8400001525878906
            self.grp.inputs['Scale'].min_value = -1000.0
            self.grp.inputs['Scale'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketFloatFactor', 'Noise Roughness')
            self.grp.inputs['Noise Roughness'].default_value = 0.7583333253860474
            self.grp.inputs['Noise Roughness'].min_value = 0.0
            self.grp.inputs['Noise Roughness'].max_value = 1.0
            self.grp.inputs.new('NodeSocketFloat', 'Hue')
            self.grp.inputs['Hue'].default_value = 0.5
            self.grp.inputs['Hue'].min_value = 0.0
            self.grp.inputs['Hue'].max_value = 1.0
            self.grp.inputs.new('NodeSocketFloat', 'Saturation')
            self.grp.inputs['Saturation'].default_value = 1.0
            self.grp.inputs['Saturation'].min_value = 0.0
            self.grp.inputs['Saturation'].max_value = 2.0
            self.grp.inputs.new('NodeSocketFloat', 'Lightness')
            self.grp.inputs['Lightness'].default_value = 1.0
            self.grp.inputs['Lightness'].min_value = 0.0
            self.grp.inputs['Lightness'].max_value = 2.0
            self.grp.inputs.new('NodeSocketFloat', 'Roughness')
            self.grp.inputs['Roughness'].default_value = 1.0
            self.grp.inputs['Roughness'].min_value = -10000.0
            self.grp.inputs['Roughness'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketFloatFactor', 'Bump Strength')
            self.grp.inputs['Bump Strength'].default_value = 0.2749999761581421
            self.grp.inputs['Bump Strength'].min_value = 0.0
            self.grp.inputs['Bump Strength'].max_value = 1.0
            self.grp.inputs.new('NodeSocketVector', 'Normal')
            self.grp.inputs['Normal'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['Normal'].min_value = -1.0
            self.grp.inputs['Normal'].max_value = 1.0
            self.grp.inputs.new('NodeSocketVector', 'Coord')
            self.grp.inputs['Coord'].default_value = (0.0,8.59999942779541,0.0)
            self.grp.inputs['Coord'].min_value = -10000.0
            self.grp.inputs['Coord'].max_value = 10000.0
            node.outputs['Scale'].default_value = 0.8400001525878906
            node.outputs['Noise Roughness'].default_value = 0.7583333253860474
            node.outputs['Hue'].default_value = 0.5
            node.outputs['Saturation'].default_value = 1.0
            node.outputs['Lightness'].default_value = 1.0
            node.outputs['Roughness'].default_value = 1.0
            node.outputs['Bump Strength'].default_value = 0.2749999761581421
            node.outputs['Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Coord'].default_value = (0.0,8.59999942779541,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1083.162841796875
            node.location[1] = -60.59709930419922
            node.mute = False
            node.name = 'Group Input'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 80.0

            node = self.grp.nodes.new('ShaderNodeMapRange')
            node.inputs['Value'].default_value = 1.0
            node.inputs['From Min'].default_value = 0.05000000074505806
            node.inputs['From Max'].default_value = 1.0
            node.inputs['To Min'].default_value = 0.05000000074505806
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
            node.location[0] = -349.0216979980469
            node.location[1] = -279.06097412109375
            node.mute = False
            node.name = 'Map Range.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            links = self.grp.links
            links.new(self.grp.nodes["Rust.001"].outputs[0], self.grp.nodes["Map Range"].inputs[0])
            links.new(self.grp.nodes["Map Range"].outputs[0], self.grp.nodes["ColorRamp.001"].inputs[0])
            links.new(self.grp.nodes["Rust.001"].outputs[0], self.grp.nodes["Bump"].inputs[2])
            links.new(self.grp.nodes["Bump"].outputs[0], self.grp.nodes["Principled BSDF.001"].inputs[19])
            links.new(self.grp.nodes["Principled BSDF.001"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Rust.001"].outputs[0], self.grp.nodes["Map Range.001"].inputs[0])
            links.new(self.grp.nodes["ColorRamp.001"].outputs[0], self.grp.nodes["Hue Saturation Value"].inputs[4])
            links.new(self.grp.nodes["Group Input"].outputs[8], self.grp.nodes["Rust.001"].inputs[3])
            links.new(self.grp.nodes["Group Input"].outputs[7], self.grp.nodes["Bump"].inputs[5])
            links.new(self.grp.nodes["Hue Saturation Value"].outputs[0], self.grp.nodes["Principled BSDF.001"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Hue Saturation Value"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Hue Saturation Value"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Hue Saturation Value"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Rust.001"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Rust.001"].inputs[2])
            links.new(self.grp.nodes["Math"].outputs[0], self.grp.nodes["Principled BSDF.001"].inputs[7])
            links.new(self.grp.nodes["Group Input"].outputs[6], self.grp.nodes["Bump"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[5], self.grp.nodes["Math"].inputs[1])
            links.new(self.grp.nodes["Map Range.001"].outputs[0], self.grp.nodes["Math"].inputs[0])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Dirt"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Dirt" : 
                return True

        return False







