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

#bl_infos#
bl_info = {
    "name": "",
    "description": "Muscles ",
    "author": "Romain Gilliot",
    "version": (1,0,0),
    "blender" : (2, 80, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": "" }
    
#bl_infos#
#imports#
import bpy
import sys
import bmesh
import mathutils as ma
import math

from lpqflv import lpqflv_popup as pp
from lpqflv import lpqflv_obj as objRead
from lpqflv import mesure as mes
from lpqflv.rigManager import drivers as driv


#imports#


class Muscle : 
    def __init__ (self, selection, side="") : 
        self.side = side
        if len(selection)<1 : 
            pp.popup("You must select at least one Armature", "ERROR")
            self.armature = False
            return

        if selection[0].type != "ARMATURE" : 
            pp.popup("The first selected object must be an Armature", "ERROR")
            self.armature = False 
            return

        self.armature = selection[0]

        if len(selection)<2 : 
            data = bpy.data.meshes.new("musclesShape")
            self.muscles = bpy.data.objects.new("muscle_rig" + self.side, data)

        self.sc = bpy.context.scene

    def simple(self) : 
        if self.armature == False : 
            return

        self.createMuscleMsh() 
        self.muscleOnLayer(10)
        self.createBones()
        self.bonesToLayer(16)
        self.createConstrain()
        self.skinMuscle()
        self.createShapes()
        self.sc.update()
        self.placeBones()
        self.setMaterial()

    def fourPoints(self) : 
        if self.armature == False : 
            return

        self.createFourPointsMsh() 
        self.muscleOnLayer(10) 
        self.create4Bones() 
        self.fourBonesToLayer(16)
        self.create4Constrains()
        self.skin4Muscle()
        self.createShapes(four = True)
        self.sc.update()
        self.placeBones(four = True)
        self.setMaterial()

    def threePoints(self) : 
        if self.armature == False : 
            return

        self.createMuscleMsh(path="/muscleModel3Pts.obj", three=True) 
        self.muscleOnLayer(10)
        self.create3Bones()
        self.threeBonesToLayer(16)
        self.create3Contrains()
        self.skin3Muscle()
        self.createShapes(three=True)
        self.placeBones(three = True)
        self.setMaterial()

    def createMuscleMsh(self, path = "/muscleModel.obj", three = False) : 
        obj = objRead.Obj (MUSCLES_OBJS + path)
        bm = obj.readLines()
        bmesh.ops.rotate(bm, 
            verts=bm.verts, 
            cent=(0,0,0), 
            matrix=ma.Matrix.Rotation(math.radians(90.0), 3, "X"))
        
        if three == False : 
            bmesh.ops.rotate(bm, 
                verts=bm.verts, 
                cent=(0,0,0), 
                matrix=ma.Matrix.Rotation(math.radians(90.0), 3, "Z"))

        self.rPos = bm.verts[0].co
        self.tPos = bm.verts[1].co
        if three : 
            self.midPos = [0,0,0]

        bm.to_mesh(self.muscles.data)
        bm.free() 
        self.sc.collection.objects.link(self.muscles)

    def createFourPointsMsh(self) : 
        obj = objRead.Obj (MUSCLES_OBJS + "/muscleModel4Pts.obj")
        bm = obj.readLines() 
        bmesh.ops.rotate(bm, 
            verts=bm.verts, 
            cent=(0,0,0), 
            matrix=ma.Matrix.Rotation(math.radians(90.0), 3, "X"))
        
        bmesh.ops.rotate(bm, 
            verts=bm.verts, 
            cent=(0,0,0), 
            matrix=ma.Matrix.Rotation(math.radians(90.0), 3, "Z"))

        self.pos1 =  mes.center([bm.verts[19], bm.verts[4]])#19-4
        self.pos2 =  mes.center([bm.verts[6], bm.verts[7]])#6-7
        self.pos3 =  mes.center([bm.verts[1], bm.verts[2]])#22-9
        self.pos4 =  mes.center([bm.verts[22], bm.verts[9]])#1-2

        bm.to_mesh(self.muscles.data)
        bm.free() 
        self.sc.collection.objects.link(self.muscles)

    def muscleOnLayer(self, layerNb) : 
        self.muscles.layers[layerNb] = True 
        for i in range(20) : 
            self.muscles.layers[i] = (i==layerNb)

        self.sc.layers[layerNb] = True

    def createBones(self) : 
        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set("INVOKE_DEFAULT", mode = 'EDITMODE_HLT')

        eBones = self.armature.data.edit_bones
        self.hBone = eBones.new("handle_muscle_head" + self.side)
        self.tBone = eBones.new("handle_muscle_tail" + self.side)
        self.skBone = eBones.new("sk_muscle" + self.side)

        self.hBone.head = self.rPos
        self.hBone.tail = self.rPos
        self.hBone.tail[1] += 1

        self.hBone.use_deform = False
        self.tBone.use_deform = False
        self.skBone.use_deform = True

        self.tBone.head = self.tPos
        self.tBone.tail = self.tPos
        self.tBone.tail[1] += 1

        self.skBone.head = self.rPos
        self.skBone.tail = self.tPos

        self.hBone.roll = 0
        self.tBone.roll = 0
        self.skBone.roll = 0

        self.skBone.parent = self.hBone

        self.hBone.use_inherit_rotation = False
        self.tBone.use_inherit_rotation = False
        self.skBone.use_inherit_rotation = False

    def create4Bones(self) : 
        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set("INVOKE_DEFAULT", mode = 'EDITMODE_HLT')

        eBones = self.armature.data.edit_bones
        self.c1 = eBones.new("handle_muscle" + self.side)
        self.c1Name = self.c1.name
        self.c1.use_deform = False

        self.c2 = eBones.new("handle_muscle" + self.side)
        self.c2Name = self.c2.name
        self.c2.use_deform = False

        self.c3 = eBones.new("handle_muscle" + self.side)
        self.c3Name = self.c3.name
        self.c3.use_deform = False

        self.c4 = eBones.new("handle_muscle" + self.side)
        self.c4Name = self.c4.name
        self.c4.use_deform = False

        # skbines
        self.sk1 = eBones.new("sk_muscle" + self.side)
        self.sk1Name = self.sk1.name

        self.sk2 = eBones.new("sk_muscle" + self.side)
        self.sk2Name = self.sk2.name

        self.sk3 = eBones.new("sk_muscle" + self.side)
        self.sk3Name = self.sk3.name

        self.sk4 = eBones.new("sk_muscle" + self.side)
        self.sk4Name = self.sk4.name

        #position the bones # 
        #controllers 

        self.c1.head = self.pos1
        self.c1.tail = self.pos1
        self.c1.tail[1] += 0.25

        self.c2.head = self.pos2
        self.c2.tail = self.pos2
        self.c2.tail[1] += 0.25

        self.c3.head = self.pos3
        self.c3.tail = self.pos3
        self.c3.tail[1] += 0.25

        self.c4.head = self.pos4
        self.c4.tail = self.pos4
        self.c4.tail[1] += 0.25

        #sk bones

        self.sk1.head = self.pos1
        self.sk1.tail = self.pos2

        self.sk2.head = self.pos4
        self.sk2.tail = self.pos2

        self.sk3.head = self.pos3
        self.sk3.tail = self.pos1

        self.sk4.head = self.pos3
        self.sk4.tail = self.pos4

        #parents
        self.sk1.parent = self.c1
        self.sk2.parent = self.c4
        self.sk3.parent = self.c3
        self.sk4.parent = self.c3

        #rotations 
        self.c1.use_inherit_rotation = False
        self.c2.use_inherit_rotation = False
        self.c3.use_inherit_rotation = False
        self.c4.use_inherit_rotation = False

    def create3Bones(self) : 
        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set("INVOKE_DEFAULT", mode = 'EDITMODE_HLT')

        eb = self.armature.data.edit_bones

        self.hName = eb.new("handle_muscle_head" + self.side).name
        self.midName = eb.new("handle_muscle_midle" + self.side).name
        self.tName = eb.new("handle_muscle_tail" + self.side).name
        self.sk1Name = eb.new("sk_muscle" + self.side).name
        self.sk2Name = eb.new("sk_muscle" + self.side).name

        eb[self.hName].head = self.rPos
        eb[self.hName].tail = self.rPos
        eb[self.hName].tail[1] +=1

        eb[self.midName].head = self.midPos
        eb[self.midName].tail = self.midPos
        eb[self.midName].tail[1] +=1

        eb[self.tName].head = self.tPos
        eb[self.tName].tail = self.tPos
        eb[self.tName].tail[1] += 1

        eb[self.sk1Name].head = eb[self.hName].head
        eb[self.sk1Name].tail = eb[self.midName].head

        eb[self.sk2Name].head = eb[self.midName].head
        eb[self.sk2Name].tail = eb[self.tName].head

        eb[self.hName].use_deform = False
        eb[self.midName].use_deform = False
        eb[self.tName].use_deform = False

        eb[self.hName].use_inherit_rotation = False
        eb[self.midName].use_inherit_rotation = False
        eb[self.tName].use_inherit_rotation = False
        eb[self.sk1Name].use_inherit_rotation = False
        eb[self.sk2Name].use_inherit_rotation = False

        eb[self.hName].roll = 0        
        eb[self.midName].roll = 0
        eb[self.tName].roll = 0
        eb[self.sk1Name].roll = 0
        eb[self.sk2Name].roll = 0

        eb[self.sk1Name].parent = eb[self.hName]
        eb[self.sk2Name].parent = eb[self.midName]

    def bonesToLayer(self, layerNb) : 

        self.hBone.layers[8] = True
        self.tBone.layers[8] = True
        self.skBone.layers[layerNb] = True

        for i in range (32) : 
            self.hBone.layers[i] = (i == 8)
            self.tBone.layers[i] = (i == 8)
            self.skBone.layers[i] = (i == layerNb)

        self.armature.data.layers[8] = True

    def fourBonesToLayer(self, layerNb) : 
        self.c1.layers[8] = True
        self.c2.layers[8] = True
        self.c3.layers[8] = True
        self.c4.layers[8] = True

        self.sk1.layers[layerNb] = True
        self.sk2.layers[layerNb] = True
        self.sk3.layers[layerNb] = True
        self.sk4.layers[layerNb] = True

        for i in range(32) : 
            self.c1.layers[i] = (i == 8)
            self.c2.layers[i] = (i == 8)
            self.c3.layers[i] = (i == 8)
            self.c4.layers[i] = (i == 8)

            self.sk1.layers[i] = (i == layerNb)
            self.sk2.layers[i] = (i == layerNb)
            self.sk3.layers[i] = (i == layerNb)
            self.sk4.layers[i] = (i == layerNb)
 
        self.armature.data.layers[8] = True

    def threeBonesToLayer (self, layerNb) : 
        eb = self.armature.data.edit_bones

        eb[self.hName].layers[8] = True
        eb[self.midName].layers[8] = True
        eb[self.tName].layers[8] = True

        eb[self.sk1Name].layers[layerNb] = True
        eb[self.sk2Name].layers[layerNb] = True

        self.armature.data.layers[8] = True

        for i in range(32) : 
            eb[self.hName].layers[i] = (i==8)
            eb[self.midName].layers[i] = (i==8)
            eb[self.tName].layers[i] = (i==8) 

            eb[self.sk1Name].layers[i] = (i == layerNb)
            eb[self.sk2Name].layers[i] = (i == layerNb)

    def createConstrain(self) : 
        self.skn = self.skBone.name 
        self.hn = self.hBone.name 
        self.tn = self.tBone.name

        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set("INVOKE_DEFAULT", mode = 'POSE')

        pBones = self.armature.pose.bones
        self.pose_skBone = pBones[self.skn]
        self.strech = self.pose_skBone.constraints.new("STRETCH_TO")
        self.strech.target = self.armature
        self.strech.subtarget = self.tn

        self.pose_hBone = pBones[self.hn]
        self.pose_tBone = pBones[self.tn]

        self.strech.keep_axis = 'PLANE_Z'

    def create4Constrains(self) : 
        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set("INVOKE_DEFAULT", mode = 'POSE')

        poses = self.armature.pose.bones
        self.st1 = poses[self.sk1Name].constraints.new("STRETCH_TO")
        self.st1.target = self.armature
        self.st1.subtarget = self.c2Name

        self.st2 = poses[self.sk2Name].constraints.new("STRETCH_TO")
        self.st2.target = self.armature
        self.st2.subtarget = self.c2Name

        self.st3 = poses[self.sk3Name].constraints.new("STRETCH_TO")
        self.st3.target = self.armature
        self.st3.subtarget = self.c1Name

        self.st4 = poses[self.sk4Name].constraints.new("STRETCH_TO")
        self.st4.target = self.armature
        self.st4.subtarget = self.c4Name

        self.sc.update()

    def create3Contrains(self) : 
        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set("INVOKE_DEFAULT", mode = 'POSE')

        poses = self.armature.pose.bones
        self.st1 = poses[self.sk1Name].constraints.new("STRETCH_TO")
        self.st1.target = self.armature
        self.st1.subtarget = self.midName

        self.st2 = poses[self.sk2Name].constraints.new("STRETCH_TO")
        self.st2.target = self.armature
        self.st2.subtarget = self.tName

        self.sc.id_data.update()

    def skinMuscle(self) : 

        self.skinModifier = None

        for m in self.muscles.modifiers : 
            if m.type == "ARMATURE" : 
                self.skinModifier = m 

        if self.skinModifier == None : 
            self.skinModifier = self.muscles.modifiers.new(type="ARMATURE", name=self.skn)
            self.skinModifier.object = self.armature
            self.skinModifier.show_in_editmode = True 
            self.skinModifier.show_on_cage = True

        self.vg = self.muscles.vertex_groups.new(self.skn)
        i = 0 
        while i< len(self.muscles.data.vertices) : 
            if len(self.muscles.data.vertices[i].groups) == 0 : 
                self.vg.add([i], 1, 'REPLACE')
            i+=1

        self.sc.update()

        # subsrf # 
        sbs = self.muscles.modifiers.new(type="SUBSURF", name="subdiv")
        sbs.levels = 2
        sbs.show_on_cage = True

        self.sc.update()

    def skin4Muscle (self) : 
        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set("INVOKE_DEFAULT", mode = 'OBJECT')

        self.skinModifier = None

        for m in self.muscles.modifiers : 
            if m.type == "ARMATURE" : 
                self.skinModifier = m 
        
        if self.skinModifier == None : 
            self.skinModifier = self.muscles.modifiers.new(type="ARMATURE", name=self.sk1Name)
            self.skinModifier.object = self.armature
            self.skinModifier.show_in_editmode = True 
            self.skinModifier.show_on_cage = True

        self.vg1 = self.muscles.vertex_groups.new(self.sk1Name)
        self.vg2 = self.muscles.vertex_groups.new(self.sk2Name)
        self.vg3 = self.muscles.vertex_groups.new(self.sk3Name)
        self.vg4 = self.muscles.vertex_groups.new(self.sk4Name)

        self.vg1.add([6,7,15,10,20,5,31,27,28,12,19,4], 1, 'REPLACE')
        self.vg2.add([22,9,8,21,23,13,15,10,16,11,6,7], 1, 'REPLACE')
        self.vg3.add([19,4,31,18,3,27,26,30,25,14,1,2], 1, 'REPLACE')
        self.vg4.add([1,2,0,17,26,30,23,24,13,29,22,9], 1, 'REPLACE')

        self.sc.update()

        # subsrf # 
        sbs = self.muscles.modifiers.new(type="SUBSURF", name="subdiv")
        sbs.levels = 2
        sbs.show_on_cage = True

        self.sc.update()

    def skin3Muscle (self) : 
        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set("INVOKE_DEFAULT", mode = 'OBJECT')

        self.skinModifier = None

        for m in self.muscles.modifiers : 
            if m.type == "ARMATURE" : 
                self.skinModifier = m 
        
        if self.skinModifier == None : 
            self.skinModifier = self.muscles.modifiers.new(type="ARMATURE", name=self.sk1Name)
            self.skinModifier.object = self.armature
            self.skinModifier.show_in_editmode = True 
            self.skinModifier.show_on_cage = True

        self.skinModifier.use_deform_preserve_volume = True

        self.vg1 = self.muscles.vertex_groups.new(self.sk1Name)
        self.vg2 = self.muscles.vertex_groups.new(self.sk2Name)

        self.vg1.add([0], 1, 'REPLACE')
        self.vg1.add([4,25,6,22,8,19,16,11], 1, 'REPLACE')
        self.vg1.add([3,24,5,21,18,10,15,13], 0.5, 'REPLACE')
        
        self.vg2.add([1], 1, 'REPLACE')
        self.vg2.add([3,24,5,21,18,10,15,13], 0.5, 'REPLACE')
        self.vg2.add([2,23,7,20,17,9,14,12], 1, 'REPLACE')

        # subsrf # 
        sbs = self.muscles.modifiers.new(type="SUBSURF", name="subdiv")
        sbs.levels = 2
        sbs.show_on_cage = True

        self.sc.update()

    def createShapes(self, four = False, three = False) : 

        d = None

        try :
            self.cubeShape = bpy.data.objects["rigShape_cube"]
            d = self.cubeShape.data
        except:
            d = bpy.data.meshes.new("cube")
            self.cubeShape = bpy.data.objects.new("rigShape_cube", d)
            self.sc.collection.objects.link(self.cubeShape)

        bm = bmesh.new()
        bm.from_mesh(d)
        bmesh.ops.create_cube(bm, size=1.0, matrix=ma.Matrix.Identity(4), calc_uvs=False)
        bm.to_mesh(d)
        bm.free()

        pb = self.armature.pose.bones
        if four : 
            pb[self.c1Name].bone.show_wire = True
            pb[self.c2Name].bone.show_wire = True
            pb[self.c3Name].bone.show_wire = True
            pb[self.c4Name].bone.show_wire = True

            pb[self.c1Name].custom_shape = self.cubeShape
            pb[self.c2Name].custom_shape = self.cubeShape
            pb[self.c3Name].custom_shape = self.cubeShape
            pb[self.c4Name].custom_shape = self.cubeShape

        elif three : 
            pb[self.hName].bone.show_wire = True
            pb[self.midName].bone.show_wire = True
            pb[self.tName].bone.show_wire = True

            pb[self.hName].custom_shape = self.cubeShape
            pb[self.midName].custom_shape = self.cubeShape
            pb[self.tName].custom_shape = self.cubeShape

        else : 
            self.pose_hBone.bone.show_wire = True
            self.pose_hBone.custom_shape = self.cubeShape
            self.pose_tBone.bone.show_wire = True
            self.pose_tBone.custom_shape = self.cubeShape

        self.cubeShape.hide_viewport = True

    def placeBones (self, four = False, three=False) : 
        
        if four == False and three == False: 
            hbName = self.pose_hBone.name 
            tbName = self.pose_tBone.name

        selected_bones = []

        for pb in self.armature.pose.bones : 
            if pb.bone.select_get( : )
                selected_bones.append(pb)

        if (len(selected_bones) == 0) : 
            return 

        last = None
        for pb in selected_bones : 
            if bpy.context.active_bone.name == pb.bone.name : 
                last= pb
                selected_bones.remove (pb)

        if last == None : 
            pp.popup("The last bone must be the active one\nNo bone in active.", "ERROR")
            return

        if len(selected_bones) == 0 : 
            return
        
        first = selected_bones[0]

        fpos = first.head
        lpos = last.head

        pb = self.armature.pose.bones

        if four : 
            fpos = [fpos[0] - pb[self.c3Name].head[0],
                    fpos[1] - pb[self.c3Name].head[1],
                    fpos[2] - pb[self.c3Name].head[2]]
            
            lpos = [lpos[0] - pb[self.c2Name].head[0],
                    lpos[1] - pb[self.c2Name].head[1],
                    lpos[2] - pb[self.c2Name].head[2]]

            pb[self.c1Name].location = [lpos[0] + 1, lpos[1], lpos[2]]
            pb[self.c4Name].location = [fpos[0] - 1, fpos[1], fpos[2]]

            pb[self.c2Name].location = lpos
            pb[self.c3Name].location = fpos

        elif three : 
            fpos = [fpos[0] - pb[self.hName].head[0],
                    fpos[1] - pb[self.hName].head[1],
                    fpos[2] - pb[self.hName].head[2]]
            
            lpos = [lpos[0] - pb[self.tName].head[0],
                    lpos[1] - pb[self.tName].head[1],
                    lpos[2] - pb[self.tName].head[2]]

            pb[self.hName].location = fpos
            pb[self.midName].location = [fpos[0] + 1, fpos[1], fpos[2]]
            pb[self.tName].location = lpos

        else : 
            fpos = [fpos[0] - self.pose_hBone.head[0],
                    fpos[1] - self.pose_hBone.head[1],
                    fpos[2] - self.pose_hBone.head[2]]
            
            lpos = [lpos[0] - self.pose_tBone.head[0],
                    lpos[1] - self.pose_tBone.head[1],
                    lpos[2] - self.pose_tBone.head[2]]

            self.pose_hBone.location = fpos
            self.pose_tBone.location = lpos

        firstName = first.name 
        lastName = last.name

        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set("INVOKE_DEFAULT", mode = 'EDITMODE_HLT')

        edits = self.armature.data.edit_bones
        currentDist = mes.dist(edits[firstName].head, edits[lastName].head)

        if four : 
            origDist = mes.dist(edits[self.c2Name].head, edits[self.c3Name].head)
            nScale = currentDist/origDist

            if bpy.ops.object.mode_set.poll():
                bpy.ops.object.mode_set("INVOKE_DEFAULT", mode = 'POSE')

            pb[self.c1Name].scale = [nScale, nScale, nScale]
            pb[self.c2Name].scale = [nScale, nScale, nScale]
            pb[self.c3Name].scale = [nScale, nScale, nScale]
            pb[self.c4Name].scale = [nScale, nScale, nScale]

            self.sc.update()
            if bpy.ops.object.mode_set.poll():
                bpy.ops.object.mode_set("INVOKE_DEFAULT", mode = 'EDITMODE_HLT')

            edits[self.c2Name].parent = edits[lastName]
            edits[self.c3Name].parent = edits[firstName]

        elif three : 
            origDist = mes.dist(edits[self.hName].head, edits[self.tName].head)
            nScale = currentDist/origDist

            if bpy.ops.object.mode_set.poll():
                bpy.ops.object.mode_set("INVOKE_DEFAULT", mode = 'POSE')

            pb[self.hName].scale = [nScale, nScale, nScale]
            pb[self.midName].scale = [nScale, nScale, nScale]
            pb[self.tName].scale = [nScale, nScale, nScale]

            self.sc.update()

            if bpy.ops.object.mode_set.poll():
                bpy.ops.object.mode_set("INVOKE_DEFAULT", mode = 'EDITMODE_HLT')

            edits[self.hName].parent = edits[firstName]
            edits[self.midName].parent = edits[firstName]
            edits[self.tName].parent = edits[lastName]

        else : 
            origDist = mes.dist(edits[hbName].head, edits[tbName].head)
            
            nScale = currentDist/origDist

            if bpy.ops.object.mode_set.poll():
                bpy.ops.object.mode_set("INVOKE_DEFAULT", mode = 'POSE')

            self.pose_hBone.scale = [nScale, nScale, nScale]
            self.pose_tBone.scale = [nScale, nScale, nScale]

            self.sc.update()

            if bpy.ops.object.mode_set.poll():
                bpy.ops.object.mode_set("INVOKE_DEFAULT", mode = 'EDITMODE_HLT')

            edits[hbName].parent = edits[firstName]
            edits[tbName].parent = edits[lastName]

        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set("INVOKE_DEFAULT", mode = 'POSE')

    def setMaterial(self) : 
        
        sh = bpy.data.materials.get("sh_muscle_rig")

        if sh == None :
            sh = bpy.data.materials.new("sh_muscle_rig")
            sh.diffuse_color = [0.8, 0.118, 0.053]

        obj = self.muscles
        if "muscle_rig" in obj.name : 
            if obj.data.materials : 
                obj.data.materials[0] = sh
            else : 
                obj.data.materials.append (sh)

class MuscleMesh : 

    vertices = []
    name =""

    def fromObject(self, object) : 
        sc = bpy.context.scene

        sc.update()

        data = object.to_mesh(sc, True, 'PREVIEW')

        self.vertices = [v.co.copy() for v in data.vertices]
        self.name = object.name
        bpy.data.meshes.remove(data)

        sc.update()

class Muscles : 
    
    def __init__ (self, selection) :   
        self.ok = True 
        if len (selection) == 0 or selection[0].type != "MESH": 
            pp.popup("You have to select the skinned mesh first.", "ERROR")
            self.ok = False
            return 

        self.meshes = []
        self.muscleMeshes = []
        self.toSkinn = selection[0]
        self.scene = bpy.context.scene
        self.objects = self.scene.objects

        for obj in self.objects : 
            if "muscle_rig" in obj.name : 
                self.meshes.append (obj)

        if len(self.meshes) == 0 : 
            pp.popup("You have to create some muscles first.", "ERROR")
            self.ok = False
            return

    def createVertexGroups (self) : 
        if self.ok==False : 
            return 

        vGrps = self.toSkinn.vertex_groups
        self.musclesGrps = []
        exist = False

        for m in self.meshes : 
            for vGrp in vGrps : 
                if vGrp.name == m.name : 
                    exist = True
                    self.musclesGrps.append (vGrp)
                    break
            if exist == False : 
                grp = vGrps.new (m.name)
                self.musclesGrps.append (grp)

    def deformedMusclesVert (self) : 
        for m in self.meshes : 
            mm = MuscleMesh() 
            mm.fromObject(m)
            self.muscleMeshes.append(mm)

    def setVertexGroups (self) : 
        minDist = bpy.context.window_manager.muscles.bindDistance
        sVerts = self.toSkinn.data.vertices

        for mm in self.muscleMeshes : 
            grp = self.toSkinn.vertex_groups[mm.name]
            i=0
            dists = []
            while i<len(sVerts) : 
                worldCo = self.toSkinn.matrix_world * sVerts[i].co
                for v in mm.vertices : 
                    dist = mes.dist(worldCo, v)
                    if dist<minDist : 
                        sVerts[i].select_set(True))
                        grp.add ([i], 1, 'REPLACE')
                        break
                    else : 
                        grp.remove ([i])
                i+=1

    def smoothVertexGroups (self) : 
        self.view_layer.objects.active = self.toSkinn

        bpy.ops.object.mode_set(mode="WEIGHT_PAINT")
        for grp in self.musclesGrps : 
            self.toSkinn.vertex_groups.active_index = grp.index
            self.scene.update() 
            bpy.ops.object.vertex_group_smooth(group_select_mode= 'ACTIVE', 
                factor = 1, 
                repeat=2)

        bpy.ops.object.mode_set(mode="OBJECT")

    def createWraps (self) : 
        exist = False

        for m in self.toSkinn.modifiers : 
            for grp in self.musclesGrps : 
                if "wrap_" + grp.name == m.name : 
                    exist = True

        if exist : 
            return

        for grp in self.musclesGrps : 
            wrap = self.toSkinn.modifiers.new(type="SHRINKWRAP", name="wrap_" + grp.name)
            wrap.vertex_group = grp.name
            wrap.target = self.objects[grp.name]
            wrap.show_expanded = False

    def mvSubsurf (self) : 

        if self.toSkinn.modifiers[-1].type != "SUBSURF" or self.toSkinn.modifiers[-1].type != "MULTIRES" : 
            return

        sub = None

        for m in self.toSkinn.modifiers : 
            if m.type == "SUBSURF" or m.type == "MULTIRES" : 
                sub = m
                break

        if sub == None : 
            return

        self.view_layer.objects.active = self.toSkinn
        while self.toSkinn.modifiers[-1].type != "SUBSURF" or self.toSkinn.modifiers[-1].type != "MULTIRES": 
            bpy.ops.object.modifiers_move_down(modifier=sub.name)

    def bind(self) : 
        if self.ok == False : 
            return
        self.createVertexGroups()
        self.deformedMusclesVert()
        self.setVertexGroups()
        self.smoothVertexGroups()
        self.createWraps()
        self.mvSubsurf()

    @staticmethod
    def onActiveAllChange (self, context) : 
        for o in context.scene.objects : 
            if o.type == "MESH" : 
                for m in o.modifiers : 
                    if "wrap_muscle_rig" in m .name : 
                        if self.active : 
                            m.show_viewport = True 
                        else : 
                            m.show_viewport = False

    @staticmethod
    def onActiveMuscleChange (self, context) : 
        for o in context.scene.objects : 
            if o.type == "MESH" : 
                for m in o.modifiers : 
                    if "wrap_muscle_rig" in m.name : 
                        if m.target == self.id_data : 
                            if self.active : 
                                m.show_viewport = True 
                            else : 
                                m.show_viewport = False

    @staticmethod
    def onActiveObjectChange (self, context) :  
        for m in self.id_data.modifiers : 
            if "wrap_muscle_rig" in m.name : 
                if self.activeDeform : 
                    m.show_viewport = True
                else : 
                    m.show_viewport = False
    
    @staticmethod
    def onActiveRenderAllChange (self, context) : 
        for o in context.scene.objects : 
            if o.type == "MESH" : 
                for m in o.modifiers : 
                    if "wrap_muscle_rig" in m .name : 
                        if self.activeRender : 
                            m.show_render = True 
                        else : 
                            m.show_render = False

    @staticmethod
    def onActiveRenderMuscleChange (self, context) : 
        for o in context.scene.objects : 
            if o.type == "MESH" : 
                for m in o.modifiers : 
                    if "wrap_muscle_rig" in m.name : 
                        if m.target == self.id_data : 
                            if self.activeRender : 
                                m.show_render = True 
                            else : 
                                m.show_render = False

    @staticmethod
    def onActiveRenderObjectChange (self, context) :  
        for m in self.id_data.modifiers : 
            if "wrap_muscle_rig" in m.name : 
                if self.activeDeformRender : 
                    m.show_render = True
                else : 
                    m.show_render = False

    @staticmethod 
    def onVolumeDistortChange (self, context) : 
        bn = self.id_data.vertex_groups[0].name 
        armatures = []

        for m in self.id_data.modifiers : 
            if m.type == "ARMATURE" : 
                armatures.append (m.object)

        for a in armatures : 
            b = a.pose.bones[bn]
            b.constraints[0].bulge = self.volumeVariation

    
    # mirrors # 

    @staticmethod
    def toggleMirror(self = None, context = bpy.context) : 
        if context.window_manager.muscles.mirrorX == False and context.window_manager.muscles.mirrorY == False and context.window_manager.muscles.mirrorZ == False : 
            print (Muscles.mirrorHandler in bpy.app.handlers.depsgraph_update_post)
            if Muscles.mirrorHandler in bpy.app.handlers.depsgraph_update_post : 
                bpy.app.handlers.depsgraph_update_post.remove(Muscles.mirrorHandler)
        else : 
            if Muscles.mirrorHandler not in bpy.app.handlers.depsgraph_update_post : 
                bpy.app.handlers.depsgraph_update_post.append(Muscles.mirrorHandler)

        context.scene.update()

    @staticmethod
    def removeMirrorhandler() :
        if Muscles.mirrorHandler in bpy.app.handlers.depsgraph_update_post : 
            bpy.app.handlers.depsgraph_update_post.remove(Muscles.mirrorHandler)

    @staticmethod
    def mirrorHandler (scene) : 
        ctx = bpy.context 
        musclesSettings = ctx.window_manager.muscles
        armature = ctx.object
        if armature == None or armature.type !="ARMATURE" or armature.mode !="POSE": 
            return
        
        handlesL = [] 
        handles = []
        for pb in armature.pose.bones : 
            if "handle_muscle" in pb.name and ".L" in pb.name : 
                handlesL.append (pb)

        if len(handlesL)==0 : 
            return 

        for pb in handlesL : 
            nameR = pb.name.replace(".L", ".R")
            if armature.pose.bones.find(nameR) != -1 : 
                handles.append ((pb, armature.pose.bones[nameR])) # left n right tuple

        if (len(handles)==0) : 
            return

        for couple in handles : 

            mR = ma.Matrix()
            mR[0] = couple[0].matrix[0]
            mR[1] = couple[0].matrix[1]
            mR[2] = couple[0].matrix[2]

            if musclesSettings.mirrorX : 
                mR[0][3] = -couple[0].matrix[0][3]
            if musclesSettings.mirrorY : 
                mR[1][3] = -couple[0].matrix[1][3]
            if musclesSettings.mirrorZ : 
                mR[2][3] = -couple[0].matrix[2][3]

            couple[1].matrix = mR


class Drivers : 
    def __init__(self, selected) : 
        self.select_get(ed = None )
        self.bone = None 
        self.shapeKey = None 
        self.armature = None

        if len(selected)<2 : 
            pp.popup("You have to select the muscle (with the active shape at 1)\nand then the driver bone", "ERROR") 
            return 

        for o in selected : 
            if o.type == "MESH" : 
                self.shapeKey = o.active_shape_key
            elif o.type == "ARMATURE" : 
                self.bone = o.pose.bones[bpy.context.active_bone.name] 
                self.armature = self.bone.id_data

        if self.bone == None or self.shapeKey == None : 
            pp.popup("Error in your selection.\nSelect the muscle then the driver bone (in pose mode)", "ERROR")
            return

    def makeDriver (self) : 
        if self.bone == None or self.shapeKey == None : 
            return

        transformType = bpy.context.window_manager.muscles.driverTransformType
        transformSpace = bpy.context.window_manager.muscles.driverTransformSpace

        self.fc = driv.createTransformDrivenKey(self.shapeKey, self.bone, transformType, transformSpace)

        k0 = self.fc.keyframe_points[0]
        k1 = self.fc.keyframe_points[1]

        if transformSpace == "LOCAL_SPACE" : 
            axis = transformType.split("_")[-1]
            if "LOC" in transformType : 
                if axis == "X" : 
                    if self.location[0]<0 : 
                        k0.co = [self.bone.location[0], 1]
                        k1.co = [0,0]
                    else : 
                        k1.co = [self.bone.location[0], 1]
                        k0.co = [0,0]

                elif axis == "Y" : 
                    if self.location[1]<0 : 
                        k0.co = [self.bone.location[1], 1]
                        k1.co = [0,0]
                    else :
                        k1.co = [self.bone.location[1], 1]
                        k0.co = [0,0]

                else : 
                    if self.location[2]<0 : 
                        k0.co = [self.bone.location[2], 1]
                        k1.co = [0,0]
                    else : 
                        k1.co = [self.bone.location[2], 1]
                        k0.co = [0,0]

            elif "ROT" in transformType : 
                oldRotMode = self.bone.rotation_mode 
                self.bone.rotation_mode = "XYZ"
                bpy.context.scene.update()
                print (self.bone.rotation_euler[2])
                if axis == "X" : 
                    if self.bone.rotation_euler[0]<0 : 
                        k0.co = [self.bone.rotation_euler[0], 1]
                        k1.co = [0,0]
                    else : 
                        k1.co = [self.bone.rotation_euler[0], 1]
                        k0.co = [0,0]

                elif axis == "Y" : 
                    if self.bone.rotation_euler[1]<0 : 
                        k0.co = [self.bone.rotation_euler[1], 1]
                        k1.co = [0,0]
                    else :
                        k1.co = [self.bone.rotation_euler[1], 1]
                        k0.co = [0,0]

                else :
                    if self.bone.rotation_euler[2]<0 :  
                        k0.co = [self.bone.rotation_euler[2], 1]
                        k1.co = [0,0]
                    else :
                        k1.co = [self.bone.rotation_euler[2], 1]
                        k0.co = [0,0]

                print (k0.co)
                print (k1.co)
                bpy.context.scene.update()
                self.bone.rotation_mode = oldRotMode

            else : 
                if axis == "X" : 
                    if self.bone.scale[0]<0 : 
                        k0.co = [self.bone.scale[0], 1]
                    else : 
                        k1.co = [self.bone.scale[0], 1]

                elif axis == "Y" : 
                    if self.bone.scale[1]<0 : 
                        k0.co = [self.bone.scale[1], 1]
                    else :
                        k1.co = [self.bone.scale[1], 1]

                else : 
                    if self.bone.scale[2]<0 : 
                        k0.co = [self.bone.scale[2], 1]
                    else :
                        k1.co = [self.bone.scale[2], 1]

#operators#
#operator - Simple#
class Simple (bpy.types.Operator):
    bl_idname = "lpqflv_rig.simple"
    bl_label = "Simple"
    bl_description = "Create a simple muscle"
    bl_options = {'REGISTER'}
    @classmethod
    def poll(cls, context):
        return True
    def execute(self, context):
        
        if context.window_manager.muscles.mirrorX or context.window_manager.muscles.mirrorY or context.window_manager.muscles.mirrorZ: 
            m = Muscle(context.selected_objects, side=".L"))
            m.simple()
            m = Muscle(context.selected_objects, side=".R"))
            m.simple()
        else :
            m = Muscle(context.selected_objects))
            m.simple()
        return {"FINISHED"} 
        
