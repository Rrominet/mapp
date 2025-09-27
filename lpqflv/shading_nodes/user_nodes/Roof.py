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

class Roof (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Roof"
    bl_idname = "roof"

    def createTree (self) : 

        if Roof.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Roof', 'ShaderNodeTree')

            node = self.grp.nodes.new('ShaderNodeRGBCurve')
            node.inputs['Fac'].default_value = 1.0
            node.inputs['Color'].default_value = (0.0,0.0,0.0,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 304.4366149902344
            node.location[1] = -360.1453857421875
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
            point.location = (0.0,0.018749989569187164)
            point = node.mapping.curves[3].points.new(0,0)
            point.handle_type = 'AUTO'
            point.location = (0.22727294266223907,0.12499994784593582)
            point = node.mapping.curves[3].points.new(0,0)
            point.handle_type = 'AUTO'
            point.location = (0.44090938568115234,0.737499475479126)
            point = node.mapping.curves[3].points.new(0,0)
            point.handle_type = 'AUTO'
            point.location = (1.0,0.9312500953674316)
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
            node.inputs['Scale'].default_value = 6.400000095367432
            node.inputs['Detail'].default_value = 11.929999351501465
            node.inputs['Roughness'].default_value = 0.574999988079071
            node.inputs['Distortion'].default_value = 0.0
            node.inputs['Color1'].default_value = (1.0,1.0,1.0,1.0)
            node.inputs['Color2'].default_value = (0.0,0.0,0.0,1.0)
            node.inputs['Additionnal Coord'].default_value = (1.0,1.0,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,1.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -293.67578125
            node.location[1] = -339.71148681640625
            node.mute = False
            node.name = 'Realistic Color.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexNoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 1000.0
            node.inputs['Detail'].default_value = 16.0
            node.inputs['Roughness'].default_value = 0.4749999940395355
            node.inputs['Distortion'].default_value = 0.0
            node.outputs['Fac'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -534.6075439453125
            node.location[1] = 348.38397216796875
            node.mute = False
            node.name = 'Noise Texture'
            node.noise_dimensions = '3D'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.25
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -229.45458984375
            node.location[1] = 486.34588623046875
            node.mute = False
            node.name = 'Math.001'
            node.operation = 'MULTIPLY'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeBsdfPrincipled')
            node.inputs['Base Color'].default_value = (0.010805626399815083,0.015411971136927605,0.0034793925005942583,1.0)
            node.inputs['Subsurface'].default_value = 0.0
            node.inputs['Subsurface Radius'].default_value = (1.0,0.20000000298023224,0.10000000149011612)
            node.inputs['Subsurface Color'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            node.inputs['Metallic'].default_value = 0.0
            node.inputs['Specular'].default_value = 0.7227272987365723
            node.inputs['Specular Tint'].default_value = 0.0
            node.inputs['Roughness'].default_value = 0.09090907871723175
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
            node.location[0] = 624.4036254882812
            node.location[1] = 583.7520141601562
            node.mute = False
            node.name = 'Principled BSDF.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.subsurface_method = 'BURLEY'
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1066.6839599609375
            node.location[1] = -157.68731689453125
            node.mute = False
            node.name = 'Reroute'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeBsdfPrincipled')
            node.inputs['Base Color'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            node.inputs['Subsurface'].default_value = 0.0
            node.inputs['Subsurface Radius'].default_value = (1.0,0.20000000298023224,0.10000000149011612)
            node.inputs['Subsurface Color'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            node.inputs['Metallic'].default_value = 0.0
            node.inputs['Specular'].default_value = 0.25
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
            node.label = ''
            node.location[0] = 682.271728515625
            node.location[1] = -226.86990356445312
            node.mute = False
            node.name = 'Principled BSDF'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.subsurface_method = 'BURLEY'
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeBump')
            node.inputs['Strength'].default_value = 1.0
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
            node.location[0] = -37.76904296875
            node.location[1] = 279.44866943359375
            node.mute = False
            node.name = 'Bump.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeBump')
            node.inputs['Strength'].default_value = 0.4583333134651184
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
            node.location[0] = 321.4490661621094
            node.location[1] = 211.314453125
            node.mute = False
            node.name = 'Bump.002'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.7000000476837158
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 115.47015380859375
            node.location[1] = 18.69134521484375
            node.mute = False
            node.name = 'Math.002'
            node.operation = 'MULTIPLY'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
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
            node.location[0] = 1565.3724365234375
            node.location[1] = -0.0
            node.mute = False
            node.name = 'Group Output'
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
            node.location[0] = -1689.5054931640625
            node.location[1] = -156.790283203125
            node.mute = False
            node.name = 'Texture Coordinate'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeVectorMath')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Scale'].default_value = 1.0
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1321.0040283203125
            node.location[1] = -140.45889282226562
            node.mute = False
            node.name = 'Vector Math'
            node.operation = 'MULTIPLY'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexMusgrave')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.3999999761581421
            node.inputs['Scale'].default_value = 145.63998413085938
            node.inputs['Detail'].default_value = 16.0
            node.inputs['Dimension'].default_value = 0.6899999380111694
            node.inputs['Lacunarity'].default_value = 0.800000011920929
            node.inputs['Offset'].default_value = 0.0
            node.inputs['Gain'].default_value = 1.0
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -493.80029296875
            node.location[1] = 78.6041259765625
            node.musgrave_dimensions = '4D'
            node.musgrave_type = 'FBM'
            node.mute = False
            node.name = 'Musgrave Texture'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 150.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = -2.559999465942383
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -299.45361328125
            node.location[1] = 56.9962158203125
            node.mute = False
            node.name = 'Math'
            node.operation = 'POWER'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = True
            node.use_custom_color = False
            node.width = 138.19586181640625
            node.width_hidden = 42.0

            node = self.grp.nodes.new('realisticcolor')
            node.inputs['Scale'].default_value = 6.400000095367432
            node.inputs['Detail'].default_value = 11.929999351501465
            node.inputs['Roughness'].default_value = 0.574999988079071
            node.inputs['Distortion'].default_value = 0.0
            node.inputs['Color1'].default_value = (0.02308487705886364,0.021157097071409225,0.020099397748708725,1.0)
            node.inputs['Color2'].default_value = (0.013578826561570168,0.012636300176382065,0.006300130393356085,1.0)
            node.inputs['Additionnal Coord'].default_value = (1.0,1.0,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,1.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 335.3475036621094
            node.location[1] = -57.95513916015625
            node.mute = False
            node.name = 'Realistic Color'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('realisticcolor')
            node.inputs['Scale'].default_value = 6.400000095367432
            node.inputs['Detail'].default_value = 11.929999351501465
            node.inputs['Roughness'].default_value = 0.574999988079071
            node.inputs['Distortion'].default_value = 0.0
            node.inputs['Color1'].default_value = (0.010805999860167503,0.015412000007927418,0.003478999948129058,1.0)
            node.inputs['Color2'].default_value = (0.004345880821347237,0.00719022611156106,0.0027263162191957235,1.0)
            node.inputs['Additionnal Coord'].default_value = (1.0,1.0,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,1.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -630.06689453125
            node.location[1] = 722.7682495117188
            node.mute = False
            node.name = 'Realistic Color.002'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexBrick')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Color1'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            node.inputs['Color2'].default_value = (0.43972691893577576,0.43972691893577576,0.43972691893577576,1.0)
            node.inputs['Mortar'].default_value = (0.0,0.0,0.0,1.0)
            node.inputs['Scale'].default_value = 8.069999694824219
            node.inputs['Mortar Size'].default_value = 0.009999999776482582
            node.inputs['Mortar Smooth'].default_value = 0.10000000149011612
            node.inputs['Bias'].default_value = 0.0
            node.inputs['Brick Width'].default_value = 0.5
            node.inputs['Row Height'].default_value = 0.25
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -606.29052734375
            node.location[1] = -308.1066589355469
            node.mute = False
            node.name = 'Brick Texture'
            node.offset = 0.5
            node.offset_frequency = 2
            node.show_options = True
            node.show_preview = False
            node.show_texture = True
            node.squash = 1.0
            node.squash_frequency = 2
            node.use_custom_color = False
            node.width = 150.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeBump')
            node.inputs['Strength'].default_value = 0.23333333432674408
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
            node.location[0] = 29.816402435302734
            node.location[1] = -605.58251953125
            node.mute = False
            node.name = 'Bump'
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
            node.location[0] = 1069.9288330078125
            node.location[1] = -8.909610748291016
            node.mute = False
            node.name = 'Mix Shader'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketColor', 'Roof color 1')
            self.grp.inputs['Roof color 1'].default_value = (0.02308487705886364,0.021157097071409225,0.020099397748708725,1.0)
            self.grp.inputs.new('NodeSocketColor', 'Roof color 2')
            self.grp.inputs['Roof color 2'].default_value = (0.013578826561570168,0.012636300176382065,0.006300130393356085,1.0)
            self.grp.inputs.new('NodeSocketColor', 'Dirt Color 1')
            self.grp.inputs['Dirt Color 1'].default_value = (0.010805999860167503,0.015412000007927418,0.003478999948129058,1.0)
            self.grp.inputs.new('NodeSocketColor', 'Dirt Color 2')
            self.grp.inputs['Dirt Color 2'].default_value = (0.004345880821347237,0.00719022611156106,0.0027263162191957235,1.0)
            self.grp.inputs.new('NodeSocketFloat', 'Dirt Seed')
            self.grp.inputs['Dirt Seed'].default_value = 0.3999999761581421
            self.grp.inputs['Dirt Seed'].min_value = -1000.0
            self.grp.inputs['Dirt Seed'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketFloat', 'Dirt Size')
            self.grp.inputs['Dirt Size'].default_value = 0.6899999380111694
            self.grp.inputs['Dirt Size'].min_value = 0.0
            self.grp.inputs['Dirt Size'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketFloat', 'Dirt contrast')
            self.grp.inputs['Dirt contrast'].default_value = -2.559999465942383
            self.grp.inputs['Dirt contrast'].min_value = -10000.0
            self.grp.inputs['Dirt contrast'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketFloat', 'Brick Scale')
            self.grp.inputs['Brick Scale'].default_value = 8.069999694824219
            self.grp.inputs['Brick Scale'].min_value = -1000.0
            self.grp.inputs['Brick Scale'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketFloatFactor', 'Brick Bump Strength')
            self.grp.inputs['Brick Bump Strength'].default_value = 0.23333333432674408
            self.grp.inputs['Brick Bump Strength'].min_value = 0.0
            self.grp.inputs['Brick Bump Strength'].max_value = 1.0
            self.grp.inputs.new('NodeSocketVector', 'Normal')
            self.grp.inputs['Normal'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['Normal'].min_value = -1.0
            self.grp.inputs['Normal'].max_value = 1.0
            self.grp.inputs.new('NodeSocketVector', 'Vector')
            self.grp.inputs['Vector'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['Vector'].min_value = -10000.0
            self.grp.inputs['Vector'].max_value = 10000.0
            node.outputs['Roof color 1'].default_value = (0.02308487705886364,0.021157097071409225,0.020099397748708725,1.0)
            node.outputs['Roof color 2'].default_value = (0.013578826561570168,0.012636300176382065,0.006300130393356085,1.0)
            node.outputs['Dirt Color 1'].default_value = (0.010805999860167503,0.015412000007927418,0.003478999948129058,1.0)
            node.outputs['Dirt Color 2'].default_value = (0.004345880821347237,0.00719022611156106,0.0027263162191957235,1.0)
            node.outputs['Dirt Seed'].default_value = 0.3999999761581421
            node.outputs['Dirt Size'].default_value = 0.6899999380111694
            node.outputs['Dirt contrast'].default_value = -2.559999465942383
            node.outputs['Brick Scale'].default_value = 8.069999694824219
            node.outputs['Brick Bump Strength'].default_value = 0.23333333432674408
            node.outputs['Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1836.3853759765625
            node.location[1] = 293.1596374511719
            node.mute = False
            node.name = 'Group Input'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            links = self.grp.links
            links.new(self.grp.nodes["Reroute"].outputs[0], self.grp.nodes["Brick Texture"].inputs[0])
            links.new(self.grp.nodes["Brick Texture"].outputs[0], self.grp.nodes["Bump"].inputs[2])
            links.new(self.grp.nodes["RGB Curves"].outputs[0], self.grp.nodes["Principled BSDF"].inputs[7])
            links.new(self.grp.nodes["Realistic Color"].outputs[0], self.grp.nodes["Principled BSDF"].inputs[0])
            links.new(self.grp.nodes["Realistic Color.001"].outputs[0], self.grp.nodes["RGB Curves"].inputs[1])
            links.new(self.grp.nodes["Reroute"].outputs[0], self.grp.nodes["Musgrave Texture"].inputs[0])
            links.new(self.grp.nodes["Musgrave Texture"].outputs[0], self.grp.nodes["Math"].inputs[0])
            links.new(self.grp.nodes["Reroute"].outputs[0], self.grp.nodes["Noise Texture"].inputs[0])
            links.new(self.grp.nodes["Noise Texture"].outputs[0], self.grp.nodes["Bump.001"].inputs[2])
            links.new(self.grp.nodes["Realistic Color.002"].outputs[0], self.grp.nodes["Principled BSDF.001"].inputs[0])
            links.new(self.grp.nodes["Noise Texture"].outputs[0], self.grp.nodes["Math.001"].inputs[0])
            links.new(self.grp.nodes["Math.001"].outputs[0], self.grp.nodes["Principled BSDF.001"].inputs[7])
            links.new(self.grp.nodes["Texture Coordinate"].outputs[3], self.grp.nodes["Vector Math"].inputs[0])
            links.new(self.grp.nodes["Math"].outputs[0], self.grp.nodes["Math.002"].inputs[0])
            links.new(self.grp.nodes["Principled BSDF"].outputs[0], self.grp.nodes["Mix Shader"].inputs[1])
            links.new(self.grp.nodes["Principled BSDF.001"].outputs[0], self.grp.nodes["Mix Shader"].inputs[2])
            links.new(self.grp.nodes["Math"].outputs[0], self.grp.nodes["Bump.002"].inputs[2])
            links.new(self.grp.nodes["Bump.001"].outputs[0], self.grp.nodes["Bump.002"].inputs[5])
            links.new(self.grp.nodes["Bump.002"].outputs[0], self.grp.nodes["Principled BSDF.001"].inputs[19])
            links.new(self.grp.nodes["Bump"].outputs[0], self.grp.nodes["Principled BSDF"].inputs[19])
            links.new(self.grp.nodes["Math.002"].outputs[0], self.grp.nodes["Mix Shader"].inputs[0])
            links.new(self.grp.nodes["Vector Math"].outputs[0], self.grp.nodes["Reroute"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[10], self.grp.nodes["Vector Math"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Musgrave Texture"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[5], self.grp.nodes["Musgrave Texture"].inputs[4])
            links.new(self.grp.nodes["Group Input"].outputs[6], self.grp.nodes["Math"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Realistic Color"].inputs[4])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Realistic Color"].inputs[5])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Realistic Color.002"].inputs[4])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Realistic Color.002"].inputs[5])
            links.new(self.grp.nodes["Group Input"].outputs[7], self.grp.nodes["Brick Texture"].inputs[4])
            links.new(self.grp.nodes["Group Input"].outputs[8], self.grp.nodes["Bump"].inputs[0])
            links.new(self.grp.nodes["Mix Shader"].outputs[0], self.grp.nodes["Group Output"].inputs[0])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Roof"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Roof" : 
                return True

        return False







