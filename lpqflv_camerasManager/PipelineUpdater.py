class PipelineUpdater : 
    def __init__(self) : 
        self.pnt = None
        self.nodeUpdaters = []

    def getNodes(self) : 
        for node in self.pnt.nodes : 
            exists = False
            for upNode in self.nodeUpdaters : 
                if upNode.node == node : 
                    exists = True
                    break
            if not exists : 
                self.nodeUpdaters.append(NodeUpdater(node))
        
        for upNode in self.nodeUpdaters : 
            exists = False 
            for node in self.pnt.nodes : 
                if node == upNode.node  : 
                    exists = True 
                    break
            if not exists : 
                upNode.toDelete = True

            goods = []
            for upNode in self.nodeUpdaters : 
                if not upNode.toDelete : 
                    goods.append(upNode)

            self.nodeUpdaters = goods

    def new(self, bl_node) : 
        self.nodeUpdaters.append(NodeUpdater(bl_node))

    def terminate(self) : 
        self.pnt = None 
        self.nodeUpdaters = []

class NodeUpdater : 
    def __init__(self, bl_node) : 
        self.node = bl_node 
        self.linkedSockets = []
        self.unlinkedSockets = []
        self.toDelete = False

    def updateLinked(self) : 
        sockets = []
        for s in self.node.inputs : 
            if s.is_linked : 
                sockets.append(s)
        self.linkedSockets = []
        self.linkedSockets = sockets.copy()

    def updateUnlinked(self) : 
        sockets = []
        for s in self.node.inputs : 
            if not s.is_linked : 
                sockets.append(s)
        self.unlinkedSockets = []
        self.unlinkedSockets = sockets.copy()

    def connectionMade(self) : 
        so = None
        for s in self.node.inputs : 
            if not s.is_linked : 
                continue
            if not s in self.linkedSockets : 
                so = s
                break
        self.updateLinked()
        return so

    def connectionBroke(self) : 
        so = []
        for s in self.node.inputs : 
            if s.is_linked : 
                continue
            if not s in self.unlinkedSockets  : 
                so.append(s)
        self.updateUnlinked()
        return so