#operator - Simple#
#operator - Arm#
class FourPts (bpy.types.Operator):
    bl_idname = "lpqflv_rig.four_pts_muscle"
    bl_label = "4 Points" 
    bl_description = "Create a muscle with 4 controlers" 
    bl_options = {'REGISTER'}
    @classmethod
    def poll(cls, context):
        return True
    def execute(self, context):
        if context.window_manager.muscles.mirrorX or context.window_manager.muscles.mirrorY or context.window_manager.muscles.mirrorZ: 
            m = Muscle(context.selected_objects, side=".L"))
            m.fourPoints()
            m = Muscle(context.selected_objects, side=".R"))
            m.fourPoints()
        else : 
            m = Muscle(context.selected_objects))
            m.fourPoints()
        return {"FINISHED"} 
        
#operator - Arm#
#operator - Leg#
class ThreePts (bpy.types.Operator):
    bl_idname = "lpqflv_rig.three_pts_muscle"
    bl_label = "3 Points"
    bl_description = "Create a muscle with 3 controlers"
    bl_options = {'REGISTER'}
    @classmethod
    def poll(cls, context):
        return True
    def execute(self, context):
        if context.window_manager.muscles.mirrorX or context.window_manager.muscles.mirrorY or context.window_manager.muscles.mirrorZ: 
            m = Muscle(context.selected_objects, side = ".L"))
            m.threePoints()
            context.scene.update()
            m = Muscle(context.selected_objects, side = ".R"))
            m.threePoints()
        else : 
            m = Muscle(context.selected_objects))
            m.threePoints()
        return {"FINISHED"}

