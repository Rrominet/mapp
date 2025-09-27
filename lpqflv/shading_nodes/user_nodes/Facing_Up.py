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

class Facing_Up (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Facing Up"
    bl_idname = "facingup"

    def createTree (self) : 

        if Facing_Up.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Facing Up', 'ShaderNodeTree')

            node = self.grp.nodes.new('NodeGroupOutput')
            self.grp.outputs.new('NodeSocketColor', 'Color')
            node.inputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.is_active_output = True
            node.label = ''
            node.location[0] = 344.7413635253906
            node.location[1] = -15.150142669677734
            node.mute = False
            node.name = 'Group Output'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMapping')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Location'].default_value = (0.2199999988079071,0.0,0.0)
            node.inputs['Rotation'].default_value = (0.0,1.5707963705062866,0.0)
            node.inputs['Scale'].default_value = (0.0,0.0,0.10999999940395355)
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -548.18798828125
            node.location[1] = 110.46424865722656
            node.mute = False
            node.name = 'Mapping.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.vector_type = 'POINT'
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexGradient')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.gradient_type = 'LINEAR'
            node.hide = False
            node.label = ''
            node.location[0] = -315.47088623046875
            node.location[1] = 104.73448944091797
            node.mute = False
            node.name = 'Gradient Texture'
            node.show_options = True
            node.show_preview = False
            node.show_texture = True
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeNormal')
            node.inputs['Normal'].default_value = (0.0,0.0,1.0)
            node.outputs['Normal'].default_value = (0.008333333767950535,0.98333340883255,0.181620791554451)
            node.outputs['Dot'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -374.5415344238281
            node.location[1] = -147.84707641601562
            node.mute = False
            node.name = 'Normal'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 1.0
            node.inputs['Color1'].default_value = (0.5,0.5,0.5,1.0)
            node.inputs['Color2'].default_value = (0.0,0.0,0.0,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'MULTIPLY'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -29.7318115234375
            node.location[1] = 74.68587493896484
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
            self.grp.inputs.new('NodeSocketVector', 'Vector')
            self.grp.inputs['Vector'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['Vector'].min_value = -3.4028234663852886e+38
            self.grp.inputs['Vector'].max_value = 3.4028234663852886e+38
            self.grp.inputs.new('NodeSocketVectorTranslation', 'Location')
            self.grp.inputs['Location'].default_value = (0.2199999988079071,0.0,0.0)
            self.grp.inputs['Location'].min_value = -3.4028234663852886e+38
            self.grp.inputs['Location'].max_value = 3.4028234663852886e+38
            self.grp.inputs.new('NodeSocketVectorEuler', 'Rotation')
            self.grp.inputs['Rotation'].default_value = (0.0,1.5707963705062866,0.0)
            self.grp.inputs['Rotation'].min_value = -3.4028234663852886e+38
            self.grp.inputs['Rotation'].max_value = 3.4028234663852886e+38
            self.grp.inputs.new('NodeSocketVectorXYZ', 'Scale')
            self.grp.inputs['Scale'].default_value = (0.0,0.0,0.10999999940395355)
            self.grp.inputs['Scale'].min_value = -3.4028234663852886e+38
            self.grp.inputs['Scale'].max_value = 3.4028234663852886e+38
            self.grp.inputs.new('NodeSocketVectorDirection', 'Normal')
            self.grp.inputs['Normal'].default_value = (0.0,0.0,1.0)
            self.grp.inputs['Normal'].min_value = -1.0
            self.grp.inputs['Normal'].max_value = 1.0
            self.grp.inputs.new('NodeSocketFloatFactor', 'Facing factor')
            self.grp.inputs['Facing factor'].default_value = 1.0
            self.grp.inputs['Facing factor'].min_value = 0.0
            self.grp.inputs['Facing factor'].max_value = 1.0
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.outputs['Location'].default_value = (0.2199999988079071,0.0,0.0)
            node.outputs['Rotation'].default_value = (0.0,1.5707963705062866,0.0)
            node.outputs['Scale'].default_value = (0.0,0.0,0.10999999940395355)
            node.outputs['Normal'].default_value = (0.0,0.0,1.0)
            node.outputs['Facing factor'].default_value = 1.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -957.0042724609375
            node.location[1] = -20.200191497802734
            node.mute = False
            node.name = 'Group Input'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            links = self.grp.links
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Mapping.001"].inputs[0])
            links.new(self.grp.nodes["Mapping.001"].outputs[0], self.grp.nodes["Gradient Texture"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Normal"].inputs[0])
            links.new(self.grp.nodes["Gradient Texture"].outputs[0], self.grp.nodes["Mix"].inputs[1])
            links.new(self.grp.nodes["Normal"].outputs[1], self.grp.nodes["Mix"].inputs[2])
            links.new(self.grp.nodes["Mix"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Mapping.001"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Mapping.001"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Mapping.001"].inputs[3])
            links.new(self.grp.nodes["Group Input"].outputs[5], self.grp.nodes["Mix"].inputs[0])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Facing Up"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Facing Up" : 
                return True

        return False







