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
import os
import platform
from mathutils import *

from lpqflv import stringTools as s

class LPQFLV_Area : 
    def __init__(self, bl_area):
        self.width = bl_area.width
        self.height = bl_area.height
        self.bl_area = bl_area
        
        self.lb = (bl_area.x, bl_area.y)
        self.lt = (bl_area.x, bl_area.y + self.height) 
        self.rt = (bl_area.x + self.width, bl_area.y + self.height) 
        self.rb = (bl_area.x + self.width, bl_area.y)
        
    def inArea(self, x, y) : 
        if (x >= self.lb[0] and 
            x <= self.rb[0] and 
            y >= self.lb[1] and 
            y <= self.lt[1]) : 
                return True
        
        return False

    @staticmethod 
    def coordFromTopLeft(bl_area) : 
        _r = {}
        _r["x"] = bl_area.x
        _r["width"] = bl_area.width
        _r["height"] = bl_area.height
        _r["y"] = bpy.context.window.height - bl_area.height - bl_area.y
        _r["bl_y"] = bl_area.y

        return _r
        
def focusedArea(e) : 
    return _focuedArea(e.mouse_x, e.mouse_y)

def _focuedArea(x, y) : 
    ctx = bpy.context 
    sc = ctx.window.screen
    for bl_area in sc.areas : 
        area = LPQFLV_Area(bl_area)
        if area.inArea(x, y) : 
            return area.bl_area
        
    return sc.areas[0]

def newCollectionInstanceToScene(collection, scene, prefix = "", useFullName = False) : 
    objects = bpy.data.objects
    if useFullName : 
        name = collection.name_full.replace(".blend", "")
        name = name.replace("[", "_")
        name = name.replace("]", "")
        instance = objects.new(prefix + name, None)
    else : 
        instance = objects.new(prefix + collection, None)

    instance.instance_type = 'COLLECTION'
    instance.instance_collection = collection

    scene.collection.objects.link(instance)

def newCollectionInstanceToActiveScene (collection) : 
    newCollectionInstanceToScene(collection, bpy.context.scene)

#if merge, the collection will be merged with existed one if it exist
def linkAllFromCollection (fromCollection, parentCollection, merge=False) : 
    if not merge : 
        copieName = fromCollection.name + "_cp"
    else : 
        copieName = fromCollection.name

    toCollection = None
    if copieName in parentCollection.children : 
        toCollection = parentCollection.children[copieName]
    else : 
        toCollection = bpy.data.collections.new(copieName)
        parentCollection.children.link(toCollection)

    for obj in fromCollection.objects : 
        if not obj.name in toCollection.objects : 
            toCollection.objects.link(obj)

    for col in fromCollection.children : 
        linkAllFromCollection(col, toCollection)

def linkAllFromScene (fromScene) : 
    linkAllFromCollection(fromScene.collection, bpy.context.scene.collection)

def addHandler(func, handlersGrp) : 
    if func not in handlersGrp : 
        handlersGrp.append(func)

def removeHandler(func, handlersGrp) : 
    if func in handlersGrp : 
        handlersGrp.remove(func)

def blendDataCollectionFromObject(object, asStr = False) :
    typeName = objectTypeAsStr(object)
    return blendDataCollectionFromTypeStr(typeName, asStr)

def blendDataCollectionFromTypeStr(type, asStr=False) : 
        # datas = [
    #     d.objects,
    #     d.actions,
    #     d.cameras,
    #     d.collections,
    #     d.curves,
    #     d.fonts,
    #     d.images,
    #     d.masks,
    #     d.materials,
    #     d.meshes,
    #     d.metaballs,
    #     d.movieclips,
    #     d.node_groups,
    #     d.particles,
    #     d.scenes,
    #     d.texts,
    #     d.textures
    # ]
    typeName = shortTypeName(type)
    if typeName == "Mesh" : 
        colName = typeName.lower() + "es"

    elif typeName == "SurfaceCurve" or typeName == "TextCurve"  : 
        colName = "curves"

    elif (typeName == "PointLight" or 
          typeName == "SunLight" or 
          typeName == "AreaLight" or 
          typeName == "SpotLight") : 
        colName = "lights"

    else : 
        colName = typeName.lower() + "s"

    if asStr : 
        return colName
    
    d = bpy.data
    if hasattr(d, colName) : 
        return getattr(d, colName)
    else :
        return None

