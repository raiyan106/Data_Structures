class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def addNode(self, newNode):
        if(newNode.val<self.val):
            if(self.left==None):
                self.left = newNode
            else:
                self.left.addNode(newNode)

        elif(newNode.val>self.val):
            if(self.right==None):
                self.right = newNode
            else:
                self.right.addNode(newNode)
    
    def findNode(self, newNode):
        if(self.val == newNode.val):
            #print("Found the value {}".format(newNode.val))
            return True
        elif(self.val>newNode.val):
            if(self.left != None):
                return self.left.findNode(newNode)
        elif(self.val<newNode.val):
            if(self.right!=None):
                return self.right.findNode(newNode)

        return False
        