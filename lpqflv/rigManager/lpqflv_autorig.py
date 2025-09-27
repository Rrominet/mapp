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
import blf
import bgl
import sys
import os
import mathutils
import time
from pathlib import Path
import math
from mathutils import *

from bpy_extras import view3d_utils
from rna_prop_ui import rna_idprop_ui_prop_get

AR = None

class LocationRef : 

    def __init__ (self, name, location=[0,0,0], type="body", autoRig=False) : 
        if autoRig : 
            self.createObject (name + "_arRef")
        else : 
            self.createObject (name + "_qrRef")

        self.object.location = location

        s = bpy.context.window_manager.quickRig.refsScale
        self.object.scale = [s,s,s]
        self.type = type # "body", "arm", "leg", "handFinger", "footFinger"

    def __del__(self) : 
        print ("delete : " + self.object.name)
        bpy.data.objects.remove (self.object, do_unlink=True)


    def createObject (self, name) : 
        
        self.setBMesh()

        self.mesh = bpy.data.meshes.new("LocationRef_data")
        self.object = bpy.data.objects.new(name, self.mesh)

        bpy.context.scene.collection.objects.link(self.object)
        self.bm.to_mesh(self.mesh) 
        self.bm.free()


    def setBMesh (self) :
        self.bm = LocationRef.bMesh()

    @staticmethod
    def bMesh() : 
        bm = bmesh.new() 

        x = bm.verts.new ((1,0,0))
        x1 = bm.verts.new ((-1,0,0))

        y = bm.verts.new ((0,1,0))
        y1 = bm.verts.new ((0,-1,0))

        z = bm.verts.new ((0,0,1))
        z1 = bm.verts.new ((0,0,-1))

        v = []
        v.append(x)
        v.append(x1)

        bm.edges.new(v)
        v=[]

        v.append(y)
        v.append(y1)
        bm.edges.new(v)
        v=[]

        v.append(z)
        v.append(z1)
        bm.edges.new(v)
        v=[]

        v = [x, y]
        bm.edges.new(v)

        v = [x, y1]
        bm.edges.new(v)
        v = [x1, y]
        bm.edges.new(v)
        v = [x1, y1]
        bm.edges.new(v)

        v = [z, x1]
        bm.edges.new(v)
        v = [z, x]
        bm.edges.new(v)

        v = [z1, x1]
        bm.edges.new(v)
        v = [z1, x]
        bm.edges.new(v)

        v = [z, y1]
        bm.edges.new(v)
        v = [z, y]
        bm.edges.new(v)

        v = [z1, y1]
        bm.edges.new(v)
        v = [z1, y]
        bm.edges.new(v)

        return bm

    def scale (self, f) : 
        self.object.scale = [f,f,f]

    def location2D(self) : 

        matrix = self.object.matrix_world
        x = matrix[0][3]
        y = matrix[1][3]
        z = matrix[2][3]

        loc = [x,y,z]

        # print (view3d_utils.location_3d_to_region_2d (bpy.context.region, bpy.context.space_data.region_3d, loc))
        return view3d_utils.location_3d_to_region_2d (bpy.context.region, bpy.context.space_data.region_3d, loc)

class Font : 

    def draw(loc2d, fontSize, color, text, xOffset = 0, yOffset = 0) : 
        blf.color(0, color[0], color[1], color[2], 1)

        blf.size (0, fontSize, 72)
        blf.position(0, loc2d[0] + xOffset, loc2d[1] + yOffset, 0)
        blf.draw(0, text)

class AutoRig : 
    def __init__(self) : 
        self.locators = Locators()

    @staticmethod
    def state () : 
        objects = bpy.context.scene.objects 
        state = "noGuides"
        for o in objects : 
            if "_arRef" in o.name : 
                state = "guides"
                return state

        return state

    @staticmethod
    def onLinkSidesChange (self, context) : 
        if self.link_Left_n_Right : 
            Locators.addMirrorHandler(AR)
        else : 
            Locators.removeMirrorHandler(AR)

