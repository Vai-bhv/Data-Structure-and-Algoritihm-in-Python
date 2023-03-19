class Queue(object):
    # # Queue() method to create an empty queue
    def __init__(self):
        self.items = []
    # enqueue(item) to add an item to the rear of Queue
    def enqueue(self, item):
        self.items.insert(0,item)
    # dequeue() to remove the item from the begining of the Queue
    def dequeue(self):
        self.items.pop()
    # isEmpty() to check wheter the queue is empty or not
    def isEmpty(self):
        return self.items == []
    # size()  returns the size of the Queue
    def size(self):
        return len(self.items)

