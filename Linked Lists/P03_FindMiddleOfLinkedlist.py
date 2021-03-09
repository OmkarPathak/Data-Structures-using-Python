class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None

    def append(self, data):
        temp=Node(data)
        if self.head==None:
            self.head=temp
        else:
            p=self.head
            while p.next!=None:
                p=p.next
            p.next=temp

    def get_mid(self, head):
        if head == None:
            return head
        slow = fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow.data

ll=linked_list()
ll.append(2)
ll.append(6)
ll.append(8)
ll.append(1)
ll.append(4)
print(f'Middle element : {ll.get_mid(ll.head)}')