def shortTypeName(type) : 
    typeName = str(type)
    if typeName == "<class 'cycles.properties.CyclesObjectSettings'>" or typeName == "cycles.properties.CyclesVisibilitySettings" :
        return "Object"

    typeName = typeName.replace("<class 'bpy_types.", "")
    typeName = typeName.replace("<class 'bpy.types.", "")
    typeName = typeName.replace("'>", "")

    return typeName

def objectTypeAsStr(object) : 
    t = type(object)
    return shortTypeName(t)

def setAttrFromRNA(object, rna, value) : 
    """set the value of the prop when rna has several levels"""
    hie = rna.split(".")
    setattr(parentFromRNA(object, rna), hie[-1], value)
     
def propNameFromRNA(rna) : 
    return rna.split(".")[-1]

def attrFromRNA(object, rna) : 
    """get the value of the prop when rna has several levels"""
    hie = rna.split(".")
    return getattr(parentFromRNA(object, rna), hie[-1])

def parentFromRNA(object, rna) : 
    """get the parent of the prop when rna has several levels"""
    hie = rna.split(".")
    parent = object

    for i in range(len(hie) - 1) : 
        parent = getattr(parent, hie[i])

    return parent

def blenderExecPath() : 
    d = bpy.utils.resource_path("LOCAL")
    exe = d + os.sep + ".." + os.sep + "blender"
    if platform.system() == "Windows" :
        exe += ".exe"
    return exe

def configPath() : 
    return bpy.utils.resource_path("USER")

def addonsPath() : 
    return configPath() + "/scripts/addons"

def startupScene() : 
    return configPath() + os.sep + "config" + os.sep + "startup.blend"

#return blendDataCollection object in a list - avoid the reference problem
def collectionAsList(blendCollection) : 
    ls = []
    for obj in blendCollection : 
        ls.append(obj)

    return ls

#ex if val == 1 (int)
# return 'bpy.props.IntProperty'
def propTypeAsBlString(val) : 
    pre = "bpy.props."
    typ = ""
    
    if type(val) == bool : 
        typ = "BoolProperty"
    elif type(val) == int : 
        typ = "IntProperty"
    elif type(val) == float : 
        typ = "FloatProperty"
    elif type(val) == str : 
        typ = "StringProperty"

    return pre + typ

def layerFromPointer(pointer) : 
    for l in bpy.context.scene.view_layers : 
        if l.as_pointer() == pointer : 
            return l

def objectFromPointer(blCollection, pointer) : 
    for o in blCollection : 
        if o.as_pointer() == pointer : 
            return o

#propPath ex : 
#obj.data.dof.length
#propPath = data.dof.length
def subObject(obj, propPath) : 
    ls = propPath.split(".")
    ls.pop() 
    module = obj
    for m in ls : 
        if m : 
            if "[" in m : 
                m = m.replace("'", "\"")
                m = m.replace("[\"", "")
                tmp = m.split("[\"")
                m = tmp[0]

            module = getattr(module, m)
    return module

def isRegistered(cl) : 
    idn = cl.bl_idname
    modules = idn.split(".")
    if modules[0] in dir (bpy.ops) : 
        if len(modules)>1 and modules[1] in dir(getattr(bpy.ops, modules[0])) : 
            return True 
        else : 
            return False 
        return True 
    else : 
        return False

def mulBlVector(prop, coef, length=3) : 
    coef *= 1 
    ls = []
    for i in range(length) : 
        ls.append(prop[i])
    v = Vector(ls)
    return v*coef

def allCollectionFromScene(scene) : 
    return allSubCollections(scene.collection)
        
