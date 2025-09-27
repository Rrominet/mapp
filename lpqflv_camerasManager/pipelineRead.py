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
import os 

from lpqflv import fileTools


class Scene : 
    def __init__(self, filepath) : 
        self.type = ""
        self.content = ""
        self.charType = ""
        
        self.filepath = fileTools.cleanPath(filepath, False)
        self.filename = ""
        self.nodeType = ""
        self.seq = 0
        
        self.infos()
        self.setNodeType()
        
    def infos(self) : 
        folders = self.filepath.split("/");
        self.filename = folders[-1]
        tmp = self.filename.split("_")
        self.type = tmp[0]
        if len(tmp) >1 : 
            self.content = tmp[1]
        
        if "modeling" in folders : 
            self.charType = "modeling"
        
        elif "rig" in folders : 
            self.charType = "rig"
            
        if len(tmp)>2 : 
            try : 
                self.seq = int(tmp[2].replace("seq", ""))
            except : pass
            
    def setNodeType(self) : 
        if "asset" in self.type : 
            self.nodeType = "AssetSceneNode"
        elif "character" in self.type and self.charType == "modeling": 
            self.nodeType = "CharModSceneNode"
        elif "character" in self.type and self.charType == "rig" : 
            self.nodeType = "CharRigSceneNode"
        elif "animation" in self.type : 
            self.nodeType = "AnimSceneNode"
        elif "lighting-shading" in self.type : 
            self.nodeType = "LightingSceneNode"
        elif "render-settings" in self.type : 
            self.nodeType = "RenderSceneNode"
        else : 
            self.nodeType = "None"

def scenesFromFiles () : 
    root = bpy.context.scene.projectPath 
    if len(root) == 0 : 
        return 
    
    if not os.path.exists(root) : 
        return 
    
    root = fileTools.cleanPath(root)
    
    files = fileTools.hierarchie(root, True, ["__trash__"])
    
    sceneFiles = []
    for f in files : 
        if ".blend" in f and ".blend1" not in f : 
            goodName = f.split(".")[0]
            if goodName not in sceneFiles : 
                sceneFiles.append(goodName)
                
    scenes = []
    for f in sceneFiles : 
        scene = Scene(f)
        scenes.append(scene)
        
    return scenes
    
