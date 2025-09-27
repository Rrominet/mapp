
#this file contains some useful functions for bmesh and/or modeling operations.
#all this function are note forcelly relative to bmesh but they are relatives to modeling

import bpy 
import bmesh
import mathutils
import math

def selectedVerticesWorldPosition() : 
    bm = bmesh.new()
    ob = bpy.context.object
    bm = bmesh.from_edit_mesh(ob.data)

    points = []
    for v in bm.verts:
        if (v.select == True):
            obMat = ob.matrix_world
            points.append(obMat @ v.co)
    #Here, we multiply the vertex coordinate by the object's world matrix, in case the object is
    # transformed.
    #It is important to put the obMat before the v.co
    # the @ (matrix multiplication) operator is NOT commutative.
    return points


def selectedFaces(object=None) : 
    if not object :
        object = bpy.context.object

    _r = []
    if object.type != 'MESH' :
        raise Exception("The selected object is not a Mesh. Can't retreive selected faces.")
    for p in object.data.polygons :
        if p.select :
            _r.append(p)
    return _r

#this is for a blender polygon, not a blender bmech face
def faceVertices(mesh, face) : 
    _r = []
    for v in face.vertices :
        _r.append(mesh.vertices[v])

    return _r

#vertices is a list of vector3 representing the verticles position.
#they are NOT blender vertices objects.
def boundingBox(vertices) : 
    min_x, min_y, min_z = vertices[0]
    max_x, max_y, max_z = vertices[0]

    # Iterate through all points to find the min and max for each dimension
    for v in vertices:
        min_x = min(min_x, v[0])
        min_y = min(min_y, v[1])
        min_z = min(min_z, v[2])
        max_x = max(max_x, v[0])
        max_y = max(max_y, v[1])
        max_z = max(max_z, v[2])

    return (min_x, min_y, min_z), (max_x, max_y, max_z)


# TODO : could be optimized because the code is duplicated.
# but not that easy because you need convert vertices of blender into an array of vector3
def boundingBoxF(mesh, face) : 
    vertices = faceVertices(mesh, face)
    min_x, min_y, min_z = vertices[0].co
    max_x, max_y, max_z = vertices[0].co

    # Iterate through all points to find the min and max for each dimension
    for v in vertices:
        min_x = min(min_x, v.co[0])
        min_y = min(min_y, v.co[1])
        min_z = min(min_z, v.co[2])
        max_x = max(max_x, v.co[0])
        max_y = max(max_y, v.co[1])
        max_z = max(max_z, v.co[2])

    return (min_x, min_y, min_z), (max_x, max_y, max_z)


#return an array of vector3 that matche the face vertices number and order. This array of vertices represent the same face but aligned to axis given by the agument 'axis' in the world via a rotation.
#axis is either X, Y or Z
#return the rotation matrix used too.
def rotatedOnAxis(mesh, face, axis='Z') : 
    _r = []
    rot = rotatedOnAxisMatrix(mesh, face, axis)
    for v in faceVertices(mesh, face) : 
        co = v.co
        co = rot @ co
        _r.append(co)

    return (_r, rot)

#return the rotation matrix used in rotatedOnAxis to move the returned vertices
def rotatedOnAxisMatrix(mesh, face, axis='Z') : 
    face_normal = face.normal
    target_normal = mathutils.Vector((1,0,0))
    if axis == 'Y' : 
        target_normal = mathutils.Vector((0,1,0))
    elif axis == 'Z' : 
        target_normal = mathutils.Vector((0,0,1))

    rot_axis = face_normal.cross(target_normal)
    rot_angle = face_normal.angle(target_normal)

    if rot_axis.length == 0 : 
        return mathutils.Matrix.Identity(4) if face_normal.z > 0 else mathutils.Matrix.Rotation(math.pi, 4, 'X')

    rot = mathutils.Matrix.Rotation(rot_angle, 4, rot_axis)
    return rot

def vectorFromVertices(v1, v2) : 
    return v2.co - v1.co

# contrary to the function above, this take 2 mathutils.Vector as arg directly.
def vectorFromCoords(v1, v2) : 
    return v2 - v1

def rotationDifferenceMatrix(v1, v2, axis=mathutils.Vector((0,0,1))) : 
    angle = v1.angle(v2)
    return mathutils.Matrix.Rotation(angle, 4, axis)

def applyMatrix(vertices, matrix) : 
    for v in vertices : 
        v.co = matrix @ v.co

#return the average of z local values from the vertices
def position(mesh, face) : 
    vertices = faceVertices(mesh, face)
    x = sum([v.co[0] for v in vertices]) / len(vertices)
    y = sum([v.co[1] for v in vertices]) / len(vertices)
    z = sum([v.co[2] for v in vertices]) / len(vertices)
    return mathutils.Vector((x, y, z))
