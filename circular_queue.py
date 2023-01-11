class CircularQueue:
    def __init__(self, size):
        # Initialize an empty queue with a fixed size
        self.size = size
        self.queue = [None] * size
        self.head = 0
        self.tail = 0
        self.elements=0
        self.sum = 0
        
    def enqueue(self, n):
        # print(self.tail, self.head)
        # Add a value to the tail of the queue
        self.queue[self.tail] = n
        if self.tail + 1< self.size:
            self.tail+=1
        elif self.head > 0:
            self.tail = 0
        else:
            self.tail+=1

        # self.tail = (self.tail + 1) % self.size
        self.elements += 1
        self.sum += n

        if self.tail == self.head or (self.tail == len(self.queue) and self.head == 0):
            self.resize()
            print(f'Resized to {self.size} elements')
            self.head = 0
            self.tail = self.elements
        
    def dequeue(self):
        # Remove and return a value from the head of the queue
        value = self.queue[self.head]
        self.queue[self.head] = None
        self.head+=1
        if self.head == len(self.queue):
            self.head = 0
        self.elements -= 1
        self.sum -= value
        return value
    
    def count(self):
        # Return the number of values in the queue
        return self.elements
    
    def avg(self):
        # Return the average of all values in the queue
        return self.sum / self.elements

    def resize(self):
        self.size = self.size*2
        old_queue = self.queue
        self.queue = self.size * [None]

        if self.head < self.tail:
            self.queue[:len(old_queue)] = old_queue
        else:
            self.queue[:len(old_queue)] = old_queue[self.head:] + old_queue[:self.tail]



# def sample2():
#     q = CircularQueue(20)
#     for x in range(10):
#         q.enqueue(x)
#     for x in range(5):
#         q.dequeue()
#     for x in range(100):
#         q.enqueue(x)
#     print('count =', q.count())
#     print('average =', q.avg())
#     print(q.dequeue())

# sample2()


