#  Author: VARNIT SHARMA (LunaticProgrammer)

import SinglyLinkedList

def findMid(myLinkedList):
    '''
    The approch is simple:
    1. creating a fast pointer that is moving and skipping one element of the linked-list
    2. creating a slow pointer that goes through every next element in the linked-list
    3. when the fast pointer has reached the end the slower one is supposed to be at mid
    4. return the element pointed by slow pointer

    Time-O(logN) where N is the number of elements in linked-list

    '''
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
