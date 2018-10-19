
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)

        if self.root is None:
            self.root = node
        else:
            self.insert_again(data, self.root)

    def insert_again(self, data, node):
        if data < node.data:
            if node.left_child:
                self.insert_again(data, node.left_child)
            else:
                node.left_child = Node(data)
        else:
            if node.right_child:
                self.insert_again(data, node.right_child)
            else:
                node.right_child = Node(data)

    def min_element(self):
        self.min_rec(self.root)

    def min_rec(self, node):
        if node.left_child is not None:
            self.min_rec(node.left_child)
        else:
            print('Smallest is ', node.data)
        pass

    def max_element(self):
        self.max_rec(self.root)

    def max_rec(self, node):
        if node.right_child is not None:
            self.max_rec(node.right_child)
        else:
            print('Largest is ', node.data)
        pass

import random
b = BinarySearchTree()

for i in range(100):
    b.insert(random.randint(0,1000))


b.min_element()
b.max_element()
