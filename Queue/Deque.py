# Author: OMKAR PATHAK

class Deque(object):
    def __init__(self, limit = 10):
        self.queue = []
        self.limit = limit

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # check if queue is empty
    def isEmpty(self):
        return len(self.queue) <= 0

    # check if queue is full
    def isFull(self):
        return len(self.queue) >= self.limit

    # for inserting at rear
    def insertRear(self, data):
        if self.isFull():
            return
        else:
            self.queue.insert(0, data)

    # for inserting at front end
    def insertFront(self, data):
        if self.isFull():
            return
        else:
            self.queue.append(data)

    # deleting from rear end
    def deleteRear(self):
        if self.isEmpty():
            return
        else:
            return self.queue.pop(0)

    # deleting from front end
    def deleteFront(self):
        if self.isFull():
            return
        else:
            return self.queue.pop()

if __name__ == '__main__':
    myDeque = Deque()
    myDeque.insertFront(1)    # 1
    myDeque.insertRear(2)     # 2 1
    myDeque.insertFront(3)    # 2 1 3
    myDeque.insertRear(10)    #10 2 1 3
    print(myDeque)
    myDeque.deleteRear()      # 2 1 3
    print(myDeque)
    myDeque.deleteFront()     # 2 1
    print(myDeque)
