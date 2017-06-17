# Author: OMKAR PATHAK

class CircularQueue(object):
    def __init__(self, limit = 10):
        self.front = None
        self.rear = None
        self.limit = limit
        self.queue = []

    # for printing the queue
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if queue is empty
    def isEmpty(self):
        return self.queue == []

    # for checking if the queue is full
    def isFull(self):
        return len(self.queue) == self.limit

    # for adding an element at the rear end
    def enqueue(self, data):
        if self.isFull():
            print('Queue is Full!')
        elif self.isEmpty():
            self.front = self.rear = 0
            self.queue.append(data)
        else:
            self.rear += 1
            self.queue.append(data)

    # for deleting the deleting an element from front end
    def dequeue(self):
        if self.isEmpty():
            print('Queue is Empty!')
        else:
            self.front += 1
            return self.queue.pop(0)

if __name__ == '__main__':
    myCQ = CircularQueue(5)
    myCQ.enqueue(14)
    myCQ.enqueue(22)
    myCQ.enqueue(13)
    myCQ.enqueue(16)
    print('Queue:',myCQ)
    myCQ.dequeue()
    myCQ.dequeue()
    print('Queue:',myCQ)
    myCQ.enqueue(9)
    myCQ.enqueue(20)
    myCQ.enqueue(5)
    myCQ.enqueue(5)
    print('Queue:',myCQ)
