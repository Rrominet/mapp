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
import blf 
import os

class Font : 
    """callback takes 2 args (self, context)
params is a dict with position, color, size and rotation attributes
space is the space where to draw the text
    """
    def __init__(self, text, params=None , space=None, font="") : 
        self.text = text
        self.fontId = 0
        self.setFont(font)
        if not space and bpy.context.area : 
            self.space = bpy.context.area.spaces.active
        else : 
            self.space = space

        if not self.space : 
            self.space = bpy.data.window_managers[0].windows[0].workspace.screens[0].areas[0].spaces[0]

        self.handler = None
        self.params = {}
        if params : 
            self.params = params
        else : 
            self.params = {
                "position" : [16, 16, 0],
                "color" : [1,1,1,1],
                "size" : 12,
                "rotation" : 0.0
            }

    def setPosition(self, x, y) : 
        self.params["position"][0] = x
        self.params["position"][1] = y
    
    def setFont(self, font) : 
        if font : 
            path = bpy.path.abspath(font)
            if os.path.exists(path) : 
                self.fontId = blf.load(path)
            else :
                self.fontId = 0
        else : 
            self.fontId = 0

    def draw(self) : 
        try : self.clear()
        except : pass
        self.handler = self.space.draw_handler_add(Font.drawCallBack, (self, None), "WINDOW", "POST_PIXEL")

    def setText(self, text) : 
        self.text = text

    def clear(self) : 
        self.space.draw_handler_remove(self.handler, "WINDOW")
        self.handler = None

    @staticmethod
    # arg1 : font object
    def drawCallBack (arg1, arg2) : 

        f = arg1
        params = f.params

        texts = f.text.split("\n")
        
        blf.position(f.fontId,
        params["position"][0],
        params["position"][1],
        params["position"][2])

        blf.size(f.fontId, params["size"])
        blf.color(f.fontId, 
        params["color"][0],
        params["color"][1],
        params["color"][2],
        params["color"][3])

        i = 0
        for t in texts :
            blf.draw(f.fontId, t)
            i += 1
            blf.position(f.fontId,
                params["position"][0],
                params["position"][1] + i*(f.params["size"] + 2),
                params["position"][2])
