import bpy
from lpqflv import errors as error
from lpqflv import math as _m
import mathutils
import copy

def tree(nodes=None) : 
    if not nodes : 
        nodes = bpy.context.area
    _t = type(nodes)

    if issubclass(_t, bpy.types.bpy_prop_collection) : 
        return nodes

    if issubclass(_t, bpy.types.NodeTree) : 
        return nodes

    if issubclass(_t, bpy.types.Material) : 
        return nodes.node_tree

    if issubclass(_t, bpy.types.Object) : 
        if len(nodes.data.materials) == 0 : 
            raise error.empty("object.data.materials", "bl_nodes.get")
        return nodes.data.materials[0].node_tree

    if issubclass(_t, bpy.types.Space) : 
        return nodes.edit_tree

    if issubclass(_t, bpy.types.Area) : 
        return nodes.spaces[0].edit_tree

    raise error.type(nodes, "NodeTree", "bl_nodes.tree")

#return the nodes from nodes arg, if no arg, it will be founded from context
def get(nodes=None) : 
    if not nodes : 
        nodes = bpy.context.area
    _t = type(nodes)

    if issubclass(_t, bpy.types.bpy_prop_collection) : 
        return nodes

    _tree = tree(nodes)
    if not _tree : 
        raise Exception("There is no Node Tree to work on.")
    return _tree.nodes

def link(node1, outIdx, node2, inIdx, _tree) : 
    _tree.links.new(node2.inputs[inIdx], node1.outputs[outIdx])

def _2nodesInOrderToBeLinkedFromSelection(_tree=None) : 
    _tree = tree(_tree)
    sls = selected(_tree.nodes)
    if len(sls) == 0 : 
        raise error.empty("selected nodes", "bl_nodes.tree")
    n1 = sls[0]
    try : 
        n2 = sls[1]
    except : 
        raise error.bad_length("selected nodes", 2, sls, "bl_nodes.tree")

    if n1.location[0] > n2.location[0] : 
        tmp = n1
        n1 = n2
        n2 = tmp

    return (n1, n2)

def findSocketFromLetter(letter, sockets) : 
    for s in sockets : 
        if s.name[0].lower() == letter.lower() : 
            return s
    raise error.not_found("Socket not founds in " + str(sockets) + " from letter " + letter, "nodes.findSocketFromLetter")

#data could be and index or a letter
def socket(data, sockets) : 
    s = None
    if type(data) == int : 
        data -=1
        s = sockets[data]
    else : 
        s = findSocketFromLetter(data, sockets)
    return s

#out could be a lettre of a number(idx)
#idem for in
def linkSelected(out, _in, _tree=None) : 
    _tree = tree(_tree)
    ns = _2nodesInOrderToBeLinkedFromSelection(_tree)
    so = socket(out, ns[0].outputs)
    si = socket(_in, ns[1].inputs)
    _tree.links.new(si, so)

def linkAllForSelected(_tree=None) : 
    _tree = tree(_tree)
    ns = _2nodesInOrderToBeLinkedFromSelection(_tree)
    for i in range(len(ns[0].outputs)) : 
        if i>=len(ns[1].inputs) : 
            break
        _tree.links.new(ns[1].inputs[i], ns[0].outputs[i])

def selected(nodes=None) :
    nds = get(nodes)
    _r = []
    for n in nds : 
        if n.select : 
            _r.append(n)
    return _r

def selectAll(nodes = None):
    nds = get(nodes)
    for n in nds :
        n.select=True

def deselectAll(nodes = None):
    nds = get(nodes)
    for n in nds :
        n.select=False

def region(area = None) : 
    if not area : 
        area = bpy.context.area

    if type(area) == bpy.types.Region : 
        return area

    error.checkType(area, bpy.types.Area, "bl_nodes.view")
    for r in area.regions : 
        if r.type == "WINDOW" : 
            return r

def view(area=None) : 
    return region(area).view2d

#region could be an area
def regionCenter(reg=None) : 
    r = region(reg)
    x = r.width/2
    y = r.height/2
    return (x, y)

def viewCenter(reg=None) : 
    center = regionCenter(reg)
    _view = view(reg)

    return _view.region_to_view(center[0], center[1])

def nodeCenter(node) : 
    return (node.location[0] + node.dimensions[0]/2, node.location[1] - node.dimensions[1]/2)

def moveNodeToCenter(node=None, area=None, later=False) :
    if not node :
        node = get().active
        if not node :
            sls = selected()
            if len(sls) > 0 :
                node = sls[0]
    if not node : 
        raise error.type(node, "bpy.types.Node", "bl_nodes.moveNodeToCenter")

    center = viewCenter(area)
    w = node.dimensions[0]
    h = node.dimensions[1]
    if w < 10 :
        w = node.bl_width_default
    if h < 10 :
        h = node.bl_height_default

    node.location[0] = center[0] - w/2
    node.location[1] = center[1] + h/2

