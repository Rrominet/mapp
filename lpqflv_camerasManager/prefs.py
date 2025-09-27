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


from lpqflv_camerasManager import ops
from lpqflv_camerasManager import config as cfg
from lpqflv_camerasManager import menus
from lpqflv_camerasManager import PipelineNodeTree as pnt
from lpqflv import update

from lpqflv_camerasManager.vse import menus as vse_menus

import bpy

class Prefs(bpy.types.AddonPreferences) : 
    bl_idname = "lpqflv_camerasManager"

    defaultCameraAlpha : bpy.props.FloatProperty(name="Passepartout", description="Default PassePartout value when creating a camera via the addon.", min=0, max=1, default=1)
    defaultClipStart : bpy.props.FloatProperty(name="Clip Start", description="Default Clip Start value when creating a camera via the addon.", min=0.0001, max=100, default=0.01)
    defaultClipEnd : bpy.props.FloatProperty(name="Clip End", description="Default Clip End value when creating a camera via the addon.", min=0.1, max=1000000000000000, default=10000)
    defaultLens : bpy.props.FloatProperty(name="Focal Length", description="Default Focal Length when creating a camera via the addon.", min=1, max=10000, default=50)
    
    keymaps = None
    saveKeyMap = None
    
    def draw(self, context) : 
        update.draw(self, context)
        l = self.layout
        box = l.box()
        r = box.row()
        r.label(text="Shortcuts : ", icon="EVENT_RETURN")
        r = box.row(align=True)
        kmi1 = keyMapFromAddonByName(menus.SaveMenu.bl_label)
        kmi2 = keyMapFromAddonByName(menus.CamerasMenu.bl_label)
        kmi3 = keyMapFromAddonByName(ops.ActiveCameraOptions.bl_label)
        kmi4 = keyMapFromAddonByName(vse_menus.MappSequencerMenu.bl_label)
        
        self.drawForKeyMapItem(box, kmi1)
        self.drawForKeyMapItem(box, kmi2)
        self.drawForKeyMapItem(box, kmi3)
        self.drawForKeyMapItem(box, kmi4)
        
        box = l.box()
        
        r = box.row()
        r.label(text="Preferences for your best Camera : View 3D->Add->Cameras : ", icon="VIEW_CAMERA")
        r = box.row()
        r.prop(self, "defaultCameraAlpha")
        c = box.row(align=True)
        c.prop(self, "defaultClipStart")
        c.prop(self, "defaultClipEnd")
        r = box.row()
        r.prop(self, "defaultLens")
        box = l.box()
        r = box.row()
        r.label(text="Modal Handler managment (Don't touch it if you don't know what you're doing) : ")
        r = box.column(align=True)
        if cfg.CM.running : 
            r.operator(ops.StartStopCameraHandler.bl_idname, icon="VIEW_CAMERA", text="Cameras link handler running...")
        else : 
            r.operator(ops.StartStopCameraHandler.bl_idname, icon="ERROR", text="Cameras link handler not running.")
            
        pipe = pnt.PipelineNodeTree.get()
        if pipe : 
            if pipe.handlerRunning : 
                r.operator(ops.PIPE_StartStopPipelineHandler.bl_idname, icon="FILE_REFRESH", text="Pipeline modal handler running...")
            else : 
                r.operator(ops.PIPE_StartStopPipelineHandler.bl_idname, icon="ERROR", text="Pipeline modal handler not running.")
                
    def drawForKeyMapItem(self, layout, kmi) :
        r = layout.row(align=True)
        r.label(text=kmi.name)
        r.prop(kmi, "map_type")
        r.prop(kmi, "type", text="Key")
        r.prop(kmi, "shift", icon="EVENT_SHIFT", text="")
        r.prop(kmi, "ctrl", icon="EVENT_CTRL", text="")
        r.prop(kmi, "alt", icon="EVENT_ALT", text="")
        r.prop(kmi, "oskey", icon="EVENT_OS", text="")
        
            
    @staticmethod
    def get() : 
        return bpy.context.preferences.addons['lpqflv_camerasManager'].preferences
    
def activeKeyConfig() : 
    return bpy.context.window_manager.keyconfigs.active

def findKeyMaps(name) : 
    if name in activeKeyConfig().keymaps : 
        return activeKeyConfig().keymaps[name]
    return None
    
def findKeyMapItem(name, keymaps) :
    for km in keymaps.keymap_items :
        print (name)
        print (km.name)
        if km.name == name : 
            return km
    
    return None

def keyMapFromAddonByName(name) : 
    wm = bpy.context.window_manager
    for km in wm.keyconfigs.addon.keymaps : 
        for kmi in km.keymap_items : 
            if kmi.name == name : 
                return kmi

addon_keymaps = []

def registerKeyMaps() : 
        # handle the keymap
        wm = bpy.context.window_manager
        if 'Window' not in wm.keyconfigs.addon.keymaps : 
            km = wm.keyconfigs.addon.keymaps.new(name='Window', space_type='EMPTY')
        else : 
            km = wm.keyconfigs.addon.keymaps['Window']

        if 'Sequencer' not in wm.keyconfigs.addon.keymaps : 
            kmseq= wm.keyconfigs.addon.keymaps.new(name='Sequencer', space_type='SEQUENCE_EDITOR')
        else : 
            kmseq= wm.keyconfigs.addon.keymaps['Sequencer']
        
        #kmi = prefsm.findKeyMapItem(menus.SaveMenu.bl_label, km)
        #if not kmi : 
        
        kmi2 = km.keymap_items.new('wm.call_menu', value="PRESS", type="S", ctrl=True, alt=True, shift=False)
        kmi2.properties.name = menus.SaveMenu.bl_idname
        
        kmi3 = km.keymap_items.new('wm.call_menu', value="PRESS", type="C", ctrl=True, alt=True, shift=False)
        kmi3.properties.name = menus.CamerasMenu.bl_idname

        kmi4 = km.keymap_items.new(ops.ActiveCameraOptions.bl_idname, value="PRESS", type="C", ctrl=True, alt=False, shift=True)

        kmi5 = kmseq.keymap_items.new('wm.call_menu', value="PRESS", type="Z", ctrl=False, alt=False, shift=False)
        kmi5.properties.name = vse_menus.MappSequencerMenu.bl_idname
        
        addon_keymaps.append((km, kmi2))
        addon_keymaps.append((km, kmi3))
        addon_keymaps.append((km, kmi4))
        addon_keymaps.append((kmseq, kmi5))

def unregisterKeyMaps() : 
    # handle the keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    
def register () : 
    bpy.utils.register_class(Prefs)
    registerKeyMaps()

def unregister () : 
    bpy.utils.unregister_class(Prefs)
    unregisterKeyMaps()
    