class Transparent (bpy.types.Operator):
    bl_idname = "lpqflv_rig.transparent_toggle"
    bl_label = "Toggle Transparent"
    bl_description = "Set the selected object transparent on/off"
    bl_options = {'REGISTER'}
    @classmethod
    def poll(cls, context):
        if context.object : 
            try : 
                if context.object.type == "MESH" : 
                    return True 
                else : 
                    return False 
            except : 
                return False
        else : 
            return False

    def execute(self, context):

        obj = context.object
        if obj.show_transparent : # rendre non transparent
            obj.show_transparent = False

        else : 
            obj.show_transparent = True 
            
            if obj.data.materials : 
                pass
            else : 
                sh = bpy.data.materials.new("sh_transparent")
                obj.data.materials.append (sh)

            sh = obj.data.materials[0]
            sh.alpha = 0.350
            sh.diffuse_color = [0.8, 0.8, 0.8]

        return {"FINISHED"}


class ToggleMuscles (bpy.types.Operator):
    bl_idname = "lpqflv_rig.show_hide_muscles"
    bl_label = "Show/Hide Muscles"
    bl_description = "Set the muscles visibility on/off"
    bl_options = {'REGISTER'}
    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        muscles = []
        
        for obj in context.scene.objects : 
            if "muscle_rig" in obj.name : 
                muscles.append (obj)

        if len(muscles) == 0 : 
            return {"CANCELLED"}

        hidden = muscles[0].hide_viewport

        if hidden : 
            for m in muscles : 
                m.hide_viewport = False
        else : 
            for m in muscles : 
                m.hide_viewport = True
        
        return {"FINISHED"}


