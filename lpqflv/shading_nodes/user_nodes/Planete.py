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

class Planete (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Planete"
    bl_idname = "planete"

    def createTree (self) : 

        if Planete.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Planete', 'ShaderNodeTree')

            node = self.grp.nodes.new('NodeFrame')
            node.color[0] = 0.6000000238418579
            node.color[1] = 0.6000000238418579
            node.color[2] = 0.6000000238418579
            node.hide = False
            node.label = 'Athmo'
            node.label_size = 20
            node.location[0] = 246.86842346191406
            node.location[1] = -1811.1287841796875
            node.mute = False
            node.name = 'Frame.002'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.shrink = True
            node.use_custom_color = True
            node.width = 951.7755126953125
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeFrame')
            node.color[0] = 0.6000000238418579
            node.color[1] = 0.6000000238418579
            node.color[2] = 0.6000000238418579
            node.hide = False
            node.label = 'Clouds'
            node.label_size = 20
            node.location[0] = 885.6231079101562
            node.location[1] = -1124.7098388671875
            node.mute = False
            node.name = 'Frame.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.shrink = True
            node.use_custom_color = True
            node.width = 1668.7177734375
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeFrame')
            node.color[0] = 0.6000000238418579
            node.color[1] = 0.6000000238418579
            node.color[2] = 0.6000000238418579
            node.hide = False
            node.label = ' '
            node.label_size = 20
            node.location[0] = 1675.5352783203125
            node.location[1] = -1068.236083984375
            node.mute = False
            node.name = 'Frame'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.shrink = True
            node.use_custom_color = True
            node.width = 2128.169677734375
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixShader')
            node.inputs['Fac'].default_value = 0.5
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 1181.2904052734375
            node.location[1] = -521.1198120117188
            node.mute = False
            node.name = 'Mix Shader'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixShader')
            node.inputs['Fac'].default_value = 0.5
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 1353.6197509765625
            node.location[1] = -572.7528076171875
            node.mute = False
            node.name = 'Mix Shader.003'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeAddShader')
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 1518.6253662109375
            node.location[1] = -612.4705200195312
            node.mute = False
            node.name = 'Add Shader'
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
            node.location[0] = 1674.2808837890625
            node.location[1] = -642.9207153320312
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
            node.location[0] = -556.0784912109375
            node.location[1] = 31.62255859375
            node.mute = False
            node.name = 'Emission'
            node.parent = self.grp.nodes["Frame.002"]
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
            node.location[0] = -764.0181274414062
            node.location[1] = 60.9588623046875
            node.mute = False
            node.name = 'Math.015'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
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
            node.location[0] = -941.6796264648438
            node.location[1] = 65.400634765625
            node.mute = False
            node.name = 'Math.016'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = True
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeVectorMath')
            node.inputs['Vector'].default_value = (-0.7911105155944824,0.13984301686286926,0.5954728722572327)
            node.inputs['Vector'].default_value = (-0.8043993711471558,0.14213362336158752,0.5768359303474426)
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Scale'].default_value = 1.0
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1123.919189453125
            node.location[1] = -52.99609375
            node.mute = False
            node.name = 'Vector Math'
            node.operation = 'DOT_PRODUCT'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeFresnel')
            node.inputs['IOR'].default_value = 1.5
            node.inputs['Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1307.5673828125
            node.location[1] = 171.2432861328125
            node.mute = False
            node.name = 'Fresnel'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeNewGeometry')
            node.outputs['Position'].default_value = (0.0,0.0,0.0)
            node.outputs['Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Tangent'].default_value = (0.0,0.0,0.0)
            node.outputs['True Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Incoming'].default_value = (0.0,0.0,0.0)
            node.outputs['Parametric'].default_value = (0.0,0.0,0.0)
            node.outputs['Backfacing'].default_value = 0.0
            node.outputs['Pointiness'].default_value = 0.0
            node.outputs['Random Per Island'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1307.85400390625
            node.location[1] = 63.054931640625
            node.mute = False
            node.name = 'Geometry'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeBsdfPrincipled')
            node.inputs['Base Color'].default_value = (0.5907295942306519,0.5531636476516724,0.5999131202697754,1.0)
            node.inputs['Subsurface'].default_value = 0.0
            node.inputs['Subsurface Radius'].default_value = (1.0,0.20000000298023224,0.10000000149011612)
            node.inputs['Subsurface Color'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            node.inputs['Metallic'].default_value = 0.0
            node.inputs['Specular'].default_value = 1.0
            node.inputs['Specular Tint'].default_value = 0.0
            node.inputs['Roughness'].default_value = 0.831818163394928
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
            node.label = 'Clouds'
            node.location[0] = -579.03271484375
            node.location[1] = 222.6785888671875
            node.mute = False
            node.name = 'Principled BSDF.004'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.subsurface_method = 'BURLEY'
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMapRange')
            node.inputs['Value'].default_value = 1.0
            node.inputs['From Min'].default_value = 0.0
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
            node.label = 'clouds Mask'
            node.location[0] = -747.565185546875
            node.location[1] = -9.0863037109375
            node.mute = False
            node.name = 'Map Range.006'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.0
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -943.5013427734375
            node.location[1] = 53.940185546875
            node.mute = False
            node.name = 'Math.012'
            node.operation = 'ADD'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
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
            node.location[0] = -1336.6439208984375
            node.location[1] = 219.2947998046875
            node.mute = False
            node.name = 'Math.010'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.0
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1138.1661376953125
            node.location[1] = 172.65185546875
            node.mute = False
            node.name = 'Math.009'
            node.operation = 'ADD'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.0
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1183.9951171875
            node.location[1] = -103.578857421875
            node.mute = False
            node.name = 'Math.008'
            node.operation = 'ADD'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexNoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 1.7999999523162842
            node.inputs['Detail'].default_value = 16.0
            node.inputs['Roughness'].default_value = 0.8416666984558105
            node.inputs['Distortion'].default_value = 0.19999998807907104
            node.outputs['Fac'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1938.8275146484375
            node.location[1] = 297.90386962890625
            node.mute = False
            node.name = 'Noise Texture.005'
            node.noise_dimensions = '3D'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = True
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexNoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 10.399999618530273
            node.inputs['Detail'].default_value = 16.0
            node.inputs['Roughness'].default_value = 0.6000000238418579
            node.inputs['Distortion'].default_value = 0.25
            node.outputs['Fac'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1505.061279296875
            node.location[1] = 262.58319091796875
            node.mute = False
            node.name = 'Noise Texture.002'
            node.noise_dimensions = '3D'
            node.parent = self.grp.nodes["Frame.001"]
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
            element = node.color_ramp.elements.new(0.5681821703910828)
            element.color = (1.0,1.0,1.0,1.0)
            element.alpha = 1.0
            element.position = 0.5681821703910828
            node.hide = False
            node.label = ''
            node.location[0] = -1774.291748046875
            node.location[1] = 302.19085693359375
            node.mute = False
            node.name = 'ColorRamp'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexMusgrave')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 4.699999809265137
            node.inputs['Detail'].default_value = 16.0
            node.inputs['Dimension'].default_value = 0.8000000715255737
            node.inputs['Lacunarity'].default_value = 2.0
            node.inputs['Offset'].default_value = 0.0
            node.inputs['Gain'].default_value = 1.0
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1490.618896484375
            node.location[1] = -204.0133056640625
            node.musgrave_dimensions = '3D'
            node.musgrave_type = 'FBM'
            node.mute = False
            node.name = 'Musgrave Texture'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 150.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexNoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 1.0
            node.inputs['Detail'].default_value = 16.0
            node.inputs['Roughness'].default_value = 0.7000000476837158
            node.inputs['Distortion'].default_value = 1.5999999046325684
            node.outputs['Fac'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1646.035400390625
            node.location[1] = -204.0133056640625
            node.mute = False
            node.name = 'Noise Texture.004'
            node.noise_dimensions = '3D'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.4000000059604645
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1794.8756103515625
            node.location[1] = -204.0133056640625
            node.mute = False
            node.name = 'Math.013'
            node.operation = 'ADD'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 1.0
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1947.75048828125
            node.location[1] = -204.0133056640625
            node.mute = False
            node.name = 'Math.014'
            node.operation = 'DIVIDE'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
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
            node.location[0] = -1357.64697265625
            node.location[1] = 37.715087890625
            node.mute = False
            node.name = 'Math.011'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexNoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 68.99999237060547
            node.inputs['Detail'].default_value = 16.0
            node.inputs['Roughness'].default_value = 0.7000000476837158
            node.inputs['Distortion'].default_value = 0.0
            node.outputs['Fac'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1522.787353515625
            node.location[1] = 41.637451171875
            node.mute = False
            node.name = 'Noise Texture.003'
            node.noise_dimensions = '3D'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexNoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 0.800000011920929
            node.inputs['Detail'].default_value = 16.0
            node.inputs['Roughness'].default_value = 0.8166667222976685
            node.inputs['Distortion'].default_value = 0.4000000059604645
            node.outputs['Fac'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1945.044921875
            node.location[1] = 45.6788330078125
            node.mute = False
            node.name = 'Noise Texture.006'
            node.noise_dimensions = '3D'
            node.parent = self.grp.nodes["Frame.001"]
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
            element = node.color_ramp.elements.new(0.5681821703910828)
            element.color = (1.0,1.0,1.0,1.0)
            element.alpha = 1.0
            element.position = 0.5681821703910828
            node.hide = False
            node.label = ''
            node.location[0] = -1791.6083984375
            node.location[1] = 45.2535400390625
            node.mute = False
            node.name = 'ColorRamp.001'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeBsdfPrincipled')
            node.inputs['Base Color'].default_value = (0.9844908118247986,0.9210675954818726,1.0,1.0)
            node.inputs['Subsurface'].default_value = 0.0
            node.inputs['Subsurface Radius'].default_value = (1.0,0.20000000298023224,0.10000000149011612)
            node.inputs['Subsurface Color'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            node.inputs['Metallic'].default_value = 0.0
            node.inputs['Specular'].default_value = 0.5
            node.inputs['Specular Tint'].default_value = 0.0
            node.inputs['Roughness'].default_value = 0.5
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
            node.label = 'Cold'
            node.location[0] = -1375.5577392578125
            node.location[1] = 942.8115234375
            node.mute = False
            node.name = 'Principled BSDF.002'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.subsurface_method = 'BURLEY'
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('hardnoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Scale'].default_value = 2.0
            node.inputs['Roughness'].default_value = 0.8560000061988831
            node.inputs['Distortion'].default_value = 0.0
            node.inputs['Details'].default_value = 7.099999904632568
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1786.8326416015625
            node.location[1] = 954.6090698242188
            node.mute = False
            node.name = 'Hard Noise.004'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixShader')
            node.inputs['Fac'].default_value = 0.5
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -802.49609375
            node.location[1] = 1206.32470703125
            node.mute = False
            node.name = 'Mix Shader.001'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixShader')
            node.inputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -994.9225463867188
            node.location[1] = 1513.018310546875
            node.mute = False
            node.name = 'Mix Shader.002'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeGamma')
            node.inputs['Color'].default_value = (1.0,1.0,1.0,1.0)
            node.inputs['Gamma'].default_value = 9.999999046325684
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -2026.371337890625
            node.location[1] = 779.258544921875
            node.mute = False
            node.name = 'Gamma'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.800000011920929
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1788.2769775390625
            node.location[1] = 616.2499389648438
            node.mute = False
            node.name = 'Math.002'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = True
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 0.5
            node.inputs['Color1'].default_value = (0.9844909906387329,0.921068012714386,1.0,1.0)
            node.inputs['Color2'].default_value = (0.32862091064453125,0.3482204079627991,0.4721958637237549,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MIX'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1785.8388671875
            node.location[1] = 789.8687133789062
            node.mute = False
            node.name = 'Mix.002'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_alpha = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMapRange')
            node.inputs['Value'].default_value = 1.0
            node.inputs['From Min'].default_value = 0.0
            node.inputs['From Max'].default_value = 0.5800000429153442
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
            node.location[0] = -1581.0670166015625
            node.location[1] = 976.1304931640625
            node.mute = False
            node.name = 'Map Range.003'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 1.0
            node.inputs['Color1'].default_value = (0.5,0.5,0.5,1.0)
            node.inputs['Color2'].default_value = (0.1632324904203415,0.05701287463307381,0.01703963801264763,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MULTIPLY'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -2314.655517578125
            node.location[1] = 1383.35546875
            node.mute = False
            node.name = 'Mix.004'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_alpha = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('hardnoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Scale'].default_value = 2.0
            node.inputs['Roughness'].default_value = 0.8560000061988831
            node.inputs['Distortion'].default_value = 0.0
            node.inputs['Details'].default_value = 27.100000381469727
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -2314.40625
            node.location[1] = 1551.6463623046875
            node.mute = False
            node.name = 'Hard Noise.003'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 0.5
            node.inputs['Color1'].default_value = (0.02280518226325512,0.11470810323953629,0.03412305936217308,1.0)
            node.inputs['Color2'].default_value = (0.02344626560807228,0.009978349320590496,0.004156310576945543,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MIX'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -2099.811279296875
            node.location[1] = 1560.011962890625
            node.mute = False
            node.name = 'Mix.003'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_alpha = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeBsdfPrincipled')
            node.inputs['Base Color'].default_value = (0.25406816601753235,0.05655979365110397,0.004090158734470606,1.0)
            node.inputs['Subsurface'].default_value = 0.0
            node.inputs['Subsurface Radius'].default_value = (1.0,0.20000000298023224,0.10000000149011612)
            node.inputs['Subsurface Color'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            node.inputs['Metallic'].default_value = 0.0
            node.inputs['Specular'].default_value = 0.05909091234207153
            node.inputs['Specular Tint'].default_value = 0.0
            node.inputs['Roughness'].default_value = 0.7272727489471436
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
            node.label = 'Grass'
            node.location[0] = -1880.017333984375
            node.location[1] = 1552.4559326171875
            node.mute = False
            node.name = 'Principled BSDF.003'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.subsurface_method = 'BURLEY'
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMapRange')
            node.inputs['Value'].default_value = 1.0
            node.inputs['From Min'].default_value = 0.42000001668930054
            node.inputs['From Max'].default_value = 0.5
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
            node.location[0] = -2527.527587890625
            node.location[1] = 1536.5572509765625
            node.mute = False
            node.name = 'Map Range.004'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('hardnoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Scale'].default_value = 7.300000190734863
            node.inputs['Roughness'].default_value = 0.699999988079071
            node.inputs['Distortion'].default_value = 1.7999999523162842
            node.inputs['Details'].default_value = 11.600000381469727
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -2492.1025390625
            node.location[1] = 1729.010009765625
            node.mute = False
            node.name = 'Hard Noise.001'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('hardnoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Scale'].default_value = 6.590000152587891
            node.inputs['Roughness'].default_value = 0.699999988079071
            node.inputs['Distortion'].default_value = 0.0
            node.inputs['Details'].default_value = 71.0
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -2718.59423828125
            node.location[1] = 1505.62744140625
            node.mute = False
            node.name = 'Hard Noise.002'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexNoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 11.800000190734863
            node.inputs['Detail'].default_value = 15.899999618530273
            node.inputs['Roughness'].default_value = 0.6833333373069763
            node.inputs['Distortion'].default_value = 0.0
            node.outputs['Fac'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -2730.665771484375
            node.location[1] = 1749.6298828125
            node.mute = False
            node.name = 'Noise Texture.001'
            node.noise_dimensions = '3D'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeBsdfPrincipled')
            node.inputs['Base Color'].default_value = (0.25406816601753235,0.05655979365110397,0.004090158734470606,1.0)
            node.inputs['Subsurface'].default_value = 0.0
            node.inputs['Subsurface Radius'].default_value = (1.0,0.20000000298023224,0.10000000149011612)
            node.inputs['Subsurface Color'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            node.inputs['Metallic'].default_value = 0.0
            node.inputs['Specular'].default_value = 0.5
            node.inputs['Specular Tint'].default_value = 0.0
            node.inputs['Roughness'].default_value = 0.5
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
            node.label = 'Sand'
            node.location[0] = -1343.0662841796875
            node.location[1] = 1915.65576171875
            node.mute = False
            node.name = 'Principled BSDF'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.subsurface_method = 'BURLEY'
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.7300000190734863
            node.inputs['Value'].default_value = 0.07000000029802322
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = 'Cold Mask'
            node.location[0] = -2336.30224609375
            node.location[1] = 1944.8468017578125
            node.mute = False
            node.name = 'Math.001'
            node.operation = 'GREATER_THAN'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMapRange')
            node.inputs['Value'].default_value = 1.0
            node.inputs['From Min'].default_value = 1.0
            node.inputs['From Max'].default_value = 0.0
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
            node.location[0] = -2336.30224609375
            node.location[1] = 2184.164306640625
            node.mute = False
            node.name = 'Map Range.002'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.10000000149011612
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -2336.30224609375
            node.location[1] = 2374.130615234375
            node.mute = False
            node.name = 'Math.006'
            node.operation = 'ADD'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.05000000074505806
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -2554.126953125
            node.location[1] = 2187.04052734375
            node.mute = False
            node.name = 'Math.007'
            node.operation = 'DIVIDE'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('hardnoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Scale'].default_value = 6.400000095367432
            node.inputs['Roughness'].default_value = 0.8031089901924133
            node.inputs['Distortion'].default_value = 0.0
            node.inputs['Details'].default_value = 7.100000381469727
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -2554.099853515625
            node.location[1] = 2363.064697265625
            node.mute = False
            node.name = 'Hard Noise'
            node.parent = self.grp.nodes["Frame"]
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
            node.location[0] = -2218.6513671875
            node.location[1] = 1763.407958984375
            node.mute = False
            node.name = 'Math.005'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMapRange')
            node.inputs['Value'].default_value = 1.0
            node.inputs['From Min'].default_value = 0.559999942779541
            node.inputs['From Max'].default_value = 0.29999998211860657
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
            node.location[0] = -1995.7333984375
            node.location[1] = 2417.2109375
            node.mute = False
            node.name = 'Map Range.001'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexNoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 1500.0
            node.inputs['Detail'].default_value = 5.0
            node.inputs['Roughness'].default_value = 0.5
            node.inputs['Distortion'].default_value = 2.0299999713897705
            node.outputs['Fac'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -2137.943359375
            node.location[1] = 2226.15966796875
            node.mute = False
            node.name = 'Noise Texture'
            node.noise_dimensions = '3D'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMapRange')
            node.inputs['Value'].default_value = 1.0
            node.inputs['From Min'].default_value = 0.0
            node.inputs['From Max'].default_value = 0.6000000238418579
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
            node.location[0] = -2176.97021484375
            node.location[1] = 2561.98583984375
            node.mute = False
            node.name = 'Map Range'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeBsdfPrincipled')
            node.inputs['Base Color'].default_value = (0.018719591200351715,0.022212138399481773,0.040624573826789856,1.0)
            node.inputs['Subsurface'].default_value = 0.0
            node.inputs['Subsurface Radius'].default_value = (1.0,0.20000000298023224,0.10000000149011612)
            node.inputs['Subsurface Color'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            node.inputs['Metallic'].default_value = 0.0
            node.inputs['Specular'].default_value = 0.04545453190803528
            node.inputs['Specular Tint'].default_value = 0.0
            node.inputs['Roughness'].default_value = 0.5
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
            node.label = 'Sea'
            node.location[0] = -1595.832763671875
            node.location[1] = 2516.609375
            node.mute = False
            node.name = 'Principled BSDF.001'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.subsurface_method = 'BURLEY'
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeBump')
            node.inputs['Strength'].default_value = 0.10000000149011612
            node.inputs['Distance'].default_value = 0.9100000262260437
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
            node.location[0] = -1776.737060546875
            node.location[1] = 2167.85009765625
            node.mute = False
            node.name = 'Bump'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.8999999761581421
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1775.07568359375
            node.location[1] = 2337.29638671875
            node.mute = False
            node.name = 'Math'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 0.5
            node.inputs['Color1'].default_value = (0.050220370292663574,0.06085747107863426,0.11842139065265656,1.0)
            node.inputs['Color2'].default_value = (0.0,0.0,0.0,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MIX'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1778.4453125
            node.location[1] = 2530.11572265625
            node.mute = False
            node.name = 'Mix'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_alpha = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeBump')
            node.inputs['Strength'].default_value = 0.25
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
            node.location[0] = -1580.157470703125
            node.location[1] = 1537.5018310546875
            node.mute = False
            node.name = 'Bump.001'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 2.5
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1578.8165283203125
            node.location[1] = 1707.880859375
            node.mute = False
            node.name = 'Math.004'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = True
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
            node.location[0] = -2009.876220703125
            node.location[1] = 1898.550048828125
            node.mute = False
            node.name = 'Math.003'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = True
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMapRange')
            node.inputs['Value'].default_value = 1.0
            node.inputs['From Min'].default_value = 0.0
            node.inputs['From Max'].default_value = 0.32999998331069946
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
            node.location[0] = -1779.4906005859375
            node.location[1] = 1986.972900390625
            node.mute = False
            node.name = 'Map Range.005'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 0.5
            node.inputs['Color1'].default_value = (1.0,0.40549376606941223,0.09224849194288254,1.0)
            node.inputs['Color2'].default_value = (0.0,0.0,0.0,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MIX'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1595.333740234375
            node.location[1] = 1923.3038330078125
            node.mute = False
            node.name = 'Mix.001'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_alpha = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketFloat', 'Sea Scale')
            self.grp.inputs['Sea Scale'].default_value = 0.17000000178813934
            self.grp.inputs['Sea Scale'].min_value = -1000.0
            self.grp.inputs['Sea Scale'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketFloat', 'Sea Mask Details')
            self.grp.inputs['Sea Mask Details'].default_value = 9.0
            self.grp.inputs['Sea Mask Details'].min_value = -1000.0
            self.grp.inputs['Sea Mask Details'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketFloat', 'Sea Density')
            self.grp.inputs['Sea Density'].default_value = 0.5
            self.grp.inputs['Sea Density'].min_value = 0.0
            self.grp.inputs['Sea Density'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketFloat', 'Sea Mask Contrast')
            self.grp.inputs['Sea Mask Contrast'].default_value = 0.5
            self.grp.inputs['Sea Mask Contrast'].min_value = -10000.0
            self.grp.inputs['Sea Mask Contrast'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketColor', 'Sea Color')
            self.grp.inputs['Sea Color'].default_value = (0.050220370292663574,0.06085747107863426,0.11842139065265656,1.0)
            self.grp.inputs.new('NodeSocketFloat', 'Wave Size')
            self.grp.inputs['Wave Size'].default_value = 1500.0
            self.grp.inputs['Wave Size'].min_value = -1000.0
            self.grp.inputs['Wave Size'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketFloat', 'Wave Height')
            self.grp.inputs['Wave Height'].default_value = 0.9100000262260437
            self.grp.inputs['Wave Height'].min_value = 0.0
            self.grp.inputs['Wave Height'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketFloat', 'Cold Height')
            self.grp.inputs['Cold Height'].default_value = 0.7300000190734863
            self.grp.inputs['Cold Height'].min_value = -10000.0
            self.grp.inputs['Cold Height'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketColor', 'Cold Color')
            self.grp.inputs['Cold Color'].default_value = (0.0,0.0,0.0,1.0)
            self.grp.inputs.new('NodeSocketFloat', 'Cold Texture Scale')
            self.grp.inputs['Cold Texture Scale'].default_value = 11.800000190734863
            self.grp.inputs['Cold Texture Scale'].min_value = -1000.0
            self.grp.inputs['Cold Texture Scale'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketColor', 'Sand Color')
            self.grp.inputs['Sand Color'].default_value = (1.0,0.40549376606941223,0.09224849194288254,1.0)
            self.grp.inputs.new('NodeSocketColor', 'Grass Color')
            self.grp.inputs['Grass Color'].default_value = (0.5,0.5,0.5,1.0)
            self.grp.inputs.new('NodeSocketFloat', 'Send Density')
            self.grp.inputs['Send Density'].default_value = 0.5800000429153442
            self.grp.inputs['Send Density'].min_value = 0.0
            self.grp.inputs['Send Density'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketFloatFactor', 'Sand Mask Roughness')
            self.grp.inputs['Sand Mask Roughness'].default_value = 0.5750000476837158
            self.grp.inputs['Sand Mask Roughness'].min_value = 0.0
            self.grp.inputs['Sand Mask Roughness'].max_value = 1.0
            self.grp.inputs.new('NodeSocketFloat', 'Sand Mask Scale')
            self.grp.inputs['Sand Mask Scale'].default_value = 0.9000001549720764
            self.grp.inputs['Sand Mask Scale'].min_value = -1000.0
            self.grp.inputs['Sand Mask Scale'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketColor', 'Clouds Color')
            self.grp.inputs['Clouds Color'].default_value = (0.5907295942306519,0.5531636476516724,0.5999131202697754,1.0)
            self.grp.inputs.new('NodeSocketFloat', 'Clouds Density')
            self.grp.inputs['Clouds Density'].default_value = 0.5
            self.grp.inputs['Clouds Density'].min_value = -10000.0
            self.grp.inputs['Clouds Density'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketColor', 'Athmosphere Color')
            self.grp.inputs['Athmosphere Color'].default_value = (1.0,1.0,1.0,1.0)
            self.grp.inputs.new('NodeSocketFloat', 'Athmosphere Power')
            self.grp.inputs['Athmosphere Power'].default_value = 0.5
            self.grp.inputs['Athmosphere Power'].min_value = 0.0
            self.grp.inputs['Athmosphere Power'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketFloat', 'Athmosphere IOR')
            self.grp.inputs['Athmosphere IOR'].default_value = 1.5
            self.grp.inputs['Athmosphere IOR'].min_value = 0.0
            self.grp.inputs['Athmosphere IOR'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketVector', 'Light Direction')
            self.grp.inputs['Light Direction'].default_value = (-0.8043993711471558,0.14213362336158752,0.5768359303474426)
            self.grp.inputs['Light Direction'].min_value = -10000.0
            self.grp.inputs['Light Direction'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketVector', 'Ground Mapping')
            self.grp.inputs['Ground Mapping'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['Ground Mapping'].min_value = -3.4028234663852886e+38
            self.grp.inputs['Ground Mapping'].max_value = 3.4028234663852886e+38
            self.grp.inputs.new('NodeSocketVector', 'Cloud Mapping')
            self.grp.inputs['Cloud Mapping'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['Cloud Mapping'].min_value = -3.4028234663852886e+38
            self.grp.inputs['Cloud Mapping'].max_value = 3.4028234663852886e+38
            node.outputs['Sea Scale'].default_value = 0.17000000178813934
            node.outputs['Sea Mask Details'].default_value = 9.0
            node.outputs['Sea Density'].default_value = 0.5
            node.outputs['Sea Mask Contrast'].default_value = 0.5
            node.outputs['Sea Color'].default_value = (0.050220370292663574,0.06085747107863426,0.11842139065265656,1.0)
            node.outputs['Wave Size'].default_value = 1500.0
            node.outputs['Wave Height'].default_value = 0.9100000262260437
            node.outputs['Cold Height'].default_value = 0.7300000190734863
            node.outputs['Cold Color'].default_value = (0.0,0.0,0.0,1.0)
            node.outputs['Cold Texture Scale'].default_value = 11.800000190734863
            node.outputs['Sand Color'].default_value = (1.0,0.40549376606941223,0.09224849194288254,1.0)
            node.outputs['Grass Color'].default_value = (0.5,0.5,0.5,1.0)
            node.outputs['Send Density'].default_value = 0.5800000429153442
            node.outputs['Sand Mask Roughness'].default_value = 0.5750000476837158
            node.outputs['Sand Mask Scale'].default_value = 0.9000001549720764
            node.outputs['Clouds Color'].default_value = (0.5907295942306519,0.5531636476516724,0.5999131202697754,1.0)
            node.outputs['Clouds Density'].default_value = 0.5
            node.outputs['Athmosphere Color'].default_value = (1.0,1.0,1.0,1.0)
            node.outputs['Athmosphere Power'].default_value = 0.5
            node.outputs['Athmosphere IOR'].default_value = 1.5
            node.outputs['Light Direction'].default_value = (-0.8043993711471558,0.14213362336158752,0.5768359303474426)
            node.outputs['Ground Mapping'].default_value = (0.0,0.0,0.0)
            node.outputs['Cloud Mapping'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1512.70703125
            node.location[1] = -494.48944091796875
            node.mute = False
            node.name = 'Group Input'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            links = self.grp.links
            links.new(self.grp.nodes["Map Range"].outputs[0], self.grp.nodes["Mix Shader"].inputs[0])
            links.new(self.grp.nodes["Principled BSDF.001"].outputs[0], self.grp.nodes["Mix Shader"].inputs[1])
            links.new(self.grp.nodes["Map Range.001"].outputs[0], self.grp.nodes["Mix"].inputs[0])
            links.new(self.grp.nodes["Mix"].outputs[0], self.grp.nodes["Principled BSDF.001"].inputs[0])
            links.new(self.grp.nodes["Noise Texture"].outputs[0], self.grp.nodes["Bump"].inputs[2])
            links.new(self.grp.nodes["Bump"].outputs[0], self.grp.nodes["Principled BSDF.001"].inputs[19])
            links.new(self.grp.nodes["Noise Texture"].outputs[0], self.grp.nodes["Math"].inputs[0])
            links.new(self.grp.nodes["Math"].outputs[0], self.grp.nodes["Principled BSDF.001"].inputs[7])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Mix"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[5], self.grp.nodes["Noise Texture"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[6], self.grp.nodes["Bump"].inputs[1])
            links.new(self.grp.nodes["Map Range.002"].outputs[0], self.grp.nodes["Math.003"].inputs[0])
            links.new(self.grp.nodes["Mix.001"].outputs[0], self.grp.nodes["Principled BSDF"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[7], self.grp.nodes["Math.001"].inputs[1])
            links.new(self.grp.nodes["Principled BSDF.002"].outputs[0], self.grp.nodes["Mix Shader.001"].inputs[2])
            links.new(self.grp.nodes["Math.001"].outputs[0], self.grp.nodes["Mix Shader.001"].inputs[0])
            links.new(self.grp.nodes["Mix Shader.001"].outputs[0], self.grp.nodes["Mix Shader"].inputs[2])
            links.new(self.grp.nodes["Mix.002"].outputs[0], self.grp.nodes["Principled BSDF.002"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[8], self.grp.nodes["Mix.002"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[8], self.grp.nodes["Gamma"].inputs[0])
            links.new(self.grp.nodes["Gamma"].outputs[0], self.grp.nodes["Mix.002"].inputs[2])
            links.new(self.grp.nodes["Noise Texture.001"].outputs[0], self.grp.nodes["Mix.002"].inputs[0])
            links.new(self.grp.nodes["Noise Texture.001"].outputs[0], self.grp.nodes["Math.002"].inputs[0])
            links.new(self.grp.nodes["Math.002"].outputs[0], self.grp.nodes["Principled BSDF.002"].inputs[7])
            links.new(self.grp.nodes["Group Input"].outputs[9], self.grp.nodes["Noise Texture.001"].inputs[2])
            links.new(self.grp.nodes["Math.003"].outputs[0], self.grp.nodes["Map Range.005"].inputs[0])
            links.new(self.grp.nodes["Math.003"].outputs[0], self.grp.nodes["Bump.001"].inputs[2])
            links.new(self.grp.nodes["Bump.001"].outputs[0], self.grp.nodes["Principled BSDF"].inputs[19])
            links.new(self.grp.nodes["Math.003"].outputs[0], self.grp.nodes["Math.004"].inputs[0])
            links.new(self.grp.nodes["Math.004"].outputs[0], self.grp.nodes["Principled BSDF"].inputs[7])
            links.new(self.grp.nodes["Group Input"].outputs[10], self.grp.nodes["Mix.001"].inputs[1])
            links.new(self.grp.nodes["Hard Noise.003"].outputs[0], self.grp.nodes["Mix.003"].inputs[0])
            links.new(self.grp.nodes["Mix.003"].outputs[0], self.grp.nodes["Principled BSDF.003"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[11], self.grp.nodes["Mix.004"].inputs[1])
            links.new(self.grp.nodes["Mix.004"].outputs[0], self.grp.nodes["Mix.003"].inputs[2])
            links.new(self.grp.nodes["Principled BSDF"].outputs[0], self.grp.nodes["Mix Shader.002"].inputs[1])
            links.new(self.grp.nodes["Principled BSDF.003"].outputs[0], self.grp.nodes["Mix Shader.002"].inputs[2])
            links.new(self.grp.nodes["Map Range.003"].outputs[0], self.grp.nodes["Mix Shader.002"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[12], self.grp.nodes["Map Range.003"].inputs[2])
            links.new(self.grp.nodes["Mix Shader.002"].outputs[0], self.grp.nodes["Mix Shader.001"].inputs[1])
            links.new(self.grp.nodes["Map Range.004"].outputs[0], self.grp.nodes["Math.005"].inputs[1])
            links.new(self.grp.nodes["Math.005"].outputs[0], self.grp.nodes["Math.003"].inputs[1])
            links.new(self.grp.nodes["Map Range.005"].outputs[0], self.grp.nodes["Mix.001"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Math.006"].inputs[0])
            links.new(self.grp.nodes["Math.006"].outputs[0], self.grp.nodes["Map Range"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Math.007"].inputs[1])
            links.new(self.grp.nodes["Math.007"].outputs[0], self.grp.nodes["Math.006"].inputs[1])
            links.new(self.grp.nodes["Noise Texture.004"].outputs[1], self.grp.nodes["Musgrave Texture"].inputs[0])
            links.new(self.grp.nodes["Musgrave Texture"].outputs[0], self.grp.nodes["Math.008"].inputs[0])
            links.new(self.grp.nodes["Noise Texture.003"].outputs[0], self.grp.nodes["Math.011"].inputs[0])
            links.new(self.grp.nodes["Noise Texture.005"].outputs[0], self.grp.nodes["ColorRamp"].inputs[0])
            links.new(self.grp.nodes["ColorRamp"].outputs[0], self.grp.nodes["Math.010"].inputs[1])
            links.new(self.grp.nodes["Noise Texture.002"].outputs[0], self.grp.nodes["Math.010"].inputs[0])
            links.new(self.grp.nodes["Noise Texture.006"].outputs[0], self.grp.nodes["ColorRamp.001"].inputs[0])
            links.new(self.grp.nodes["Math.011"].outputs[0], self.grp.nodes["Math.009"].inputs[1])
            links.new(self.grp.nodes["ColorRamp.001"].outputs[0], self.grp.nodes["Math.011"].inputs[1])
            links.new(self.grp.nodes["Math.010"].outputs[0], self.grp.nodes["Math.009"].inputs[0])
            links.new(self.grp.nodes["Math.009"].outputs[0], self.grp.nodes["Math.012"].inputs[0])
            links.new(self.grp.nodes["Math.008"].outputs[0], self.grp.nodes["Math.012"].inputs[1])
            links.new(self.grp.nodes["Math.012"].outputs[0], self.grp.nodes["Map Range.006"].inputs[0])
            links.new(self.grp.nodes["Math.013"].outputs[0], self.grp.nodes["Map Range.006"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[16], self.grp.nodes["Math.014"].inputs[1])
            links.new(self.grp.nodes["Math.014"].outputs[0], self.grp.nodes["Math.013"].inputs[0])
            links.new(self.grp.nodes["Math.014"].outputs[0], self.grp.nodes["Map Range.006"].inputs[1])
            links.new(self.grp.nodes["Mix Shader"].outputs[0], self.grp.nodes["Mix Shader.003"].inputs[1])
            links.new(self.grp.nodes["Principled BSDF.004"].outputs[0], self.grp.nodes["Mix Shader.003"].inputs[2])
            links.new(self.grp.nodes["Map Range.006"].outputs[0], self.grp.nodes["Mix Shader.003"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[15], self.grp.nodes["Principled BSDF.004"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[17], self.grp.nodes["Emission"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[18], self.grp.nodes["Math.015"].inputs[1])
            links.new(self.grp.nodes["Fresnel"].outputs[0], self.grp.nodes["Math.016"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[19], self.grp.nodes["Fresnel"].inputs[0])
            links.new(self.grp.nodes["Math.015"].outputs[0], self.grp.nodes["Emission"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[20], self.grp.nodes["Vector Math"].inputs[1])
            links.new(self.grp.nodes["Geometry"].outputs[1], self.grp.nodes["Vector Math"].inputs[0])
            links.new(self.grp.nodes["Math.016"].outputs[0], self.grp.nodes["Math.015"].inputs[0])
            links.new(self.grp.nodes["Vector Math"].outputs[1], self.grp.nodes["Math.016"].inputs[1])
            links.new(self.grp.nodes["Mix Shader.003"].outputs[0], self.grp.nodes["Add Shader"].inputs[0])
            links.new(self.grp.nodes["Emission"].outputs[0], self.grp.nodes["Add Shader"].inputs[1])
            links.new(self.grp.nodes["Add Shader"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[21], self.grp.nodes["Noise Texture"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[21], self.grp.nodes["Noise Texture.001"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[22], self.grp.nodes["Noise Texture.005"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[22], self.grp.nodes["Noise Texture.006"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[22], self.grp.nodes["Noise Texture.002"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[22], self.grp.nodes["Noise Texture.003"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[22], self.grp.nodes["Noise Texture.004"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Map Range"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[11], self.grp.nodes["Mix.003"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Hard Noise"].inputs[4])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Hard Noise"].inputs[1])
            links.new(self.grp.nodes["Hard Noise"].outputs[0], self.grp.nodes["Map Range"].inputs[0])
            links.new(self.grp.nodes["Hard Noise"].outputs[0], self.grp.nodes["Map Range.002"].inputs[0])
            links.new(self.grp.nodes["Hard Noise"].outputs[0], self.grp.nodes["Math.001"].inputs[0])
            links.new(self.grp.nodes["Hard Noise"].outputs[0], self.grp.nodes["Map Range.001"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[21], self.grp.nodes["Hard Noise"].inputs[0])
            links.new(self.grp.nodes["Hard Noise.001"].outputs[0], self.grp.nodes["Math.005"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[21], self.grp.nodes["Hard Noise.001"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[21], self.grp.nodes["Hard Noise.002"].inputs[0])
            links.new(self.grp.nodes["Hard Noise.002"].outputs[0], self.grp.nodes["Map Range.004"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[21], self.grp.nodes["Hard Noise.003"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[21], self.grp.nodes["Hard Noise.004"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[14], self.grp.nodes["Hard Noise.004"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[13], self.grp.nodes["Hard Noise.004"].inputs[2])
            links.new(self.grp.nodes["Hard Noise.004"].outputs[0], self.grp.nodes["Map Range.003"].inputs[0])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Planete"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Planete" : 
                return True

        return False







