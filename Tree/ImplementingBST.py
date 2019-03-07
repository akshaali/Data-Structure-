# Binary Search Tree in Python

class Node:
    def __init__(self,value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

class BSTree:
    def __init__(self):
        self.root = None


    # insert Function
    def insert(self,value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)   #private FUnction


    # the reason why we are putting two insert function here 'cause it's 
    # gonna be recursive , it's easier to handle a recursive  case in a single fun.

    def _insert(self, value , currentNode):
        if value < currentNode.value:
            if currentNode.leftChild == None:
                currentNode.leftChild = Node(value)
            else:
                self._insert(value , currentNode.leftChild )
        elif value > currentNode.value:
            if currentNode.rightChild == None:
                currentNode.rightChild = Node(value)
            else:
                self._insert(value, currentNode.rightChild)
        else:
            print("value already in tree!")


    # printing elements
    def printTree(self):
        if self.root != None:
            self._printTree(self.root)

    def _printTree(self , currentNode):
            if currentNode != None :
                self._printTree(currentNode.leftChild)
                print(str(currentNode.value))
                self._printTree(currentNode.rightChild)



def fillTree(tree , numElements=10 , maxInt= 100):
    from random import randint
    for _ in range(numElements):
        currentElem = randint(0,maxInt)
        #print(currentElem)
        tree.insert(currentElem)
    return tree

tree = BSTree()
#tree.insert(6)
#tree.insert(9)
#tree.insert(10)
#tree.insert(0)
#tree.insert(0)
tree = fillTree(tree)
tree.printTree()
    
                    
