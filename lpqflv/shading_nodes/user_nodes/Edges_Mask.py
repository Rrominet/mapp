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

class Edges_Mask (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Edges Mask"
    bl_idname = "edgesmask"

    def createTree (self) : 

        if Edges_Mask.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Edges Mask', 'ShaderNodeTree')

            node = self.grp.nodes.new('ShaderNodeNewGeometry')
            node.outputs['Position'].default_value = (0.0,0.0,0.0)
            node.outputs['Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Tangent'].default_value = (0.0,0.0,0.0)
            node.outputs['True Normal'].default_value = (0.0,0.0,0.0)
            node.outputs['Incoming'].default_value = (0.0,0.0,0.0)
            node.outputs['Parametric'].default_value = (0.0,0.0,0.0)
            node.outputs['Backfacing'].default_value = 0.0
            node.outputs['Pointiness'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -372.5682678222656
            node.location[1] = 34.710968017578125
            node.mute = False
            node.name = 'Geometry'
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
            element = node.color_ramp.elements.new(0.41363611817359924)
            element.color = (0.0,0.0,0.0,1.0)
            element.alpha = 1.0
            element.position = 0.41363611817359924
            element = node.color_ramp.elements.new(0.5090909600257874)
            element.color = (1.0,1.0,1.0,1.0)
            element.alpha = 1.0
            element.position = 0.5090909600257874
            node.hide = False
            node.label = ''
            node.location[0] = -179.37828063964844
            node.location[1] = -222.50418090820312
            node.mute = False
            node.name = 'ColorRamp.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 240.0
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
            element = node.color_ramp.elements.new(0.4181819558143616)
            element.color = (1.0,1.0,1.0,1.0)
            element.alpha = 1.0
            element.position = 0.4181819558143616
            element = node.color_ramp.elements.new(0.49545422196388245)
            element.color = (0.0,0.0,0.0,1.0)
            element.alpha = 1.0
            element.position = 0.49545422196388245
            node.hide = False
            node.label = ''
            node.location[0] = -186.0850067138672
            node.location[1] = 38.746795654296875
            node.mute = False
            node.name = 'ColorRamp'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupOutput')
            self.grp.outputs.new('NodeSocketColor', 'Color')
            node.inputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.is_active_output = True
            node.label = ''
            node.location[0] = 527.3233032226562
            node.location[1] = -91.87869262695312
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
            node.inputs['Value'].default_value = 3.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 109.12136840820312
            node.location[1] = 25.998443603515625
            node.mute = False
            node.name = 'Math'
            node.operation = 'POWER'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = True
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexMusgrave')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 0.2800002098083496
            node.inputs['Detail'].default_value = 16.0
            node.inputs['Dimension'].default_value = 0.35999998450279236
            node.inputs['Lacunarity'].default_value = 1.7999999523162842
            node.inputs['Offset'].default_value = 0.0
            node.inputs['Gain'].default_value = 1.0
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -378.2993469238281
            node.location[1] = -210.87173461914062
            node.musgrave_dimensions = '3D'
            node.musgrave_type = 'FBM'
            node.mute = False
            node.name = 'Musgrave Texture'
            node.show_options = True
            node.show_preview = False
            node.show_texture = True
            node.use_custom_color = False
            node.width = 150.0
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
            node.location[0] = 327.3233337402344
            node.location[1] = -98.24197387695312
            node.mute = False
            node.name = 'Mix'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_alpha = False
            node.use_clamp = True
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketFloat', 'Contrast')
            self.grp.inputs['Contrast'].default_value = 3.0
            self.grp.inputs['Contrast'].min_value = -10000.0
            self.grp.inputs['Contrast'].max_value = 10000.0
            self.grp.inputs.new('NodeSocketFloat', 'Noise Scale')
            self.grp.inputs['Noise Scale'].default_value = 0.2800002098083496
            self.grp.inputs['Noise Scale'].min_value = -1000.0
            self.grp.inputs['Noise Scale'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketFloatFactor', 'Noise Factor')
            self.grp.inputs['Noise Factor'].default_value = 1.0
            self.grp.inputs['Noise Factor'].min_value = 0.0
            self.grp.inputs['Noise Factor'].max_value = 1.0
            self.grp.inputs.new('NodeSocketVector', 'Vector')
            self.grp.inputs['Vector'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['Vector'].min_value = 0.0
            self.grp.inputs['Vector'].max_value = 1.0
            node.outputs['Contrast'].default_value = 3.0
            node.outputs['Noise Scale'].default_value = 0.2800002098083496
            node.outputs['Noise Factor'].default_value = 1.0
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -670.0562744140625
            node.location[1] = -264.1512451171875
            node.mute = False
            node.name = 'Group Input'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            links = self.grp.links
            links.new(self.grp.nodes["Geometry"].outputs[7], self.grp.nodes["ColorRamp"].inputs[0])
            links.new(self.grp.nodes["ColorRamp"].outputs[0], self.grp.nodes["Math"].inputs[0])
            links.new(self.grp.nodes["Musgrave Texture"].outputs[0], self.grp.nodes["ColorRamp.001"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Musgrave Texture"].inputs[0])
            links.new(self.grp.nodes["ColorRamp.001"].outputs[0], self.grp.nodes["Mix"].inputs[2])
            links.new(self.grp.nodes["Math"].outputs[0], self.grp.nodes["Mix"].inputs[1])
            links.new(self.grp.nodes["Mix"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Math"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Musgrave Texture"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Mix"].inputs[0])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Edges Mask"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Edges Mask" : 
                return True

        return False







