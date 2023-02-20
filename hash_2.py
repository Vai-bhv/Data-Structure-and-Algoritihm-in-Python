import sys
class HashMap:
    def __init__(self):
        # Initialize an empty hash table with 5 buckets
        self.buckets = 5
        self.table = [[] for _ in range(self.buckets)]
    
    def set(self, key, value):
        # Hash the key to get the index for the bucket
        idx = hash(key) % self.buckets
        
        # Check if the key already exists in the bucket
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                # If the key exists, update the value and return
                self.table[idx][i] = (key, value)
                return
        
        # If the key does not exist, add it to the bucket
        self.table[idx].append((key, value))
        
        # Check if the load factor exceeds 4
        if len(self.table[idx]) / self.buckets > 4:
            # Double the number of buckets and rehash the keys
            self.resize()
    
    def get(self, key):
        # Hash the key to get the index for the bucket
        idx = hash(key) % self.buckets
        
        # Check if the key exists in the bucket
        for k, v in self.table[idx]:
            if k == key:
                # If the key exists, return the value
                return v
        
        # If the key does not exist, return None
        return None
    
    def remove(self, key):
        # Remove a key from the hash map if present
        bucket = self._hash(key)
        for i, kv in enumerate(self.buckets[bucket]):
            if kv[0] == key:
                self.buckets[bucket].pop(i)
                break

m = HashMap()

# Read the input text line by line
for line in sys.stdin:
    # Stop when you reach the end of the input
    if line.strip() == "== END ==":
        break
    # Split the line into words
    words = line.split()
    # Iterate over the words and add them to the HashMap
    for word in words:
        m.set(word, m.get(word) + 1)



