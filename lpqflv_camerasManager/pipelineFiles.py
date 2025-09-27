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

import os 

def lastIncrement (folderPath, fullPath=False) : 
    scenes = blendScenes(folderPath, fullPath, True) 
    if not scenes : 
        return None

    for s in scenes : 
        if "MASTER" in s : 
            scenes.remove(s)
            
    if scenes : 
        return scenes[-1]
    
    return None

def lastIncrementFromScenesList(sceneList) : 
    if len(sceneList) == 0 : 
        return None

    sceneObjects = Scene.getFromList(sceneList)
    scenes = sort(sceneObjects)
    return scenes[-1]

def blendScenes (folderPath, fullPath=False, sortScene=True) : 
    folderPath = cleanPath(folderPath)
    if not folderPath : 
        return False
    
    files = os.listdir(folderPath) 
    scenes = []
    sceneObjects = []
    
    for f in files : 
        if ".blend" in f and ".blend1" not in f : 
            scenes.append(f)
            
    if not fullPath : 
        if sortScene : 
            sceneObjects = Scene.getFromList(scenes)
            scenes = sort(sceneObjects)
        return scenes
    
    for i in range(0, len(scenes)) : 
        scenes[i] = folderPath + "/" + scenes[i]
        
    if sortScene : 
        sceneObjects = Scene.getFromList(scenes)
        scenes = sort(sceneObjects)
    return scenes

class Scene : 
    def __init__(self, file) : 
        self.file = file
        self.name = file.replace("\\", "/").split("/")[-1]
        self.increment = -1
        self.getIncrement()

    def getIncrement(self) : 
        if self.increment != -1 : 
            return self.increment

        self.increment = self.name.replace(".blend", "").split(".")[-1]
        try : 
            self.increment = int(self.increment)
        except : 
            self.increment = -1

        return self.increment

    @staticmethod
    def getFromList (files) : 
        _r = []
        for f in files : 
            sc = Scene(f)
            _r.append(sc)

        return _r

def sort(sceneObjects) : 
    if type(sceneObjects) == bool : 
        return []

    _r = []
    for i in range(len(sceneObjects)) : 
        for j in range(len(sceneObjects)) : 
            if i>j and sceneObjects[i].getIncrement() < sceneObjects[j].getIncrement() : 
                sceneObjects[i], sceneObjects[j] = sceneObjects[j], sceneObjects[i]

    
    for so in sceneObjects : 
        _r.append(so.file)
    return _r

def master (folderpath, fullPath=False) : 
    scenes = blendScenes(folderpath, fullPath)
    master = None 
    for s in scenes : 
        if "MASTER" in s : 
            master = s
    
    return master

def cleanPath(path) : 
    if not os.path.exists(path) : 
        return False
    
    if len(path) == 0 : 
        return False
    
    path = path.replace("\\", "/") 
    
    if path[-1] == "/" : 
        path = path[:-1]
        
    return path
