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

class Uber_Mapping (bpy.types.NodeCustomGroup, bpy.types.NodeTree): 
    
    bl_label = "Uber Mapping"
    bl_idname = "ubermapping"

    def createTree (self) : 

        if Uber_Mapping.exists() == False : 

            #grpNodeContent#
            self.grp = bpy.data.node_groups.new('Uber Mapping', 'ShaderNodeTree')

            node = self.grp.nodes.new('NodeFrame')
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = 'Combine'
            node.label_size = 64
            node.location[0] = 2508.0
            node.location[1] = 1734.0
            node.mute = False
            node.name = 'Frame.003'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.shrink = True
            node.use_custom_color = False
            node.width = 518.47998046875
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeFrame')
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = 'Mosaic Rotation'
            node.label_size = 64
            node.location[0] = 280.0
            node.location[1] = 1906.0
            node.mute = False
            node.name = 'Frame.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.shrink = True
            node.use_custom_color = False
            node.width = 671.47998046875
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeFrame')
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = 'Translation'
            node.label_size = 64
            node.location[0] = 3296.0
            node.location[1] = 1664.0
            node.mute = False
            node.name = 'Frame.006'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.shrink = True
            node.use_custom_color = False
            node.width = 695.479736328125
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeFrame')
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = 'GridView'
            node.label_size = 64
            node.location[0] = 7736.0
            node.location[1] = 714.0
            node.mute = False
            node.name = 'Frame.004'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.shrink = True
            node.use_custom_color = False
            node.width = 485.320068359375
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeFrame')
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = 'Scale'
            node.label_size = 64
            node.location[0] = -3604.0
            node.location[1] = 2028.0
            node.mute = False
            node.name = 'Frame'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.shrink = True
            node.use_custom_color = False
            node.width = 403.47998046875
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeFrame')
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = 'Mosaic Noise'
            node.label_size = 64
            node.location[0] = -1090.0
            node.location[1] = 1436.0
            node.mute = False
            node.name = 'Frame.002'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.shrink = True
            node.use_custom_color = False
            node.width = 1456.47998046875
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeFrame')
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = 'Rotation'
            node.label_size = 64
            node.location[0] = 5634.0
            node.location[1] = 1828.0
            node.mute = False
            node.name = 'Frame.005'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.shrink = True
            node.use_custom_color = False
            node.width = 1308.47998046875
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeFrame')
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = 'Aspect Ratio'
            node.label_size = 64
            node.location[0] = 7742.0
            node.location[1] = 1748.0
            node.mute = False
            node.name = 'Frame.008'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.shrink = True
            node.use_custom_color = False
            node.width = 689.48046875
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
            node.hide = True
            node.label = ''
            node.location[0] = -1331.0
            node.location[1] = -1262.0
            node.mute = False
            node.name = 'Mix'
            node.parent = self.grp.nodes["Frame.003"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_alpha = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeCombineXYZ')
            node.inputs['X'].default_value = 0.0
            node.inputs['Y'].default_value = 0.0
            node.inputs['Z'].default_value = 0.0
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = -1498.0
            node.location[1] = -1235.0
            node.mute = False
            node.name = 'Combine XYZ.004'
            node.parent = self.grp.nodes["Frame.003"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeCombineXYZ')
            node.inputs['X'].default_value = 0.0
            node.inputs['Y'].default_value = 0.0
            node.inputs['Z'].default_value = 0.0
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = -1334.0
            node.location[1] = -1160.0
            node.mute = False
            node.name = 'Combine XYZ.001'
            node.parent = self.grp.nodes["Frame.003"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeVectorMath')
            node.inputs['Vector'].default_value = (0.5,0.5,0.5)
            node.inputs['Vector'].default_value = (0.5,0.5,0.5)
            node.inputs['Scale'].default_value = 1.0
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = -1180.0
            node.location[1] = -1220.0
            node.mute = False
            node.name = 'Vector Math'
            node.operation = 'ADD'
            node.parent = self.grp.nodes["Frame.003"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 10.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 264.0
            node.location[1] = -1350.0
            node.mute = False
            node.name = 'Math.014'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 10.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 262.0
            node.location[1] = -1287.0
            node.mute = False
            node.name = 'Math.011'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.4000000059604645
            node.inputs['Value'].default_value = 1.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 62.0
            node.location[1] = -1258.0
            node.mute = False
            node.name = 'Math.010'
            node.operation = 'COSINE'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 10.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 259.0
            node.location[1] = -1208.0
            node.mute = False
            node.name = 'Math.013'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 10.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 265.0
            node.location[1] = -1113.0
            node.mute = False
            node.name = 'Math.009'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 10.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 478.0
            node.location[1] = -1191.0
            node.mute = False
            node.name = 'Math.012'
            node.operation = 'SUBTRACT'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 10.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 471.0
            node.location[1] = -1309.0
            node.mute = False
            node.name = 'Math.015'
            node.operation = 'ADD'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 1.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 7.0
            node.location[1] = -1085.0
            node.mute = False
            node.name = 'Math'
            node.operation = 'MODULO'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 1.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 27.0
            node.location[1] = -1342.0
            node.mute = False
            node.name = 'Math.005'
            node.operation = 'MODULO'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.4000000059604645
            node.inputs['Value'].default_value = 1.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 61.0
            node.location[1] = -1184.0
            node.mute = False
            node.name = 'Math.008'
            node.operation = 'SINE'
            node.parent = self.grp.nodes["Frame.001"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 147.0
            node.location[1] = 803.0
            node.mute = False
            node.name = 'Reroute.009'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 150.0
            node.location[1] = 544.0
            node.mute = False
            node.name = 'Reroute.007'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -69.0
            node.location[1] = 481.0
            node.mute = False
            node.name = 'Reroute.006'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1358.0
            node.location[1] = -1283.0
            node.mute = False
            node.name = 'Reroute.022'
            node.parent = self.grp.nodes["Frame.003"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 1667.0
            node.location[1] = 195.0
            node.mute = False
            node.name = 'Reroute.031'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 1641.0
            node.location[1] = 222.0
            node.mute = False
            node.name = 'Reroute.033'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 109.0
            node.location[1] = 777.0
            node.mute = False
            node.name = 'Reroute.036'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 2330.0
            node.location[1] = 149.0
            node.mute = False
            node.name = 'Reroute.040'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1571.0
            node.location[1] = -1203.0
            node.mute = False
            node.name = 'Reroute.032'
            node.parent = self.grp.nodes["Frame.006"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1541.0
            node.location[1] = -1372.0
            node.mute = False
            node.name = 'Reroute.030'
            node.parent = self.grp.nodes["Frame.006"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

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
            node.location[0] = -1246.0
            node.location[1] = -1092.0
            node.mute = False
            node.name = 'Combine XYZ.005'
            node.parent = self.grp.nodes["Frame.006"]
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
            node.location[0] = -1508.0
            node.location[1] = -1237.0
            node.mute = False
            node.name = 'Math.021'
            node.operation = 'ADD'
            node.parent = self.grp.nodes["Frame.006"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
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
            node.location[0] = -1500.0
            node.location[1] = -1068.0
            node.mute = False
            node.name = 'Math.019'
            node.operation = 'ADD'
            node.parent = self.grp.nodes["Frame.006"]
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
            node.location[0] = -1741.0
            node.location[1] = -1123.0
            node.mute = False
            node.name = 'Separate XYZ.001'
            node.parent = self.grp.nodes["Frame.006"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexChecker')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Color1'].default_value = (0.0,0.0,0.0,1.0)
            node.inputs['Color2'].default_value = (1.0,1.0,1.0,1.0)
            node.inputs['Scale'].default_value = 1.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -4083.0
            node.location[1] = -217.0
            node.mute = False
            node.name = 'Checker Texture.001'
            node.parent = self.grp.nodes["Frame.004"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexChecker')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['Color1'].default_value = (0.010022825561463833,0.010022825561463833,0.010022825561463833,1.0)
            node.inputs['Color2'].default_value = (0.7874122262001038,0.7874122262001038,0.7874122262001038,1.0)
            node.inputs['Scale'].default_value = 4.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -4086.0
            node.location[1] = -389.0
            node.mute = False
            node.name = 'Checker Texture.002'
            node.parent = self.grp.nodes["Frame.004"]
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
            node.blend_type = 'DIFFERENCE'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -3837.0
            node.location[1] = -256.0
            node.mute = False
            node.name = 'Mix.001'
            node.parent = self.grp.nodes["Frame.004"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_alpha = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -4118.0
            node.location[1] = -374.0
            node.mute = False
            node.name = 'Reroute.041'
            node.parent = self.grp.nodes["Frame.004"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1539.0
            node.location[1] = 589.0
            node.mute = False
            node.name = 'Reroute.004'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1283.0
            node.location[1] = 588.0
            node.mute = False
            node.name = 'Reroute.012'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1329.0
            node.location[1] = 563.0
            node.mute = False
            node.name = 'Reroute.026'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1358.0
            node.location[1] = 533.0
            node.mute = False
            node.name = 'Reroute.028'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1328.0
            node.location[1] = 232.0
            node.mute = False
            node.name = 'Reroute.027'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1353.0
            node.location[1] = 207.0
            node.mute = False
            node.name = 'Reroute.029'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1290.0
            node.location[1] = 813.0
            node.mute = False
            node.name = 'Reroute.034'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1285.0
            node.location[1] = 776.0
            node.mute = False
            node.name = 'Reroute.035'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1380.0
            node.location[1] = 514.0
            node.mute = False
            node.name = 'Reroute.037'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1375.0
            node.location[1] = 175.0
            node.mute = False
            node.name = 'Reroute.038'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 1063.0
            node.location[1] = 244.0
            node.mute = False
            node.name = 'Reroute.023'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 152.0
            node.location[1] = 272.0
            node.mute = False
            node.name = 'Reroute.010'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -69.0
            node.location[1] = 277.0
            node.mute = False
            node.name = 'Reroute.014'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -57.0
            node.location[1] = 251.0
            node.mute = False
            node.name = 'Reroute.008'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1284.0
            node.location[1] = 283.0
            node.mute = False
            node.name = 'Reroute.011'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1307.0
            node.location[1] = 250.0
            node.mute = False
            node.name = 'Reroute.024'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1255.0
            node.location[1] = 609.0
            node.mute = False
            node.name = 'Reroute.043'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1306.0
            node.location[1] = 493.0
            node.mute = False
            node.name = 'Reroute.025'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 2067.0
            node.location[1] = -1295.0
            node.mute = False
            node.name = 'Reroute.003'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1397.0
            node.location[1] = 474.0
            node.mute = False
            node.name = 'Reroute.047'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 2066.0
            node.location[1] = -1333.0
            node.mute = False
            node.name = 'Reroute.005'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1392.0
            node.location[1] = 149.0
            node.mute = False
            node.name = 'Reroute.048'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.49999991059303284
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = -112.0
            node.location[1] = -858.0
            node.mute = False
            node.name = 'Math.004'
            node.operation = 'SUBTRACT'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.49999991059303284
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = -110.0
            node.location[1] = -793.0
            node.mute = False
            node.name = 'Math.003'
            node.operation = 'SUBTRACT'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 1008.0
            node.location[1] = -933.0
            node.mute = False
            node.name = 'Reroute.019'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 1109.0
            node.location[1] = -782.0
            node.mute = False
            node.name = 'Reroute.016'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 1020.0
            node.location[1] = -903.0
            node.mute = False
            node.name = 'Reroute.013'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 14.19999885559082
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 1144.0
            node.location[1] = -779.0
            node.mute = False
            node.name = 'Math.016'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame.002"]
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
            node.inputs['Scale'].default_value = 9.399999618530273
            node.inputs['Detail'].default_value = 5.0
            node.inputs['Dimension'].default_value = 4.0
            node.inputs['Lacunarity'].default_value = 2.5
            node.inputs['Offset'].default_value = 0.9999999403953552
            node.inputs['Gain'].default_value = 1.0
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 822.0
            node.location[1] = -792.0
            node.musgrave_dimensions = '3D'
            node.musgrave_type = 'HETERO_TERRAIN'
            node.mute = False
            node.name = 'Musgrave Texture.002'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 150.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexMusgrave')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 9.399999618530273
            node.inputs['Detail'].default_value = 5.0
            node.inputs['Dimension'].default_value = 4.0
            node.inputs['Lacunarity'].default_value = 2.5
            node.inputs['Offset'].default_value = 0.9999999403953552
            node.inputs['Gain'].default_value = 1.0
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 914.0
            node.location[1] = -866.0
            node.musgrave_dimensions = '3D'
            node.musgrave_type = 'HETERO_TERRAIN'
            node.mute = False
            node.name = 'Musgrave Texture'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 150.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 10.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 1059.0
            node.location[1] = -935.0
            node.mute = False
            node.name = 'Math.007'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 10.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 1060.0
            node.location[1] = -885.0
            node.mute = False
            node.name = 'Math.006'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame.002"]
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
            node.inputs['Scale'].default_value = 9.399999618530273
            node.inputs['Detail'].default_value = 5.0
            node.inputs['Dimension'].default_value = 4.0
            node.inputs['Lacunarity'].default_value = 2.5
            node.inputs['Offset'].default_value = 1.0
            node.inputs['Gain'].default_value = 1.0
            node.outputs['Fac'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 821.0
            node.location[1] = -960.0
            node.musgrave_dimensions = '3D'
            node.musgrave_type = 'HETERO_TERRAIN'
            node.mute = False
            node.name = 'Musgrave Texture.001'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 150.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeCombineXYZ')
            node.inputs['X'].default_value = 0.0
            node.inputs['Y'].default_value = 0.30000001192092896
            node.inputs['Z'].default_value = 16.399999618530273
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 635.0
            node.location[1] = -958.0
            node.mute = False
            node.name = 'Combine XYZ.002'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeCombineXYZ')
            node.inputs['X'].default_value = 0.0
            node.inputs['Y'].default_value = 0.0
            node.inputs['Z'].default_value = 8.09999942779541
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 641.0
            node.location[1] = -775.0
            node.mute = False
            node.name = 'Combine XYZ.003'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeCombineXYZ')
            node.inputs['X'].default_value = 0.0
            node.inputs['Y'].default_value = 0.0
            node.inputs['Z'].default_value = 0.19999998807907104
            node.outputs['Vector'].default_value = (0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 728.0
            node.location[1] = -859.0
            node.mute = False
            node.name = 'Combine XYZ'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 1035.0
            node.location[1] = -796.0
            node.mute = False
            node.name = 'Reroute.015'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 1109.0
            node.location[1] = -889.0
            node.mute = False
            node.name = 'Reroute.017'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 1008.0
            node.location[1] = -816.0
            node.mute = False
            node.name = 'Reroute.018'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 1045.0
            node.location[1] = -887.0
            node.mute = False
            node.name = 'Reroute.021'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 1045.0
            node.location[1] = -983.0
            node.mute = False
            node.name = 'Reroute.020'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1255.0
            node.location[1] = 514.0
            node.mute = False
            node.name = 'Reroute.042'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1283.0
            node.location[1] = 505.0
            node.mute = False
            node.name = 'Reroute.044'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1754.0
            node.location[1] = 781.0
            node.mute = False
            node.name = 'Reroute'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1756.0
            node.location[1] = 607.0
            node.mute = False
            node.name = 'Reroute.001'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -1714.0
            node.location[1] = 585.0
            node.mute = False
            node.name = 'Reroute.002'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 112.0
            node.location[1] = -859.0
            node.mute = False
            node.name = 'Reroute.051'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 112.0
            node.location[1] = -776.0
            node.mute = False
            node.name = 'Reroute.050'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 186.0
            node.location[1] = -799.0
            node.mute = False
            node.name = 'Reroute.046'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 185.0
            node.location[1] = -938.0
            node.mute = False
            node.name = 'Reroute.045'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 185.0
            node.location[1] = -881.0
            node.mute = False
            node.name = 'Reroute.052'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 0.0
            node.inputs['Color1'].default_value = (0.5,0.5,0.5,1.0)
            node.inputs['Color2'].default_value = (0.5,0.5,0.5,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'DIFFERENCE'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 152.0
            node.location[1] = -860.0
            node.mute = False
            node.name = 'Mix.003'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_alpha = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMixRGB')
            node.inputs['Fac'].default_value = 0.0
            node.inputs['Color1'].default_value = (0.5,0.5,0.5,1.0)
            node.inputs['Color2'].default_value = (0.5,0.5,0.5,1.0)
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.blend_type = 'DIFFERENCE'
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 244.0
            node.location[1] = -777.0
            node.mute = False
            node.name = 'Mix.002'
            node.parent = self.grp.nodes["Frame.002"]
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
            node.inputs['Value'].default_value = 1.2999999523162842
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 327.0
            node.location[1] = -863.0
            node.mute = False
            node.name = 'Math.002'
            node.operation = 'ROUND'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 1.2999999523162842
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 415.0
            node.location[1] = -779.0
            node.mute = False
            node.name = 'Math.001'
            node.operation = 'ROUND'
            node.parent = self.grp.nodes["Frame.002"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -976.0
            node.location[1] = 148.0
            node.mute = False
            node.name = 'Reroute.049'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeTexNoise')
            node.inputs['Vector'].default_value = (0.0,0.0,0.0)
            node.inputs['W'].default_value = 0.0
            node.inputs['Scale'].default_value = 5.0
            node.inputs['Detail'].default_value = 2.0
            node.inputs['Distortion'].default_value = 0.0
            node.outputs['Fac'].default_value = 0.0
            node.outputs['Color'].default_value = (0.0,0.0,0.0,0.0)
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = -98.0
            node.location[1] = -922.0
            node.mute = False
            node.name = 'Noise Texture'
            node.noise_dimensions = '3D'
            node.parent = self.grp.nodes["Frame.002"]
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
            node.hide = True
            node.label = ''
            node.location[0] = 1897.0
            node.location[1] = -1237.0
            node.mute = False
            node.name = 'Separate XYZ'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 10.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 2097.0
            node.location[1] = -1277.0
            node.mute = False
            node.name = 'Math.017'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 10.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = 2100.0
            node.location[1] = -1316.0
            node.mute = False
            node.name = 'Math.018'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 2791.0
            node.location[1] = 577.0
            node.mute = False
            node.name = 'Reroute.053'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = 2635.0
            node.location[1] = 528.0
            node.mute = False
            node.name = 'Reroute.054'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 0.5
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = -2602.0
            node.location[1] = -1386.0
            node.mute = False
            node.name = 'Math.029'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame.005"]
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
            node.location[0] = -3359.0
            node.location[1] = -1234.0
            node.mute = False
            node.name = 'Separate XYZ.002'
            node.parent = self.grp.nodes["Frame.005"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeReroute')
            node.inputs['Input'].default_value = 0.0
            node.outputs['Output'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -3207.0
            node.location[1] = -1367.0
            node.mute = False
            node.name = 'Reroute.039'
            node.parent = self.grp.nodes["Frame.005"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 16.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 3.1410000324249268
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = -3166.0
            node.location[1] = -1363.0
            node.mute = False
            node.name = 'Math.022'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame.005"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 180.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = -2995.0
            node.location[1] = -1367.0
            node.mute = False
            node.name = 'Math.023'
            node.operation = 'DIVIDE'
            node.parent = self.grp.nodes["Frame.005"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 1.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = -2817.0
            node.location[1] = -1377.0
            node.mute = False
            node.name = 'Math.025'
            node.operation = 'COSINE'
            node.parent = self.grp.nodes["Frame.005"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 1.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = True
            node.label = ''
            node.location[0] = -2817.0
            node.location[1] = -1332.0
            node.mute = False
            node.name = 'Math.024'
            node.operation = 'SINE'
            node.parent = self.grp.nodes["Frame.005"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
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
            node.hide = True
            node.label = ''
            node.location[0] = -2607.0
            node.location[1] = -1487.0
            node.mute = False
            node.name = 'Math.030'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame.005"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
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
            node.hide = True
            node.label = ''
            node.location[0] = -2443.0
            node.location[1] = -1437.0
            node.mute = False
            node.name = 'Math.031'
            node.operation = 'ADD'
            node.parent = self.grp.nodes["Frame.005"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
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
            node.hide = True
            node.label = ''
            node.location[0] = -2611.0
            node.location[1] = -1313.0
            node.mute = False
            node.name = 'Math.027'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame.005"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
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
            node.hide = True
            node.label = ''
            node.location[0] = -2615.0
            node.location[1] = -1235.0
            node.mute = False
            node.name = 'Math.026'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame.005"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
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
            node.hide = True
            node.label = ''
            node.location[0] = -2451.0
            node.location[1] = -1277.0
            node.mute = False
            node.name = 'Math.028'
            node.operation = 'SUBTRACT'
            node.parent = self.grp.nodes["Frame.005"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

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
            node.location[0] = -2251.0
            node.location[1] = -1244.0
            node.mute = False
            node.name = 'Combine XYZ.006'
            node.parent = self.grp.nodes["Frame.005"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupOutput')
            self.grp.outputs.new('NodeSocketVector', 'UV')
            self.grp.outputs.new('NodeSocketFloat', 'GridView')
            node.inputs['UV'].default_value = (0.0,0.0,0.0)
            node.inputs['GridView'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.is_active_output = True
            node.label = ''
            node.location[0] = 4444.0
            node.location[1] = 580.0
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
            node.location[0] = -4125.0
            node.location[1] = -1010.0
            node.mute = False
            node.name = 'Separate XYZ.003'
            node.parent = self.grp.nodes["Frame.008"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('ShaderNodeMath')
            node.inputs['Value'].default_value = 0.5
            node.inputs['Value'].default_value = 1.0
            node.outputs['Value'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -3871.0
            node.location[1] = -878.0
            node.mute = False
            node.name = 'Math.020'
            node.operation = 'MULTIPLY'
            node.parent = self.grp.nodes["Frame.008"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_clamp = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

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
            node.location[0] = -3636.0
            node.location[1] = -986.0
            node.mute = False
            node.name = 'Combine XYZ.007'
            node.parent = self.grp.nodes["Frame.008"]
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            node = self.grp.nodes.new('NodeGroupInput')
            self.grp.inputs.new('NodeSocketVector', 'UV')
            self.grp.inputs['UV'].default_value = (0.0,0.0,0.0)
            self.grp.inputs['UV'].min_value = -3.4028234663852886e+38
            self.grp.inputs['UV'].max_value = 3.4028234663852886e+38
            self.grp.inputs.new('NodeSocketFloat', 'Scale')
            self.grp.inputs['Scale'].default_value = 1.0
            self.grp.inputs['Scale'].min_value = 0.0
            self.grp.inputs['Scale'].max_value = 3.4028234663852886e+38
            self.grp.inputs.new('NodeSocketFloat', 'Aspect Ratio')
            self.grp.inputs['Aspect Ratio'].default_value = 1.0
            self.grp.inputs['Aspect Ratio'].min_value = 0.0
            self.grp.inputs['Aspect Ratio'].max_value = 3.4028234663852886e+38
            self.grp.inputs.new('NodeSocketFloat', 'Translate X')
            self.grp.inputs['Translate X'].default_value = 0.0
            self.grp.inputs['Translate X'].min_value = -3.4028234663852886e+38
            self.grp.inputs['Translate X'].max_value = 3.4028234663852886e+38
            self.grp.inputs.new('NodeSocketFloat', 'Translate Y')
            self.grp.inputs['Translate Y'].default_value = 0.0
            self.grp.inputs['Translate Y'].min_value = -3.4028234663852886e+38
            self.grp.inputs['Translate Y'].max_value = 3.4028234663852886e+38
            self.grp.inputs.new('NodeSocketFloat', 'Global Rotation')
            self.grp.inputs['Global Rotation'].default_value = 0.0
            self.grp.inputs['Global Rotation'].min_value = -3.4028234663852886e+38
            self.grp.inputs['Global Rotation'].max_value = 3.4028234663852886e+38
            self.grp.inputs.new('NodeSocketFloat', 'Mosaic Rotation')
            self.grp.inputs['Mosaic Rotation'].default_value = 0.0
            self.grp.inputs['Mosaic Rotation'].min_value = -3.4028234663852886e+38
            self.grp.inputs['Mosaic Rotation'].max_value = 3.4028234663852886e+38
            self.grp.inputs.new('NodeSocketFloat', 'Mosaic Noise')
            self.grp.inputs['Mosaic Noise'].default_value = 0.0
            self.grp.inputs['Mosaic Noise'].min_value = 0.0
            self.grp.inputs['Mosaic Noise'].max_value = 1.0
            node.outputs['UV'].default_value = (0.0,0.0,0.0)
            node.outputs['Scale'].default_value = 0.0
            node.outputs['Aspect Ratio'].default_value = 0.0
            node.outputs['Translate X'].default_value = 0.0
            node.outputs['Translate Y'].default_value = 0.0
            node.outputs['Global Rotation'].default_value = 0.0
            node.outputs['Mosaic Rotation'].default_value = 0.0
            node.outputs['Mosaic Noise'].default_value = 0.0
            node.color[0] = 0.6079999804496765
            node.color[1] = 0.6079999804496765
            node.color[2] = 0.6079999804496765
            node.hide = False
            node.label = ''
            node.location[0] = -2148.0
            node.location[1] = 639.0
            node.mute = False
            node.name = 'Group Input'
            node.show_options = True
            node.show_preview = False
            node.show_texture = False
            node.use_custom_color = False
            node.width = 140.0
            node.width_hidden = 42.0

            links = self.grp.links
            links.new(self.grp.nodes["Separate XYZ"].outputs[0], self.grp.nodes["Math.017"].inputs[0])
            links.new(self.grp.nodes["Separate XYZ"].outputs[1], self.grp.nodes["Math.018"].inputs[0])
            links.new(self.grp.nodes["Combine XYZ.001"].outputs[0], self.grp.nodes["Vector Math"].inputs[0])
            links.new(self.grp.nodes["Math.006"].outputs[0], self.grp.nodes["Combine XYZ.004"].inputs[0])
            links.new(self.grp.nodes["Math.007"].outputs[0], self.grp.nodes["Combine XYZ.004"].inputs[1])
            links.new(self.grp.nodes["Reroute"].outputs[0], self.grp.nodes["Separate XYZ"].inputs[0])
            links.new(self.grp.nodes["Reroute.013"].outputs[0], self.grp.nodes["Math.006"].inputs[1])
            links.new(self.grp.nodes["Reroute.015"].outputs[0], self.grp.nodes["Math.016"].inputs[1])
            links.new(self.grp.nodes["Math.001"].outputs[0], self.grp.nodes["Combine XYZ"].inputs[0])
            links.new(self.grp.nodes["Math.002"].outputs[0], self.grp.nodes["Combine XYZ"].inputs[1])
            links.new(self.grp.nodes["Math.003"].outputs[0], self.grp.nodes["Mix.002"].inputs[1])
            links.new(self.grp.nodes["Math.001"].outputs[0], self.grp.nodes["Combine XYZ.002"].inputs[0])
            links.new(self.grp.nodes["Math.002"].outputs[0], self.grp.nodes["Combine XYZ.002"].inputs[1])
            links.new(self.grp.nodes["Combine XYZ.002"].outputs[0], self.grp.nodes["Musgrave Texture.001"].inputs[0])
            links.new(self.grp.nodes["Math.001"].outputs[0], self.grp.nodes["Combine XYZ.003"].inputs[0])
            links.new(self.grp.nodes["Math.002"].outputs[0], self.grp.nodes["Combine XYZ.003"].inputs[1])
            links.new(self.grp.nodes["Combine XYZ"].outputs[0], self.grp.nodes["Musgrave Texture"].inputs[0])
            links.new(self.grp.nodes["Combine XYZ.003"].outputs[0], self.grp.nodes["Musgrave Texture.002"].inputs[0])
            links.new(self.grp.nodes["Math.017"].outputs[0], self.grp.nodes["Math.003"].inputs[0])
            links.new(self.grp.nodes["Math.018"].outputs[0], self.grp.nodes["Math.004"].inputs[0])
            links.new(self.grp.nodes["Reroute.016"].outputs[0], self.grp.nodes["Math.016"].inputs[0])
            links.new(self.grp.nodes["Reroute.021"].outputs[0], self.grp.nodes["Math.006"].inputs[0])
            links.new(self.grp.nodes["Reroute.019"].outputs[0], self.grp.nodes["Math.007"].inputs[0])
            links.new(self.grp.nodes["Math"].outputs[0], self.grp.nodes["Math.009"].inputs[0])
            links.new(self.grp.nodes["Math.008"].outputs[0], self.grp.nodes["Math.009"].inputs[1])
            links.new(self.grp.nodes["Math.010"].outputs[0], self.grp.nodes["Math.011"].inputs[0])
            links.new(self.grp.nodes["Math.005"].outputs[0], self.grp.nodes["Math.011"].inputs[1])
            links.new(self.grp.nodes["Math"].outputs[0], self.grp.nodes["Math.013"].inputs[0])
            links.new(self.grp.nodes["Math.010"].outputs[0], self.grp.nodes["Math.013"].inputs[1])
            links.new(self.grp.nodes["Math.008"].outputs[0], self.grp.nodes["Math.014"].inputs[0])
            links.new(self.grp.nodes["Math.005"].outputs[0], self.grp.nodes["Math.014"].inputs[1])
            links.new(self.grp.nodes["Math.013"].outputs[0], self.grp.nodes["Math.012"].inputs[0])
            links.new(self.grp.nodes["Math.014"].outputs[0], self.grp.nodes["Math.012"].inputs[1])
            links.new(self.grp.nodes["Math.009"].outputs[0], self.grp.nodes["Math.015"].inputs[0])
            links.new(self.grp.nodes["Math.011"].outputs[0], self.grp.nodes["Math.015"].inputs[1])
            links.new(self.grp.nodes["Math.016"].outputs[0], self.grp.nodes["Math.008"].inputs[0])
            links.new(self.grp.nodes["Reroute.034"].outputs[0], self.grp.nodes["Math"].inputs[0])
            links.new(self.grp.nodes["Reroute.036"].outputs[0], self.grp.nodes["Math.005"].inputs[0])
            links.new(self.grp.nodes["Math.016"].outputs[0], self.grp.nodes["Math.010"].inputs[0])
            links.new(self.grp.nodes["Math.012"].outputs[0], self.grp.nodes["Combine XYZ.001"].inputs[0])
            links.new(self.grp.nodes["Math.015"].outputs[0], self.grp.nodes["Combine XYZ.001"].inputs[1])
            links.new(self.grp.nodes["Combine XYZ.004"].outputs[0], self.grp.nodes["Mix"].inputs[1])
            links.new(self.grp.nodes["Mix"].outputs[0], self.grp.nodes["Vector Math"].inputs[1])
            links.new(self.grp.nodes["Reroute.022"].outputs[0], self.grp.nodes["Mix"].inputs[2])
            links.new(self.grp.nodes["Reroute.009"].outputs[0], self.grp.nodes["Math"].inputs[1])
            links.new(self.grp.nodes["Vector Math"].outputs[0], self.grp.nodes["Separate XYZ.001"].inputs[0])
            links.new(self.grp.nodes["Separate XYZ.001"].outputs[0], self.grp.nodes["Math.019"].inputs[0])
            links.new(self.grp.nodes["Separate XYZ.001"].outputs[1], self.grp.nodes["Math.021"].inputs[0])
            links.new(self.grp.nodes["Math.019"].outputs[0], self.grp.nodes["Combine XYZ.005"].inputs[0])
            links.new(self.grp.nodes["Math.021"].outputs[0], self.grp.nodes["Combine XYZ.005"].inputs[1])
            links.new(self.grp.nodes["Reroute.032"].outputs[0], self.grp.nodes["Math.019"].inputs[1])
            links.new(self.grp.nodes["Reroute.030"].outputs[0], self.grp.nodes["Math.021"].inputs[1])
            links.new(self.grp.nodes["Math.022"].outputs[0], self.grp.nodes["Math.023"].inputs[0])
            links.new(self.grp.nodes["Math.023"].outputs[0], self.grp.nodes["Math.024"].inputs[0])
            links.new(self.grp.nodes["Math.023"].outputs[0], self.grp.nodes["Math.025"].inputs[0])
            links.new(self.grp.nodes["Reroute.053"].outputs[0], self.grp.nodes["Math.026"].inputs[0])
            links.new(self.grp.nodes["Math.025"].outputs[0], self.grp.nodes["Math.026"].inputs[1])
            links.new(self.grp.nodes["Reroute.054"].outputs[0], self.grp.nodes["Math.027"].inputs[0])
            links.new(self.grp.nodes["Math.024"].outputs[0], self.grp.nodes["Math.027"].inputs[1])
            links.new(self.grp.nodes["Math.026"].outputs[0], self.grp.nodes["Math.028"].inputs[0])
            links.new(self.grp.nodes["Math.027"].outputs[0], self.grp.nodes["Math.028"].inputs[1])
            links.new(self.grp.nodes["Math.028"].outputs[0], self.grp.nodes["Combine XYZ.006"].inputs[0])
            links.new(self.grp.nodes["Math.024"].outputs[0], self.grp.nodes["Math.029"].inputs[1])
            links.new(self.grp.nodes["Math.025"].outputs[0], self.grp.nodes["Math.030"].inputs[1])
            links.new(self.grp.nodes["Math.029"].outputs[0], self.grp.nodes["Math.031"].inputs[0])
            links.new(self.grp.nodes["Math.030"].outputs[0], self.grp.nodes["Math.031"].inputs[1])
            links.new(self.grp.nodes["Combine XYZ.005"].outputs[0], self.grp.nodes["Separate XYZ.002"].inputs[0])
            links.new(self.grp.nodes["Reroute.041"].outputs[0], self.grp.nodes["Checker Texture.001"].inputs[0])
            links.new(self.grp.nodes["Reroute.039"].outputs[0], self.grp.nodes["Math.022"].inputs[0])
            links.new(self.grp.nodes["Reroute.001"].outputs[0], self.grp.nodes["Reroute"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[0], self.grp.nodes["Reroute.001"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[1], self.grp.nodes["Reroute.002"].inputs[0])
            links.new(self.grp.nodes["Reroute.002"].outputs[0], self.grp.nodes["Reroute.004"].inputs[0])
            links.new(self.grp.nodes["Reroute.003"].outputs[0], self.grp.nodes["Math.017"].inputs[1])
            links.new(self.grp.nodes["Reroute.005"].outputs[0], self.grp.nodes["Reroute.003"].inputs[0])
            links.new(self.grp.nodes["Reroute.004"].outputs[0], self.grp.nodes["Reroute.005"].inputs[0])
            links.new(self.grp.nodes["Reroute.014"].outputs[0], self.grp.nodes["Reroute.010"].inputs[0])
            links.new(self.grp.nodes["Reroute.044"].outputs[0], self.grp.nodes["Reroute.011"].inputs[0])
            links.new(self.grp.nodes["Reroute.004"].outputs[0], self.grp.nodes["Reroute.012"].inputs[0])
            links.new(self.grp.nodes["Reroute.011"].outputs[0], self.grp.nodes["Reroute.014"].inputs[0])
            links.new(self.grp.nodes["Reroute.006"].outputs[0], self.grp.nodes["Reroute.013"].inputs[0])
            links.new(self.grp.nodes["Reroute.007"].outputs[0], self.grp.nodes["Reroute.009"].inputs[0])
            links.new(self.grp.nodes["Reroute.014"].outputs[0], self.grp.nodes["Reroute.006"].inputs[0])
            links.new(self.grp.nodes["Reroute.006"].outputs[0], self.grp.nodes["Math.007"].inputs[1])
            links.new(self.grp.nodes["Reroute.010"].outputs[0], self.grp.nodes["Reroute.007"].inputs[0])
            links.new(self.grp.nodes["Reroute.007"].outputs[0], self.grp.nodes["Math.005"].inputs[1])
            links.new(self.grp.nodes["Reroute.024"].outputs[0], self.grp.nodes["Reroute.008"].inputs[0])
            links.new(self.grp.nodes["Reroute.008"].outputs[0], self.grp.nodes["Reroute.015"].inputs[0])
            links.new(self.grp.nodes["Reroute.017"].outputs[0], self.grp.nodes["Reroute.016"].inputs[0])
            links.new(self.grp.nodes["Musgrave Texture"].outputs[0], self.grp.nodes["Reroute.017"].inputs[0])
            links.new(self.grp.nodes["Musgrave Texture.002"].outputs[0], self.grp.nodes["Reroute.018"].inputs[0])
            links.new(self.grp.nodes["Reroute.018"].outputs[0], self.grp.nodes["Reroute.019"].inputs[0])
            links.new(self.grp.nodes["Musgrave Texture.001"].outputs[0], self.grp.nodes["Reroute.020"].inputs[0])
            links.new(self.grp.nodes["Reroute.020"].outputs[0], self.grp.nodes["Reroute.021"].inputs[0])
            links.new(self.grp.nodes["Reroute.023"].outputs[0], self.grp.nodes["Reroute.022"].inputs[0])
            links.new(self.grp.nodes["Reroute.008"].outputs[0], self.grp.nodes["Reroute.023"].inputs[0])
            links.new(self.grp.nodes["Reroute.025"].outputs[0], self.grp.nodes["Reroute.024"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[6], self.grp.nodes["Reroute.025"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[3], self.grp.nodes["Reroute.026"].inputs[0])
            links.new(self.grp.nodes["Reroute.026"].outputs[0], self.grp.nodes["Reroute.027"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[4], self.grp.nodes["Reroute.028"].inputs[0])
            links.new(self.grp.nodes["Reroute.028"].outputs[0], self.grp.nodes["Reroute.029"].inputs[0])
            links.new(self.grp.nodes["Reroute.031"].outputs[0], self.grp.nodes["Reroute.030"].inputs[0])
            links.new(self.grp.nodes["Reroute.029"].outputs[0], self.grp.nodes["Reroute.031"].inputs[0])
            links.new(self.grp.nodes["Reroute.033"].outputs[0], self.grp.nodes["Reroute.032"].inputs[0])
            links.new(self.grp.nodes["Reroute.027"].outputs[0], self.grp.nodes["Reroute.033"].inputs[0])
            links.new(self.grp.nodes["Math.017"].outputs[0], self.grp.nodes["Reroute.034"].inputs[0])
            links.new(self.grp.nodes["Math.018"].outputs[0], self.grp.nodes["Reroute.035"].inputs[0])
            links.new(self.grp.nodes["Reroute.035"].outputs[0], self.grp.nodes["Reroute.036"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[5], self.grp.nodes["Reroute.037"].inputs[0])
            links.new(self.grp.nodes["Reroute.037"].outputs[0], self.grp.nodes["Reroute.038"].inputs[0])
            links.new(self.grp.nodes["Reroute.040"].outputs[0], self.grp.nodes["Reroute.039"].inputs[0])
            links.new(self.grp.nodes["Reroute.038"].outputs[0], self.grp.nodes["Reroute.040"].inputs[0])
            links.new(self.grp.nodes["Reroute.041"].outputs[0], self.grp.nodes["Checker Texture.002"].inputs[0])
            links.new(self.grp.nodes["Checker Texture.001"].outputs[0], self.grp.nodes["Mix.001"].inputs[1])
            links.new(self.grp.nodes["Checker Texture.002"].outputs[0], self.grp.nodes["Mix.001"].inputs[2])
            links.new(self.grp.nodes["Mix.001"].outputs[0], self.grp.nodes["Group Output"].inputs[1])
            links.new(self.grp.nodes["Combine XYZ.006"].outputs[0], self.grp.nodes["Reroute.041"].inputs[0])
            links.new(self.grp.nodes["Math.004"].outputs[0], self.grp.nodes["Mix.003"].inputs[1])
            links.new(self.grp.nodes["Reroute.042"].outputs[0], self.grp.nodes["Noise Texture"].inputs[0])
            links.new(self.grp.nodes["Reroute.043"].outputs[0], self.grp.nodes["Reroute.042"].inputs[0])
            links.new(self.grp.nodes["Reroute.001"].outputs[0], self.grp.nodes["Reroute.043"].inputs[0])
            links.new(self.grp.nodes["Mix.002"].outputs[0], self.grp.nodes["Math.001"].inputs[0])
            links.new(self.grp.nodes["Mix.003"].outputs[0], self.grp.nodes["Math.002"].inputs[0])
            links.new(self.grp.nodes["Reroute.012"].outputs[0], self.grp.nodes["Reroute.044"].inputs[0])
            links.new(self.grp.nodes["Noise Texture"].outputs[0], self.grp.nodes["Reroute.045"].inputs[0])
            links.new(self.grp.nodes["Reroute.052"].outputs[0], self.grp.nodes["Reroute.046"].inputs[0])
            links.new(self.grp.nodes["Reroute.046"].outputs[0], self.grp.nodes["Mix.002"].inputs[2])
            links.new(self.grp.nodes["Reroute.005"].outputs[0], self.grp.nodes["Math.018"].inputs[1])
            links.new(self.grp.nodes["Reroute.050"].outputs[0], self.grp.nodes["Mix.002"].inputs[0])
            links.new(self.grp.nodes["Group Input"].outputs[7], self.grp.nodes["Reroute.047"].inputs[0])
            links.new(self.grp.nodes["Reroute.047"].outputs[0], self.grp.nodes["Reroute.048"].inputs[0])
            links.new(self.grp.nodes["Reroute.048"].outputs[0], self.grp.nodes["Reroute.049"].inputs[0])
            links.new(self.grp.nodes["Reroute.051"].outputs[0], self.grp.nodes["Reroute.050"].inputs[0])
            links.new(self.grp.nodes["Reroute.049"].outputs[0], self.grp.nodes["Reroute.051"].inputs[0])
            links.new(self.grp.nodes["Reroute.051"].outputs[0], self.grp.nodes["Mix.003"].inputs[0])
            links.new(self.grp.nodes["Reroute.045"].outputs[0], self.grp.nodes["Reroute.052"].inputs[0])
            links.new(self.grp.nodes["Reroute.052"].outputs[0], self.grp.nodes["Mix.003"].inputs[2])
            links.new(self.grp.nodes["Reroute.044"].outputs[0], self.grp.nodes["Noise Texture"].inputs[2])
            links.new(self.grp.nodes["Reroute.053"].outputs[0], self.grp.nodes["Math.029"].inputs[0])
            links.new(self.grp.nodes["Separate XYZ.002"].outputs[0], self.grp.nodes["Reroute.053"].inputs[0])
            links.new(self.grp.nodes["Reroute.054"].outputs[0], self.grp.nodes["Math.030"].inputs[0])
            links.new(self.grp.nodes["Separate XYZ.002"].outputs[1], self.grp.nodes["Reroute.054"].inputs[0])
            links.new(self.grp.nodes["Math.031"].outputs[0], self.grp.nodes["Combine XYZ.006"].inputs[1])
            links.new(self.grp.nodes["Combine XYZ.006"].outputs[0], self.grp.nodes["Separate XYZ.003"].inputs[0])
            links.new(self.grp.nodes["Separate XYZ.003"].outputs[0], self.grp.nodes["Combine XYZ.007"].inputs[0])
            links.new(self.grp.nodes["Separate XYZ.003"].outputs[1], self.grp.nodes["Math.020"].inputs[0])
            links.new(self.grp.nodes["Separate XYZ.003"].outputs[2], self.grp.nodes["Combine XYZ.007"].inputs[2])
            links.new(self.grp.nodes["Combine XYZ.007"].outputs[0], self.grp.nodes["Group Output"].inputs[0])
            links.new(self.grp.nodes["Math.020"].outputs[0], self.grp.nodes["Combine XYZ.007"].inputs[1])
            links.new(self.grp.nodes["Group Input"].outputs[2], self.grp.nodes["Math.020"].inputs[1])#grpNodeContent#

        self.node_tree = bpy.data.node_groups["Uber Mapping"]
        self.nodes = self.node_tree.nodes

            # self.node_tree.links.new(self.node_tree.nodes('fromnode').outputs('fromsocket'), self.node_tree.nodes('tonode').inputs('tosocket'))

    def init(self, context):
        self.createTree()


    @staticmethod
    def exists() : 
        for g in bpy.data.node_groups : 
            if g.name == "Uber Mapping" : 
                return True

        return False







