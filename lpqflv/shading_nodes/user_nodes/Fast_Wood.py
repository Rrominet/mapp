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

class Fast_Wood (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Fast Wood"
    bl_idname = "fastwood"

    def createTree (self) : 

        if Fast_Wood.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Fast Wood', 'ShaderNodeTree')

            node = self.grp.nodes.new('ShaderNodeMapping')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Location'].default_value = (0.0,0.0,0.0)
            node.inputs['Rotation'].default_value = (0.0,0.0,0.0)
            node.inputs['Scale'].default_value = (0.11999999731779099,1.0,1.0)
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -664.343505859375
            node.location[1] = 199.08639526367188
            node.mute = False
            node.name = 'Mapping'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.vector_type = 'POINT'
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMapping')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Location'].default_value = (0.0,0.0,0.0)
            node.inputs['Rotation'].default_value = (0.0,0.0,0.0)
            node.inputs['Scale'].default_value = (-0.039999961853027344,1.0,1.0)
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -675.0472412109375
            node.location[1] = -170.53187561035156
            node.mute = False
            node.name = 'Mapping.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.vector_type = 'POINT'
            node.width = 240.0
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
            node.location[0] = -270.5147705078125
            node.location[1] = -101.16952514648438
            node.mute = False
            node.name = 'Vector Math'
            node.operation = 'ADD'
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
            node.location[0] = 623.5620727539062
            node.location[1] = 39.974891662597656
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
            point.location = (0.0,0.3749997913837433)
            point = node.mapping.curves[3].points.new(0,0)
            point.handle_type = 'AUTO'
            point.location = (0.30454543232917786,0.7562502026557922)
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
            node.location[0] = 268.42181396484375
            node.location[1] = -277.21258544921875
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

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 1.0
            node.inputs['Color1'].default_value = (0.5,0.5,0.5,1.0)
            node.inputs['Color2'].default_value = (0.5,0.5,0.5,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MULTIPLY'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 697.5799560546875
            node.location[1] = 306.91131591796875
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

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 0.5
            node.inputs['Color1'].default_value = (1.0,1.0,1.0,1.0)
            node.inputs['Color2'].default_value = (0.04717940464615822,0.024976054206490517,0.008188584819436073,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MIX'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 364.09423828125
            node.location[1] = 364.3834228515625
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
            node.location[0] = -620.5389404296875
            node.location[1] = 380.1162109375
            node.mute = False
            node.name = 'Object Info'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeBsdfPrincipled')
            node.inputs['Base Color'].default_value = (0.31853100657463074,0.14512999355793,0.07933299988508224,1.0)
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
            node.inputs['Clearcoat'].default_value = 0.25
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
            node.location[0] = 955.9722900390625
            node.location[1] = 257.3533630371094
            node.mute = False
            node.name = 'Principled BSDF'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.subsurface_method = 'BURLEY'
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexNoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 6.300000190734863
            node.inputs['Detail'].default_value = 4.0
            node.inputs['Roughness'].default_value = 0.7250000238418579
            node.inputs['Distortion'].default_value = 0.0
            node.outputs['Fac'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -36.24786376953125
            node.location[1] = 152.19696044921875
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
            node.inputs['Scale'].default_value = 1.4400004148483276
            node.inputs['Detail'].default_value = 10.199999809265137
            node.inputs['Roughness'].default_value = 0.699999988079071
            node.inputs['Distortion'].default_value = 10.149999618530273
            node.outputs['Fac'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -41.13348388671875
            node.location[1] = -143.8521728515625
            node.mute = False
            node.name = 'Noise Texture.001'
            node.noise_dimensions = '3D'
            node.show_options = True
            node.show_preview = False
            node.show_texture = True
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 0.5
            node.inputs['Color1'].default_value = (0.31853097677230835,0.1231904923915863,0.06017953157424927,1.0)
            node.inputs['Color2'].default_value = (0.01784469000995159,0.00978283490985632,0.006346689071506262,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MIX'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 404.5694274902344
            node.location[1] = 103.50283813476562
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
            self.grp.outputs.new('NodeSocketShader', 'BSDF')
            self.grp.outputs.new('NodeSocketColor', 'Diffuse')
            self.grp.outputs.new('NodeSocketColor', 'Roughness')
            self.grp.outputs.new('NodeSocketVector', 'Normal')
            node.inputs['Diffuse'].default_value = (0.0,0.0,0.0,0.0)
            node.inputs['Roughness'].default_value = (0.0,0.0,0.0,0.0)
            node.inputs['Normal'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.is_active_output = True
            node.label = ''
            node.location[0] = 1340.93798828125
            node.location[1] = 71.81744384765625
            node.mute = False
            node.name = 'Group Output'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeBump')
            node.inputs['Strength'].default_value = 0.28333333134651184
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
            node.location[0] = 655.3123168945312
            node.location[1] = -370.5405578613281
            node.mute = False
            node.name = 'Bump'
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
            node.location[0] = -890.102294921875
            node.location[1] = -259.02386474609375
            node.mute = False
            node.name = 'Reroute'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
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
            node.location[0] = -1338.797119140625
            node.location[1] = -239.5686492919922
            node.mute = False
            node.name = 'Texture Coordinate'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketFloat', 'Small noise Scale')
            self.grp.inputs['Small noise Scale'].default_value = 6.300000190734863
            self.grp.inputs['Small noise Scale'].min_value = -1000.0
            self.grp.inputs['Small noise Scale'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketFloat', 'Large Noise Sacle')
            self.grp.inputs['Large Noise Sacle'].default_value = 1.4400004148483276
            self.grp.inputs['Large Noise Sacle'].min_value = -1000.0
            self.grp.inputs['Large Noise Sacle'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketFloat', 'Distortion')
            self.grp.inputs['Distortion'].default_value = 10.149999618530273
            self.grp.inputs['Distortion'].min_value = -1000.0
            self.grp.inputs['Distortion'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketColor', 'Light Color')
            self.grp.inputs['Light Color'].default_value = (0.31853097677230835,0.1231904923915863,0.06017953157424927,1.0)
            self.grp.inputs.new('NodeSocketColor', 'Dark Color')
            self.grp.inputs['Dark Color'].default_value = (0.01784469000995159,0.00978283490985632,0.006346689071506262,1.0)
            self.grp.inputs.new('NodeSocketColor', 'Dirt')
            self.grp.inputs['Dirt'].default_value = (0.04717940464615822,0.024976054206490517,0.008188584819436073,1.0)
            self.grp.inputs.new('NodeSocketFloatFactor', 'Dirt Mix')
            self.grp.inputs['Dirt Mix'].default_value = 1.0
            self.grp.inputs['Dirt Mix'].min_value = 0.0
            self.grp.inputs['Dirt Mix'].max_value = 1.0
            self.grp.inputs.new('NodeSocketFloatFactor', 'Bump')
            self.grp.inputs['Bump'].default_value = 0.28333333134651184
            self.grp.inputs['Bump'].min_value = 0.0
            self.grp.inputs['Bump'].max_value = 1.0
            self.grp.inputs.new('NodeSocketVector', 'Normal')
            self.grp.inputs['Normal'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['Normal'].min_value = -1.0
            self.grp.inputs['Normal'].max_value = 1.0
            self.grp.inputs.new('NodeSocketVector', 'Vector')
            self.grp.inputs['Vector'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['Vector'].min_value = -10000.0
            self.grp.inputs['Vector'].max_value = 10000.0
            node.outputs['Small noise Scale'].default_value = 6.300000190734863
            node.outputs['Large Noise Sacle'].default_value = 1.4400004148483276
            node.outputs['Distortion'].default_value = 10.149999618530273
            node.outputs['Light Color'].default_value = (0.31853097677230835,0.1231904923915863,0.06017953157424927,1.0)
            node.outputs['Dark Color'].default_value = (0.01784469000995159,0.00978283490985632,0.006346689071506262,1.0)
            node.outputs['Dirt'].default_value = (0.04717940464615822,0.024976054206490517,0.008188584819436073,1.0)
            node.outputs['Dirt Mix'].default_value = 1.0
            node.outputs['Bump'].default_value = 0.28333333134651184
            node.outputs['Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1396.164306640625
            node.location[1] = 69.4923095703125
            node.mute = False
            node.name = 'Group Input'
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
            node.location[0] = -1118.102294921875
            node.location[1] = -215.41302490234375
            node.mute = False
            node.name = 'Vector Math.001'
            node.operation = 'MULTIPLY'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            links = self.grp.links
            links.new(self.grp.nodes["Mapping"].outputs[0], self.grp.nodes["Noise Texture"].inputs[0])
            links.new(self.grp.nodes["Reroute"].outputs[0], self.grp.nodes["Mapping"].inputs[0])
            links.new(self.grp.nodes["Reroute"].outputs[0], self.grp.nodes["Mapping.001"].inputs[0])
            links.new(self.grp.nodes["Noise Texture.001"].outputs[0], self.grp.nodes["Mix"].inputs[0])
            links.new(self.grp.nodes["Noise Texture"].outputs[0], self.grp.nodes["Mix.001"].inputs[0])
            links.new(self.grp.nodes["Mix.002"].outputs[0], self.grp.nodes["Principled BSDF"].inputs[0])
            links.new(self.grp.nodes["Mix.001"].outputs[0], self.grp.nodes["Mix.002"].inputs[2])
            links.new(self.grp.nodes["Mix"].outputs[0], self.grp.nodes["Mix.002"].inputs[1])
            links.new(self.grp.nodes["Noise Texture"].outputs[0], self.grp.nodes["Bump"].inputs[2])
            links.new(self.grp.nodes["Bump"].outputs[0], self.grp.nodes["Principled BSDF"].inputs[19])
            links.new(self.grp.nodes["Noise Texture.001"].outputs[0], self.grp.nodes["Math"].inputs[0])
            links.new(self.grp.nodes["Noise Texture"].outputs[0], self.grp.nodes["Math"].inputs[1])
            links.new(self.grp.nodes["Math"].outputs[0], self.grp.nodes["RGB Curves"].inputs[1])
            links.new(self.grp.nodes["RGB Curves"].outputs[0], self.grp.nodes["Principled BSDF"].inputs[7])
            links.new(self.grp.nodes["Mapping.001"].outputs[0], self.grp.nodes["Vector Math"].inputs[0])
            links.new(self.grp.nodes["Object Info"].outputs[4], self.grp.nodes["Vector Math"].inputs[1])
            links.new(self.grp.nodes["Vector Math"].outputs[0], self.grp.nodes["Noise Texture.001"].inputs[0])
            links.new(self.grp.nodes["Principled BSDF"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Noise Texture"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Noise Texture.001"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Noise Texture.001"].inputs[5])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Mix"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Mix"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[5], self.grp.nodes["Mix.001"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[6], self.grp.nodes["Mix.002"].inputs[0])
            links.new(self.grp.nodes["Mix.002"].outputs[0], self.grp.nodes["Group Output"].inputs[1])
            links.new(self.grp.nodes["RGB Curves"].outputs[0], self.grp.nodes["Group Output"].inputs[2])
            links.new(self.grp.nodes["Bump"].outputs[0], self.grp.nodes["Group Output"].inputs[3])
            links.new(self.grp.nodes["Group Input"].outputs[7], self.grp.nodes["Bump"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[8], self.grp.nodes["Bump"].inputs[5])
            links.new(self.grp.nodes["Texture Coordinate"].outputs[3], self.grp.nodes["Vector Math.001"].inputs[0])
            links.new(self.grp.nodes["Vector Math.001"].outputs[0], self.grp.nodes["Reroute"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[9], self.grp.nodes["Vector Math.001"].inputs[1])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Fast Wood"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Fast Wood" : 
                return True

        return False







