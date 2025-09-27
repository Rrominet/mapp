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

class Edges (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Edges"
    bl_idname = "edges"

    def createTree (self) : 

        if Edges.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Edges', 'ShaderNodeTree')

            node = self.grp.nodes.new('ShaderNodeGamma')
            node.inputs['Color'].default_value = (1.0,1.0,1.0,1.0)
            node.inputs['Gamma'].default_value = 15.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 153.45294189453125
            node.location[1] = 129.79891967773438
            node.mute = False
            node.name = 'Gamma'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeHueSaturation')
            node.inputs['Hue'].default_value = 0.5
            node.inputs['Saturation'].default_value = 0.0
            node.inputs['Value'].default_value = 1.0
            node.inputs['Fac'].default_value = 1.0
            node.inputs['Color'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 360.9347839355469
            node.location[1] = 127.79205322265625
            node.mute = False
            node.name = 'Hue Saturation Value'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 150.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupOutput')
            self.grp.outputs.new('NodeSocketFloat', 'Value')
            self.grp.outputs.new('NodeSocketVector', 'Bevel')
            node.inputs['Value'].default_value = 0.0
            node.inputs['Bevel'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.is_active_output = True
            node.label = ''
            node.location[0] = 779.097412109375
            node.location[1] = -0.0
            node.mute = False
            node.name = 'Group Output'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.5
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 579.097412109375
            node.location[1] = 10.712230682373047
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
            node.location[0] = -806.9085693359375
            node.location[1] = -22.481796264648438
            node.mute = False
            node.name = 'Texture Coordinate'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketFloat', 'EdgesWidth')
            self.grp.inputs['EdgesWidth'].default_value = 0.08999998867511749
            self.grp.inputs['EdgesWidth'].min_value = 0.0
            self.grp.inputs['EdgesWidth'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketFloat', 'Noise Factor')
            self.grp.inputs['Noise Factor'].default_value = 0.0
            self.grp.inputs['Noise Factor'].min_value = -10000.0
            self.grp.inputs['Noise Factor'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketFloat', 'Noise Min')
            self.grp.inputs['Noise Min'].default_value = 0.22999997437000275
            self.grp.inputs['Noise Min'].min_value = -10000.0
            self.grp.inputs['Noise Min'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketFloat', 'Noise Max')
            self.grp.inputs['Noise Max'].default_value = 0.8700000047683716
            self.grp.inputs['Noise Max'].min_value = -10000.0
            self.grp.inputs['Noise Max'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketVector', 'Normal')
            self.grp.inputs['Normal'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['Normal'].min_value = -1.0
            self.grp.inputs['Normal'].max_value = 1.0
            node.outputs['EdgesWidth'].default_value = 0.08999998867511749
            node.outputs['Noise Factor'].default_value = 0.0
            node.outputs['Noise Min'].default_value = 0.22999997437000275
            node.outputs['Noise Max'].default_value = 0.8700000047683716
            node.outputs['Normal'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -568.2432861328125
            node.location[1] = 239.14810180664062
            node.mute = False
            node.name = 'Group Input'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMapRange')
            node.inputs['Value'].default_value = 1.0
            node.inputs['From Min'].default_value = 0.22999997437000275
            node.inputs['From Max'].default_value = 0.8700000047683716
            node.inputs['To Min'].default_value = 0.0
            node.inputs['To Max'].default_value = 1.0
            node.outputs['Result'].default_value = 0.0
            node.clamp = True
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 1.6295623779296875
            node.location[1] = -154.4821014404297
            node.mute = False
            node.name = 'Map Range'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexNoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 1.2800002098083496
            node.inputs['Detail'].default_value = 16.0
            node.inputs['Distortion'].default_value = 0.7000000476837158
            node.outputs['Fac'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -520.9310302734375
            node.location[1] = -234.54421997070312
            node.mute = False
            node.name = 'Noise Texture'
            node.noise_dimensions = '3D'
            node.show_options = True
            node.show_preview = False
            node.show_texture = True
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMapping')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Location'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929)
            node.inputs['Rotation'].default_value = (0.0,0.0,0.0)
            node.inputs['Scale'].default_value = (0.009999999776482582,0.009999999776482582,0.009999999776482582)
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -497.0918273925781
            node.location[1] = 75.85686492919922
            node.mute = False
            node.name = 'Mapping'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.vector_type = 'POINT'
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeBevel')
            node.inputs['Radius'].default_value = 0.08999998867511749
            node.inputs['Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Normal'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -126.15608215332031
            node.location[1] = 198.20643615722656
            node.mute = False
            node.name = 'Bevel'
            node.samples = 4
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeBevel')
            node.inputs['Radius'].default_value = 0.08999998867511749
            node.inputs['Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Normal'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -115.36199951171875
            node.location[1] = 347.7099304199219
            node.mute = False
            node.name = 'Bevel.001'
            node.samples = 4
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            links = self.grp.links
            links.new(self.grp.nodes["Bevel"].outputs[0], self.grp.nodes["Gamma"].inputs[0])
            links.new(self.grp.nodes["Texture Coordinate"].outputs[3], self.grp.nodes["Mapping"].inputs[0])
            links.new(self.grp.nodes["Mapping"].outputs[0], self.grp.nodes["Bevel"].inputs[1])
            links.new(self.grp.nodes["Gamma"].outputs[0], self.grp.nodes["Hue Saturation Value"].inputs[4])
            links.new(self.grp.nodes["Texture Coordinate"].outputs[3], self.grp.nodes["Noise Texture"].inputs[0])
            links.new(self.grp.nodes["Noise Texture"].outputs[0], self.grp.nodes["Map Range"].inputs[0])
            links.new(self.grp.nodes["Hue Saturation Value"].outputs[0], self.grp.nodes["Math"].inputs[0])
            links.new(self.grp.nodes["Map Range"].outputs[0], self.grp.nodes["Math"].inputs[1])
            links.new(self.grp.nodes["Math"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Bevel"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Map Range"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Map Range"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Map Range"].inputs[3])
            links.new(self.grp.nodes["Bevel.001"].outputs[0], self.grp.nodes["Group Output"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Bevel.001"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Bevel.001"].inputs[0])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Edges"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Edges" : 
                return True

        return False