def allSubCollections(collection) : 
    cols = []
    for c in collection.children : 
        cols.append(c)
        cols += allSubCollections(c)
    return cols

def redraw() : 
    bpy.ops.wm.redraw_timer(type="DRAW_WIN_SWAP", iterations=1)

def tag_redraw() : 
    for w in bpy.data.window_managers[0].windows : 
        for area in w.screen.areas : 
            area.tag_redraw()

def stillExists(bl_obj, inScene=True) : 
    if "invalid" in str(bl_obj) : 
        return False

    if inScene and bpy.context.scene.objects.find(bl_obj.name) == -1 : 
        return False

    return True

def deepChildren(bl_obj, extend=False) : 
    _r = []
    if extend : 
        _r = [bl_obj]

    for c in bl_obj.children : 
        _r += deepChildren(c, True)
    return _r

def registerMod(ls) : 
    for i in ls : 
        i.register()

def registerCls(ls) : 
    for i in ls : 
        bpy.utils.register_class(i)

def unregisterMod(ls) : 
    for i in ls : 
        i.unregister()

def unregisterCls(ls) : 
    for i in ls : 
        bpy.utils.unregister_class(i)

def ls(_list) : 
    if type(_list) is not list : 
        _list = [_list]
    return _list

#take in to account if 'filter' in type name
def types(filter="") : 
    _r = []
    if filter == "": 
        return dir(bpy.types)

    for t in dir(bpy.types) : 
        if filter in t : 
            _r.append(t)
    return _r

def menus() : 
    return types("_MT_")

def panels() : 
    return types("_PT_")

def headers() : 
    return types("_HT_")

def asItems(ls) : 
    items = []
    for i in range(len(ls)) : 
        items.append((s.getCleanName(ls[i]), ls[i], "", i))

    return items

def stringAsClsName(string) : 
    className = ""
    className = string
    if " " in className : 
        tmp = className.split(" ")
        for t in tmp : 
            t = t[0].upper() + t[1:]
        className = "".join(tmp)
    className = s.getCleanName(className)
    return className

def stringAsBlId(string) : 
    _id = string
    _id = _id.lower()
    _id = s.getCleanName(_id)
    return _id

#factor is 0 to 1 flaot
def showProgress(factor) : 
    ws = bpy.data.window_managers[0].windows[0].workspace
    ws.status_text_set("Progress : " + str(round(factor*100)) + "%")
    bpy.ops.wm.redraw_timer(type="DRAW_WIN_SWAP", iterations=1)

def clearProgress() : 
    ws = bpy.data.window_managers[0].windows[0].workspace
    ws.status_text_set(None)
    bpy.ops.wm.redraw_timer(type="DRAW_WIN_SWAP", iterations=1)

#parse pgr from blender cmd line output render
def parsePgr(line) : 
    line = line.decode("utf-8")
    if "Append frame" not in line : 
        return -1
    line = line.replace("Append frame ", "")
    line = line.replace("\n", "")
    frame = int(line)
    return frame

# we use the attr of object for forcing it to be passes as reference
def watchPgr(dic, attr) : 
    def f () : 
        if not attr in dic : 
            return .016
        showProgress(dic[attr])
        if (dic[attr]>=0.99) : 
            clearProgress()
            return None
        return .016
    bpy.app.timers.register(f, first_interval=0.016)

def execOnSelectedObjects(func) : 
    for o in bpy.context.selected_objects : 
        func(o)

def unselectAll() :
    for o in bpy.context.scene.objects : 
        o.select_set(False)

    bpy.context.view_layer.objects.active = None

# obj could be a list
def select(obj) : 
    if type(obj) is list : 
        for o in obj : 
            o.select_set(True)
        bpy.context.view_layer.objects.active = obj[0]
    else : 
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj


