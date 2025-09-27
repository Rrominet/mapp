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

from lpqflv_camerasManager import prefs as prefsm
from lpqflv_camerasManager import ops
from lpqflv_camerasManager import Camera as cam



import bpy

class CamerasMenu (bpy.types.Menu) :
    bl_idname = "INFO_MT_cameras_add"
    bl_label = "LPQFLV : Add Cameras"

    @classmethod
    def poll(cls, context) : 
        return context.mode == "OBJECT"

    def draw (self, context) : 

        prefs = context.preferences.addons[prefsm.Prefs.bl_idname].preferences
        persoLens = round(prefs.defaultLens, 2)

        l = self.layout
        r = l.column() 
        r.operator (ops.CameraPresetOperator.bl_idname, text="Lens : 15mm", icon="CAMERA_DATA").lens = 15
        r.operator (ops.CameraPresetOperator.bl_idname, text="Lens : 25mm", icon="CAMERA_DATA").lens = 25
        r.operator (ops.CameraPresetOperator.bl_idname, text="Lens : 35mm", icon="CAMERA_DATA").lens = 35
        r.operator (ops.CameraPresetOperator.bl_idname, text="Lens : 50mm", icon="CAMERA_DATA").lens = 50
        r.operator (ops.CameraPresetOperator.bl_idname, text="Lens : 75mm", icon="CAMERA_DATA").lens = 75
        r.operator (ops.CameraPresetOperator.bl_idname, text="Lens : 150mm", icon="CAMERA_DATA").lens = 150
        r.operator (ops.CameraPresetOperator.bl_idname, text="Lens : 200mm", icon="CAMERA_DATA").lens = 200
        r.operator (ops.CameraPresetOperator.bl_idname, text="Lens (prefs) : " + str(persoLens) + "mm", icon="CAMERA_DATA").lens = prefs.defaultLens

    @staticmethod
    def activeDraw(self, ctx) : 
        l =self.layout
        l.separator()
        l.operator(ops.ActiveCameraOptions.bl_idname, icon="CAMERA_DATA")

def drawSaveOps(self, ctx) : 
    l = self.layout
    l.separator()
    l.operator(ops.PIPE_SaveIncrement.bl_idname, text="Save Increment", icon="FILE_TICK")
    l.operator(ops.PIPE_SaveMaster.bl_idname, text="Save Master", icon="MONKEY")
    if ops.PIPE_SaveIncrement.poll(ctx) :
        l.separator()
        l.operator(ops.PIPE_DuplicateCurrentScene.bl_idname, text="Duplicate current Scene", icon="DUPLICATE")

class SaveMenu (bpy.types.Menu) : 
    bl_idname = "LPQFLV_MT_lpqflv_save_menu"
    bl_label = "LPQFLV : Pipeline Save"
    
    def draw(self, context) : 
        l = self.layout
        c = l.column(align=True) 
        
        c.operator(ops.PIPE_SaveIncrement.bl_idname, text="Save Increment", icon="FILE_TICK")
        c.operator(ops.PIPE_SaveMaster.bl_idname, icon="MONKEY")
        
def drawSequencerContextMenu(self, context) : 
    strip = cam.activeStrip()
    if not strip or not strip.cm.isCamera : 
        return 
    
    l = self.layout
    l.separator() 
    r = l.row() 
    camera = cam.cameraFromStrip(strip.name)
    r.operator(ops.MkActiveCamera.bl_idname, icon="OUTLINER_OB_CAMERA").cameraName = camera.name
    
class LinkFromBlendDataMenu (bpy.types.Menu) : 
    bl_idname = "LPQFLV_MT_link_blenddata_menu"
    bl_label = "Link from BlendData"
    
    def draw(self, context) : 
        l = self.layout
        c = l.column(align=True) 
        
        c.operator(ops.PIPE_LinkFromDataObjects.bl_idname, icon="OBJECT_DATAMODE")
        c.operator(ops.PIPE_LinkFromDataData.bl_idname, icon="MESH_DATA") 
        c.separator() 
        c.operator(ops.PIPE_LinkObjectsFromCollection.bl_idname, icon="COLLECTION_NEW")
        c.operator(ops.PIPE_LinkObjectsFromScene.bl_idname, icon="SCENE_DATA")
    
    def drawAddCtxMenu(self, context) :
        self.layout.separator()
        self.layout.menu(LinkFromBlendDataMenu.bl_idname, icon="DECORATE_LINKED")

def dopesheetCtx (self, ctx) : 
    l = self.layout
    if ops.CameraRangeFromKeyframes.poll(ctx) : 
        l.separator()
        l.operator(ops.CameraRangeFromKeyframes.bl_idname, icon="OUTLINER_OB_CAMERA")

def drawRightClickCtx (self, ctx) : 
    l = self.layout
    l.operator_context = "INVOKE_DEFAULT"
    if ops.CreateDOFTarget.poll(ctx) : 
        l.operator(ops.CreateDOFTarget.bl_idname)

        
def register () : 
    bpy.utils.register_class(CamerasMenu)
    bpy.types.VIEW3D_MT_add.append(ops.CameraPresetOperator.drawMenu)
    bpy.utils.register_class(SaveMenu)
    bpy.utils.register_class(LinkFromBlendDataMenu)
    bpy.types.SEQUENCER_MT_context_menu.append(drawSequencerContextMenu)
    bpy.types.VIEW3D_MT_add.append(LinkFromBlendDataMenu.drawAddCtxMenu)
    bpy.types.VIEW3D_MT_view.append(CamerasMenu.activeDraw)
    bpy.types.DOPESHEET_MT_context_menu.append(dopesheetCtx)
    bpy.types.GRAPH_MT_context_menu.append(dopesheetCtx)
    bpy.types.VIEW3D_MT_object_context_menu.prepend(drawRightClickCtx)
    bpy.types.TOPBAR_MT_file.append(drawSaveOps)

def unregister() : 
    bpy.utils.unregister_class(CamerasMenu)
    bpy.types.VIEW3D_MT_add.remove(ops.CameraPresetOperator.drawMenu)
    bpy.utils.unregister_class(SaveMenu)
    bpy.utils.unregister_class(LinkFromBlendDataMenu)
    bpy.types.VIEW3D_MT_add.remove(LinkFromBlendDataMenu.drawAddCtxMenu)
    bpy.types.VIEW3D_MT_view.remove(CamerasMenu.activeDraw)
    bpy.types.DOPESHEET_MT_context_menu.remove(dopesheetCtx)
    bpy.types.GRAPH_MT_context_menu.remove(dopesheetCtx)
    bpy.types.VIEW3D_MT_object_context_menu.prepend(drawRightClickCtx)
    bpy.types.TOPBAR_MT_file.remove(drawSaveOps)

