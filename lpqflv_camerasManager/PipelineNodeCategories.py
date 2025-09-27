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
import nodeitems_utils
from nodeitems_utils import NodeCategory, NodeItem

class PipelineNodeCategory(NodeCategory) : 
    @classmethod
    def poll(cls, context):
        if context.space_data.type != "NODE_EDITOR" : 
            return False
        return context.space_data.tree_type == 'PipelineNodeTree'
    
    
    # identifier, label, items list
files = PipelineNodeCategory("RESSOURCES", "Ressources", items =
                             [
                                 NodeItem("FileNode"),
                                 NodeItem("AlembicNode")
                             ])

    # identifier, label, items list
scenes = PipelineNodeCategory("SCENES", "Scenes", items =
                             [
                                 NodeItem("AssetSceneNode"),
                                 NodeItem("CharModSceneNode"),
                                 NodeItem("CharRigSceneNode"),
                                 NodeItem("AnimSceneNode"),
                                 NodeItem("LightingSceneNode"),
                                 NodeItem("RenderSceneNode")
                             ])
    # identifier, label, items list
layout = PipelineNodeCategory("LAYOUT", "layout", items =
                             [
                                 NodeItem("NodeFrame"),
                                 NodeItem("NodeReroute")
                             ])
                             
                             
    
# all categories in a list
categories = [files, scenes, layout]
        
def register() : 
    nodeitems_utils.register_node_categories('PIPELINE_NODES', categories)

def unregister () : 
    nodeitems_utils.unregister_node_categories('PIPELINE_NODES')
