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

class Building_Lights (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Building Lights"
    bl_idname = "buildinglights"

    def createTree (self) : 

        if Building_Lights.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Building Lights', 'ShaderNodeTree')

            node = self.grp.nodes.new('ShaderNodeMapRange')
            node.inputs['Value'].default_value = 1.0
            node.inputs['From Min'].default_value = 0.7999999523162842
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
            node.location[0] = 147.29116821289062
            node.location[1] = -20.17828369140625
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
            node.inputs['Value'].default_value = 10.0
            node.inputs['Value'].default_value = 0.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 341.4901123046875
            node.location[1] = -32.652862548828125
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
            self.grp.outputs.new('NodeSocketShader', 'Emission')
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.is_active_output = True
            node.label = ''
            node.location[0] = 723.3162841796875
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
            node.location[0] = -663.191162109375
            node.location[1] = -121.60392761230469
            node.mute = False
            node.name = 'Texture Coordinate'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMapping')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Location'].default_value = (0.0,0.0,0.0)
            node.inputs['Rotation'].default_value = (0.0,0.0,0.0)
            node.inputs['Scale'].default_value = (1.0,1.0,1.0)
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -369.1061706542969
            node.location[1] = -17.792341232299805
            node.mute = False
            node.name = 'Mapping'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.vector_type = 'POINT'
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('brick3d')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Color1'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            node.inputs['Color2'].default_value = (0.007650217041373253,0.007650217041373253,0.007650217041373253,1.0)
            node.inputs['Mortar'].default_value = (0.0,0.0,0.0,1.0)
            node.inputs['Scale'].default_value = 0.04000038281083107
            node.inputs['Mortar Size'].default_value = 0.019999999552965164
            node.inputs['Mortar Smooth'].default_value = 0.10000000149011612
            node.inputs['Bias'].default_value = 0.0
            node.inputs['Brick Width'].default_value = 1.1999999284744263
            node.inputs['Row Height'].default_value = 0.44999998807907104
            node.outputs['Color'].default_value = (0.0,0.0,0.0,1.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -59.31407165527344
            node.location[1] = -21.271453857421875
            node.mute = False
            node.name = 'Brick 3D'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeEmission')
            node.inputs['Color'].default_value = (0.0,0.8764453530311584,1.0,1.0)
            node.inputs['Strength'].default_value = 1.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 533.3162841796875
            node.location[1] = 32.652862548828125
            node.mute = False
            node.name = 'Emission'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketColor', 'Color')
            self.grp.inputs['Color'].default_value = (0.0,0.8764453530311584,1.0,1.0)
            self.grp.inputs.new('NodeSocketFloat', 'Strength')
            self.grp.inputs['Strength'].default_value = 10.0
            self.grp.inputs['Strength'].min_value = -10000.0
            self.grp.inputs['Strength'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketFloat', 'Scale')
            self.grp.inputs['Scale'].default_value = 0.04000038281083107
            self.grp.inputs['Scale'].min_value = -1000.0
            self.grp.inputs['Scale'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketFloat', 'Mortar Size')
            self.grp.inputs['Mortar Size'].default_value = 0.10000000149011612
            self.grp.inputs['Mortar Size'].min_value = 0.0
            self.grp.inputs['Mortar Size'].max_value = 1.0
            self.grp.inputs.new('NodeSocketFloat', 'Brick Width')
            self.grp.inputs['Brick Width'].default_value = 1.1999999284744263
            self.grp.inputs['Brick Width'].min_value = 0.009999999776482582
            self.grp.inputs['Brick Width'].max_value = 100.0
            self.grp.inputs.new('NodeSocketFloat', 'Row Height')
            self.grp.inputs['Row Height'].default_value = 0.44999998807907104
            self.grp.inputs['Row Height'].min_value = 0.009999999776482582
            self.grp.inputs['Row Height'].max_value = 100.0
            node.outputs['Color'].default_value = (0.0,0.8764453530311584,1.0,1.0)
            node.outputs['Strength'].default_value = 10.0
            node.outputs['Scale'].default_value = 0.04000038281083107
            node.outputs['Mortar Size'].default_value = 0.10000000149011612
            node.outputs['Brick Width'].default_value = 1.1999999284744263
            node.outputs['Row Height'].default_value = 0.44999998807907104
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -724.8656616210938
            node.location[1] = 121.0570297241211
            node.mute = False
            node.name = 'Group Input'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            links = self.grp.links
            links.new(self.grp.nodes["Emission"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Brick 3D"].outputs[0], self.grp.nodes["Map Range"].inputs[0])
            links.new(self.grp.nodes["Mapping"].outputs[0], self.grp.nodes["Brick 3D"].inputs[0])
            links.new(self.grp.nodes["Texture Coordinate"].outputs[3], self.grp.nodes["Mapping"].inputs[0])
            links.new(self.grp.nodes["Map Range"].outputs[0], self.grp.nodes["Math"].inputs[0])
            links.new(self.grp.nodes["Math"].outputs[0], self.grp.nodes["Emission"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Brick 3D"].inputs[4])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Brick 3D"].inputs[8])
            links.new(self.grp.nodes["Group Input"].outputs[5], self.grp.nodes["Brick 3D"].inputs[9])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Brick 3D"].inputs[5])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Emission"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Math"].inputs[1])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Building Lights"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Building Lights" : 
                return True

        return False







