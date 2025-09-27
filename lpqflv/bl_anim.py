import bpy

def keyframes(object, dataPath) : 
    if not object.animation_data :
        return None
    if not object.animation_data.action : 
        return None
    fcurves = object.animation_data.action.fcurves
    fcurve = fcurves.find(dataPath)
    if not fcurve : 
        return None
    return fcurve.keyframe_points

def addKeyframe(object, dataPath, value, frame) : 
    kfs = keyframes(object, dataPath)
    if not kfs : 
        if not object.animation_data : 
            object.animation_data_create()
        if not object.animation_data.action : 
            object.animation_data.action = bpy.data.actions.new(object.name + "Action")
        fcurves = object.animation_data.action.fcurves
        fcurve = fcurves.find(dataPath)
        if not fcurve : 
            fcurve = fcurves.new(data_path=dataPath)
        return fcurve.keyframe_points.insert(frame, value)
    else : 
       return kfs.insert(frame, value) 

def keyframe(object, dataPath, frame) : 
    kfs = keyframes(object, dataPath)
    if not kfs : 
        return None
    for k in kfs : 
        if int(k.co[0]) == frame : 
            return k
    return None

def updateFcurves(objects) : 
    for o in objects : 
        if not o.animation_data :
            continue
        if not o.animation_data.action : 
            continue
        for fcurve in o.animation_data.action.fcurves : 
            fcurve.update()

def selectedKeyframes(o) : 
    if not o.animation_data : 
        return []

    action = o.animation_data.action
    if not action : 
        return []

    kfs = []

    for fcurve in action.fcurves : 
        for kf in fcurve.keyframe_points : 
            if kf.select_control_point : 
                kfs.append(kf)

    return kfs

def shapeKey(obj, name) : 
    return obj.data.shape_keys.key_blocks[name]

def setShapeKey(obj, name, value) : 
    obj.data.shape_keys.key_blocks[name].value = value

def fcurvesFromBone(object, boneName) : 
    fcurves = []
    if not object.animation_data :
        return fcurves
    if not object.animation_data.action :
        return fcurves

    for c in object.animation_data.action.fcurves : 
        dataName = c.data_path.split("\"")
        try : 
            dataName = dataName[1]
            if boneName == dataName : 
                fcurves.append(c)
        except : pass

    return fcurves

def fcurvesFromSelectedBones(obj) : 
    names = []
    for bone in ctx.object.data.bones : 
        if bone.select : 
            names.append(bone.name)
    fcurves = []
    for n in names : 
        for c in fcurvesFromBone(ctx.object, n) : 
            fcurves.append(c)

    return fcurves