class Bind (bpy.types.Operator):
    bl_idname = "lpqflv_rig.bind"
    bl_label = "Bind"
    bl_description = "Bind the muscles to the body"
    bl_options = {'REGISTER'}
    
    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        muscles = Muscles(context.selected_objects))
        muscles.bind()
        return {"FINISHED"}

class CreateDriver (bpy.types.Operator):
    bl_idname = "lpqflv_rig.create_muscle_driver"
    bl_label = "Driver from current position"
    bl_description = "Create a driver on the active shape key\nfrom the current position of the selected bone.\nYou had to select the muscle (with the active shape at 1) and then the driver bone"
    bl_options = {'REGISTER'}
    
    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        drivers = Drivers(context.selected_objects) )
        drivers.makeDriver()
        return {"FINISHED"}
        
#operator - Leg#
#operators#
#panels#
class MusclesPanel(bpy.types.Panel): 
    """Musles system Panel"""
    bl_idname = "muscles" 
    bl_label = "Muscles"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = "Asset Manager"
    bl_context = ""
    def draw (self, context) : 
        layout = self.layout

        c = layout.column(align = True) 
        c.menu(Create.bl_idname, icon='NONE')   
        c.operator (Transparent.bl_idname, icon="RESTRICT_VIEW_ON")
        c.operator (ToggleMuscles.bl_idname, icon="OUTLINER_OB_META")

        c = layout.column(align=True)
        c.operator(Bind.bl_idname, icon="MOD_SHRINKWRAP")
        c.prop(context.window_manager.muscles, "bindDistance")

        c = layout.column(align=True) 
        c.operator(CreateDriver.bl_idname, icon="DRIVER")
        c.prop(context.window_manager.muscles, "driverTransformType")
        c.prop(context.window_manager.muscles, "driverTransformSpace")

        c = layout.column(align=True)
        r = c.row(align=True)
        r.label(text="Active (all) : ")
        r.prop(context.window_manager.muscles, "active", text="", icon="VISIBLE_NONE_ON")
        r.prop(context.window_manager.muscles, "activeRender", text ="", icon="RESTRICT_RENDER_OFF")
        
        r = layout.row(align=True)
        r.label(text="Mirror options")
        r = layout.row(align=True)
        r.prop(context.window_manager.muscles, "mirrorX")
        r.prop(context.window_manager.muscles, "mirrorY")
        r.prop(context.window_manager.muscles, "mirrorZ")
        if context.object == None : 
            return

        if context.object.type == "MESH" : 
            r = c.row(align=True)
            r.label(text="Active (selected) : ")
            r.prop(context.object.muscle, "activeDeform", text="", icon="VISIBLE_NONE_ON")
            r.prop(context.object.muscle, "activeDeformRender", text="", icon="RESTRICT_RENDER_OFF")
        #panels#

