from Node import Node

class Tree:
    def __init__(self):
        self.root = None

    def addValue(self,value):
        n = Node(value)
        if(self.root == None):
            self.root = n
        else:
            self.root.addNode(n)
        

    def showNodes(self,node):
        if(node==None):
            return
        else:
            self.showNodes(node.left)
            print(node.val)
            self.showNodes(node.right)

    def printTree(self):
        self.showNodes(self.root)


    def findValue(self,value):
        n = Node(value)
        return self.root.findNode(n)