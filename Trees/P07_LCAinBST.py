# Lowest Common Ancestor in Binary search tree

class node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def lca(root,n1,n2):
    if root is None:
        return None

    if root.key<n1 and root.key<n2:
        return lca(root.right,n1,n2)

    if root.key>n1 and root.key>n2:
        return lca(root.left,n1,n2)

    return root

# Consider the following BST

#                  8
#               /     \
#             3         11
#           /   \     /   \
#          2     6   10    13
#              /   \      /
#             5     7    12

# Create BST
root = node(8)
l = root.left = node(3)
r = root.right = node(11)
r.left = node(10)
r.right = node(13)
r.right.left = node(12)
l.left = node(2)
l.right = node(6)
l.right.left = node(5)
l.right.right = node(7)

print(lca(root,2,7).key) # ouputs '3'
