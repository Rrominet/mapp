import bpy

def poseParent(armatureObject, poseBone) : 
    return armatureObject.pose.bones[poseBone.bone.parent.name]