#return data from element around the area in arg.
#Wich area is up, down, left and right from it.
def areaData(screen, area) : 
    data = {}
    for a in screen.areas : 
        if a == area : 
            continue
        elif a.x < area.x and a.y + a.height == area.y + area.height : 
            data["left"] = a
        elif a.x > area.x and a.y + a.height == area.y + area.height :
            data["right"] = a
        elif a.x == area.x and a.y > area.y : 
            data["up"] = a
        elif a.x == area.x and a.y < area.y : 
            data["down"] = a

    for a in screen.areas : 
        if a == area : 
            continue
        elif a.x < area.x and "left" not in data : 
            data["left"] = a
        elif a.x > area.x and "right" not in data :
            data["right"] = a
        elif a.y > area.y and "up" not in data : 
            data["up"] = a
        elif a.y < area.y and "down" not in data : 
            data["down"] = a

    return data

#rotate_around is an angle in radian that will be used to rotate the object around the aligned vector
def alignObjectToVector(obj, vec, axis="Z", up="Y", rotate_around=0) : 
    vector_normalized = vec.normalized()
    rot_mat = vector_normalized.to_track_quat(axis, up).to_matrix().to_4x4()
    rot_around = Matrix.Rotation(rotate_around, 4, vector_normalized)
    rot_mat = rot_around @ rot_mat
    obj.rotation_euler = rot_mat.to_euler()

def moveToCollection(col, obj) : 
    for c in obj.users_collection : 
        c.objects.unlink(obj)
    col.objects.link(obj)

def linkToCollection(col, obj) : 
    cl.objects.link(obj)

def serializeConstraint(constraint) : 
    tmp = dir(constraint)
    attrs = []

    for t in tmp : 
        if "__" in t or "rna" in t : 
            continue
        attrs.append(t)

    r = {}
    for a in attrs : 
        value = getattr(constraint, a)
        if not value : 
            continue
        try : 
            name = value.name # so it's a blender object
            r[a] = {"type" : "object", "name" : name}
        except : 
            r[a] = getattr(constraint, a)
    return r

# make the data of data on constraint
def deserializeConstraint(constraint, data) : 
    for key in data : 
        if type(data[key]) is dict :
            if ("type" in data[key]) : 
                setattr(constraint, key, bpy.data.objects[data[key]["name"]])
        else : 
            try :
                setattr(constraint, key, data[key])
            except Exception as e : 
                pass

#filter is a list of strs that will not be serilliazed if the name of the constraint contains is
def serializeBonesConstraints(bones, filter=[]) : 
    r = {}
    for b in bones : 
        bonesData = []
        for c in b.constraints : 
            ok = True
            for f in filter : 
                if f in c.name : 
                    ok = False
                    break
            if ok : 
                bonesData.append(serializeConstraint(c))
        r[b.name] = bonesData
    return r

def deserializeBonesConstraints(bones, data) : 
    for b in bones : 
        for key in data : 
            if key == b.name : 
                for c in data[key] : 
                    nc = b.constraints.new(type=c["type"])
                    deserializeConstraint(nc, c)

def bonesWithIk(bones) : 
    r = []
    for b in bones : 
        for c in b.constraints : 
            if c.type == "IK" : 
                r.append(b)
                break
    return r

def removeBoneAnim(object, bone) : 
    toRemove = []
    for a in object.animation_data.action.fcurves : 
        dataName = a.data_path.split("\"")
        try : 
            dataName = dataName[1]
            if bone.name == dataName : 
                toRemove.append(a)
        except : pass
    for a in toRemove :
        object.animation_data.action.fcurves.remove(a)


def selectedPoseBones() : 
    bones = []
    for b in bpy.context.object.pose.bones : 
        if b.bone.select : 
            bones.append(b)
    return bones

def unselectEditBone(bone) : 
    bone.select = False
    bone.select_tail = False
    bone.select_head = False

# when you change a value in python that is linked to a driver, blender GUI will not be updated.
#You need to run this function if you want to see the changes directly.
def updateDrivers(object) : 
    if not object.animation_data :
        return
    for fc in object.animation_data.drivers : 
        fc.driver.expression = fc.driver.expression

