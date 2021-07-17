# LCA - least common ancestor
# The lowest common ancestor of two nodes n1 and n2 is the lowest node in tree that has both n1 and n2 as descendants.


class node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def lca(root,n1,n2):
    if root is None:
        return None

    if root.key == n1 or root.key == n2:
        return root

    left = lca(root.left, n1, n2)
    right = lca(root.right, n1, n2)

    if left and right:
        return root

    return left if left else right


# Consider the following binary tree

#                  3
#               /     \
#             6         8
#           /   \         \
#          2     11        13
#              /    \      /
#             9      5    7

# Create binary tree
root=node(3)
l = root.left = node(6)
r = root.right = node(8)
r.right = node(13)
r.right.left = node(7)
l.left = node(2)
l.right = node(11)
l.right.left = node(9)
l.right.right = node(5)
 
print(lca(root, 2, 5).key)  # outputs '6'  