def centeredNode(area=None) :
    nds = get(area)
    center = viewCenter(area)

    dist = 10000000000
    node = None
    for n in nds : 
        _d = _m.dist(nodeCenter(n), center)
        if _d < dist : 
            dist = _d
            node = n
    return node

#if node == None
#if will be the active one
def node(_node=None, _nodes = None) : 
    if not _node : 
        _nodes = get(_nodes)
        r = _nodes.active
    if not r : 
        raise Exception("bl_nodes.node() : _node is None even after getting the active one.")
    return r

#side is a mathutils vector
def nodeNextTo(_node, _nodes, side) : 
    r = None
    len = 100000000000

    for n in _nodes : 
        if n == _node : 
            continue
        v2 = _m.vectorFromPoints(nodeCenter(_node), nodeCenter(n))
        v2.normalize()
        dot = side.dot(v2)
        if dot<=0.5 or dot >= 1.5 : 
            continue
        di = _m.dist(nodeCenter(_node), nodeCenter(n))
        if di < len : 
            len = di
            r = n
    return r

def leftTo(_node=None, _nodes=None) :
    _node = node(_node)
    _nodes = get(_nodes)
    return nodeNextTo(_node, _nodes, mathutils.Vector((-1, 0)))

def rightTo(_node=None, _nodes=None) :
    _node = node(_node)
    _nodes = get(_nodes)
    return nodeNextTo(_node, _nodes, mathutils.Vector((1, 0)))

def upTo(_node=None, _nodes=None) :
    _node = node(_node)
    _nodes = get(_nodes)
    return nodeNextTo(_node, _nodes, mathutils.Vector((0, 1)))

def bottomTo(_node=None, _nodes=None) :
    _node = node(_node)
    _nodes = get(_nodes)
    return nodeNextTo(_node, _nodes, mathutils.Vector((0, -1)))

class axes : 
    X = 1
    Y = 2
    Z = 3

def align(axe, nodesList=None) : 
    if not nodesList : 
        nodesList = selected()

    if len(nodesList) == 0 : 
        raise Exception("No nodes to align (bl_nodes.align)")

    active = get().active
    if not active : 
        active = nodesList[0]

    for n in nodesList : 
        if n == active :
            continue

        if axe == axes.Y : 
            n.location[0] = active.location[0]
        elif axe == axes.X : 
            n.location[1] = active.location[1]
        else : 
            raise Exception("Axes other tha X or Y not supported (bl_nodes.align)")

def swapPosition(n1=None, n2=None) :
    if not n1 :
        ns = get()
        n1 = ns.active
        for n in selected(ns) :
            if n != n1 :
                n2 = n
                break
    if not n1 or not n2 :
        raise Exception("[nl_nodes.swapPosition] n1 or n2 is None.\nn1 = " + str(n1) + "\nn2 = " + str(n2))

    tmp = copy.deepcopy(n1.location)
    n1.location = copy.deepcopy(n2.location)
    n2.location = copy.deepcopy(tmp)


def addToCenter(nodeType, area=None) :
    nds = get(area)
    nn = nds.new(nodeType)
    moveNodeToCenter(nn, area, True)
    return nn

def setActive(node, nodes=None, deselect=False) :
    nodes = get(nodes)
    if deselect :
        deselectAll(nodes)
    nodes.active = node
    node.select = True

def mix(n1=None, n2=None) :
    if not n1 :
        ns = get()
        _sls = selected(ns)
        if len(_sls) > 1 :
            n1 = _sls[0]
            n2 = _sls[1]
    if not n1 or not n2 :
        raise Exception("[nl_nodes.mix] Node 1 or Node 2 is None.\nn1 = " + str(n1) + "\nn2 = " + str(n2))

    up = None
    down = None

    if n1.location[1] > n2.location[1] :
        up = n1
        down = n2
    else :
        up = n2
        down = n1

    o1 = up.outputs[0] 
    o2 = down.outputs[0] 

    _type = "ShaderNodeMix"
    if o1.type == "SHADER" : 
        _type += "Shader"
    _tree = tree()
    nodes = _tree.nodes
    links = _tree.links
    nn = nodes.new(_type)

    #TODO
    #Place the node
    nn.location[0] = up.location[0] + up.dimensions[0] + 80
    nn.location[1] = up.location[1]

    #Check the mix type
    mtype = o1.type
    i, j = 1, 2
    if mtype == "VALUE" : 
        nn.data_type = "FLOAT"
        i, j = 2, 3
    elif mtype == "RGBA" : 
        nn.data_type = "RGBA"
        i, j = 6, 7
    elif mtype == "VECTOR" : 
        nn.data_type = "VECTOR"
        i, j = 4, 5

    #Make the connexion
    links.new(o1, nn.inputs[i])
    links.new(o2, nn.inputs[j])


def materialFromTree(tree, object=None) : 
    if not object : 
        for m in bpy.data.materials : 
            if m.node_tree == tree :
                return m
        return None
    
    for m in object.data.materials : 
        if m.node_tree == tree :
            return m
    return None
