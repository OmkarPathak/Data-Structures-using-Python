# Author: OMKAR PATHAK

# Input: root node, key
#
# Output: predecessor node, successor node
# 1. If root is NULL
#       then return
# 2. if key is found then
#     a. If its left subtree is not null
#         Then predecessor will be the right most
#         child of left subtree or left child itself.
#     b. If its right subtree is not null
#         The successor will be the left most child
#         of right subtree or right child itself.
#     return
# 3. If key is smaller then root node
#         set the successor as root
#         search recursively into left subtree
#     else
#         set the predecessor as root
#         search recursively into right subtree

# Python program to find predecessor and successor in a BST

# A BST node
class Node(object):
    # Constructor to create a new node
    def __init__(self, data):
        self.data  = data
        self.left = None
        self.right = None

    # for finding the predecessor and successor of the node
    def findPredecessorAndSuccessor(self, data):
        global predecessor, successor
        predecessor = None
        successor = None

        if self is None:
            return

        # if the data is in the root itself
        if self.data == data:
            # the maximum value in the left subtree is the predecessor
            if self.left is not None:
                temp = self.left
                if temp.right is not None:
                    while(temp.right):
                        temp = temp.right
                predecessor = temp

            # the minimum of the right subtree is the successor
            if self.right is not None:
                temp = self.right
                while(temp.left):
                    temp = temp.left
                successor = temp

            return

        #if key is smaller than root, go to left subtree
        if data < self.data:
            print('Left')
            self.left.findPredecessorAndSuccessor(data)
        else:
            print('Right')
            self.right.findPredecessorAndSuccessor(data)

    def insert(self, data):
        ''' For inserting the data in the Tree '''
        if self.data == data:
            return False        # As BST cannot contain duplicate data

        elif data < self.data:
            ''' Data less than the root data is placed to the left of the root '''
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True

        else:
            ''' Data greater than the root data is placed to the right of the root '''
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

if __name__ == '__main__':
    root = Node(50)
    root.insert(30)
    root.insert(20)
    root.insert(40)
    root.insert(70)
    root.insert(60)
    root.insert(80)

    # following BST is created
    #               50
    #            /     \
    #           30      70
    #          /  \    /  \
    #        20   40  60   80

    root.findPredecessorAndSuccessor(70)
    if  (predecessor is not None) and (successor is not None):
        print('Predecessor:', predecessor.data, 'Successor:', successor.data)
    else:
        print('Predecessor:', predecessor, 'Successor:', successor)
