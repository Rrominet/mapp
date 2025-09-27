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

class Dripping_Rust (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Dripping Rust"
    bl_idname = "drippingrust"

    def createTree (self) : 

        if Dripping_Rust.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Dripping Rust', 'ShaderNodeTree')

            node = self.grp.nodes.new('ShaderNodeSeparateXYZ')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.outputs['X'].default_value = 0.0
            node.outputs['Y'].default_value = 0.0
            node.outputs['Z'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -223.902099609375
            node.location[1] = 422.65277099609375
            node.mute = False
            node.name = 'Separate XYZ'
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
            node.location[0] = -24.367431640625
            node.location[1] = 418.35650634765625
            node.mute = False
            node.name = 'Invert'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 0.5
            node.inputs['Color1'].default_value = (0.0,0.0,0.0,1.0)
            node.inputs['Color2'].default_value = (1.0,1.0,1.0,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MIX'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 161.367919921875
            node.location[1] = 501.69189453125
            node.mute = False
            node.name = 'Mix'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_alpha = False
            node.use_clamp = True
            node.use_custom_color = False
            node.width = 136.939453125
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexNoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 6.399999618530273
            node.inputs['Detail'].default_value = 16.0
            node.inputs['Roughness'].default_value = 0.7749999761581421
            node.inputs['Distortion'].default_value = 0.0
            node.outputs['Fac'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 151.688720703125
            node.location[1] = 206.72772216796875
            node.mute = False
            node.name = 'Noise Texture'
            node.noise_dimensions = '3D'
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
            element = node.color_ramp.elements.new(0.4909090995788574)
            element.color = (0.0,0.0,0.0,1.0)
            element.alpha = 1.0
            element.position = 0.4909090995788574
            element = node.color_ramp.elements.new(0.6863637566566467)
            element.color = (1.0,1.0,1.0,1.0)
            element.alpha = 1.0
            element.position = 0.6863637566566467
            node.hide = False
            node.label = ''
            node.location[0] = 365.2620849609375
            node.location[1] = 202.63531494140625
            node.mute = False
            node.name = 'ColorRamp'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = -0.22999998927116394
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 439.3291015625
            node.location[1] = 420.5792236328125
            node.mute = False
            node.name = 'Math'
            node.operation = 'ADD'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMapping')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Location'].default_value = (0.0,0.0,0.0)
            node.inputs['Rotation'].default_value = (0.0,0.0,0.0)
            node.inputs['Scale'].default_value = (1.0,1.0,0.05000000074505806)
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -193.447021484375
            node.location[1] = -116.37136840820312
            node.mute = False
            node.name = 'Mapping.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.vector_type = 'POINT'
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
            node.location[0] = 682.13720703125
            node.location[1] = 342.98895263671875
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

            node = self.grp.nodes.new('ShaderNodeSeparateXYZ')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.outputs['X'].default_value = 0.0
            node.outputs['Y'].default_value = 0.0
            node.outputs['Z'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 118.13232421875
            node.location[1] = -131.24362182617188
            node.mute = False
            node.name = 'Separate XYZ.001'
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
            node.location[0] = 891.892578125
            node.location[1] = 240.16485595703125
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

            node = self.grp.nodes.new('ShaderNodeTexMusgrave')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 4.099999904632568
            node.inputs['Detail'].default_value = 7.799999713897705
            node.inputs['Dimension'].default_value = 1.5
            node.inputs['Lacunarity'].default_value = 2.0
            node.inputs['Offset'].default_value = 0.0
            node.inputs['Gain'].default_value = 1.0
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -344.759033203125
            node.location[1] = -498.29986572265625
            node.musgrave_dimensions = '3D'
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
            node.inputs['Value'].default_value = 6.160000324249268
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 1111.892578125
            node.location[1] = 230.3965606689453
            node.mute = False
            node.name = 'Math.003'
            node.operation = 'MULTIPLY'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = True
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 2.1800003051757812
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 1305.245849609375
            node.location[1] = 90.9754409790039
            node.mute = False
            node.name = 'Math.004'
            node.operation = 'MULTIPLY'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
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
            element = node.color_ramp.elements.new(0.0)
            element.color = (0.0,0.0,0.0,1.0)
            element.alpha = 1.0
            element.position = 0.0
            element = node.color_ramp.elements.new(0.4136367738246918)
            element.color = (1.0,1.0,1.0,1.0)
            element.alpha = 1.0
            element.position = 0.4136367738246918
            node.hide = False
            node.label = ''
            node.location[0] = -129.62353515625
            node.location[1] = -488.5684814453125
            node.mute = False
            node.name = 'ColorRamp.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
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
            node.location[0] = -1305.245849609375
            node.location[1] = -95.40232849121094
            node.mute = False
            node.name = 'Texture Coordinate'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupOutput')
            self.grp.outputs.new('NodeSocketFloat', 'Value')
            node.inputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.is_active_output = True
            node.label = ''
            node.location[0] = 1505.245849609375
            node.location[1] = -0.0
            node.mute = False
            node.name = 'Group Output'
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
            node.location[0] = -1005.2109375
            node.location[1] = -202.8327178955078
            node.mute = False
            node.name = 'Vector Math'
            node.operation = 'ADD'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeSeparateXYZ')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.outputs['X'].default_value = 0.0
            node.outputs['Y'].default_value = 0.0
            node.outputs['Z'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -667.1771240234375
            node.location[1] = -150.1788330078125
            node.mute = False
            node.name = 'Separate XYZ.002'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeCombineXYZ')
            node.inputs['X'].default_value = 0.0
            node.inputs['Y'].default_value = 0.0
            node.inputs['Z'].default_value = -0.29999998211860657
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -408.739501953125
            node.location[1] = -246.78038024902344
            node.mute = False
            node.name = 'Combine XYZ'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexNoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 0.9200001358985901
            node.inputs['Detail'].default_value = 7.899999618530273
            node.inputs['Roughness'].default_value = 0.7416666746139526
            node.inputs['Distortion'].default_value = 0.0
            node.outputs['Fac'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -554.2749633789062
            node.location[1] = -501.69189453125
            node.mute = False
            node.name = 'Noise Texture.001'
            node.noise_dimensions = '3D'
            node.show_options = True
            node.show_preview = False
            node.show_texture = True
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMapping')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Location'].default_value = (0.0,0.0,0.0)
            node.inputs['Rotation'].default_value = (0.0,0.0,0.0)
            node.inputs['Scale'].default_value = (1.0,1.0,0.05000000074505806)
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -199.568115234375
            node.location[1] = 271.36297607421875
            node.mute = False
            node.name = 'Mapping'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.vector_type = 'POINT'
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketVectorXYZ', 'Line Scale')
            self.grp.inputs['Line Scale'].default_value = (1.0,1.0,0.05000000074505806)
            self.grp.inputs['Line Scale'].min_value = -3.4028234663852886e+38
            self.grp.inputs['Line Scale'].max_value = 3.4028234663852886e+38
            self.grp.inputs.new('NodeSocketFloat', 'Z Mask')
            self.grp.inputs['Z Mask'].default_value = -0.29999998211860657
            self.grp.inputs['Z Mask'].min_value = -10000.0
            self.grp.inputs['Z Mask'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketFloat', 'Contrast')
            self.grp.inputs['Contrast'].default_value = 6.160000324249268
            self.grp.inputs['Contrast'].min_value = -10000.0
            self.grp.inputs['Contrast'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketFloat', 'Noise Scale')
            self.grp.inputs['Noise Scale'].default_value = 0.9200001358985901
            self.grp.inputs['Noise Scale'].min_value = -1000.0
            self.grp.inputs['Noise Scale'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketVector', 'Additional Coord')
            self.grp.inputs['Additional Coord'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['Additional Coord'].min_value = -10000.0
            self.grp.inputs['Additional Coord'].max_value = 10000.0
            node.outputs['Line Scale'].default_value = (1.0,1.0,0.05000000074505806)
            node.outputs['Z Mask'].default_value = -0.29999998211860657
            node.outputs['Contrast'].default_value = 6.160000324249268
            node.outputs['Noise Scale'].default_value = 0.9200001358985901
            node.outputs['Additional Coord'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1306.1002197265625
            node.location[1] = -360.4445495605469
            node.mute = False
            node.name = 'Group Input'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            links = self.grp.links
            links.new(self.grp.nodes["Mapping"].outputs[0], self.grp.nodes["Noise Texture"].inputs[0])
            links.new(self.grp.nodes["Noise Texture"].outputs[0], self.grp.nodes["ColorRamp"].inputs[0])
            links.new(self.grp.nodes["Texture Coordinate"].outputs[1], self.grp.nodes["Separate XYZ"].inputs[0])
            links.new(self.grp.nodes["Separate XYZ"].outputs[2], self.grp.nodes["Invert"].inputs[1])
            links.new(self.grp.nodes["Invert"].outputs[0], self.grp.nodes["Mix"].inputs[0])
            links.new(self.grp.nodes["Mix"].outputs[0], self.grp.nodes["Math"].inputs[0])
            links.new(self.grp.nodes["ColorRamp"].outputs[0], self.grp.nodes["Math.001"].inputs[0])
            links.new(self.grp.nodes["Math"].outputs[0], self.grp.nodes["Math.001"].inputs[1])
            links.new(self.grp.nodes["Mapping.001"].outputs[0], self.grp.nodes["Separate XYZ.001"].inputs[0])
            links.new(self.grp.nodes["Separate XYZ.002"].outputs[0], self.grp.nodes["Combine XYZ"].inputs[0])
            links.new(self.grp.nodes["Separate XYZ.002"].outputs[1], self.grp.nodes["Combine XYZ"].inputs[1])
            links.new(self.grp.nodes["Combine XYZ"].outputs[0], self.grp.nodes["Mapping.001"].inputs[1])
            links.new(self.grp.nodes["Math.001"].outputs[0], self.grp.nodes["Math.002"].inputs[0])
            links.new(self.grp.nodes["Math.002"].outputs[0], self.grp.nodes["Math.003"].inputs[0])
            links.new(self.grp.nodes["Separate XYZ.001"].outputs[2], self.grp.nodes["Math.002"].inputs[1])
            links.new(self.grp.nodes["Noise Texture.001"].outputs[1], self.grp.nodes["Musgrave Texture"].inputs[0])
            links.new(self.grp.nodes["Math.003"].outputs[0], self.grp.nodes["Math.004"].inputs[0])
            links.new(self.grp.nodes["Musgrave Texture"].outputs[0], self.grp.nodes["ColorRamp.001"].inputs[0])
            links.new(self.grp.nodes["Math.004"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["ColorRamp.001"].outputs[0], self.grp.nodes["Math.004"].inputs[1])
            links.new(self.grp.nodes["Texture Coordinate"].outputs[3], self.grp.nodes["Vector Math"].inputs[0])
            links.new(self.grp.nodes["Vector Math"].outputs[0], self.grp.nodes["Noise Texture.001"].inputs[0])
            links.new(self.grp.nodes["Vector Math"].outputs[0], self.grp.nodes["Mapping.001"].inputs[0])
            links.new(self.grp.nodes["Vector Math"].outputs[0], self.grp.nodes["Mapping"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Vector Math"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Combine XYZ"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Noise Texture.001"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Math.003"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Mapping"].inputs[3])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Dripping Rust"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Dripping Rust" : 
                return True

        return False