class MuscleObjectPanel(bpy.types.Panel) : 
    bl_idname = "muscle" 
    bl_label = "Muscle"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_category = "object"
    bl_context = "object" 

    def draw (self, context) : 
        layout = self.layout

        if context.object == None : 
            return
        c = layout.column(align = True) 
        if "muscle_rig" in context.object.name and context.object.type == "MESH" : 
            r = c.row(align = True)
            r.label(text="Active : ")
            r.prop (context.object.muscle, "active", text="", icon="VISIBLE_NONE_ON")
            r.prop (context.object.muscle, "activeRender", text="", icon="RESTRICT_RENDER_OFF")
            c.prop (context.object.muscle, "volumeVariation")
        else : 
            c.label(text="This object is not a muscle.", icon="ERROR")
#menus#
#menu - Create#
class Create (bpy.types.Menu):
    bl_idname = "lpqflv_rig.create"
    bl_label = "Create"
    def draw(self, context):
        layout = self.layout  # classic menu :  = "" and pie menu : ".menu_pie()"
        r = layout.row()
        r.operator(Simple.bl_idname, icon='EYEDROPPER')
        r = layout.row()
        r.operator(FourPts.bl_idname, icon='UV_VERTEXSEL')
        r = layout.row()
        r.operator(ThreePts.bl_idname, icon='OUTLINER_DATA_MESH')#draw#
        
