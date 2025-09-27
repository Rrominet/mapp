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

# INFO_MT_armature_add

import bpy
import bmesh

import sys 

from lpqflv import bl_collections as cl

class ShapeKeyCtlMaker : 
    def init(self, armatureName = "") : 
        try : self.armature = bpy.data.objects[armatureName]
        except : self.armature = armatureName

        if bpy.context.object : 
            if bpy.context.object.type == "MESH" or bpy.context.object.type == "CURVE" or bpy.context.object.type == "SURFACE" : 
                self.shapeKeys = bpy.context.object.data.shape_keys.key_blocks
                self.activeShapeKey = bpy.context.object.active_shape_key
                self.oppositeShapeKey = self.oppositeKey()

                if self.oppositeShapeKey :
                    self.controler = Controler (self.activeShapeKey.name, 2, self.armature)

                else : 
                    self.controler = Controler (self.activeShapeKey.name, 1, self.armature)

                self.connect(self.controler.armature)

    def oppositeKey (self) : 
        n = self.activeShapeKey.name 

        for k in self.shapeKeys : 
            kn = ShapeKeyCtlMaker.deleteSens(k.name)
            # print (kn)

            if kn in ShapeKeyCtlMaker.deleteSens(n): 
                if ShapeKeyCtlMaker.side(k.name) == ShapeKeyCtlMaker.side(n) and k.name != n : 
                    # print (k.name)
                    return k
        return False

    def connect(self, armature) : 
        
        fc = self.activeShapeKey.driver_add('value', -1)
        fc.driver.type = 'SCRIPTED'
        var = fc.driver.variables.new() 
        var.name = "x"
        var.type = "TRANSFORMS"
        var.targets[0].id = armature
        var.targets[0].bone_target = self.controler.controler.name
        var.targets[0].transform_type = 'LOC_Y'
        var.targets[0].transform_space = 'LOCAL_SPACE'

        if self.oppositeShapeKey : 
            fc.driver.expression = "x*2"

            fc2 = self.oppositeShapeKey.driver_add('value', -1)
            fc2.driver.type = 'SCRIPTED'
            var2 = fc2.driver.variables.new() 
            var2.name = "x"
            var2.type = "TRANSFORMS"
            var2.targets[0].id = armature
            var2.targets[0].bone_target = self.controler.controler.name
            var2.targets[0].transform_type = 'LOC_Y'
            var2.targets[0].transform_space = 'LOCAL_SPACE'
            fc2.driver.expression = "-x*2"

        else : 
            fc.driver.expression = "x"


    def side(n) : 
        if ".L" in n or "_L" in n or "-L" in n or ".l" in n or "-l" in n : 
            return "L"

        elif ".R" in n or "_R" in n or "-R" in n or ".r" in n or "-r" in n : 
            return "R"

        else : 
            return "none"

    def deleteSens(n) :  
        n = n.lower()
        n = n.replace("dwn", "")
        n = n.replace("down", "")
        n = n.replace("bas", "")
        n = n.replace("up", "")
        n = n.replace("haut", "")
        n = n.replace("open", "")
        n = n.replace("close", "")
        n = n.replace("closed", "")
        n = n.replace("opened", "")
        n = n.replace("angry", "")
        n = n.replace("sad", "")
        n = n.replace("ouvert", "")
        n = n.replace("ferme", "")
        n = n.replace("fermé", "")
        n = n.replace("colere", "")
        n = n.replace("triste", "")
        n = n.replace("large", "")
        n = n.replace("petite", "")
        n = n.replace("small", "")
        n = n.replace("big", "")
        n = n.replace("grande", "")
        n = n.replace("grand", "")

        #Delete sides
        n = n.replace (".L", "")
        n = n.replace ("-L", "")
        n = n.replace ("_L", "")
        n = n.replace ("_R", "")
        n = n.replace ("-R", "")
        n = n.replace (".R", "")
        n = n.replace (".l", "")
        n = n.replace ("-l", "")
        n = n.replace ("_l", "")
        n = n.replace (".r", "")
        n = n.replace ("_r", "")
        n = n.replace ("-r", "")

        return n

    @staticmethod
    def drawMenu (self, context) : 
        self.layout.separator()
        self.layout.operator(AddDriverCtlOperator.bl_idname, icon="DRIVER")

    @staticmethod
    def drawApplyMenu (self, context) : 
        self.layout.operator(ApplyTransformToDeltaOperator.bl_idname, icon="COPYDOWN")
        self.layout.operator(ApplyDeltaToPoseOperator.bl_idname, icon="NDOF_TRANS")

    @staticmethod
    def copyTransformToDelta (context) : 
        c = context
        a = c.object

        if a.type != "ARMATURE" : 
            return

        poses = a.pose.bones
        for p in poses : 
            p.delta.location = p.location
            p.delta.scale = p.scale

            if p.rotation_mode == "QUATERNION" : 
                p.delta.quaternionValue = p.rotation_quaternion[0]
                p.delta.rotationVector[0] = p.rotation_quaternion[1]
                p.delta.rotationVector[1] = p.rotation_quaternion[2]
                p.delta.rotationVector[2] = p.rotation_quaternion[3]

            else : 
                p.delta.rotationEuler = p.rotation_euler

    @staticmethod
    def applyDeltaToTransform (context) : 
        c = context
        a = c.object

        if a.type != "ARMATURE" : 
            return

        if "_proxy" in a.name : 
            orginalName = a.name.replace("_proxy", "")
            original = bpy.data.objects[orginalName]
            if original : 
                poses = a.pose.bones
                origPoses = original.pose.bones

                i = 0 
                while i<len(poses) : 
                    poses[i].location = origPoses[i].delta.location
                    poses[i].scale = origPoses[i].delta.scale

                    try : poses[i].rotation_mode = origPoses[i].rotation_mode
                    except : pass

                    if poses[i].rotation_mode == "QUATERNION" : 
                        poses[i].rotation_quaternion[0] = origPoses[i].delta.quaternionValue
                        poses[i].rotation_quaternion[1] = origPoses[i].delta.rotationVector[0]
                        poses[i].rotation_quaternion[2] = origPoses[i].delta.rotationVector[1]
                        poses[i].rotation_quaternion[3] = origPoses[i].delta.rotationVector[2]

                    else : 
                        poses[i].rotation_euler = origPoses[i].delta.rotationEuler

                    i+=1

            else : 
                return 'ERROR_NO_PROXY'

        else : 
            poses = a.pose.bones
            for p in poses : 
                p.location = p.delta.location
                p.scale = p.delta.scale

                if p.rotation_mode == "QUATERNION" : 
                    p.rotation_quaternion[0] = p.delta.quaternionValue
                    p.rotation_quaternion[1] = p.delta.rotationVector[0]
                    p.rotation_quaternion[2] = p.delta.rotationVector[1]
                    p.rotation_quaternion[3] = p.delta.rotationVector[2]

                else : 
                    p.rotation_euler = p.delta.rotationEuler


