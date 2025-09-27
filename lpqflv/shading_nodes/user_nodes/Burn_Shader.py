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

class Burn_Shader (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Burn Shader"
    bl_idname = "burnshader"

    def createTree (self) : 

        if Burn_Shader.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Burn Shader', 'ShaderNodeTree')

            node = self.grp.nodes.new('ShaderNodeRGBCurve')
            node.inputs['Fac'].default_value = 1.0
            node.inputs['Color'].default_value = (0.0,0.0,0.0,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 230.23751831054688
            node.location[1] = -273.3997802734375
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
            point.location = (0.0,0.26874998211860657)
            point = node.mapping.curves[3].points.new(0,0)
            point.handle_type = 'AUTO'
            point.location = (0.36818185448646545,0.4749998450279236)
            point = node.mapping.curves[3].points.new(0,0)
            point.handle_type = 'AUTO'
            point.location = (0.5863637328147888,0.7937497496604919)
            point = node.mapping.curves[3].points.new(0,0)
            point.handle_type = 'AUTO'
            point.location = (1.0,1.0)
            node.mapping.update()
            node.mute = False
            node.name = 'RGB Curves.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 0.5
            node.inputs['Color1'].default_value = (0.011592135764658451,0.010165924206376076,0.009679706767201424,1.0)
            node.inputs['Color2'].default_value = (0.003039283212274313,0.0024144749622792006,0.00177889340557158,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MIX'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 565.7727661132812
            node.location[1] = 104.02073669433594
            node.mute = False
            node.name = 'Mix.003'
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
            node.inputs['Value'].default_value = 1.0
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 655.2853393554688
            node.location[1] = -176.67535400390625
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

            node = self.grp.nodes.new('ShaderNodeBsdfPrincipled')
            node.inputs['Base Color'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            node.inputs['Subsurface'].default_value = 0.0
            node.inputs['Subsurface Radius'].default_value = (1.0,0.20000000298023224,0.10000000149011612)
            node.inputs['Subsurface Color'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            node.inputs['Metallic'].default_value = 0.0
            node.inputs['Specular'].default_value = 0.06818182021379471
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
            node.location[0] = 933.7803344726562
            node.location[1] = 136.4232635498047
            node.mute = False
            node.name = 'Principled BSDF.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.subsurface_method = 'BURLEY'
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupOutput')
            self.grp.outputs.new('NodeSocketShader', 'BSDF')
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.is_active_output = True
            node.label = ''
            node.location[0] = 1402.86962890625
            node.location[1] = 52.08185958862305
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
            node.inputs['Scale'].default_value = 11.399999618530273
            node.inputs['Detail'].default_value = 7.399999618530273
            node.inputs['Roughness'].default_value = 0.5916666388511658
            node.inputs['Distortion'].default_value = 0.2999999523162842
            node.outputs['Fac'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -230.4071044921875
            node.location[1] = -234.15213012695312
            node.mute = False
            node.name = 'Noise Texture.004'
            node.noise_dimensions = '3D'
            node.show_options = True
            node.show_preview = False
            node.show_texture = True
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
            node.location[0] = -460.4777526855469
            node.location[1] = -259.11566162109375
            node.mute = False
            node.name = 'Vector Math'
            node.operation = 'MULTIPLY'
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
            node.location[0] = -781.3566284179688
            node.location[1] = -303.75640869140625
            node.mute = False
            node.name = 'Texture Coordinate.002'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketColor', 'Color1')
            self.grp.inputs['Color1'].default_value = (0.011592135764658451,0.010165924206376076,0.009679706767201424,1.0)
            self.grp.inputs.new('NodeSocketColor', 'Color2')
            self.grp.inputs['Color2'].default_value = (0.003039283212274313,0.0024144749622792006,0.00177889340557158,1.0)
            self.grp.inputs.new('NodeSocketFloat', 'roughness')
            self.grp.inputs['roughness'].default_value = 1.0
            self.grp.inputs['roughness'].min_value = -10000.0
            self.grp.inputs['roughness'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketVector', 'Normal')
            self.grp.inputs['Normal'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['Normal'].min_value = -1.0
            self.grp.inputs['Normal'].max_value = 1.0
            self.grp.inputs.new('NodeSocketVector', 'Add coord')
            self.grp.inputs['Add coord'].default_value = (1.0,1.0,1.0)
            self.grp.inputs['Add coord'].min_value = -10000.0
            self.grp.inputs['Add coord'].max_value = 10000.0
            node.outputs['Color1'].default_value = (0.011592135764658451,0.010165924206376076,0.009679706767201424,1.0)
            node.outputs['Color2'].default_value = (0.003039283212274313,0.0024144749622792006,0.00177889340557158,1.0)
            node.outputs['roughness'].default_value = 1.0
            node.outputs['Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Add coord'].default_value = (1.0,1.0,1.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -993.582763671875
            node.location[1] = 2.2644286155700684
            node.mute = False
            node.name = 'Group Input'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            links = self.grp.links
            links.new(self.grp.nodes["Texture Coordinate.002"].outputs[3], self.grp.nodes["Vector Math"].inputs[0])
            links.new(self.grp.nodes["Noise Texture.004"].outputs[0], self.grp.nodes["Mix.003"].inputs[0])
            links.new(self.grp.nodes["Mix.003"].outputs[0], self.grp.nodes["Principled BSDF.001"].inputs[0])
            links.new(self.grp.nodes["Noise Texture.004"].outputs[0], self.grp.nodes["RGB Curves.001"].inputs[1])
            links.new(self.grp.nodes["RGB Curves.001"].outputs[0], self.grp.nodes["Math"].inputs[0])
            links.new(self.grp.nodes["Principled BSDF.001"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Mix.003"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Mix.003"].inputs[2])
            links.new(self.grp.nodes["Math"].outputs[0], self.grp.nodes["Principled BSDF.001"].inputs[7])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Math"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Principled BSDF.001"].inputs[19])
            links.new(self.grp.nodes["Vector Math"].outputs[0], self.grp.nodes["Noise Texture.004"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Vector Math"].inputs[1])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Burn Shader"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Burn Shader" : 
                return True

        return False







