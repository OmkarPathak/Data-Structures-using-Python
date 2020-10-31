class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break
                else:
                    lastNode=lastNode.next
            lastNode.next=newNode
    def printlist(self):
        currentNode=self.head
        while True:
            if currentNode is None:
                break
            else:
                print(currentNode.data)
                currentNode=currentNode.next

    def reverse(self, head, k):
        current = head
        next = None
        prev = None
        count = 0
        # Reverse first k nodes of the linked list
        while (current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
        if next is not None:
            head.next = self.reverse(next, k)

            # prev is new head of the input list
        return prev
if __name__=='__main__' :
        llist1=Linkedlist()
        firstNode=Node(input("Enter 1st Node Data"))
        llist1.insert(firstNode)
        secondNode = Node(input("Enter 2nd Node Data"))
        llist1.insert(secondNode)
        thirdNode = Node(input("Enter 3rd Node Data"))
        llist1.insert(thirdNode)
        fouthNode = Node(input("Enter 4th Node Data"))
        llist1.insert(fouthNode)
        fifthNode = Node(input("Enter 5th Node Data"))
        llist1.insert(fifthNode)
        sixthNode = Node(input("Enter 6th Node Data"))
        llist1.insert(sixthNode)
        seventhNode = Node(input("Enter 7th Node Data"))
        llist1.insert(seventhNode)
        k=int(input("Enter value of Key"))
        print("given Linked list",llist1.printlist())
        llist1.head=llist1.reverse(llist1.head,k)
        print("rev Linked list",llist1.printlist())



