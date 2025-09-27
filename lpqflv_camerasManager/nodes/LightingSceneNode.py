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

from lpqflv_camerasManager.nodes import SceneNode as sn
from lpqflv_camerasManager import PipelineNodeTree as pnt


import bpy 

class LightingSceneNode (sn.SceneBaseNode, sn.SceneBaseProps) : 
    
    bl_idname = "LightingSceneNode"
    bl_label = "Lighting/Shading"
    
    sceneType = "Lighting/Shading"
    sceneTypeIcon = "OUTLINER_OB_LIGHT"
   
    seq : bpy.props.IntProperty(name="Sequence", description="The number of the sequence of this scene", min=0)
    
    def init(self, context) : 
        super().init(context)
        pnt.PipelineNodeTree.get().lightingNodes.append(self)
    
    def drawBeforeOpen(self, context, layout) :
        super().drawBeforeOpen(context, layout)
        layout.prop(self, "seq")
    
    def getSceneFileName(self) : 
        return self.getSceneType() + "_" + self.content + "_seq" + str(self.seq)

    def prefix(self) : 
        return "Lighting : "
    
def register () : 
    bpy.utils.register_class (LightingSceneNode)

def unregister () : 
    bpy.utils.unregister_class (LightingSceneNode)
