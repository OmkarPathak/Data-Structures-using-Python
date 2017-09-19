# Author: OMKAR PATHAK

# This program illustrates an example of Binary Search Tree using Python
# Binary Search Tree, is a node-based binary tree data structure which has the following properties:
#
# The left subtree of a node contains only nodes with keys less than the node’s key.
# The right subtree of a node contains only nodes with keys greater than the node’s key.
# The left and right subtree each must also be a binary search tree.
# There must be no duplicate nodes.

class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        ''' For inserting the data in the Tree '''
        if self.data == data:
            return False        # As BST cannot contain duplicate data

        elif data < self.data:
            ''' Data less than the root data is placed to the left of the root '''
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        else:
            ''' Data greater than the root data is placed to the right of the root '''
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.leftChild is not None):
            current = current.leftChild

        return current

    def delete(self, data):
        ''' For deleting the node '''
        if self is None:
            return None

        # if current node's data is less than that of root node, then only search in left subtree else right subtree
        if data < self.data:
            self.leftChild = self.leftChild.delete(data)
        elif data > self.data:
            self.rightChild = self.rightChild.delete(data)
        else:
            # deleting node with one child
            if self.leftChild is None:
                temp = self.rightChild
                self = None
                return temp
            elif self.rightChild is None:
                temp = self.leftChild
                self = None
                return temp

            # deleting node with two children
            # first get the inorder successor
            temp = self.minValueNode(self.rightChild)
            self.data = temp.data
            self.rightChild = self.rightChild.delete(temp.data)

        return self

    def find(self, data):
        ''' This function checks whether the specified data is in tree or not '''
        if(data == self.data):
            return True
        elif(data < self.data):
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        '''For preorder traversal of the BST '''
        if self:
            print(str(self.data), end = ' ')
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def inorder(self):
        ''' For Inorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.data), end = ' ')
            if self.rightChild:
                self.rightChild.inorder()

    def postorder(self):
        ''' For postorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.data), end = ' ')

class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        if self.root is not None:
            print()
            print('Preorder: ')
            self.root.preorder()

    def inorder(self):
        print()
        if self.root is not None:
            print('Inorder: ')
            self.root.inorder()

    def postorder(self):
        print()
        if self.root is not None:
            print('Postorder: ')
            self.root.postorder()

if __name__ == '__main__':
    tree = Tree()
    tree.insert(10)
    tree.insert(12)
    tree.insert(5)
    tree.insert(4)
    tree.insert(20)
    tree.insert(8)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    print(tree.find(1))
    print(tree.find(12))
    ''' Following tree is getting created:
                    10
                 /      \
               5         12
              / \           \
            4     8          20
                 /          /
                7         15
                         /
                       13
    '''

    tree.preorder()
    tree.inorder()
    tree.postorder()
    print('\n\nAfter deleting 20')
    tree.delete(20)
    tree.inorder()
    tree.preorder()
    print('\n\nAfter deleting 10')
    tree.delete(10)
    tree.inorder()
    tree.preorder()
