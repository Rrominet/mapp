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

class Rust_Shader (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Rust Shader"
    bl_idname = "rustshader"

    def createTree (self) : 

        if Rust_Shader.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Rust Shader', 'ShaderNodeTree')

            node = self.grp.nodes.new('noisebump')
            node.inputs['Scale'].default_value = 414.0999755859375
            node.inputs['Strength'].default_value = 0.21666663885116577
            node.inputs['Distance'].default_value = 1.0
            node.inputs['Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Normal'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 328.1304931640625
            node.location[1] = -462.37603759765625
            node.mute = False
            node.name = 'Noise Bump'
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
            node.color_ramp.interpolation = 'CONSTANT'
            element = node.color_ramp.elements.new(0.0)
            element.color = (0.0,0.0,0.0,1.0)
            element.alpha = 1.0
            element.position = 0.0
            element = node.color_ramp.elements.new(0.21363641321659088)
            element.color = (1.0,1.0,1.0,1.0)
            element.alpha = 1.0
            element.position = 0.21363641321659088
            node.hide = False
            node.label = ''
            node.location[0] = -216.06536865234375
            node.location[1] = -326.57421875
            node.mute = False
            node.name = 'ColorRamp'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeBump')
            node.inputs['Strength'].default_value = 0.19999998807907104
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
            node.location[0] = 103.93463134765625
            node.location[1] = -414.2891845703125
            node.mute = False
            node.name = 'Bump'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeRGBCurve')
            node.inputs['Fac'].default_value = 1.0
            node.inputs['Color'].default_value = (0.0,0.0,0.0,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 195.004638671875
            node.location[1] = -45.539306640625
            node.mapping.tone = 'STANDARD'
            node.mapping.extend = 'EXTRAPOLATED'
            point = node.mapping.curves[0].points.new(0,0)
            point.handle_type = 'AUTO'
            point.location = (0.0,0.0)
            point = node.mapping.curves[0].points.new(0,0)
            point.handle_type = 'AUTO'
            point.location = (1.0,1.0)
            node.mapping.update()
            point = node.mapping.curves[1].points.new(0,0)
            point.handle_type = 'AUTO'
            point.location = (0.0,0.0)
            point = node.mapping.curves[1].points.new(0,0)
            point.handle_type = 'AUTO'
            point.location = (1.0,1.0)
            node.mapping.update()
            point = node.mapping.curves[2].points.new(0,0)
            point.handle_type = 'AUTO'
            point.location = (0.0,0.0)
            point = node.mapping.curves[2].points.new(0,0)
            point.handle_type = 'AUTO'
            point.location = (1.0,1.0)
            node.mapping.update()
            point = node.mapping.curves[3].points.new(0,0)
            point.handle_type = 'AUTO'
            point.location = (0.0,0.05625000223517418)
            point = node.mapping.curves[3].points.new(0,0)
            point.handle_type = 'AUTO'
            point.location = (0.35454559326171875,0.18125000596046448)
            point = node.mapping.curves[3].points.new(0,0)
            point.handle_type = 'AUTO'
            point.location = (0.595454752445221,0.8625002503395081)
            point = node.mapping.curves[3].points.new(0,0)
            point.handle_type = 'AUTO'
            point.location = (1.0,1.0)
            node.mapping.update()
            node.mute = False
            node.name = 'RGB Curves'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('realisticcolor')
            node.inputs['Scale'].default_value = -1.8999996185302734
            node.inputs['Detail'].default_value = 6.799999713897705
            node.inputs['Roughness'].default_value = 0.6499999761581421
            node.inputs['Distortion'].default_value = 0.0
            node.inputs['Color1'].default_value = (0.49999991059303284,0.1047055572271347,0.01735890656709671,1.0)
            node.inputs['Color2'].default_value = (0.017199670895934105,0.00760540971532464,0.004268367774784565,1.0)
            node.inputs['Coord'].default_value = (1.0,1.0,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,1.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -456.88165283203125
            node.location[1] = 462.37603759765625
            node.mute = False
            node.name = 'Realistic Color'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeBsdfPrincipled')
            node.inputs['Base Color'].default_value = (0.09487733244895935,0.01664968580007553,0.0051912362687289715,1.0)
            node.inputs['Subsurface'].default_value = 0.0
            node.inputs['Subsurface Radius'].default_value = (1.0,0.20000000298023224,0.10000000149011612)
            node.inputs['Subsurface Color'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            node.inputs['Metallic'].default_value = 1.0
            node.inputs['Specular'].default_value = 0.5
            node.inputs['Specular Tint'].default_value = 0.0
            node.inputs['Roughness'].default_value = 0.1772727370262146
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
            node.location[0] = 762.5438842773438
            node.location[1] = 129.62594604492188
            node.mute = False
            node.name = 'Principled BSDF'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.subsurface_method = 'BURLEY'
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('rust')
            node.inputs['Scale'].default_value = 0.7000001668930054
            node.inputs['Detail'].default_value = 16.0
            node.inputs['Roughness'].default_value = 0.824999988079071
            node.inputs['Coord'].default_value = (0.0,0.0,0.0)
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -448.60748291015625
            node.location[1] = -107.13262939453125
            node.mute = False
            node.name = 'Rust'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 0.925000011920929
            node.inputs['Color1'].default_value = (0.5,0.10470599681138992,0.017358999699354172,1.0)
            node.inputs['Color2'].default_value = (0.0,0.0,0.0,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MULTIPLY'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -762.5438842773438
            node.location[1] = 257.816162109375
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

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 0.9333333373069763
            node.inputs['Color1'].default_value = (0.09036199748516083,0.13874299824237823,0.07059299945831299,1.0)
            node.inputs['Color2'].default_value = (0.0,0.0,0.0,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MULTIPLY'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -757.5806274414062
            node.location[1] = 39.10772705078125
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

            node = self.grp.nodes.new('realisticcolor')
            node.inputs['Scale'].default_value = -1.1999996900558472
            node.inputs['Detail'].default_value = 6.799999713897705
            node.inputs['Roughness'].default_value = 0.6499999761581421
            node.inputs['Distortion'].default_value = 0.0
            node.inputs['Color1'].default_value = (0.09036161005496979,0.13874328136444092,0.07059308141469955,1.0)
            node.inputs['Color2'].default_value = (0.012589171528816223,0.017160972580313683,0.0038210095372051,1.0)
            node.inputs['Coord'].default_value = (1.0,1.0,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,1.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -456.15057373046875
            node.location[1] = 177.84100341796875
            node.mute = False
            node.name = 'Realistic Color.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketColor', 'Color1')
            self.grp.inputs['Color1'].default_value = (0.5,0.10470599681138992,0.017358999699354172,1.0)
            self.grp.inputs.new('NodeSocketColor', 'Color2')
            self.grp.inputs['Color2'].default_value = (0.09036199748516083,0.13874299824237823,0.07059299945831299,1.0)
            self.grp.inputs.new('NodeSocketFloat', 'Roughness')
            self.grp.inputs['Roughness'].default_value = 13.69999885559082
            self.grp.inputs['Roughness'].min_value = -10000.0
            self.grp.inputs['Roughness'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketVector', 'Normal')
            self.grp.inputs['Normal'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['Normal'].min_value = -1.0
            self.grp.inputs['Normal'].max_value = 1.0
            self.grp.inputs.new('NodeSocketVector', 'Coord')
            self.grp.inputs['Coord'].default_value = (1.0,1.0,1.0)
            self.grp.inputs['Coord'].min_value = -10000.0
            self.grp.inputs['Coord'].max_value = 10000.0
            node.outputs['Color1'].default_value = (0.5,0.10470599681138992,0.017358999699354172,1.0)
            node.outputs['Color2'].default_value = (0.09036199748516083,0.13874299824237823,0.07059299945831299,1.0)
            node.outputs['Roughness'].default_value = 13.69999885559082
            node.outputs['Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Coord'].default_value = (1.0,1.0,1.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1263.21923828125
            node.location[1] = 87.84683227539062
            node.mute = False
            node.name = 'Group Input'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 13.69999885559082
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 542.5439453125
            node.location[1] = -93.0570068359375
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

            node = self.grp.nodes.new('NodeGroupOutput')
            self.grp.outputs.new('NodeSocketShader', 'BSDF')
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.is_active_output = True
            node.label = ''
            node.location[0] = 1159.286865234375
            node.location[1] = 44.78072738647461
            node.mute = False
            node.name = 'Group Output'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

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
            node.location[0] = 233.66159057617188
            node.location[1] = 165.76361083984375
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

            links = self.grp.links
            links.new(self.grp.nodes["Noise Bump"].outputs[0], self.grp.nodes["Principled BSDF"].inputs[19])
            links.new(self.grp.nodes["Rust"].outputs[0], self.grp.nodes["Mix"].inputs[0])
            links.new(self.grp.nodes["Realistic Color"].outputs[0], self.grp.nodes["Mix"].inputs[1])
            links.new(self.grp.nodes["Realistic Color.001"].outputs[0], self.grp.nodes["Mix"].inputs[2])
            links.new(self.grp.nodes["Mix"].outputs[0], self.grp.nodes["Principled BSDF"].inputs[0])
            links.new(self.grp.nodes["Rust"].outputs[0], self.grp.nodes["RGB Curves"].inputs[1])
            links.new(self.grp.nodes["RGB Curves"].outputs[0], self.grp.nodes["Math"].inputs[0])
            links.new(self.grp.nodes["Rust"].outputs[0], self.grp.nodes["ColorRamp"].inputs[0])
            links.new(self.grp.nodes["ColorRamp"].outputs[0], self.grp.nodes["Bump"].inputs[2])
            links.new(self.grp.nodes["Bump"].outputs[0], self.grp.nodes["Noise Bump"].inputs[3])
            links.new(self.grp.nodes["Math"].outputs[0], self.grp.nodes["Principled BSDF"].inputs[7])
            links.new(self.grp.nodes["Mix.001"].outputs[0], self.grp.nodes["Realistic Color"].inputs[5])
            links.new(self.grp.nodes["Mix.002"].outputs[0], self.grp.nodes["Realistic Color.001"].inputs[5])
            links.new(self.grp.nodes["Principled BSDF"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Realistic Color"].inputs[6])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Realistic Color.001"].inputs[6])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Rust"].inputs[3])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Mix.001"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Mix.002"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Realistic Color"].inputs[4])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Realistic Color.001"].inputs[4])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Math"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Bump"].inputs[5])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Rust Shader"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Rust Shader" : 
                return True

        return False







