class Node:
    def __init__(self,value):
        self.value = value
        self.leftChild = None
        self.rightChild = None 

class BSTree:
    def __init__(self):
        self.root = None 
    

#search Function
    def search(self,value):
		if self.root!=None:
			return self._search(value,self.root)
		else:
			return False

	def _search(self,value,cur_node):
		if value==cur_node.value:
			return True
		elif value<cur_node.value and cur_node.leftChild!=None:
			return self._search(value,cur_node.leftChild)
		elif value>cur_node.value and cur_node.rightChild!=None:
			return self._search(value,cur_node.rightChild)
		return False 
