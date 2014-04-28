def string_hash(string):
    hash_val = 0
    for char in string:
        hash_val *= 26
        hash_val += ord(char) - 97
    return hash_val

def mod_hash(string, table_size):
    hash_val = 0
    for char in string:
        hash_val *= 26
        hash_val += ord(char) - 97
    return hash_val % table_size

def multmod_hash(string, table_size):
    hash_val = 0
    for char in string:
        hash_val *= 26
        hash_val += ord(char) - 97
        # avoid int overflow by taking mod M at the end of each iteration
        hash_val = hash_val % table_size
    return hash_val

class HashTableDict:
    def __init__(self, size):
        self.list=['']*size
        
    def lookup(self, key):
        # call self.hash(key) to get index
        index = self.make_hash(key)
        # find the correct key at that bucket
        return self.list[index]
    
    def insert(self, key, value):
        # call self.hash(key) to get index
        index = self.make_hash(key)
        if self.list[index]:                       # resolve collisions
            if isinstance(self.list[index], list):
                self.list[index].append(value)
            elif isinstance(self.list[index], str):
                present_str = self.list[index]
                self.list[index] = []
                self.list[index].append(present_str)
                self.list[index].append(value)
        # insert new key-value pair to that bucket.
        self.list[index] = key
        
    def make_hash(self, word):
        for char in word:
            self.hash_val *= 26
            self.hash_val += ord(char) - 97
            # avoid int overflow by taking mod M at the end of each iteration
            self.hash_val = self.hash_val % self.table_size
        return self.hash_val

if __name__ == '__main__':
    primary_dict = HashTableDict()