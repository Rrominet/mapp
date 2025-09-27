import bpy

groupsIdNames = ["GroupNode", "ShaderNodeGroup", "CompositingNodeGroup", "TextureNodeGroup"]

def addNodeGroup(material, nodeGroup) : 
    nodes = material.node_tree.nodes
    n = nodes.new("ShaderNodeGroup")
    n.node_tree = nodeGroup
    return n

def lastNode(material) : 
    nodes = material.node_tree.nodes 
    return lastNode_nodes(nodes)

def lastNode_nodes(nodes) : 
    out = nodes['Material Output']
    return nodeFromSocket(out.inputs[0])

#shaderNode1 will be up
def mixShaders(material, shaderNode1, shaderNode2) : 
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    mix = nodes.new("ShaderNodeMixShader")
    links.new(mix.inputs[1], shaderNode1.outputs[0])
    links.new(mix.inputs[2], shaderNode2.outputs[0])
    links.new(nodes['Material Output'].inputs[0], mix.outputs[0])
    return mix

def containGroupNode(material, nodeGroup) : 
    for n in material.node_tree.nodes : 
        if n.bl_idname == "ShaderNodeGroup" : 
            if n.node_tree == nodeGroup : 
                return True

    return False

def socketFromReroute(reroute) : 
    socket = reroute.inputs[0].links[0].from_socket
    while socket and socket.node.bl_idname == "NodeReroute" : 
        return socketFromReroute(socket.node)
    return socket

def nodeFromReroute(reroute) : 
    s = socketFromReroute(reroute)
    if s : 
        return s.node
    return None

def socketsToReroute(reroute) : 
    sockets = []
    for l in reroute.outputs[0].links : 
        socket = l.to_socket
        while socket and socket.node.bl_idname == "NodeReroute" : 
            sockets += socketsToReroute(socket.node)
            socket = None

    return sockets

def nodesToReroute(reroute) : 
    sockets = socketsToReroute(reroute)
    nodes = []
    for s in sockets : 
        nodes.append(s.node)

    return nodes

def nodeFromSocket(socket) : 
    s = socketFromSocket(socket)
    if s : 
        return s.node
    return None

def socketFromSocket(socket) : 
    if not socket : 
        return None
    if len(socket.links) == 0 : 
        return None
    node = socket.links[0].from_node
    socket = socket.links[0].from_socket
    while node and node.bl_idname == "NodeReroute" : 
        socket = socketFromReroute(node)
    return socket

def nodeByType(tree, bl_idname) : 
    for n in tree.nodes : 
        if n.bl_idname == bl_idname : 
            return n
    return None

def outputNode(tree) : 
    return nodeByType(tree, "NodeGroupOutput")

def inputNode(tree) : 
    return nodeByType(tree, "NodeGroupInput")

def nodesToSocket(socket) : 
    nodes = []
    for s in socketsToSocket(socket) : 
        nodes.append(s.node)
    return nodes

def socketsToSocket(socket) : 
    if not socket : 
        return []
    if len(socket.links) == 0 : 
        return []
    sockets = []
    for l in socket.links : 
        socket = l.to_socket
        while socket and socket.node.bl_idname == "NodeReroute" : 
            return socketsToReroute(socket.node)
        sockets.append(socket)
    return sockets

def socketIndex(socket) : 
    if not socket : 
        return -1
    container = socket.node.inputs
    if socket.is_output : 
        container = socket.node.outputs

    for i in range(len(container)) : 
        if container[i] == socket : 
            return i
    return -1