#menu - Create#
#menus#

#props# 

class MusclesSettings(bpy.types.PropertyGroup) : 
    bindDistance : bpy.props.FloatProperty(name="minimum distance", default=0.0)
    active : bpy.props.BoolProperty(name="Active Muscles (All)", default=True, description="Active/Desactive muscles for all", update=Muscles.onActiveAllChange)
    activeRender : bpy.props.BoolProperty(name="Active Muscles (All) - Render", default=True, description="Active/Desactive muscles for all", update=Muscles.onActiveRenderAllChange)

    driverTransformType : bpy.props.EnumProperty(items = 
        [
            ("LOC_X", "X Location", "", "", 0),
            ("LOC_Y", "Y Location", "", "", 1),
            ("LOC_Z", "Z Location", "", "", 2),
            ("ROT_X", "X Rotation", "", "", 3),
            ("ROT_Y", "Y Rotation", "", "", 4),
            ("ROT_Z", "Z Rotation", "", "", 5),
            ("SCALE_X", "X Scale", "", "", 6),
            ("SCALE_Y", "Y Scale", "", "", 7),
            ("SCALE_Z", "Z Scale", "", "", 8)
        ], default ="ROT_Z", name="Type")
    
    driverTransformSpace : bpy.props.EnumProperty(items = 
        [
            ("LOCAL_SPACE", "Local Space", "", "", 0),
            ("TRANSFORM_SPACE", "Transform Space", "", "", 1),
            ("WORLD_SPACE", "World Space", "", "", 2)
        ], default ="LOCAL_SPACE", name="Space")

    mirrorX : bpy.props.BoolProperty(name="X", description="Mirror the muscle system on the X axis", default=True, update=Muscles.toggleMirror)
    mirrorY : bpy.props.BoolProperty(name="Y", description="Mirror the muscle system on the Y axis", default=False, update=Muscles.toggleMirror)
    mirrorZ : bpy.props.BoolProperty(name="Z", description="Mirror the muscle system on the Z axis", default=False, update=Muscles.toggleMirror)


