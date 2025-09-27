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
import bmesh
import sys

import fileTools as file
from importlib import reload
reload(file)
import stringTools as string
import listTools as l

class Obj : 
    def __init__(self, filepath) : 
        self.filepath = filepath
        self.lines = []
        self.bm = bmesh.new()

    def readLines (self) : 
        self.lines = file.readFileLines(self.filepath)
        for l in self.lines : 
            self.interpretLine(l)

        return self.bm


    def interpretLine (self, line) : 
        if line[0] == "#" : 
            return

        tmp = line.split(" ")

        if tmp[0] == "v" : 
            self.bm.verts.new(
                (float(tmp[1]),
                float(tmp[2]),
                float(tmp[3])))

        if tmp[0] == "f" : 
            face = Face (line)
            bmVerts = []
            for i in face.verts : 
                self.bm.verts.ensure_lookup_table()
                bmVerts.append(self.bm.verts[i])

            self.bm.faces.new(bmVerts)



class Face : 
    def __init__ (self, line) : 
        self.verts = []

        tmp = line.split(" ")
        tmp.pop(0)

        for t in tmp : 
            elts = t.split("/")
            self.verts.append (int(elts[0]) - 1)










