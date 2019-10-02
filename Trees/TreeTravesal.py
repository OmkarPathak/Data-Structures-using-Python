

class Node(object):
	"""docstring for Node"""
	def __init__(self, val):
		self.key = val
		self.left=None
		self.right=None


class Tree:
	"""docstring for Tree"""
	def __init__(self,val):
		self.root = Node(val)
		
	def insertNode(root,val):
		if(root==None):
			root=Node(val)
		elif(root.key<val):
			root.right=Tree.insertNode(root.right,val)
		else:
			root.left=Tree.insertNode(root.left,val)
		return root

	def inorder(root):
		if(root==None):
			return ""
		else:
			return str(Tree.inorder(root.left)) +" "+ str(root.key) +" "+ str(Tree.inorder(root.right))


	def preorder(root):
		if(root==None):
			return ""
		else:
			return str(root.key) +" "+ str(Tree.preorder(root.left)) +" "+ str(Tree.preorder(root.right))


	def postorder(root):
		if(root==None):
			return ""
		else:
			return str(Tree.postorder(root.left)) +" "+ str(Tree.postorder(root.right)) +" "+ str(root.key)




array=[1,22,3,44,32,35]
treeRoot=Node(array[0])
for i in range(1,len(array)):
	treeRoot=Tree.insertNode(treeRoot,array[i])

print("Inorder:", Tree.inorder(treeRoot))
print("Preorder:", Tree.preorder(treeRoot))
print("Postorder:", Tree.postorder(treeRoot))




