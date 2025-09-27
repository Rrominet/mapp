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


class *operatorClass* (bpy.types.Operator):
    bl_idname = "*category*.*cleanName*"
    bl_label = "*name*"
    bl_description = "*decription*"
    bl_options = *option*

    @classmethod
    def poll(cls, context):
        return True

    def __init__(self): #called before the method Oprator.invoke () 
        pass

    def __del__(self): #called after the object returned {'FINISHED'}
        pass

    
    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)
        return {"RUNNING_MODAL"}

    def modal(self, context, event):

        if event.type == "LEFTMOUSE":
            return {"FINISHED"}

        if event.type in {"RIGHTMOUSE", "ESC"}:
            return {"CANCELLED"}

        return {"*mode*"}


    def execute(self, context):
        return {"FINISHED"}
        







