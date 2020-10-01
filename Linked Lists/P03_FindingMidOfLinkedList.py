#  Author: VARNIT SHARMA (LunaticProgrammer)

import SinglyLinkedList

def findMid(myLinkedList):
    if not myLinkedList or not myLinkedList.head.next: return myLinkedList.head
    
    slow = myLinkedList.head
    fast = myLinkedList.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


if __name__ == '__main__':
    myLinkedList = SinglyLinkedList.LinkedList()
    for i in range(10, 0, -1):
        myLinkedList.insertAtStart(i)
    print("LinkedList",end=" ")
    myLinkedList.printLinkedList()
    print()
    midleElement = findMid(myLinkedList)
    print("The middle element of the LinkedList is",midleElement.data)

    # OUTPUT:
    # The middle element of the LinkedList is 6
