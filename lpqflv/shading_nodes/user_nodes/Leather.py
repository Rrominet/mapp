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

class Leather (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Leather"
    bl_idname = "leather"

    def createTree (self) : 

        if Leather.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Leather', 'ShaderNodeTree')

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 1.0
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 658.8822021484375
            node.location[1] = 50.90587615966797
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

            node = self.grp.nodes.new('ShaderNodeTexNoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 20.0
            node.inputs['Detail'].default_value = 2.1000003814697266
            node.inputs['Roughness'].default_value = 0.8416666984558105
            node.inputs['Distortion'].default_value = 0.0
            node.outputs['Fac'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -858.8359375
            node.location[1] = -403.5684814453125
            node.mute = False
            node.name = 'Noise Texture'
            node.noise_dimensions = '3D'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 0.02500000037252903
            node.inputs['Color1'].default_value = (0.5,0.5,0.5,1.0)
            node.inputs['Color2'].default_value = (0.5,0.5,0.5,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MIX'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -616.173095703125
            node.location[1] = -266.3504638671875
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

            node = self.grp.nodes.new('rust')
            node.inputs['Scale'].default_value = 0.9600001573562622
            node.inputs['Detail'].default_value = 16.0
            node.inputs['Roughness'].default_value = 0.824999988079071
            node.inputs['Additional Coord'].default_value = (0.0,0.0,0.0)
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -448.103515625
            node.location[1] = -11.310394287109375
            node.mute = False
            node.name = 'Rust'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMapRange')
            node.inputs['Value'].default_value = 1.0
            node.inputs['From Min'].default_value = 0.1599999964237213
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
            node.location[0] = -212.369873046875
            node.location[1] = 3.267152786254883
            node.mute = False
            node.name = 'Map Range'
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
            node.location[0] = 77.065673828125
            node.location[1] = -79.25328063964844
            node.mute = False
            node.name = 'Math.001'
            node.operation = 'ADD'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeBsdfPrincipled')
            node.inputs['Base Color'].default_value = (0.05056534335017204,0.011340852826833725,0.0019698345568031073,1.0)
            node.inputs['Subsurface'].default_value = 0.0
            node.inputs['Subsurface Radius'].default_value = (1.0,0.20000000298023224,0.10000000149011612)
            node.inputs['Subsurface Color'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            node.inputs['Metallic'].default_value = 0.0
            node.inputs['Specular'].default_value = 0.09090907871723175
            node.inputs['Specular Tint'].default_value = 0.0
            node.inputs['Roughness'].default_value = 0.7954545021057129
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
            node.location[0] = 1071.799072265625
            node.location[1] = 272.41796875
            node.mute = False
            node.name = 'Principled BSDF'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.subsurface_method = 'BURLEY'
            node.use_custom_color = False
            node.width = 240.0
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
            node.location[0] = -1662.26318359375
            node.location[1] = -277.79119873046875
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
            node.location[0] = -1254.3592529296875
            node.location[1] = -341.13946533203125
            node.mute = False
            node.name = 'Vector Math'
            node.operation = 'ADD'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('realisticcolor')
            node.inputs['Scale'].default_value = 4.760000228881836
            node.inputs['Detail'].default_value = 13.59999942779541
            node.inputs['Roughness'].default_value = 0.7416666746139526
            node.inputs['Distortion'].default_value = 0.0
            node.inputs['Color1'].default_value = (0.050565000623464584,0.011340999975800514,0.001970000099390745,1.0)
            node.inputs['Color2'].default_value = (0.1380903720855713,0.0472598522901535,0.017865588888525963,1.0)
            node.inputs['Additionnal Coord'].default_value = (1.0,1.0,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,1.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 684.4398803710938
            node.location[1] = 403.5684814453125
            node.mute = False
            node.name = 'Realistic Color'
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
            node.location[0] = 282.39892578125
            node.location[1] = 186.4154815673828
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
            point.location = (0.0,0.07500004768371582)
            point = node.mapping.curves[3].points.new(0,0)
            point.handle_type = 'AUTO'
            point.location = (0.08636362105607986,0.38749998807907104)
            point = node.mapping.curves[3].points.new(0,0)
            point.handle_type = 'AUTO'
            point.location = (0.23636366426944733,0.4562499523162842)
            point = node.mapping.curves[3].points.new(0,0)
            point.handle_type = 'AUTO'
            point.location = (0.4681819677352905,0.8125002384185791)
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

            node = self.grp.nodes.new('NodeGroupOutput')
            self.grp.outputs.new('NodeSocketShader', 'BSDF')
            self.grp.outputs.new('NodeSocketColor', 'Roughness')
            self.grp.outputs.new('NodeSocketFloat', 'Voronois')
            self.grp.outputs.new('NodeSocketVector', 'Normal')
            node.inputs['Roughness'].default_value = (0.0,0.0,0.0,0.0)
            node.inputs['Voronois'].default_value = 0.0
            node.inputs['Normal'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.is_active_output = True
            node.label = ''
            node.location[0] = 1561.7310791015625
            node.location[1] = 245.720703125
            node.mute = False
            node.name = 'Group Output'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexVoronoi')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 111.19999694824219
            node.inputs['Smoothness'].default_value = 1.0
            node.inputs['Exponent'].default_value = 0.5
            node.inputs['Randomness'].default_value = 1.0
            node.outputs['Distance'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.outputs['Position'].default_value = (0.0,0.0,0.0)
            node.outputs['W'].default_value = 0.0
            node.outputs['Radius'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.distance = 'EUCLIDEAN'
            node.feature = 'DISTANCE_TO_EDGE'
            node.hide = False
            node.label = ''
            node.location[0] = -220.68798828125
            node.location[1] = -243.36744689941406
            node.mute = False
            node.name = 'Voronoi Texture'
            node.show_options = True
            node.show_preview = False
            node.show_texture = True
            node.use_custom_color = False
            node.voronoi_dimensions = '3D'
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeBump')
            node.inputs['Strength'].default_value = 0.20000000298023224
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
            node.location[0] = 756.76220703125
            node.location[1] = -194.82310485839844
            node.mute = False
            node.name = 'Bump'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketFloat', 'Roughness')
            self.grp.inputs['Roughness'].default_value = 1.0
            self.grp.inputs['Roughness'].min_value = -10000.0
            self.grp.inputs['Roughness'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketColor', 'Color 1')
            self.grp.inputs['Color 1'].default_value = (0.050565000623464584,0.011340999975800514,0.001970000099390745,1.0)
            self.grp.inputs.new('NodeSocketColor', 'Color 2')
            self.grp.inputs['Color 2'].default_value = (0.1380903720855713,0.0472598522901535,0.017865588888525963,1.0)
            self.grp.inputs.new('NodeSocketFloat', 'Scale')
            self.grp.inputs['Scale'].default_value = 111.19999694824219
            self.grp.inputs['Scale'].min_value = -1000.0
            self.grp.inputs['Scale'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketFloatFactor', 'Deform')
            self.grp.inputs['Deform'].default_value = 0.02500000037252903
            self.grp.inputs['Deform'].min_value = 0.0
            self.grp.inputs['Deform'].max_value = 1.0
            self.grp.inputs.new('NodeSocketFloatFactor', 'Bump Strength')
            self.grp.inputs['Bump Strength'].default_value = 0.20000000298023224
            self.grp.inputs['Bump Strength'].min_value = 0.0
            self.grp.inputs['Bump Strength'].max_value = 1.0
            self.grp.inputs.new('NodeSocketVector', 'Normal')
            self.grp.inputs['Normal'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['Normal'].min_value = -1.0
            self.grp.inputs['Normal'].max_value = 1.0
            self.grp.inputs.new('NodeSocketVector', 'Add Coord')
            self.grp.inputs['Add Coord'].default_value = (1.0,1.0,1.0)
            self.grp.inputs['Add Coord'].min_value = -10000.0
            self.grp.inputs['Add Coord'].max_value = 10000.0
            node.outputs['Roughness'].default_value = 1.0
            node.outputs['Color 1'].default_value = (0.050565000623464584,0.011340999975800514,0.001970000099390745,1.0)
            node.outputs['Color 2'].default_value = (0.1380903720855713,0.0472598522901535,0.017865588888525963,1.0)
            node.outputs['Scale'].default_value = 111.19999694824219
            node.outputs['Deform'].default_value = 0.02500000037252903
            node.outputs['Bump Strength'].default_value = 0.20000000298023224
            node.outputs['Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Add Coord'].default_value = (1.0,1.0,1.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1652.4033203125
            node.location[1] = -29.24181365966797
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
            links.new(self.grp.nodes["Mix"].outputs[0], self.grp.nodes["Voronoi Texture"].inputs[0])
            links.new(self.grp.nodes["Voronoi Texture"].outputs[0], self.grp.nodes["Bump"].inputs[2])
            links.new(self.grp.nodes["Bump"].outputs[0], self.grp.nodes["Principled BSDF"].inputs[19])
            links.new(self.grp.nodes["RGB Curves"].outputs[0], self.grp.nodes["Math"].inputs[0])
            links.new(self.grp.nodes["Math"].outputs[0], self.grp.nodes["Principled BSDF"].inputs[7])
            links.new(self.grp.nodes["Rust"].outputs[0], self.grp.nodes["Map Range"].inputs[0])
            links.new(self.grp.nodes["Voronoi Texture"].outputs[0], self.grp.nodes["Math.001"].inputs[1])
            links.new(self.grp.nodes["Map Range"].outputs[0], self.grp.nodes["Math.001"].inputs[0])
            links.new(self.grp.nodes["Math.001"].outputs[0], self.grp.nodes["RGB Curves"].inputs[1])
            links.new(self.grp.nodes["Realistic Color"].outputs[0], self.grp.nodes["Principled BSDF"].inputs[0])
            links.new(self.grp.nodes["Principled BSDF"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Texture Coordinate"].outputs[3], self.grp.nodes["Vector Math"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[7], self.grp.nodes["Vector Math"].inputs[1])
            links.new(self.grp.nodes["Vector Math"].outputs[0], self.grp.nodes["Noise Texture"].inputs[0])
            links.new(self.grp.nodes["Vector Math"].outputs[0], self.grp.nodes["Mix"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Realistic Color"].inputs[4])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Math"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Realistic Color"].inputs[5])
            links.new(self.grp.nodes["RGB Curves"].outputs[0], self.grp.nodes["Group Output"].inputs[1])
            links.new(self.grp.nodes["Bump"].outputs[0], self.grp.nodes["Group Output"].inputs[3])
            links.new(self.grp.nodes["Voronoi Texture"].outputs[0], self.grp.nodes["Group Output"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Voronoi Texture"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Mix"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[5], self.grp.nodes["Bump"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[6], self.grp.nodes["Bump"].inputs[5])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Leather"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Leather" : 
                return True

        return False