class Controler : 
    def __init__(self, shapeName = "", targets = 1, parentArmature = None) : 
        self.armature = parentArmature
        if type(self.armature) == str : 
            data = bpy.data.armatures.new(self.armature + "-data")
            self.armature = bpy.data.objects.new(self.armature, data)
            bpy.context.scene.collection.objects.link(self.armature)

        bpy.context.view_layer.objects.active = self.armature
        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set("INVOKE_DEFAULT", mode = 'EDIT')

        self.container = self.armature.data.edit_bones.new("container_" + shapeName)
        self.controler = self.armature.data.edit_bones.new("controler_" + shapeName)

        self.container.tail[1] = 1
        self.controler.tail[1] = 1

        if targets == 1 : 
            self.controler.head[1] = 0

        else : 
            self.controler.head[1] = 0.55
            self.controler.tail[1] = 1.55  

        self.controler.parent = self.container

        self.container.use_deform = False
        self.controler.use_deform = False

        self.createShapes(targets)
        self.createLimits(targets)

    def createShapes (self, targets): 
        data = bpy.data.meshes.new("driverContainerShape-data")
        self.containerShape = bpy.data.objects.new("driverContainerShape", data)

        data2 = bpy.data.meshes.new("driverControlerShape-data")
        self.controlerShape = bpy.data.objects.new("driverControlerShape", data2)

        bm = bmesh.new() #making the container shape#
        if targets == 1 : 
            v1 = bm.verts.new((-0.19, 0.1, 0))
            v2 = bm.verts.new((0.19, 0.1, 0))
            v3 = bm.verts.new((0.19, 0.01, 0))
            v4 = bm.verts.new((-0.19, 0.01, 0))
        else : 
            v1 = bm.verts.new((-0.19, 0.05, 0))
            v2 = bm.verts.new((0.19, 0.05, 0))
            v3 = bm.verts.new((0.19, -0.05, 0))
            v4 = bm.verts.new((-0.19, -0.05, 0))

        bm.edges.new([v1,v2])
        bm.edges.new([v2,v3])
        bm.edges.new([v3,v4])
        bm.edges.new([v4,v1])

        bm2 = bm.copy() 

        v1.co = (-0.2, 1.1, 0)
        v2.co = (0.2, 1.1, 0)
        v3.co = (0.2, 0, 0)
        v4.co = (-0.2, 0, 0)

        bm.to_mesh(data)
        bm2.to_mesh(data2)

        bm.free()
        bm2.free()

        bpy.context.scene.collection.objects.link(self.containerShape)
        bpy.context.scene.collection.objects.link(self.controlerShape)

        self.driversCollection = None 
        if bpy.data.collections.find("rig-shapes") == -1 : 
            self.driversCollection = cl.newCollection("rig-shapes")
        else : 
            self.driversCollection = bpy.data.collections["rig-shapes"]

        cl.moveObjToCollection (self.containerShape, self.driversCollection)
        cl.moveObjToCollection (self.controlerShape, self.driversCollection)

        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set("INVOKE_DEFAULT", mode = 'POSE')

        self.armature.pose.bones[self.container.name].custom_shape = self.containerShape
        self.armature.data.bones[self.container.name].show_wire = True
        self.armature.pose.bones[self.controler.name].custom_shape = self.controlerShape
        self.armature.data.bones[self.controler.name].show_wire = True 

        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set("INVOKE_DEFAULT", mode = 'OBJECT')

    def createLimits(self, targets) : 
        controlerP = self.armature.pose.bones[self.controler.name]
        const = controlerP.constraints.new("LIMIT_LOCATION")
        const.use_min_y = True
        const.use_max_y = True

        if targets == 1 : 
            const.min_y = 0
            const.max_y = 1

        else : 
            const.min_y = -0.5
            const.max_y = 0.5

        const.owner_space = 'LOCAL'

        controlerP.lock_location[0] = True
        controlerP.lock_location[2] = True

