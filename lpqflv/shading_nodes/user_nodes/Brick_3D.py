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

class Brick_3D (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Brick 3D"
    bl_idname = "brick3d"

    def createTree (self) : 

        if Brick_3D.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Brick 3D', 'ShaderNodeTree')

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 1.0
            node.inputs['Color1'].default_value = (0.5,0.5,0.5,1.0)
            node.inputs['Color2'].default_value = (0.5,0.5,0.5,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'OVERLAY'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 193.5208740234375
            node.location[1] = 223.3350830078125
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

            node = self.grp.nodes.new('NodeGroupOutput')
            self.grp.outputs.new('NodeSocketColor', 'Color')
            node.inputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.is_active_output = True
            node.label = ''
            node.location[0] = 663.8997192382812
            node.location[1] = -0.0
            node.mute = False
            node.name = 'Group Output'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 1.0
            node.inputs['Color1'].default_value = (0.5,0.5,0.5,1.0)
            node.inputs['Color2'].default_value = (0.5,0.5,0.5,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'OVERLAY'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 463.89971923828125
            node.location[1] = 120.007568359375
            node.mute = False
            node.name = 'Mix.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_alpha = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketVector', 'Vector')
            self.grp.inputs['Vector'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['Vector'].min_value = -3.4028234663852886e+38
            self.grp.inputs['Vector'].max_value = 3.4028234663852886e+38
            self.grp.inputs.new('NodeSocketColor', 'Color1')
            self.grp.inputs['Color1'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            self.grp.inputs.new('NodeSocketColor', 'Color2')
            self.grp.inputs['Color2'].default_value = (0.20000000298023224,0.20000000298023224,0.20000000298023224,1.0)
            self.grp.inputs.new('NodeSocketColor', 'Mortar')
            self.grp.inputs['Mortar'].default_value = (0.0,0.0,0.0,1.0)
            self.grp.inputs.new('NodeSocketFloat', 'Scale')
            self.grp.inputs['Scale'].default_value = 5.0
            self.grp.inputs['Scale'].min_value = -1000.0
            self.grp.inputs['Scale'].max_value = 1000.0
            self.grp.inputs.new('NodeSocketFloat', 'Mortar Size')
            self.grp.inputs['Mortar Size'].default_value = 0.019999999552965164
            self.grp.inputs['Mortar Size'].min_value = 0.0
            self.grp.inputs['Mortar Size'].max_value = 0.125
            self.grp.inputs.new('NodeSocketFloat', 'Mortar Smooth')
            self.grp.inputs['Mortar Smooth'].default_value = 0.10000000149011612
            self.grp.inputs['Mortar Smooth'].min_value = 0.0
            self.grp.inputs['Mortar Smooth'].max_value = 1.0
            self.grp.inputs.new('NodeSocketFloat', 'Bias')
            self.grp.inputs['Bias'].default_value = 0.0
            self.grp.inputs['Bias'].min_value = -1.0
            self.grp.inputs['Bias'].max_value = 1.0
            self.grp.inputs.new('NodeSocketFloat', 'Brick Width')
            self.grp.inputs['Brick Width'].default_value = 0.5
            self.grp.inputs['Brick Width'].min_value = 0.009999999776482582
            self.grp.inputs['Brick Width'].max_value = 100.0
            self.grp.inputs.new('NodeSocketFloat', 'Row Height')
            self.grp.inputs['Row Height'].default_value = 0.25
            self.grp.inputs['Row Height'].min_value = 0.009999999776482582
            self.grp.inputs['Row Height'].max_value = 100.0
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.outputs['Color1'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            node.outputs['Color2'].default_value = (0.20000000298023224,0.20000000298023224,0.20000000298023224,1.0)
            node.outputs['Mortar'].default_value = (0.0,0.0,0.0,1.0)
            node.outputs['Scale'].default_value = 5.0
            node.outputs['Mortar Size'].default_value = 0.019999999552965164
            node.outputs['Mortar Smooth'].default_value = 0.10000000149011612
            node.outputs['Bias'].default_value = 0.0
            node.outputs['Brick Width'].default_value = 0.5
            node.outputs['Row Height'].default_value = 0.25
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -904.2105102539062
            node.location[1] = -72.97967529296875
            node.mute = False
            node.name = 'Group Input'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMapping')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Location'].default_value = (0.0,0.0,0.0)
            node.inputs['Rotation'].default_value = (0.0,1.5707963705062866,0.0)
            node.inputs['Scale'].default_value = (1.0,1.0,1.0)
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = -462.1563415527344
            node.location[1] = 373.2458190917969
            node.mute = False
            node.name = 'Mapping.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.vector_type = 'POINT'
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMapping')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Location'].default_value = (0.0,0.0,0.0)
            node.inputs['Rotation'].default_value = (1.5707963705062866,0.0,0.0)
            node.inputs['Scale'].default_value = (1.0,1.0,1.0)
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = -396.4716796875
            node.location[1] = -95.85304260253906
            node.mute = False
            node.name = 'Mapping.002'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.vector_type = 'POINT'
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMapping')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Location'].default_value = (0.0,0.0,0.0)
            node.inputs['Rotation'].default_value = (0.0,0.0,1.5707963705062866)
            node.inputs['Scale'].default_value = (1.0,1.0,1.0)
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = -378.93182373046875
            node.location[1] = -348.8348693847656
            node.mute = False
            node.name = 'Mapping.003'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.vector_type = 'POINT'
            node.width = 240.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexBrick')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Color1'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            node.inputs['Color2'].default_value = (0.20000000298023224,0.20000000298023224,0.20000000298023224,1.0)
            node.inputs['Mortar'].default_value = (0.0,0.0,0.0,1.0)
            node.inputs['Scale'].default_value = 5.0
            node.inputs['Mortar Size'].default_value = 0.019999999552965164
            node.inputs['Mortar Smooth'].default_value = 0.10000000149011612
            node.inputs['Bias'].default_value = 0.0
            node.inputs['Brick Width'].default_value = 0.5
            node.inputs['Row Height'].default_value = 0.25
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -82.1834716796875
            node.location[1] = -410.49713134765625
            node.mute = False
            node.name = 'Brick Texture.002'
            node.offset = 0.5
            node.offset_frequency = 2
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.squash = 1.0
            node.squash_frequency = 2
            node.use_custom_color = False
            node.width = 150.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexBrick')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Color1'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            node.inputs['Color2'].default_value = (0.20000000298023224,0.20000000298023224,0.20000000298023224,1.0)
            node.inputs['Mortar'].default_value = (0.0,0.0,0.0,1.0)
            node.inputs['Scale'].default_value = 5.0
            node.inputs['Mortar Size'].default_value = 0.019999999552965164
            node.inputs['Mortar Smooth'].default_value = 0.10000000149011612
            node.inputs['Bias'].default_value = 0.0
            node.inputs['Brick Width'].default_value = 0.5
            node.inputs['Row Height'].default_value = 0.25
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -86.15966796875
            node.location[1] = 32.618408203125
            node.mute = False
            node.name = 'Brick Texture.001'
            node.offset = 0.5
            node.offset_frequency = 2
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.squash = 1.0
            node.squash_frequency = 2
            node.use_custom_color = False
            node.width = 150.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexBrick')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Color1'].default_value = (0.800000011920929,0.800000011920929,0.800000011920929,1.0)
            node.inputs['Color2'].default_value = (0.20000000298023224,0.20000000298023224,0.20000000298023224,1.0)
            node.inputs['Mortar'].default_value = (0.0,0.0,0.0,1.0)
            node.inputs['Scale'].default_value = 5.0
            node.inputs['Mortar Size'].default_value = 0.019999999552965164
            node.inputs['Mortar Smooth'].default_value = 0.10000000149011612
            node.inputs['Bias'].default_value = 0.0
            node.inputs['Brick Width'].default_value = 0.5
            node.inputs['Row Height'].default_value = 0.25
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -90.1358642578125
            node.location[1] = 447.91357421875
            node.mute = False
            node.name = 'Brick Texture'
            node.offset = 0.5
            node.offset_frequency = 2
            node.show_options = True
            node.show_preview = False
            node.show_texture = True
            node.squash = 1.0
            node.squash_frequency = 2
            node.use_custom_color = False
            node.width = 150.0
            node.width_hidden = 42.0

            links = self.grp.links
            links.new(self.grp.nodes["Mapping.001"].outputs[0], self.grp.nodes["Brick Texture"].inputs[0])
            links.new(self.grp.nodes["Mapping.002"].outputs[0], self.grp.nodes["Brick Texture.001"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Mapping.001"].inputs[0])
            links.new(self.grp.nodes["Brick Texture"].outputs[0], self.grp.nodes["Mix"].inputs[1])
            links.new(self.grp.nodes["Brick Texture.001"].outputs[0], self.grp.nodes["Mix"].inputs[2])
            links.new(self.grp.nodes["Mapping.003"].outputs[0], self.grp.nodes["Brick Texture.002"].inputs[0])
            links.new(self.grp.nodes["Mix"].outputs[0], self.grp.nodes["Mix.001"].inputs[1])
            links.new(self.grp.nodes["Brick Texture.002"].outputs[0], self.grp.nodes["Mix.001"].inputs[2])
            links.new(self.grp.nodes["Mix.001"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Mapping.002"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Mapping.003"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Brick Texture.002"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Brick Texture.002"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Brick Texture.002"].inputs[3])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Brick Texture.001"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Brick Texture.001"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Brick Texture.001"].inputs[3])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Brick Texture"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Brick Texture"].inputs[2])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Brick Texture"].inputs[3])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Brick Texture.002"].inputs[4])
            links.new(self.grp.nodes["Group Input"].outputs[5], self.grp.nodes["Brick Texture.002"].inputs[5])
            links.new(self.grp.nodes["Group Input"].outputs[6], self.grp.nodes["Brick Texture.002"].inputs[6])
            links.new(self.grp.nodes["Group Input"].outputs[7], self.grp.nodes["Brick Texture.002"].inputs[7])
            links.new(self.grp.nodes["Group Input"].outputs[8], self.grp.nodes["Brick Texture.002"].inputs[8])
            links.new(self.grp.nodes["Group Input"].outputs[9], self.grp.nodes["Brick Texture.002"].inputs[9])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Brick Texture.001"].inputs[4])
            links.new(self.grp.nodes["Group Input"].outputs[5], self.grp.nodes["Brick Texture.001"].inputs[5])
            links.new(self.grp.nodes["Group Input"].outputs[6], self.grp.nodes["Brick Texture.001"].inputs[6])
            links.new(self.grp.nodes["Group Input"].outputs[7], self.grp.nodes["Brick Texture.001"].inputs[7])
            links.new(self.grp.nodes["Group Input"].outputs[8], self.grp.nodes["Brick Texture.001"].inputs[8])
            links.new(self.grp.nodes["Group Input"].outputs[9], self.grp.nodes["Brick Texture.001"].inputs[9])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Brick Texture"].inputs[4])
            links.new(self.grp.nodes["Group Input"].outputs[5], self.grp.nodes["Brick Texture"].inputs[5])
            links.new(self.grp.nodes["Group Input"].outputs[6], self.grp.nodes["Brick Texture"].inputs[6])
            links.new(self.grp.nodes["Group Input"].outputs[7], self.grp.nodes["Brick Texture"].inputs[7])
            links.new(self.grp.nodes["Group Input"].outputs[8], self.grp.nodes["Brick Texture"].inputs[8])
            links.new(self.grp.nodes["Group Input"].outputs[9], self.grp.nodes["Brick Texture"].inputs[9])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Brick 3D"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Brick 3D" : 
                return True

        return False







