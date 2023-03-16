# Functions that i will be using
class stack(object):
# stack() - To create a new stack
    def __init__(self):
        self.stack = []
    # push(item) - to add an item on top of stack
    def push(item, self):
        self.stack.append(item)

    # pop() - remove an item from the stack
    def pop(self):
        return stack.pop()


    # peek() - returns the item on top of stack but doesnt remove it 
    def peek(self):
        return self.stack[-1]


    # isEmpty() - check whether stack is empty or not
    def isEmpty(self):
        return self.stack == []

    # size() - returns the size of stack
    def size(self):
        return len(self.stack)