dm = ShapeKeyCtlMaker() 

def armaturesItems (self, context) : 
    armatures = []
    for o in context.scene.objects : 
        if o.type == "ARMATURE" : 
            armatures.append((o.name, o.name, "Add driver to this armature"))
    if len(armatures) == 0 : 
        return None
    else : 
        return armatures


class AddDriverCtlOperator (bpy.types.Operator) : 
    
    """Add a controler to the selected Shape Key"""
    bl_idname = "drivers.add_key_shape_ctl"
    bl_label = "Add Key Shape Controler"
    bl_options = {'REGISTER', 'UNDO'}

    existingArmature : bpy.props.EnumProperty(name="Existing Armatures", items=armaturesItems, default=None)
    useExisting : bpy.props.BoolProperty(name="Use an existing Armature", description="Use as existing armature to put the controler in", default=True)

    newArmatureName : bpy.props.StringProperty(name="New Armature", default="driversController")

    def execute (self, contect): 
        if self.existingArmature and self.useExisting: 
            dm.init(self.existingArmature)
        else : 
            dm.init(self.newArmatureName)

        return {'FINISHED'}

    def draw (self, context) : 
        l = self.layout
        r = l.row()
        if self.existingArmature : 
            r.prop(self, "useExisting")
            r.prop(self, "existingArmature", icon="ARMATURE_DATA")
            r = l.row()
            r.prop(self, "newArmatureName", icon="MOD_ARMATURE")
        else :
            r.prop(self, "newArmatureName", icon="MOD_ARMATURE")

    def invoke (self, context, event) : 
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=400)

