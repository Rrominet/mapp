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

class Caustics (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Caustics"
    bl_idname = "caustics"

    def createTree (self) : 

        if Caustics.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Caustics', 'ShaderNodeTree')

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.name = 'Mix'
            node.location = [350.07781982421875, 350.07781982421875]
            node.inputs['Fac'].default_value = 0.5272727012634277
            node.inputs['Color1'].default_value = (0.5,0.5,0.5,1.0)
            node.inputs['Color2'].default_value = (0.838071882724762,0.1308314949274063,0.14656908810138702,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MIX'
            node.use_alpha = False
            node.use_clamp = False

            node = self.grp.nodes.new('ShaderNodeMixShader')
            node.name = 'Mix Shader'
            node.location = [1028.8662109375, 1028.8662109375]
            node.inputs['Fac'].default_value = 0.0

            node = self.grp.nodes.new('ShaderNodeLightPath')
            node.name = 'Light Path'
            node.location = [-1107.76220703125, -1107.76220703125]
            node.outputs['Is Camera Ray'].default_value = 0.0
            node.outputs['Is Shadow Ray'].default_value = 0.0
            node.outputs['Is Diffuse Ray'].default_value = 0.0
            node.outputs['Is Glossy Ray'].default_value = 0.0
            node.outputs['Is Singular Ray'].default_value = 0.0
            node.outputs['Is Reflection Ray'].default_value = 0.0
            node.outputs['Is Transmission Ray'].default_value = 0.0
            node.outputs['Ray Length'].default_value = 0.0
            node.outputs['Ray Depth'].default_value = 0.0
            node.outputs['Diffuse Depth'].default_value = 0.0
            node.outputs['Glossy Depth'].default_value = 0.0
            node.outputs['Transparent Depth'].default_value = 0.0
            node.outputs['Transmission Depth'].default_value = 0.0

            node = self.grp.nodes.new('ShaderNodeTexNoise')
            node.name = 'Noise Texture'
            node.location = [-358.4688720703125, -358.4688720703125]
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Scale'].default_value = 3.490000009536743
            node.inputs['Detail'].default_value = 2.0
            node.inputs['Distortion'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.outputs['Fac'].default_value = 0.0

            node = self.grp.nodes.new('ShaderNodeBrightContrast')
            node.name = 'Bright/Contrast'
            node.location = [77.15351867675781, 77.15351867675781]
            node.inputs['Color'].default_value = (1.0,1.0,1.0,1.0)
            node.inputs['Bright'].default_value = 0.0
            node.inputs['Contrast'].default_value = 2.0999999046325684
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)

            node = self.grp.nodes.new('ShaderNodeBsdfTransparent')
            node.name = 'Transparent BSDF'
            node.location = [814.4578247070312, 814.4578247070312]
            node.inputs['Color'].default_value = (1.0,1.0,1.0,1.0)

            node = self.grp.nodes.new('NodeGroupInput')
            node.name = 'Group Input'
            node.location = [-1251.3416748046875, -1251.3416748046875]
            self.grp.inputs.new('NodeSocketShader', 'Shader')
            self.grp.inputs.new('NodeSocketFloatFactor', 'Factor')
            self.grp.inputs.new('NodeSocketFloatFactor', 'Caustics Ramp')
            self.grp.inputs.new('NodeSocketVector', 'Noise Vector')
            self.grp.inputs.new('NodeSocketFloat', 'Noise Scale')
            self.grp.inputs.new('NodeSocketFloat', 'Noise Detail')
            self.grp.inputs.new('NodeSocketFloat', 'Distortion')
            self.grp.inputs.new('NodeSocketFloat', 'Noise Contrast')
            self.grp.inputs.new('NodeSocketColor', 'Color')
            self.grp.inputs.new('NodeSocketFloat', 'Intensity')
            selA['Factor'].default_value = 1.0
            self.grp.inputs['Factor'].min_value = 0.0
            self.grp.inputs['Factor'].max_value = 1.0
            self.grp.inputs['Caustics Ramp'].default_value = 0.5
            self.grp.inputs['Noise Vector'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['Noise Scale'].default_value = 3.490000009536743
            self.grp.inputs['Noise Detail'].default_value = 2.0
            self.grp.inputs['Distortion'].default_value = 0.0
            self.grp.inputs['Noise Contrast'].default_value = 2.0999999046325684
            self.grp.inputs['Color'].default_value = (1,1,1,1.0)
            self.grp.inputs['Intensity'].default_value = 1.7

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.name = 'Mix.001'
            node.location = [553.9336547851562, 553.9336547851562]
            node.inputs['Fac'].default_value = 1.0
            node.inputs['Color1'].default_value = (0.0,0.0,0.0,1.0)
            node.inputs['Color2'].default_value = (0.0,0.0,0.0,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MIX'
            node.use_alpha = False
            node.use_clamp = False

            node = self.grp.nodes.new('ShaderNodeMath')
            node.name = 'Math'
            node.location = [56.11531066894531, 56.11531066894531]
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 1.7
            node.outputs['Value'].default_value = 0.0
            node.operation = 'MULTIPLY'
            node.use_clamp = False

            node = self.grp.nodes.new('NodeGroupOutput')
            node.name = 'Group Output'
            node.location = [1336.1593017578125, 1336.1593017578125]
            self.grp.outputs.new('NodeSocketShader', 'Shader')
            node.is_active_output = True

            links = self.grp.links
            links.new(self.grp.nodes["Light Path"].outputs[1], self.grp.nodes["Mix Shader"].inputs[0])
            links.new(self.grp.nodes["Transparent BSDF"].outputs[0], self.grp.nodes["Mix Shader"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Mix Shader"].inputs[1])
            links.new(self.grp.nodes["Math"].outputs[0], self.grp.nodes["Mix"].inputs[1])
            links.new(self.grp.nodes["Mix Shader"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Noise Texture"].outputs[0], self.grp.nodes["Bright/Contrast"].inputs[0])
            links.new(self.grp.nodes["Bright/Contrast"].outputs[0], self.grp.nodes["Mix"].inputs[0])
            links.new(self.grp.nodes["Mix.001"].outputs[0], self.grp.nodes["Transparent BSDF"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Noise Texture"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Noise Texture"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[5], self.grp.nodes["Noise Texture"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[6], self.grp.nodes["Noise Texture"].inputs[3])
            links.new(self.grp.nodes["Group Input"].outputs[7], self.grp.nodes["Bright/Contrast"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[8], self.grp.nodes["Mix"].inputs[2])
            links.new(self.grp.nodes["Mix"].outputs[0], self.grp.nodes["Mix.001"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Mix.001"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[9], self.grp.nodes["Math"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Math"].inputs[0])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Caustics"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Caustics" : 
                return True

        return False







