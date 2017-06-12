# Author: OMKAR PATHAK

# Linked List and Node can be accomodated in separate classes for convenience

class Node(object):
    # Each node has its data and a pointer that points to next node in the Linked List
    def __init__(self, data, next = None):
        self.data = data;
        self.next = next;

    # function to set data
    def setData(self, data):
        self.data = data;

    # function to get data of a particular node
    def getData(self):
        return self.data

    # function to set next node
    def setNext(self, next):
        self.next = next

    # function to get the next node
    def getNext(self):
        return self.next

class LinkedList(object):
    # Defining the head of the linked list
    def __init__(self):
        self.head = None

    # printing the data in the linked list
    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next

    # inserting the node at the beginning
    def insertAtStart(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    # inserting the node in between the linked list (after a specific node)
    def insertBetween(self, previousNode, data):
        if (previousNode.next is None):
            print('Previous node should have next node!')
        else:
            newNode = Node(data)
            newNode.next = previousNode.next
            previousNode.next = newNode

    # inserting at the end of linked list
    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        while(temp.next != None):         # get last node
            temp = temp.next
        temp.next = newNode

    # deleting an item based on data(or key)
    def delete(self, data):
        temp = self.head
        # if data/key is found in head node itself
        if (temp.next is not None):
            if(temp.data == data):
                self.head = temp.next
                temp = None
                return
            else:
                #  else search all the nodes
                while(temp.next != None):
                    if(temp.data == data):
                        break
                    prev = temp          #save current node as previous so that we can go on to next node
                    temp = temp.next

                # node not found
                if temp == None:
                    return

                prev.next = temp.next
                return

    # iterative search
    def search(self, node, data):
        if node == None:
            return False
        if node.data == data:
            return True
        return self.search(node.getNext(), data)

if __name__ == '__main__':
    List = LinkedList()
    List.head = Node(1)                # create the head node
    node2 = Node(2)
    List.head.setNext(node2)           # head node's next --> node2
    node3 = Node(3)
    node2.setNext(node3)               # node2's next --> node3
    List.insertAtStart(4)              # node4's next --> head-node --> node2 --> node3
    List.insertBetween(node2, 5)       # node2's next --> node5
    List.insertAtEnd(6)
    List.printLinkedList()
    print()
    List.delete(3)
    List.printLinkedList()
    print()
    print(List.search(List.head, 1))
