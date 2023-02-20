class Node:
    def __init__(self, data = None , next = None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_in_the_beggining(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr =  self.head
        listr = ''
        while itr:
            listr = str(itr) + '-->'
            itr = itr.next
        print(listr)
