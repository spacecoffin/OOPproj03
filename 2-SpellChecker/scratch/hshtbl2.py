class HashTable:
    def __init__(self, size=101):
        self.size = size
        self.table = [[]]*self.size
        self.table = [[] for n in range(self.size)]
    
    def hash(self, word):
        pass
    
    def lookup(self, item):
        pass
    
    def add_item(self, item):
        pass