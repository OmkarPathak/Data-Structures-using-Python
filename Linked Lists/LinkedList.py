class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_data(self, data):

        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next_node = self.head
            self.head = node

    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node

    def delete_node(self, data):
        current_node = self.head
        previous_node = current_node
        while current_node.data != data:
            previous_node = current_node
            current_node = current_node.next_node

        if current_node is self.head:
            self.head = current_node.next_node

        node_pointer = current_node.next_node
        current_node.next_node = None
        previous_node.next_node = node_pointer


linked_list = LinkedList()
import time
t = time.time()
for i in range(5):
    linked_list.insert_data(i)
a = time.time()


linked_list.traverse()
print("Final ",a)



linked_list.traverse()
