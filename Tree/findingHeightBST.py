class Node:
    def __init__(self,value):
        self.value = value
        self.leftChild = None
        self.rightChild = None 

class BSTree:
    def __init__(self):
        self.root = None 


    # Find Height 
    def height(self):
        if self.root != None:
            return self._height(self.root,0)
        else:
            return 0
    def _height(self,currentNode,currentHeight):
        if currentNode is None:
            return currentHeight
        leftHeight = self._height(currentNode.leftChild,currentHeight+1)
        rightHeight =self. _height(currentNode.rightChild,currentHeight+1)
        return max(leftHeight,rightHeight)
        
