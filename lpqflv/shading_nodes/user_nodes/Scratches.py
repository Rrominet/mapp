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

class Scratches (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Scratches"
    bl_idname = "scratches"

    def createTree (self) : 

        if Scratches.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Scratches', 'ShaderNodeTree')

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
            node.location[0] = -2638.56201171875
            node.location[1] = 490.0736389160156
            node.mute = False
            node.name = 'Texture Coordinate.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 100.0

            node = self.grp.nodes.new('ShaderNodeTexNoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 0.5
            node.inputs['Detail'].default_value = 12.5
            node.inputs['Distortion'].default_value = 0.0
            node.outputs['Fac'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -2185.957763671875
            node.location[1] = 450.01580810546875
            node.mute = False
            node.name = 'Noise Texture'
            node.noise_dimensions = '3D'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 100.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 0.1345825046300888
            node.inputs['Color1'].default_value = (0.5,0.5,0.5,1.0)
            node.inputs['Color2'].default_value = (0.5,0.5,0.5,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MIX'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1746.9713134765625
            node.location[1] = 336.8837585449219
            node.mute = False
            node.name = 'Mix'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_alpha = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 100.0

            node = self.grp.nodes.new('ShaderNodeCombineXYZ')
            node.inputs['X'].default_value = 0.0
            node.inputs['Y'].default_value = 0.0
            node.inputs['Z'].default_value = 0.0
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1730.812744140625
            node.location[1] = -62.4842529296875
            node.mute = False
            node.name = 'Combine XYZ'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 100.0

            node = self.grp.nodes.new('ShaderNodeCombineXYZ')
            node.inputs['X'].default_value = 1.0
            node.inputs['Y'].default_value = 1.0
            node.inputs['Z'].default_value = 1.0
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -2083.15625
            node.location[1] = -332.15850830078125
            node.mute = False
            node.name = 'Combine XYZ.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 100.0

            node = self.grp.nodes.new('ShaderNodeMapping')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Location'].default_value = (0.0,0.0,0.0)
            node.inputs['Rotation'].default_value = (0.0,0.0,0.0)
            node.inputs['Scale'].default_value = (2.2300000190734863,0.12000003457069397,0.1300000250339508)
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1092.734130859375
            node.location[1] = 541.200927734375
            node.mute = False
            node.name = 'Mapping.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.vector_type = 'POINT'
            node.width = 140.0
            node.width_hidden = 100.0

            node = self.grp.nodes.new('ShaderNodeMapping')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Location'].default_value = (0.0,0.0,0.0)
            node.inputs['Rotation'].default_value = (1.2671089172363281,0.5480333566665649,0.6876596808433533)
            node.inputs['Scale'].default_value = (1.0,1.0,1.0)
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1295.11669921875
            node.location[1] = 541.200927734375
            node.mute = False
            node.name = 'Mapping.002'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.vector_type = 'POINT'
            node.width = 140.0
            node.width_hidden = 100.0

            node = self.grp.nodes.new('ShaderNodeMapping')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Location'].default_value = (0.0,0.0,0.0)
            node.inputs['Rotation'].default_value = (1.2671089172363281,0.5480333566665649,0.6876596808433533)
            node.inputs['Scale'].default_value = (1.0,1.0,1.0)
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1295.11669921875
            node.location[1] = -1.664896011352539
            node.mute = False
            node.name = 'Mapping.004'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.vector_type = 'POINT'
            node.width = 140.0
            node.width_hidden = 100.0

            node = self.grp.nodes.new('ShaderNodeMapping')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Location'].default_value = (0.0,0.0,0.0)
            node.inputs['Rotation'].default_value = (0.0,0.0,0.0)
            node.inputs['Scale'].default_value = (2.2300000190734863,0.12000003457069397,0.1300000250339508)
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1092.734130859375
            node.location[1] = -483.0741882324219
            node.mute = False
            node.name = 'Mapping.005'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.vector_type = 'POINT'
            node.width = 140.0
            node.width_hidden = 100.0

            node = self.grp.nodes.new('ShaderNodeMapping')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Location'].default_value = (0.0,0.0,0.0)
            node.inputs['Rotation'].default_value = (1.2671089172363281,0.5480333566665649,0.6876596808433533)
            node.inputs['Scale'].default_value = (1.0,1.0,1.0)
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1295.11669921875
            node.location[1] = -483.0741882324219
            node.mute = False
            node.name = 'Mapping.006'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.vector_type = 'POINT'
            node.width = 140.0
            node.width_hidden = 100.0

            node = self.grp.nodes.new('ShaderNodeMapping')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Location'].default_value = (0.0,0.0,0.0)
            node.inputs['Rotation'].default_value = (0.0,0.0,0.0)
            node.inputs['Scale'].default_value = (2.2300000190734863,0.12000003457069397,0.1300000250339508)
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1092.734130859375
            node.location[1] = -1.664896011352539
            node.mute = False
            node.name = 'Mapping.003'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.vector_type = 'POINT'
            node.width = 140.0
            node.width_hidden = 100.0

            node = self.grp.nodes.new('ShaderNodeTexMusgrave')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.2199999988079071
            node.inputs['Scale'].default_value = 323.8799743652344
            node.inputs['Detail'].default_value = 13.699999809265137
            node.inputs['Dimension'].default_value = 0.33000001311302185
            node.inputs['Lacunarity'].default_value = 0.8199999928474426
            node.inputs['Offset'].default_value = 0.0
            node.inputs['Gain'].default_value = 1.0
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -828.6997680664062
            node.location[1] = 541.200927734375
            node.musgrave_dimensions = '3D'
            node.musgrave_type = 'FBM'
            node.mute = False
            node.name = 'Musgrave Texture.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 150.0
            node.width_hidden = 120.0

            node = self.grp.nodes.new('ShaderNodeTexMusgrave')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.2199999988079071
            node.inputs['Scale'].default_value = 323.8799743652344
            node.inputs['Detail'].default_value = 13.699999809265137
            node.inputs['Dimension'].default_value = 0.33000001311302185
            node.inputs['Lacunarity'].default_value = 0.8199999928474426
            node.inputs['Offset'].default_value = 0.0
            node.inputs['Gain'].default_value = 1.0
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -828.6997680664062
            node.location[1] = -483.0741882324219
            node.musgrave_dimensions = '3D'
            node.musgrave_type = 'FBM'
            node.mute = False
            node.name = 'Musgrave Texture.003'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 164.9729766845703
            node.width_hidden = 120.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.5
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -616.221923828125
            node.location[1] = 241.22134399414062
            node.mute = False
            node.name = 'Math.006'
            node.operation = 'ADD'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 100.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.5
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -375.04840087890625
            node.location[1] = 39.40849304199219
            node.mute = False
            node.name = 'Math.007'
            node.operation = 'ADD'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 100.0

            node = self.grp.nodes.new('ShaderNodeMapRange')
            node.inputs['Value'].default_value = 1.0
            node.inputs['From Min'].default_value = 3.4699997901916504
            node.inputs['From Max'].default_value = 17.0
            node.inputs['To Min'].default_value = 0.0
            node.inputs['To Max'].default_value = 1.0
            node.outputs['Result'].default_value = 0.0
            node.clamp = True
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -98.07293701171875
            node.location[1] = 64.99993896484375
            node.mute = False
            node.name = 'Map Range'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexMusgrave')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.2199999988079071
            node.inputs['Scale'].default_value = 323.8799743652344
            node.inputs['Detail'].default_value = 13.699999809265137
            node.inputs['Dimension'].default_value = 0.33000001311302185
            node.inputs['Lacunarity'].default_value = 0.8199999928474426
            node.inputs['Offset'].default_value = 0.0
            node.inputs['Gain'].default_value = 1.0
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -828.6997680664062
            node.location[1] = -1.664896011352539
            node.musgrave_dimensions = '3D'
            node.musgrave_type = 'FBM'
            node.mute = False
            node.name = 'Musgrave Texture.002'
            node.show_options = True
            node.show_preview = False
            node.show_texture = True
            node.use_custom_color = False
            node.width = 150.0
            node.width_hidden = 120.0

            node = self.grp.nodes.new('NodeGroupOutput')
            self.grp.outputs.new('NodeSocketFloat', 'Scratches')
            node.inputs['Scratches'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.is_active_output = True
            node.label = ''
            node.location[0] = 302.396484375
            node.location[1] = 22.038299560546875
            node.mute = False
            node.name = 'Group Output'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 80.0

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketFloatFactor', 'Deformation')
            self.grp.inputs['Deformation'].default_value = 0.1345825046300888
            self.grp.inputs['Deformation'].min_value = 0.0
            self.grp.inputs['Deformation'].max_value = 1.0
            self.grp.inputs.new('NodeSocketFloat', 'Deformation Scale')
            self.grp.inputs['Deformation Scale'].default_value = 0.5
            self.grp.inputs['Deformation Scale'].min_value = -1000.0
            self.grp.inputs['Deformation Scale'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketFloat', 'Deformation Details')
            self.grp.inputs['Deformation Details'].default_value = 12.5
            self.grp.inputs['Deformation Details'].min_value = 0.0
            self.grp.inputs['Deformation Details'].max_value = 16.0
            self.grp.inputs.new('NodeSocketFloat', 'Width')
            self.grp.inputs['Width'].default_value = 0.0
            self.grp.inputs['Width'].min_value = -10000.0
            self.grp.inputs['Width'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketFloat', 'Length')
            self.grp.inputs['Length'].default_value = 0.0
            self.grp.inputs['Length'].min_value = -3.4028234663852886e+38
            self.grp.inputs['Length'].max_value = 3.4028234663852886e+38
            self.grp.inputs.new('NodeSocketFloat', 'Contrast')
            self.grp.inputs['Contrast'].default_value = 0.0
            self.grp.inputs['Contrast'].min_value = -3.4028234663852886e+38
            self.grp.inputs['Contrast'].max_value = 3.4028234663852886e+38
            self.grp.inputs.new('NodeSocketFloat', 'Scale')
            self.grp.inputs['Scale'].default_value = 0.0
            self.grp.inputs['Scale'].min_value = -3.4028234663852886e+38
            self.grp.inputs['Scale'].max_value = 3.4028234663852886e+38
            self.grp.inputs.new('NodeSocketVectorEuler', 'Rotation 1')
            self.grp.inputs['Rotation 1'].default_value = (1.2671089172363281,0.5480333566665649,0.6876596808433533)
            self.grp.inputs['Rotation 1'].min_value = -3.4028234663852886e+38
            self.grp.inputs['Rotation 1'].max_value = 3.4028234663852886e+38
            self.grp.inputs.new('NodeSocketVectorEuler', 'Rotation 2')
            self.grp.inputs['Rotation 2'].default_value = (1.2671089172363281,0.5480333566665649,0.6876596808433533)
            self.grp.inputs['Rotation 2'].min_value = -3.4028234663852886e+38
            self.grp.inputs['Rotation 2'].max_value = 3.4028234663852886e+38
            self.grp.inputs.new('NodeSocketVectorEuler', 'Rotation 3')
            self.grp.inputs['Rotation 3'].default_value = (1.2671089172363281,0.5480333566665649,0.6876596808433533)
            self.grp.inputs['Rotation 3'].min_value = -3.4028234663852886e+38
            self.grp.inputs['Rotation 3'].max_value = 3.4028234663852886e+38
            node.outputs['Deformation'].default_value = 0.1345825046300888
            node.outputs['Deformation Scale'].default_value = 0.5
            node.outputs['Deformation Details'].default_value = 12.5
            node.outputs['Width'].default_value = 0.0
            node.outputs['Length'].default_value = 0.0
            node.outputs['Contrast'].default_value = 0.0
            node.outputs['Scale'].default_value = 0.0
            node.outputs['Rotation 1'].default_value = (1.2671089172363281,0.5480333566665649,0.6876596808433533)
            node.outputs['Rotation 2'].default_value = (1.2671089172363281,0.5480333566665649,0.6876596808433533)
            node.outputs['Rotation 3'].default_value = (1.2671089172363281,0.5480333566665649,0.6876596808433533)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -2684.135986328125
            node.location[1] = -23.712459564208984
            node.mute = False
            node.name = 'Group Input'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 80.0

            links = self.grp.links
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Combine XYZ"].inputs[0])
            links.new(self.grp.nodes["Combine XYZ"].outputs[0], self.grp.nodes["Mapping.001"].inputs[3])
            links.new(self.grp.nodes["Mapping.001"].outputs[0], self.grp.nodes["Musgrave Texture.001"].inputs[0])
            links.new(self.grp.nodes["Mapping.002"].outputs[0], self.grp.nodes["Mapping.001"].inputs[0])
            links.new(self.grp.nodes["Texture Coordinate.001"].outputs[3], self.grp.nodes["Mix"].inputs[1])
            links.new(self.grp.nodes["Noise Texture"].outputs[1], self.grp.nodes["Mix"].inputs[2])
            links.new(self.grp.nodes["Texture Coordinate.001"].outputs[3], self.grp.nodes["Noise Texture"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Mix"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Noise Texture"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Noise Texture"].inputs[3])
            links.new(self.grp.nodes["Mix"].outputs[0], self.grp.nodes["Mapping.002"].inputs[0])
            links.new(self.grp.nodes["Mapping.003"].outputs[0], self.grp.nodes["Musgrave Texture.002"].inputs[0])
            links.new(self.grp.nodes["Mapping.004"].outputs[0], self.grp.nodes["Mapping.003"].inputs[0])
            links.new(self.grp.nodes["Mapping.005"].outputs[0], self.grp.nodes["Musgrave Texture.003"].inputs[0])
            links.new(self.grp.nodes["Mapping.006"].outputs[0], self.grp.nodes["Mapping.005"].inputs[0])
            links.new(self.grp.nodes["Combine XYZ"].outputs[0], self.grp.nodes["Mapping.003"].inputs[3])
            links.new(self.grp.nodes["Mix"].outputs[0], self.grp.nodes["Mapping.004"].inputs[0])
            links.new(self.grp.nodes["Combine XYZ"].outputs[0], self.grp.nodes["Mapping.005"].inputs[3])
            links.new(self.grp.nodes["Mix"].outputs[0], self.grp.nodes["Mapping.006"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[7], self.grp.nodes["Mapping.006"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[8], self.grp.nodes["Mapping.004"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[9], self.grp.nodes["Mapping.002"].inputs[2])
            links.new(self.grp.nodes["Math.006"].outputs[0], self.grp.nodes["Math.007"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Combine XYZ"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Combine XYZ"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[6], self.grp.nodes["Combine XYZ.001"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[6], self.grp.nodes["Combine XYZ.001"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[6], self.grp.nodes["Combine XYZ.001"].inputs[2])
            links.new(self.grp.nodes["Combine XYZ.001"].outputs[0], self.grp.nodes["Mapping.004"].inputs[3])
            links.new(self.grp.nodes["Combine XYZ.001"].outputs[0], self.grp.nodes["Mapping.006"].inputs[3])
            links.new(self.grp.nodes["Combine XYZ.001"].outputs[0], self.grp.nodes["Mapping.002"].inputs[3])
            links.new(self.grp.nodes["Math.007"].outputs[0], self.grp.nodes["Map Range"].inputs[0])
            links.new(self.grp.nodes["Musgrave Texture.002"].outputs[0], self.grp.nodes["Math.006"].inputs[1])
            links.new(self.grp.nodes["Musgrave Texture.001"].outputs[0], self.grp.nodes["Math.006"].inputs[0])
            links.new(self.grp.nodes["Musgrave Texture.003"].outputs[0], self.grp.nodes["Math.007"].inputs[1])
            links.new(self.grp.nodes["Map Range"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[5], self.grp.nodes["Map Range"].inputs[1])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Scratches"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Scratches" : 
                return True

        return False







