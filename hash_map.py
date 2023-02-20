import sys

class Node:
    def __init__(self,key,value,next):
        self.key = key
        self.value = value
        self.next = next

class HashMap:
    def __init__(self):
        self.arr = 5 * [None]
        self.count = 0
        self.unique = 0
        self.resizes = []

    def my_hash(self,s):
        h = 0
        for c in s:
            h = (h * 1_000_003 + ord(c)) % (2 ** 32)
        return h 

    def set (self, key, value):

 
        b = self.my_hash(key) % len(self.arr)
        node = self.arr[b]
        while node != None:
            if node.key == key:
              
                node.value = node.value + value
                return
            else:
                
                node = node.next
        self.arr[b] = Node(key, value ,self.arr[b])  
        self.unique +=1

        if self.unique / len(self.arr) >= 4:
            new_a = [None] * 2 * len(self.arr) 
            for p in self.arr:
                while p != None:
                    b = self.my_hash(p.key) % len(new_a)
                    new_a[b] = Node(p.key, p.value ,new_a[b])   
                    p = p.next
            self.arr = new_a
            
            self.resizes.append(('resizing to' , len(self.arr) , 'buckets'))
          
    def contains(self,key):
        b = self.my_hash(key) % len(self.arr)
        p = self.arr[b]
        while p != None:
            if p.key == key:
                return True
            p.next
        return False

    def get(self,key):
        b = self.my_hash(key) % len(self.arr)
        p = self.arr[b]
        while p != None:
            if p.key == key:
                return p.value
            p = p.next 
        return None

    def remove(self,key):
        b = self.my_hash(key) % len(self.arr)
        head = self.arr[b]  

        if head == None:  
            return
        if head.key == key:  
            self.arr[b] = head.next
        
            return
        while head.next != None:
            if head.next.key == key:
        
                head.next = head.next.next
              
                return
            head = head.next
    def print_resize(self):
        return self.resizes
       
output = []
end = False
hashmap = HashMap()
word = ''
for line in sys.stdin:
    if '== END ==' in line:
        end = True
        continue
   
    for element in line:
        if 'a' <= element <= 'z' or 'A' <= element <= 'Z':
            word += element.lower()
        elif word != '' and end == False: 
          
            hashmap.set(word.lower(),1)
            word = ''
        else:
            if word != '':
                output.append((word.lower(),hashmap.get(word.lower())))
              
                hashmap.remove(word.lower())
                word = ''
    word = ''
  
outputSize = hashmap.print_resize()

for repeatation in outputSize:
    print(repeatation[0], repeatation[1] , repeatation[2])
print('unique words = ',hashmap.unique)
for words in output:
    print(words[0],words[1])