class MusclesObjectsSettings(bpy.types.PropertyGroup) : 
    volumeVariation : bpy.props.FloatProperty(name="Volume Variation", default=1.0, min=0.0, update=Muscles.onVolumeDistortChange)
    active : bpy.props.BoolProperty(name="Active", default=True, description="Active/deactive this Muscle influence", update=Muscles.onActiveMuscleChange)
    activeRender : bpy.props.BoolProperty(name="Active - Render", default=True, description="Active/deactive this Muscle influence", update=Muscles.onActiveRenderMuscleChange)
    
    activeDeform :  bpy.props.BoolProperty(name="Active Muscles (selected)", default=True, description="Active/deactive the muscle deformation for this object", update=Muscles.onActiveObjectChange)
    activeDeformRender :  bpy.props.BoolProperty(name="Active Muscles (selected) - Render", default=True, description="Active/desactive the muscle deformation for this object", update=Muscles.onActiveRenderObjectChange)
#props#

#registerFunction#
def register():
    #register#
    
    bpy.utils.register_class(MusclesPanel)
    bpy.utils.register_class(Create)
    bpy.utils.register_class(Simple)
    bpy.utils.register_class(FourPts)
    bpy.utils.register_class(ThreePts)
    bpy.utils.register_class(Transparent) 
    bpy.utils.register_class(ToggleMuscles)
    bpy.utils.register_class(Bind)
    bpy.utils.register_class(CreateDriver)
    bpy.utils.register_class(MusclesSettings)
    bpy.utils.register_class(MusclesObjectsSettings)
    bpy.utils.register_class(MuscleObjectPanel)
    bpy.types.WindowManager.muscles : bpy.props.PointerProperty(type=MusclesSettings)
    bpy.types.Object.muscle : bpy.props.PointerProperty(type=MusclesObjectsSettings)

    Muscles.toggleMirror()
#register#
def unregister():
    #unregister#
    
    bpy.utils.unregister_class(MusclesPanel)
    bpy.utils.unregister_class(Create)
    bpy.utils.unregister_class(Simple)
    bpy.utils.unregister_class(FourPts)
    bpy.utils.unregister_class(ThreePts)
    bpy.utils.unregister_class(Transparent)
    bpy.utils.unregister_class(ToggleMuscles)
    bpy.utils.unregister_class(Bind)
    bpy.utils.unregister_class(CreateDriver)
    bpy.utils.unregister_class(MusclesSettings)
    bpy.utils.unregister_class(MusclesObjectsSettings)
    bpy.utils.unregister_class(MuscleObjectPanel)

    Muscles.removeMirrorhandler()

#unregister#
if __name__ == "__main__":
    register()
    
#registerFunction#







