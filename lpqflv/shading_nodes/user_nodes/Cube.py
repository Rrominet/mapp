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

class Cube (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Cube"
    bl_idname = "cube"

    def createTree (self) : 

        if Cube.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Cube', 'ShaderNodeTree')

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.0
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.5
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 139.000732421875
            node.location[1] = 91.143310546875
            node.mute = False
            node.name = 'Math.003'
            node.operation = 'MULTIPLY'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.0
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.5
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 366.296630859375
            node.location[1] = -45.9378662109375
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

            node = self.grp.nodes.new('NodeGroupOutput')
            self.grp.outputs.new('NodeSocketFloat', 'Value')
            node.inputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.is_active_output = True
            node.label = ''
            node.location[0] = 566.296630859375
            node.location[1] = -0.0
            node.mute = False
            node.name = 'Group Output'
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
            node.location[0] = -366.296630859375
            node.location[1] = 25.0142822265625
            node.mute = False
            node.name = 'Separate XYZ.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.0
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.8600000143051147
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -116.2646484375
            node.location[1] = 187.2109375
            node.mute = False
            node.name = 'Math'
            node.operation = 'COMPARE'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 1.0799999237060547
            node.inputs['Value'].default_value = 0.5199999809265137
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -116.01513671875
            node.location[1] = -1.55029296875
            node.mute = False
            node.name = 'Math.001'
            node.operation = 'COMPARE'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.11000001430511475
            node.inputs['Value'].default_value = 1.1699999570846558
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -117.919921875
            node.location[1] = -187.2110595703125
            node.mute = False
            node.name = 'Math.002'
            node.operation = 'COMPARE'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketFloat', 'X')
            self.grp.inputs['X'].default_value = 0.0
            self.grp.inputs['X'].min_value = -10000.0
            self.grp.inputs['X'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketFloat', 'Y')
            self.grp.inputs['Y'].default_value = 1.0799999237060547
            self.grp.inputs['Y'].min_value = -10000.0
            self.grp.inputs['Y'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketFloat', 'Z')
            self.grp.inputs['Z'].default_value = 0.11000001430511475
            self.grp.inputs['Z'].min_value = -10000.0
            self.grp.inputs['Z'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketFloat', 'Width')
            self.grp.inputs['Width'].default_value = 0.8600000143051147
            self.grp.inputs['Width'].min_value = -10000.0
            self.grp.inputs['Width'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketFloat', 'Depth')
            self.grp.inputs['Depth'].default_value = 0.5199999809265137
            self.grp.inputs['Depth'].min_value = -10000.0
            self.grp.inputs['Depth'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketFloat', 'Height')
            self.grp.inputs['Height'].default_value = 1.1699999570846558
            self.grp.inputs['Height'].min_value = -10000.0
            self.grp.inputs['Height'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketVector', 'Vector')
            self.grp.inputs['Vector'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['Vector'].min_value = -10000.0
            self.grp.inputs['Vector'].max_value = 10000.0
            node.outputs['X'].default_value = 0.0
            node.outputs['Y'].default_value = 1.0799999237060547
            node.outputs['Z'].default_value = 0.11000001430511475
            node.outputs['Width'].default_value = 0.8600000143051147
            node.outputs['Depth'].default_value = 0.5199999809265137
            node.outputs['Height'].default_value = 1.1699999570846558
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -699.76318359375
            node.location[1] = -145.15733337402344
            node.mute = False
            node.name = 'Group Input'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            links = self.grp.links
            links.new(self.grp.nodes["Group Input"].outputs[6], self.grp.nodes["Separate XYZ.001"].inputs[0])
            links.new(self.grp.nodes["Separate XYZ.001"].outputs[0], self.grp.nodes["Math"].inputs[1])
            links.new(self.grp.nodes["Separate XYZ.001"].outputs[2], self.grp.nodes["Math.002"].inputs[0])
            links.new(self.grp.nodes["Math"].outputs[0], self.grp.nodes["Math.003"].inputs[0])
            links.new(self.grp.nodes["Math.001"].outputs[0], self.grp.nodes["Math.003"].inputs[1])
            links.new(self.grp.nodes["Math.003"].outputs[0], self.grp.nodes["Math.004"].inputs[0])
            links.new(self.grp.nodes["Math.002"].outputs[0], self.grp.nodes["Math.004"].inputs[1])
            links.new(self.grp.nodes["Math.004"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Math"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Math"].inputs[2])
            links.new(self.grp.nodes["Separate XYZ.001"].outputs[1], self.grp.nodes["Math.001"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Math.001"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Math.001"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Math.002"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[5], self.grp.nodes["Math.002"].inputs[2])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Cube"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Cube" : 
                return True

        return False







