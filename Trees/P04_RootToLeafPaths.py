# Author: OMKAR PATHAK

# Use a path array path[] to store current root to leaf path. Traverse from root to all leaves in top-down fashion.
# While traversing, store data of all nodes in current path in array path[]. When we reach a leaf node, print the path
# array.

class Node(object):
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = data

def printPath(node, path = []):
    if node is None:
        return
    path.append(node.data)

    if (node.left is None) and (node.right is None):
        print(' '.join([str(i) for i in path if i != 0]))
    else:
        printPath(node.left, path)
        printPath(node.right, path[0:1])

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)

    printPath(root)
