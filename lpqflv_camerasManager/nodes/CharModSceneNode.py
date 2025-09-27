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
import os

class CharModSceneNode (sn.SceneBaseNode, sn.SceneBaseProps) : 
    
    bl_idname = "CharModSceneNode"
    bl_label = "Character - Modeling"
    
    sceneType = "Character"
    sceneTypeIcon = "EDITMODE_HLT"
    
    charType = "modeling"
    
    def init(self, context) : 
        super().init(context)
        pnt.PipelineNodeTree.get().characterNodes.append(self)
    
    def drawBeforeOpen(self, context, layout) :
        super().drawBeforeOpen(context, layout)
        
    def getDirPath(self) : 
        self.dirPath = pnt.PipelineNodeTree.root() + os.sep + self.getSceneType() + os.sep + self.charType
    
    def prefix(self) : 
        return "Char : "

def register () : 
    bpy.utils.register_class (CharModSceneNode)

def unregister () : 
    bpy.utils.unregister_class (CharModSceneNode)