#set the position of the bone in POSE space
def setPoseBonePosePosition(bone, vec) : 
    m = bone.matrix.copy()
    m[0][3] = vec[0]
    m[1][3] = vec[1]
    m[2][3] = vec[2]
    bone.matrix = m
    bpy.context.view_layer.update()

#the driver expression variable name is always "x"
def createDriver(driven, driven_path, driven_index=-1,
                 driver=None, driver_path="location", driver_index=-1, expression="x") :
    if not driver : 
        raise Exception("The driver can't be None")

    fc = driven.driver_add(driven_path, driven_index)
    fc.driver.type = "SCRIPTED"
    fc.driver.expression = expression
    var = fc.driver.variables.new()
    var.name = "x"
    var.type = "SINGLE_PROP"
    if type(driver) is bpy.types.PoseBone : 
        var.targets[0].id = driver.id_data
        if driver_index != -1 :
            var.targets[0].data_path = "pose.bones[\"" + driver.name + "\"]." + driver_path + "[" + str(driver_index) + "]"
        else : 
            var.targets[0].data_path = "pose.bones[\"" + driver.name + "\"]." + driver_path
    else : 
        var.targets[0].id = driver
        if driver_index != -1 :
            var.targets[0].data_path = driver_path + "[" + str(driver_index) + "]"
        else :
            var.targets[0].data_path = driver_path

def createBonesForABezierPoint(armature, curve, bezierPoint) : 
    bones = armature.data.edit_bones
    hlw = curve.matrix_world @ bezierPoint.handle_left
    hrw = curve.matrix_world @ bezierPoint.handle_right
    pw = curve.matrix_world @ bezierPoint.co

    hl = bones.new("handle_left")
    hl.head = armature.matrix_world.inverted() @ hlw
    hl.tail = armature.matrix_world.inverted() @ hlw
    hl.tail[1] += 1
    hr = bones.new("handle_right")
    hr.head = armature.matrix_world.inverted() @ hrw
    hr.tail = armature.matrix_world.inverted() @ hrw
    hr.tail[1] += 1

    p = bones.new("point")
    p.head = armature.matrix_world.inverted() @ pw
    p.tail = armature.matrix_world.inverted() @ pw
    p.tail[1] += 1

    hl.parent = p
    hr.parent = p

    return {"handle_left" : hl, "handle_right" : hr, "point" : p}

#what can be "head" or "tail"
def placeBoneToWorldPos(armature, boneName, worldPos, what="head") : 
    bone = armature.data.edit_bones[boneName]
    if what == "head" :
        bone.head = armature.matrix_world.inverted() @ worldPos
    else : 
        bone.tail = armature.matrix_world.inverted() @ worldPos

def worldCoordonatesFromVertices(object, vertices) : 
    r = []
    for v in vertices : 
        r.append(object.matrix_world @ v.co)
    return r

def selectedVertices() : 
    #needed to ensure vertices are correctly updated.
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    return [v for v in bpy.context.object.data.vertices if v.select]

def selectedVertexIndexes() : 
    #needed to ensure vertices are correctly updated.
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    return [v.index for v in bpy.context.object.data.vertices if v.select]

# opCls could be the bl_idname string directly too
def isOperatorRegistered(opCls) : 
    try : 
        idname = ""
        if type(opCls) == str :
            idname = opCls
        else : 
            idname = opCls.bl_idname
        names = idname.split(".")
        names[0] = names[0].upper() + "_OT_"
        name = names[0] + names[1]
        return getattr(bpy.types, name).is_registered
    except : 
        return False

def findMenu(name) : 
    name = name.lower()
    for m in menus() : 
        if name in m.lower() : 
            print (m)

def findPanel(name) : 
    name = name.lower()
    for m in panels() : 
        if name in m.lower() : 
            print (m)

def armatureFromObject(object) : 
    for m in object.modifiers : 
        if m.type == "ARMATURE" : 
            return m.object
    return None
