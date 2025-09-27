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
class Popup (bpy.types.Operator) : 
    bl_idname = "lpqflv.popup"
    bl_label = "Infos"
    bl_description = "Create a window popup"
    bl_options = {'REGISTER'}
    message : bpy.props.StringProperty(
        name = "message",
        description = "message",
        default = ''
    )
    icon : bpy.props.StringProperty(name="icon", 
        description="Icon for the message", 
        default="NONE")

    def execute(self, context):
        self.report({'INFO'}, self.message)
        return {"FINISHED"}

    def invoke (self, context, event) : 
        return context.window_manager.invoke_props_dialog(self, width = 400)

    def draw(self, context) : 
        mlist = self.message.split ("\n")
        self.layout.label(text="", icon=self.icon)
        for l in mlist : 
            self.layout.label(text=l)


def popup(msg, icon = "NONE") : 
    bpy.ops.lpqflv.popup('INVOKE_DEFAULT', message=msg, icon=icon)

def register():
    bpy.utils.register_class(Popup)

def unregister() : 
    bpy.utils.unregister_class(Popup)

register() 







