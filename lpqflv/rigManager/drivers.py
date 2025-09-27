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
import math

def dist(a,b) : 
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)

def scale(scaleFactor) : 
    return 1.0/math.sqrt(scaleFactor)

def snsb (fkChain, ik, ikChain) :
    distance = 0

    for b in ikChain : 
        distance += dist(b.head, b.tail)
        
    short = dist(fkChain[0].head, ik.head)
    
    if (short<distance) :
        for bone in fkChain :
            bone.scale = [1,1,1]
    else :
        for bone in fkChain :      
            bone.scale[0] = scale (short/distance)
            bone.scale[2] = scale (short/distance)
            bone.scale[1] = (short/distance)*1.0
            
            c = bone.scale[1] - 1
            c = c * ik["Squash & Stretch"]
            bone.scale[1] = 1 + c
            
            c = 1 - bone.scale[0]
            c = c*  ik["Squash & Stretch"]
            bone.scale[0] = 1 - c
            bone.scale[2] = 1 - c
    
    return scale (short/distance) 

def sns (object, i) : 
    s = scale(object.scale[i])
    if i == 0 : 
        object.scale[1] = s
        object.scale[2] = s
        return s
    
    elif i == 1 : 
        object.scale[0] = s
        object.scale[2] = s
        return s
    
    elif i == 2 : 
        object.scale[0] = s
        object.scale[1] = s
        return s
    
    else : 
        return 0.0
    
def snsb2 (fkChain, obj, ikChain) :
    distance = 0

    for b in ikChain : 
        distance += dist(b.head, b.tail)
        
    short = dist(fkChain[0].head, obj.location)
    
    if (short<distance) :
        for bone in fkChain :
            bone.scale = [1,1,1]
    else :
        for bone in fkChain :      
            bone.scale[0] = scale (short/distance)
            bone.scale[2] = scale (short/distance)
            bone.scale[1] = (short/distance)*1.0
            
            c = bone.scale[1] - 1
            c = c * obj["Squash & Stretch"]
            bone.scale[1] = 1 + c
            
            c = 1 - bone.scale[0]
            c = c*  obj["Squash & Stretch"]
            bone.scale[0] = 1 - c
            bone.scale[2] = 1 - c
    
    return scale (short/distance) 

# the driverPropName should includes the index as location[1] but noe the drivenPropName
# works only with objects ans Keys (shapekey) for now
def createDrivenKey (driven, driver, 
                     drivenPropName,  
                     driverPropName,  
                     drivenIndex=-1,
                     keyframes=True) : 
    fc = driven.driver_add(drivenPropName, drivenIndex)
    fc.driver.type = "AVERAGE"
    var = fc.driver.variables.new() 
    var.type = "SINGLE_PROP"
    if "key_blocks" in driverPropName : 
        var.targets[0].id_type = "KEY"
    else : 
        var.targets[0].id_type = "OBJECT"
    var.targets[0].id = driver
    var.targets[0].data_path = driverPropName

    for m in fc.modifiers : 
        fc.modifiers.remove(m)

    if keyframes : 
        fc.keyframe_points.insert(0, 0)
        fc.keyframe_points.insert(1,1)

        cycles = fc.modifiers.new("CYCLES")
        cycles.mode_before = "REPEAT_OFFSET"
        cycles.mode_after = "REPEAT_OFFSET"

    return fc

def createTransformDrivenKey(driven, boneDriver, transformType, transformSpace = "LOCAL_SPACE", keyframes=True) : 
    fc = driven.driver_add('value', -1)
    fc.driver.type = "AVERAGE"
    var = fc.driver.variables.new() 
    var.type = "TRANSFORMS"
    var.targets[0].id = boneDriver.id_data
    var.targets[0].bone_target = boneDriver.name
    var.targets[0].transform_type = transformType
    var.targets[0].transform_space = transformSpace

    for m in fc.modifiers : 
        fc.modifiers.remove(m)

    k = None

    if keyframes : 
        k0 = fc.keyframe_points.insert(0, 0)
        k0.interpolation = "LINEAR"
        k1 = fc.keyframe_points.insert(1,1)
        k1.interpolation = "LINEAR"


        cycles = fc.modifiers.new("CYCLES")
        cycles.mode_before = "REPEAT_OFFSET"
        cycles.mode_after = "REPEAT_OFFSET"

    return (fc)

bpy.app.driver_namespace["snsb"] = snsb
bpy.app.driver_namespace["sns"] = sns
bpy.app.driver_namespace["snsb2"] = snsb2