class DriversProps(bpy.types.PropertyGroup) : 
    location : bpy.props.FloatVectorProperty(name="Location", description="Back up for location of the bone. \nUseful when you want to tranfert it\nfrom original file in proxy mode.", precision=5)
    rotationEuler : bpy.props.FloatVectorProperty(name="Rotation", precision=3)
    rotationVector : bpy.props.FloatVectorProperty(name="Rotation", precision=3)
    quaternionValue : bpy.props.FloatProperty(name="W", precision=3)
    scale : bpy.props.FloatVectorProperty(name="Scale", precision=3)


class ApplyTransformToDeltaOperator(bpy.types.Operator) : 
    """Copy bones'transforms to bones'delta"""
    bl_idname = "drivers.copy_transform_to_delta"
    bl_label = "Copy Transform to Delta"
    bl_options = {'REGISTER', 'UNDO'}

    def execute (self, context) :
        ShapeKeyCtlMaker.copyTransformToDelta(context)
        return {'FINISHED'}

class ApplyDeltaToPoseOperator(bpy.types.Operator) : 
    """Apply the bones'delta tranform values to there current pose transform"""
    bl_idname = "drivers.apply_delta_to_pose"
    bl_label = "Apply Delta to Pose"
    bl_options = {'REGISTER', 'UNDO'}

    def execute (self, context) : 
        ShapeKeyCtlMaker.applyDeltaToTransform(context)
        return {'FINISHED'}

class Delta(bpy.types.Panel): 
    """Transform infos for transferts"""
    bl_idname = "LPQFLV_PT_delta" 
    bl_label = "Delta Transform"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_category = "BONE"
    bl_context = "bone"
    def draw (self, context) : 
        layout = self.layout
        #draw#
        
        try : 
            r = layout.row()
            c = r.column(align=False) #-0- 
            c.prop(context.active_pose_bone.delta, "location")
            if (context.active_pose_bone.rotation_mode == "QUATERNION") : 
                c = r.column(align=True)
                c.prop(context.active_pose_bone.delta, "quaternionValue")
                c.prop(context.active_pose_bone.delta, "rotationVector")
            else : 
                c.prop(context.active_pose_bone.delta, "rotationEuler")
            c = r.column(align=False)
            c.prop(context.active_pose_bone.delta, "scale")

            r = layout.row(align=True) #-2- 
            r.operator(ApplyTransformToDeltaOperator.bl_idname, icon='COPYDOWN')
            r.operator(ApplyDeltaToPoseOperator.bl_idname, icon='NDOF_TRANS')#draw#
        except : 
            pass


def registerDriversProps () : 
    bpy.utils.register_class (DriversProps)
    bpy.types.PoseBone.delta = bpy.props.PointerProperty (type=DriversProps)
    bpy.utils.register_class (Delta)
    bpy.types.VIEW3D_MT_pose_apply.append(ShapeKeyCtlMaker.drawApplyMenu)
    bpy.utils.register_class (ApplyTransformToDeltaOperator)
    bpy.utils.register_class (ApplyDeltaToPoseOperator)


def unregisterDriversProps () : 
    bpy.utils.unregister_class (DriversProps)
    bpy.utils.unregister_class (Delta)
    bpy.types.VIEW3D_MT_pose_apply.remove(ShapeKeyCtlMaker.drawApplyMenu)
    bpy.utils.unregister_class (ApplyTransformToDeltaOperator)
    bpy.utils.unregister_class (ApplyDeltaToPoseOperator)

