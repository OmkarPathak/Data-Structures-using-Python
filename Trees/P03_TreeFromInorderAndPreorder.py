# Python program to construct tree using inorder and
# preorder traversals

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

"""Recursive function to construct binary of size len from
   Inorder traversal in[] and Preorder traversal pre[].  Initial values
   of start and end should be 0 and len -1.  The function doesn't
   do any error checking for cases where inorder and preorder
   do not form a tree """
def buildTree(inOrder, preOrder, start, end):
    if (start > end):
        return None

    # Pick current node from Preorder traversal using
    # preIndex and increment preIndex
    tNode = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1

    # If this node has no children then return
    if start == end :
        return tNode

    # Else find the index of this node in Inorder traversal
    rootIndex = search(inOrder, start, end, tNode.data)

    # Using index in Inorder Traversal, construct left
    # and right subtrees
    tNode.left = buildTree(inOrder, preOrder, start, rootIndex-1)
    tNode.right = buildTree(inOrder, preOrder, rootIndex+1, end)

    return tNode

# function to search for the index
def search(arr, start, end, value):
    for i in range(start, end+1):
        if arr[i] == value:
            return i

# function to print the contents of the tree in inorder fashion
def inorder(node):
    if node is None:
        return

    # first recur on left child
    inorder(node.left)
    #then print the data of node
    print (node.data, end = ' ')
    # now recur on right child
    inorder(node.right)

# Driver program to test above function
inOrder = ['D', 'B' ,'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']

# Static variable preIndex
buildTree.preIndex = 0
root = buildTree(inOrder, preOrder, 0, len(inOrder)-1)

# Let us test the build tree by priting Inorder traversal
print ("Inorder traversal of the constructed tree is")
inorder(root)
