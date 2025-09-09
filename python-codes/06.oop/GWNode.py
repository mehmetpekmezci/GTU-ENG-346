from Node import Node

class GWNode(Node) :
    def __init__(self, ip, nodeName,gw_property):
        Node.__init__(self,  ip, nodeName)
        self.gw_property=gw_property

    def getNodeType(self):
         return "Gateway Node"
