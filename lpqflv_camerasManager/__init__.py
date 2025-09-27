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

#updated
bl_info = {
    "name": "MAPP : Pipeline and Cameras Manager",
    "author": "Romain Gilliot",
    "version": (7, 5, 1),
    "blender" : (4, 0, 1),
    "location": "Pipeline Editor, Property Editor, VSE",
    "description": "Manage your project with an advanced Pipeline Tool.",
    "warning": "",
    "wiki_url": "https://lpqflv.com/mini-formations/01/",
    "tracker_url" : "https://lpqflv.com/bug-report/?soft=mapp&version=blender",
    "category": "Le Plug Qui Facilite La Vie",
    } 


import bpy 
import sys 
import os

from . import config as cfg 
from . import CameraManager as cm
from . import ops
from . import panels
from . import menus 
from . import prefs
from . import PipelineNodeTree as pnt
from . import PipelineNodeCategories as pnc
from . import Pipeline as p
from . import uiLists
from . import multiCamRender as mcr
from . import Camera as cam
from . import icons as ic

from .nodes import FileNode
from .nodes import AlembicNode
from .nodes import SceneNode
from .nodes import AssetSceneNode
from .nodes import CharModSceneNode
from .nodes import CharRigSceneNode
from .nodes import AnimSceneNode
from .nodes import LightingSceneNode
from .nodes import RenderSceneNode
from .nodes import PipelineNode

from .sockets import FileSocket
from .sockets import BlendSocket
from .sockets import LinkSocket

from lpqflv import update

from lpqflv_camerasManager.renderFarm import ops as rfops
from lpqflv_camerasManager.renderFarm import props as rfprops
from lpqflv_camerasManager.renderFarm import handlers as rfhandlers

from lpqflv_camerasManager.vse import props as vse_props
from lpqflv_camerasManager.vse import ops as vse_ops
from lpqflv_camerasManager.vse import menus as vse_menus
from lpqflv_camerasManager.vse import panels as vse_panels
    
        

## properties 

bpy.types.Scene.projectPath = bpy.props.StringProperty(name="Project Path ", subtype='DIR_PATH', update=p.Pipeline.setExistingSeqs) 

bpy.types.Scene.sceneContent = bpy.props.StringProperty(name="Scene Content ") 
bpy.types.Scene.sceneType = bpy.props.EnumProperty(items=[("assets", "asset", "asset", "MESH_CUBE", 0),
 ("animations", "animation", "animation", "TIME", 1), 
 ("characters", "character", "character", "POSE_HLT", 2), 
 ("render-settings", "render settings", "render settings", "SETTINGS", 4), 
 ("lighting-shading", "lighting/shading", "lighting/shading", "MATERIAL", 3)],
  name="Scene Type ", update=p.Pipeline.onSceneTypeChange)
bpy.types.Scene.charType = bpy.props.EnumProperty(items=[("modeling","Modeling","modeling","EDITMODE_HLTMODE_HLT",0),
("rig","Rig","Rig","POSE_HLT",1)], name = "Character Type ")
bpy.types.Scene.seq = bpy.props.IntProperty(name="Sequence", min = 0)
bpy.types.Scene.reloadGlobalLibraries = bpy.props.BoolProperty(name="Global Lib", description="Change all libraries in the scene with a global path when saving.", default=True)
bpy.types.Scene.pathToReplace = bpy.props.StringProperty(name="Replace in path")
bpy.types.Scene.pathFromReplace = bpy.props.StringProperty(name="With")

bpy.types.Scene.existingScenes = bpy.props.EnumProperty(items=cfg.EXISTING_SEQS,
  name="Existing sequences ")

bpy.types.WindowManager.showPath = bpy.props.BoolProperty(name="Path and libs", description="Manage Path and libs conflicts \nbetween scenes in the pipeline.", default=False)
  
bpy.types.Scene.previousProject = bpy.props.EnumProperty(items=cfg.PREVIOUS_PROJECTS,
  name="Previous projects ", update=p.Pipeline.onPreviousProjectChange)

## 

def register():
    
    ## register##
        
    cfg.CM = cm.CameraManager() 
    cfg.CM.register()
    
    cfg.PIPE = p.Pipeline()
    cfg.icons = ic.Icons() 
    
    bpy.types.WindowManager.isAutoUpdateCam = bpy.props.BoolProperty(name="Auto camera change", description="Update the active camera when blender is playing...", default=False, update=cm.CameraManager.onAutoCameraChangeUpdate)  
    
    panels.register()
    ops.register()
    menus.register()
    prefs.register()
    bpy.utils.register_class(pnt.PipelineNodeTree)
    FileNode.register()
    AlembicNode.register()
    FileSocket.register()
    BlendSocket.register()
    LinkSocket.register()
    AssetSceneNode.register()
    CharModSceneNode.register()
    CharRigSceneNode.register()
    AnimSceneNode.register()
    LightingSceneNode.register()
    RenderSceneNode.register()
    PipelineNode.register()
    pnt.register()

    pnc.register()
    uiLists.register()
    mcr.register()
    cam.register()
    update.register()
    rfops.register()
    rfprops.register()
    rfhandlers.register()

    vse_props.register()
    vse_ops.register()
    vse_menus.register()
    vse_panels.register()
    
def unregister():
    cfg.CM.unregister()
    
    panels.unregister()
    ops.unregister()
    menus.unregister()
    prefs.unregister()
    bpy.utils.unregister_class(pnt.PipelineNodeTree)
    FileNode.unregister()
    AlembicNode.unregister()
    FileSocket.unregister()
    BlendSocket.unregister()
    LinkSocket.unregister()
    AssetSceneNode.unregister()
    CharModSceneNode.unregister()
    CharRigSceneNode.unregister()
    AnimSceneNode.unregister()
    LightingSceneNode.unregister()
    RenderSceneNode.unregister()
    PipelineNode.unregister()
    pnt.unregister()
    
    pnc.unregister()
    uiLists.unregister()
    mcr.unregister()
    cam.unregister()
    update.unregister()
    rfops.unregister()
    rfprops.unregister()
    rfhandlers.unregister()

    vse_props.unregister()
    vse_ops.unregister()
    vse_menus.unregister()
    vse_panels.unregister()

if __name__ == "__main__":
    register()
 
