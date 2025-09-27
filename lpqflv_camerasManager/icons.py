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
import bpy.utils.previews
import os
from lpqflv import fileTools as ft

class Icons : 
    def __init__ (self) : 
        self.pipeline = bpy.utils.previews.new()
        self.pipelineInfos = []
        
    def newIcon (self, collection, name, path, type='IMAGE') : 
        try : col = getattr(self, collection)
        except : return 
        try : infos = getattr(self, collection + "Infos")
        except : return
        col.load(name, path, type) 
        info = IconInfos(name, path)
        infos.append(info)
        
    def getInfos (self, collection, name) : 
        try : infos = getattr(self, collection + "Infos")
        except : pass
        
        for i in infos : 
            if i.name == name : 
                return i
        
    def getInfosIndex (self, collection, name) : 
        try : infos = getattr(self, collection + "Infos")
        except : pass
        
        ind = 0
        for i in infos : 
            if i.name == name : 
                return ind
            ind += 1
            
        return -1
    
    def remove(self, collection, name) : 
        try : col = getattr(self, collection)
        except : return 
        try : infos = getattr(self, collection + "Infos")
        except : return
    
        i = 0 
        for c in col : 
            if c == name : 
                col.pop(name) 
                infos.pop(i)
                break 
            i+=1
    
    def clear(self) : 
        try : self.pipeline.clear() 
        except : pass
        self.pipelineInfos = []
        
        
        
class IconInfos : 
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.size = 0
        self.computeSize()
        
    def computeSize(self) : 
        self.size = os.path.getsize(self.path)
        
    def hasChanged(self) : 
        if self.size != os.path.getsize(self.path) : 
            return True
        else :
            return False
