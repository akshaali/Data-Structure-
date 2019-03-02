class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None


    #Tells length
    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length +=1
            currentNode = currentNode.next
        return length
        
        

    # Insertion function    
    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
        while True:
            if lastNode.next is None:
                break
            lastNode = lastNode.next
        lastNode.next = newNode



    # Insert in between
    def insertAt(self, newNode, position):
        currentNode = self.head
        currentPosition = 0
        if position == 0:
            self.inserthead(newNode)
            return
        if position <0 or posittion > self.listLength():
            print("Invalid position")
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition +=1





    #Insert head
    def inserthead(self, newNode):
        temporaryNode = self.head
        self.head = NewNode
        self.head.next = temporaryNode
        del temporaryNode

    #Delete from last node
    def deleteEnd(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        del lastNode
        previousNode.next = None


    # Delete At position
    def deleteAt(self, position):
        if position < 0 or position >= self.listlength():
            print("Invalid position")
            return
        if self.isListEmpty() is False:
            if position is 0:
                self.deleteHead()
                return
            currentPosition = 0
            currentNode = self.head
            while True:
                if currentNode == position:
                    previousNode.next = currentNode.next
                    currentNode.next = None
                    break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition +=1
            
            
        
    

        
    #print the linked list element       
    def printlist(self):
        if self.head is None:
            print("List is empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
    







firstNode = Node("John")
linkedlist = LinkedList()
linkedlist.insertEnd(firstNode)
secondNode = Node("Ross")
linkedlist.insertEnd(secondNode)
thirdNode = Node("April")
linkedlist.insertEnd(thirdNode)
headNode = Node("Pink")
linkedlist.inserthead()
inbetweenNode = Node(10)
linkedlist.insertAt(inbetweenNode,1)
linkedlist.deleteEnd()
linkedlist.deleteAt(1)
linkedlist.printlist()