class Locators : 
    def __init__(self, locators = []) : 
        self.list = locators

    def append(self, locationRef) : 
        self.list.append(locationRef)

    def clear(self) : 
        del self.list[:]

    def create (self) : 
        ar = bpy.context.window_manager.autoRig

        if ar.head : 
            head = LocationRef(name="head", type="body", autoRig=True, location=[0,0,10])
            self.append(head)
        
        if ar.neck : 
            neck = LocationRef(name="neck", type="body", autoRig=True, location=[0,0,9])
            self.append(neck)

        if ar.chest : 
            chest = LocationRef(name="chest", type="body", autoRig=True)
            self.append(chest)
        
        if ar.pelvis : 
            pelvis = LocationRef(name="pelvis", type="body", autoRig=True)
            self.append(pelvis)
        
        for i in range(ar.columns) : 
            col = LocationRef(name="column_" + str(i+1), type="body", autoRig=True)
            self.append(col)
        Locators.setConstraints(self.columns())
        # self.placeColumn()
        
        up = LocationRef(name="upArm_" + str(i+1) + ".R", type="arm", autoRig=True)
        dwn = LocationRef(name="dwnArm_" + str(i+1) + ".R", type="arm", autoRig=True)
        self.append(up)
        for i in range(ar.elbow_R) : 
            med = LocationRef(name="medArm_" + str(i+1) + ".R", type="arm", autoRig=True)
            self.append(med)

        self.append(dwn)
        Locators.setConstraints(self.arms("r"))
        
        up = LocationRef(name="upArm_" + str(i+1) + ".L", type="arm", autoRig=True)
        dwn = LocationRef(name="dwnArm_" + str(i+1) + ".L", type="arm", autoRig=True)
        self.append(up)
        for i in range(ar.elbow_L) : 
            med = LocationRef(name="medArm_" + str(i+1) + ".L", type="arm", autoRig=True)
            self.append(med)
        self.append(dwn)
        
        Locators.setConstraints(self.arms("l"))
        self.placeElbowsL()      
        
        up = LocationRef(name="upLeg_" + str(i+1) + ".R", type="leg", autoRig=True)
        dwn = LocationRef(name="dwnLeg_" + str(i+1) + ".R", type="leg", autoRig=True)
        self.append(up)
        for i in range(ar.knee_R) : 
            med = LocationRef(name="medLeg_" + str(i+1) + ".R", type="leg", autoRig=True)
            self.append(med)
        self.append(dwn)  

        Locators.setConstraints(self.legs("r"))
        
        up = LocationRef(name="upLeg_" + str(i+1) + ".L", type="leg", autoRig=True)
        dwn = LocationRef(name="dwnLeg_" + str(i+1) + ".L", type="leg", autoRig=True)
        self.append(up)
        for i in range(ar.knee_L) : 
            med = LocationRef(name="medLeg_" + str(i+1) + ".L", type="leg", autoRig=True)
            self.append(med)
        self.append(dwn)
        Locators.setConstraints(self.legs("l"))

        self.placeKneesL()     
        
        for i in range(ar.fingers_L) : 
            up = LocationRef(name="upFingerHand_" + str(i+1) + ".L", type="handFinger", autoRig=True)
            dwn = LocationRef(name="dwnFingerHand_" + str(i+1) + ".L", type="handFinger", autoRig=True)
            med = LocationRef(name="medFingerHand_" + str(i+1) + ".L", type="handFinger", autoRig=True)
            self.append(up) 
            self.append(dwn) 
            self.append(med) 
        
        for i in range(ar.fingers_R) : 
            up = LocationRef(name="upFingerHand_" + str(i+1) + ".R", type="handFinger", autoRig=True)
            dwn = LocationRef(name="dwnFingerHand_" + str(i+1) + ".R", type="handFinger", autoRig=True)
            med = LocationRef(name="medFingerHand_" + str(i+1) + ".R", type="handFinger", autoRig=True)
            self.append(up) 
            self.append(dwn) 
            self.append(med)     
        
        for i in range(ar.foot_L) : 
            up = LocationRef(name="upFingerFoot_" + str(i+1) + ".L", type="footFinger", autoRig=True)
            dwn = LocationRef(name="dwnFingerFoot_" + str(i+1) + ".L", type="footFinger", autoRig=True)
            med = LocationRef(name="medFingerFoot_" + str(i+1) + ".L", type="footFinger", autoRig=True)
            self.append(up)
            self.append(dwn)
            self.append(med)
        
        for i in range(ar.foot_R) : 
            up = LocationRef(name="upFingerFoot_" + str(i+1) + ".R", type="footFinger", autoRig=True)
            dwn = LocationRef(name="dwnFingerFoot_" + str(i+1) + ".R", type="footFinger", autoRig=True)
            med = LocationRef(name="medFingerFoot_" + str(i+1) + ".R", type="footFinger", autoRig=True)
            self.append(up)
            self.append(dwn)
            self.append(med)

        #locations # 

        self.pelvis().object.location = [0,0,5]
        self.chest().object.location = [0,0,8]

    def head(self) : 
        for l in self.list : 
            if l.object.name == "head_arRef" : 
                return l
        return None

    def neck(self) : 
        for l in self.list : 
            if l.object.name == "neck_arRef" : 
                return l
        return None

    def chest(self) : 
        for l in self.list : 
            if l.object.name == "chest_arRef" : 
                return l
        return None

    def columns(self, chest=True, pelvis=True) :
        toReturn = []
        for l in self.list : 
            if "column" in l.object.name : 
                toReturn.append(l)

        if chest : 
            toReturn.append (self.chest())
        if pelvis : 
            toReturn.insert(0, self.pelvis())
        return toReturn

    def pelvis(self) : 
        for l in self.list : 
            if l.object.name == "pelvis_arRef" : 
                return l
        return None

    def fingersMed(self, side="both", footOrHand = "hand") : 
        toReturn = []

        if side == "both" and footOrHand == "both" : 
            for l in self.list : 
                if "finger" in l.object.name : 
                    toReturn.append(l)

        elif side == "both" and footOrHand == "hand" : 
            for l in self.list : 
                if "fingerHand" in l.object.name : 
                    toReturn.append(l)

        elif side == "both" and footOrHand == "foot" : 
            for l in self.list : 
                if "fingerFoot" in l.object.name : 
                    toReturn.append(l) 

        elif side == "l" and footOrHand == "both" : 
            for l in self.list : 
                if "finger" in l.object.name and ".L" in l.object.name : 
                    toReturn.append(l)

        elif side == "r" and footOrHand == "both" : 
            for l in self.list : 
                if "finger" in l.object.name and ".R" in l.object.name : 
                    toReturn.append(l)

        elif side == "l" and footOrHand == "hand" : 
            for l in self.list : 
                if "fingerHand" in l.object.name and ".L" in l.object.name : 
                    toReturn.append(l)

        elif side == "r" and footOrHand == "hand" : 
            for l in self.list : 
                if "fingerHand" in l.object.name and ".R" in l.object.name : 
                    toReturn.append(l)

        elif side == "l" and footOrHand == "foot" : 
            for l in self.list : 
                if "fingerFoot" in l.object.name and ".L" in l.object.name : 
                    toReturn.append(l)

        elif side == "r" and footOrHand == "foot" : 
            for l in self.list : 
                if "fingerFoot" in l.object.name and ".R" in l.object.name : 
                    toReturn.append(l)

        return toReturn

    def elbowsMed(self, side="both", legOrArm = "arm") : 
        toReturn = []

        if side == "both" and legOrArm == "both" : 
            for l in self.list : 
                if "med" in l.object.name : 
                    toReturn.append(l)

        elif side == "both" and legOrArm == "arm" : 
            for l in self.list : 
                if "medArm" in l.object.name : 
                    toReturn.append(l)

        elif side == "both" and legOrArm == "leg" : 
            for l in self.list : 
                if "medLeg" in l.object.name : 
                    toReturn.append(l) 

        elif side == "l" and legOrArm == "both" : 
            for l in self.list : 
                if "med" in l.object.name and ".L" in l.object.name : 
                    toReturn.append(l)

        elif side == "r" and legOrArm == "both" : 
            for l in self.list : 
                if "med" in l.object.name and ".R" in l.object.name : 
                    toReturn.append(l)

        elif side == "l" and legOrArm == "arm" : 
            for l in self.list : 
                if "medArm" in l.object.name and ".L" in l.object.name : 
                    toReturn.append(l)

        elif side == "r" and legOrArm == "arm" : 
            for l in self.list : 
                if "medArm" in l.object.name and ".R" in l.object.name : 
                    toReturn.append(l)

        elif side == "l" and legOrArm == "leg" : 
            for l in self.list : 
                if "medLeg" in l.object.name and ".L" in l.object.name : 
                    toReturn.append(l)

        elif side == "r" and legOrArm == "leg" : 
            for l in self.list : 
                if "medLeg" in l.object.name and ".R" in l.object.name : 
                    toReturn.append(l)

        return toReturn

    def arms(self, side="both") : 
        toReturn = []
        for l in self.list : 
            if l.type == "arm" : 
                if side=="both" : 
                    toReturn.append (l)
                
                elif side=="l" : 
                    if '.L' in l.object.name : 
                        toReturn.append (l)

                elif side=="r" : 
                    if '.R' in l.object.name : 
                        toReturn.append (l)

        return toReturn


    def legs(self, side="both") : 
        toReturn = []
        for l in self.list : 
            if l.type == "leg" : 
                if side=="both" : 
                    toReturn.append (l)
                
                elif side=="l" : 
                    if '.L' in l.object.name : 
                        toReturn.append (l)

                elif side=="r" : 
                    if '.R' in l.object.name : 
                        toReturn.append (l)

        return toReturn

    def handFingers(self, side="both") : 
        toReturn = []
        for l in self.list : 
            if l.type == "handFinger" : 
                if side=="both" : 
                    toReturn.append (l)
                
                elif side=="l" : 
                    if '.L' in l.object.name : 
                        toReturn.append (l)

                elif side=="r" : 
                    if '.R' in l.object.name : 
                        toReturn.append (l)

        return toReturn

    def footFingers(self, side="both") : 
        toReturn = []
        for l in self.list : 
            if l.type == "foorFinger" : 
                if side=="both" : 
                    toReturn.append (l)
                
                elif side=="l" : 
                    if '.L' in l.object.name : 
                        toReturn.append (l)

                elif side=="r" : 
                    if '.R' in l.object.name : 
                        toReturn.append (l)

        return toReturn

    def lefts (self) : 
        toReturn = []
        for l in self.list : 
            if ".L" in l.object.name : 
                toReturn.append (l)

        return toReturn

    def rights (self) : 
        toReturn = []
        for l in self.list : 
            if ".R" in l.object.name : 
                toReturn.append (l)

        return toReturn

    def scale(self, context) : 
        wm = context.window_manager
        for l in self.list : 
            l.scale(wm.quickRig.refsScale)

    def placeColumn(self) : 
        posMin = 5
        posMax = 8
        r = posMax - posMin
        sides = self.columns()
        sides[0].object.location = [0, 0, posMin]
        sides[-1].object.location = [0, 0, posMax]

    def placeElbowsL(self) : 
        posMin = 0
        posMax = 5
        sides = self.arms("l")
        sides[0].object.location = [posMin + 1, 0, self.chest().object.location[2]]
        sides[-1].object.location = [posMax, 0, self.chest().object.location[2]]

    def placeKneesL(self) : 
        posMin = 5
        posMax = 0.25
        sides = self.legs("l")
        sides[0].object.location = [1, 0, posMin]
        sides[-1].object.location = [1, 0, posMax]

    def placeRight(self) : 
        lefts = self.lefts()
        right = self.rights()

        i = 0
        for l in right : 
            l.object.location = Locators.getInverseX(lefts[i].object.location)

            i+=1
        pass

    @staticmethod
    def setConstraints(locators) : 
        up = locators[0].object
        if len(locators)>3 : 
            mids = locators[1:len(locators)-1]
        else : 
            mids = [locators[1]]

        dwn = locators[-1].object

        i = 1
        for mid in mids : 
            
            coef = 1.0* (i/(len(mids)+1))

            o = mid.object

            pUp = o.constraints.new(type="CHILD_OF")
            pDown = o.constraints.new(type="CHILD_OF")
            
            pUp.influence = 1-coef
            pUp.use_rotation_x = False
            pUp.use_rotation_y = False
            pUp.use_rotation_z = False
            pUp.use_scale_x = False
            pUp.use_scale_y = False
            pUp.use_scale_z = False
            
            pDown.influence = coef
            pDown.use_rotation_x = False
            pDown.use_rotation_y = False
            pDown.use_rotation_z = False
            pDown.use_scale_x = False
            pDown.use_scale_y = False
            pDown.use_scale_z = False

            pUp.target = up
            pDown.target = dwn

            i+=1

    @staticmethod
    def setParent(child, parent, scale = False) : 
        c = child.constraints.new(type="CHILD_OF")

        c.influence = 1
        c.use_rotation_x = True
        c.use_rotation_y = True
        c.use_rotation_z = True

        if scale : 
            c.use_scale_x = True
            c.use_scale_y = True
            c.use_scale_z = True

        else : 
            c.use_scale_x = False
            c.use_scale_y = False
            c.use_scale_z = False

        c.target = parent

    @staticmethod
    def getInverseX (coor) : 
        return (-coor[0], coor[1], coor[2])
    
    @staticmethod
    def getInverseY (coor) : 
        return (coor[0], -coor[1], coor[2])
    
    @staticmethod
    def getInverseZ (coor) : 
        return (coor[0], coor[1], -coor[2])

    @staticmethod
    def handlerMirrorX(scene) : 
        global AR
        try : 
            AR.locators.placeRight()
        except : 
            pass

    @staticmethod
    def addMirrorHandler(autoRig) : 
        if Locators.handlerMirrorX not in bpy.app.handlers.depsgraph_update_post : 
            bpy.app.handlers.depsgraph_update_post.append(Locators.handlerMirrorX)

    @staticmethod
    def removeMirrorHandler(autoRig) : 
        if Locators.handlerMirrorX in bpy.app.handlers.depsgraph_update_post : 
            bpy.app.handlers.depsgraph_update_post.remove(Locators.handlerMirrorX)
    
    @staticmethod
    def clearHandlers(autoRig) : 
        if Locators.handlerMirrorX in bpy.app.handlers.depsgraph_update_post : 
            bpy.app.handlers.depsgraph_update_post.remove(Locators.handlerMirrorX)

class OpenGlDraw : 
    def __init__(self, font) : 
        self.font = font

    @staticmethod
    def draw_callback_px(self, context) : 
        wm = context.window_manager
        sc = context.scene
