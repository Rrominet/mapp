import mathutils
import bpy

# the positions are passed by copy
def test_def(dep, obj, mesh, positions) : 
    print (dep)
    print ("o")
    print (obj.material_slots)
    print ("m")
    print (mesh.vertices)
    print ("m_e")
#    print(positions.get(0))
#    print(positions.size())
#
#    positions.set(0, 0, 0, 0)

# should use the mesh data, hot object->data becasuse its updated from the previous modifiers
def test_mod(dep, obj, mesh) : 
    print (dep)
    print ("o")
    print (obj.material_slots)
    print ("m")
    print (mesh.vertices)
    print ("m_e")
#    print(positions.get(0))
#    print(positions.size())
#
#    positions.set(0, 0, 0, 0)

def disabled() : 
    print ("disabled (py)")
    return True
