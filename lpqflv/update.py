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
from bpy.app.handlers import persistent
from lpqflv import thread
from lpqflv import bl_events
from lpqflv import network
from lpqflv import bl_addons
from lpqflv import bl_utils
from lpqflv import lpqflv_popup as pp
from lpqflv import fileTools as ft
import os 
import urllib

LPQFLV = None
LPQFLV_DOMAIN = "https://lpqflv.com/blender"
LPQFLV_PATH = bl_addons.addonsPath() + "/lpqflv"

INSTALLING = 1
DOWNLOADING = 2
NONE = 0

class Update : 
    updatable = False
    report = False
    newVersion = ""
    installed = False
    state = NONE

    def init (self) :
        self.launchCheckUpdates()

    def currentVersion(self) : 
        return ft.readFileContent(LPQFLV_PATH + os.path.sep + "version") 

    def checkUpdates(self) : 
        if not network.hasInternet() : 
            return
        aviables = network.asJson(LPQFLV_DOMAIN + "/ajax.php?func=versions")
        for a in aviables : 
            if isMoreRecent(a, self.currentVersion()) : 
                self.updatable = True
                self.newVersion = a
    def launchCheckUpdates(self) : 
        thread.startOnObj(Update.checkUpdates, LPQFLV)

def isMoreRecent(f1, f2) : 
    """If f1>f2 return True"""
    if not f1 or not f2 : 
        return False
    n1 = f1.split("_")[:-1]
    n1 = "_".join(n1)
    n2 = f2.split("_")[:-1]
    n2 = "_".join(n2)

    if n1 != n2 : 
        return False
    
    f1 = f1.split("_")[-1].replace(".zip", "")
    f2 = f2.split("_")[-1].replace(".zip", "")

    f1 = float(f1)
    f2 = float(f2)

    return f1>f2

def draw (self, context) : 
    if not (LPQFLV.updatable) : 
        return 
    l = self.layout
    box = l.box()
    r = box.row()
    if LPQFLV.installed : 
        r.label(text="Update succefully installed. Reboot Blender to reload", icon="QUIT")
        return

    r.label(text="An update is available for LPQFV : (current version : " + LPQFLV.currentVersion() +
            ")", icon="URL")
    r = box.row()
    r.operator(UPDATE_install.bl_idname, text="Install the update : " + LPQFLV.newVersion.split("_")[-1].replace(".zip", ""), icon="FILE_REFRESH")

class UPDATE_install(bpy.types.Operator) : 
    bl_description = "Update the addon"

    bl_idname = "lpqflv_update.install"
    bl_label = "Install the update"
    
    def execute(self, context) : 
        LPQFLV.state = DOWNLOADING
        dwnDir = context.preferences.filepaths.temporary_directory
        zip = network.download(LPQFLV_DOMAIN + "/installs/" + LPQFLV.newVersion, dwnDir + os.path.sep + LPQFLV.newVersion)
        LPQFLV.state = INSTALLING
        bpy.ops.preferences.addon_install(filepath = zip)
        LPQFLV.installed = True
        LPQFLV.state = NONE
        return {'FINISHED'}

class Update_Report(bpy.types.Operator) : 
    bl_description = "Report version state and availables updates"

    bl_idname = "lpqflv_update.report"
    bl_label = "Report"
    
    def invoke (self, ctx, e) : 
        ctx.window_manager.modal_handler_add(self)
        return{"RUNNING_MODAL"}

    def modal(self, ctx, e) : 
        if LPQFLV.updatable and not LPQFLV.report : 
            self.report({"WARNING"}, "An update is available for LPQFLV : See the addon preferences : Updates - for upgrade.")
            LPQFLV.report = True
            return {"FINISHED"}
        return{"PASS_THROUGH"}

@persistent
def onLoad(scene) : 
    bl_events.remove(onLoad, bl_events.LOAD )
    bpy.ops.lpqflv_update.report("INVOKE_DEFAULT")

def register() : 
    if not bl_utils.isRegistered(UPDATE_install) : 
        bpy.utils.register_class(UPDATE_install)
    if not bl_utils.isRegistered(Update_Report) : 
        bpy.utils.register_class(Update_Report)
        
    bl_events.add(onLoad, bl_events.LOAD )
    
    global LPQFLV
    LPQFLV = Update()
    LPQFLV.init()

def unregister() : 
    if bl_utils.isRegistered(UPDATE_install) : 
        bpy.utils.unregister_class(UPDATE_install)
    if bl_utils.isRegistered(Update_Report) : 
        bpy.utils.unregister_class(Update_Report)

    bl_events.remove(onLoad, bl_events.LOAD )
