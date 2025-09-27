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
from lpqflv import utils
from lpqflv import bl_utils
from bpy.app.handlers import persistent


props = {}

SCENE_UPDATE = 1
SCENE_UPDATE_PRE = 2 
FRAME_CHANGE = 3 
FRAME_CHANGE_PRE = 4
PREFS_LOAD = 5
FACTORY_LOAD = 6
LOAD = 7
LOAD_PRE = 8
REDO = 9 
REDO_PRE = 10 
RENDER_CANCEL = 11 
RENDER_COMPLETE = 12
RENDER_INIT = 13
RENDER = 14
RENDER_PRE = 15 
RENDER_STATS = 16 
RENDER_WRITE = 17
SAVE = 18 
SAVE_PRE = 19 
UNDO = 20 
UNDO_PRE = 21 
VERSION = 22

def addHandler(func, handlersGrp) : 
    if func not in handlersGrp : 
        handlersGrp.append(func)

def removeHandler(func, handlersGrp) : 
    if func in handlersGrp : 
        handlersGrp.remove(func)

def handlersGrpFromConst(const) : 
    if   const == SCENE_UPDATE : 
        return bpy.app.handlers.depsgraph_update_post
    elif const == SCENE_UPDATE_PRE : 
        return bpy.app.handlers.depsgraph_update_pre
    elif const == FRAME_CHANGE : 
        return bpy.app.handlers.frame_change_post
    elif const == FRAME_CHANGE_PRE : 
        return bpy.app.handlers.frame_change_pre
    elif const == PREFS_LOAD : 
        return bpy.app.handlers.load_factory_preferences_post
    elif const == FACTORY_LOAD : 
        return bpy.app.handlers.load_factory_startup_post
    elif const == LOAD : 
        return bpy.app.handlers.load_post
    elif const == LOAD_PRE : 
        return bpy.app.handlers.load_pre
    elif const == REDO : 
        return bpy.app.handlers.redo_post
    elif const == REDO_PRE : 
        return bpy.app.handlers.redo_pre
    elif const == RENDER_CANCEL : 
        return bpy.app.handlers.render_cancel
    elif const == RENDER_COMPLETE : 
        return bpy.app.handlers.render_complete
    elif const == RENDER_INIT : 
        return bpy.app.handlers.render_init
    elif const == RENDER : 
        return bpy.app.handlers.render_post
    elif const == RENDER_PRE : 
        return bpy.app.handlers.render_pre
    elif const == RENDER_STATS : 
        return bpy.app.handlers.render_stats
    elif const == RENDER_WRITE : 
        return bpy.app.handlers.render_write
    elif const == SAVE : 
        return bpy.app.handlers.save_post
    elif const == SAVE_PRE : 
        return bpy.app.handlers.save_pre
    elif const == UNDO : 
        return bpy.app.handlers.undo_post
    elif const == UNDO_PRE : 
        return bpy.app.handlers.undo_pre
    elif const == VERSION : 
        return bpy.app.handlers.version_update


def add(func, pType = SCENE_UPDATE) : 
    addHandler(func, handlersGrpFromConst(pType))

def remove(func, pType = SCENE_UPDATE) : 
    removeHandler(func, handlersGrpFromConst(pType))

# return an event object
# func can take one argument : the property
def addOnUpdate(func, blCollection, objName, propPath, id=None) : 
    if not id : 
        id = utils.uniqId()
    obj = blCollection.get(objName)
    subObj = bl_utils.subObject(obj, propPath)
    props[id] = getattr(subObj, propPath.split(".")[-1])
    
    e = Event()
    e.id = id 
    e.collection = blCollection
    e.objPointer = obj.as_pointer()
    e.propPath = propPath

    @persistent
    def handlerFunc (dum) : 
        #check if object is still here
        newObj = bl_utils.objectFromPointer(blCollection, e.objPointer)
        if not newObj : 
            return
        ### 

        subObj = bl_utils.subObject(newObj, e.propPath)
        currentValue = getattr(subObj, e.propPath.split(".")[-1])
        if props[id] != currentValue : 
            func(currentValue)
        props[id] = currentValue

    add(handlerFunc)
    e.func = handlerFunc
    return e

class Event : 
    id = None 
    collection = None
    objPointer = None 
    propName = None 
    func = None
    eType = SCENE_UPDATE

    def remove(self) : 
        remove (self.func, self.eType)
