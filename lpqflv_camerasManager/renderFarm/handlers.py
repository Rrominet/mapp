import bpy 
from bpy.app.handlers import persistent
from lpqflv_camerasManager import config as cf
from lpqflv import bl_events

@persistent
def readRenderFarm(dum1=None, dum2=None): 
    cf.MCR.renderFarm.read()

@persistent
def saveRenderFarm(dum1, dum2) : 
    cf.MCR.renderFarm.save()

def register() : 
    bl_events.add(readRenderFarm, bl_events.LOAD)
    bl_events.add(saveRenderFarm, bl_events.SAVE_PRE)

def unregister() : 
    bl_events.remove(readRenderFarm, bl_events.LOAD)
    bl_events.remove(saveRenderFarm, bl_events.SAVE_PRE)

