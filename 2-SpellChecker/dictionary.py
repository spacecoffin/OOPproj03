import os

def isPrime(num):
    if num > 1:
        if num == 2 or num == 3:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, num, 2):
            if num % i == 0:
                return False
        return True
    return False

def nextPrime(num):
    while True:
        if isPrime(num):
            return num
        num += 1

class HashTable:
    def __init__(self, size=5003):
        self.size = size
        self.table = [[] for n in range(self.size)]
        
    def lookup(self, item):
        # call self.hash(key) to get index
        index = self.hash(item)
        # find the correct key at that bucket
        if item in self.table[index]:
            return item
        else:
            return None
    # REMEMBER YOU CHANGED LIST TO HASH_LIST, ADD_WORD to ADD_ITEM ETC
    def add_item(self, item):
        # call self.hash(key) to get index
        index = self.hash(item)
        # insert new key-value pair to that bucket.
        self.table[index].append(item) # resolve collisions
        
    def hash(self, word):
        hash_val = 0
        for char in word:
            hash_val *= 26
            if not char is "'":
                hash_val += ord(char) - 97
            # avoid int overflow by taking mod M at the end of each iteration
            hash_val = hash_val % self.size
        return hash_val

class Dictionary:
    """
    Maintains the following lists.
      primary: hashTable of 500 most frequently occuring words in dictionary.
      secondary: hashTable of the rest of the dictionary words.
      keepwords: list of words that are not in the dictionary, but the
                 user wants to keep.
      mapper: dictionary with 'key:value' pair such that every
              occurance of 'key' in the document is to be replaced by
              'value'.
    """

    def __init__(self, dic='words.dat'):
        
        #check if the file exists
        assert os.path.exists(dic),\
               'Dictionary \'%s\' does not exist.' % dic 
        file = open(dic, 'r')
        
        line_count = 0
        for line in file:
            line_count += 1
        line_count = nextPrime(abs((line_count - 500)//2))
        file.seek(0)
            
        self.primary = HashTable(size=5003)
        self.secondary = HashTable(size=line_count)
        
        current_line = 0
        while current_line < 500:
            word = file.readline()
            word = word.rstrip('\n')
            self.primary.add_item(word)
            current_line += 1
        
        for word in file:
            word = word.rstrip('\n')
            self.secondary.add_item(word)
            
        self.mapper = {}
        self.keepwords = []
        self.keepwords.append('a'); self.keepwords.append('i')
        file.close()

    def verify(self, word):
        """
        check if the word is in the dictionary or in 'keepwords'. If
        so, word is returned. If not, we check if the user has a
        mapping defined for the word. If so, the replacement word is
        returned. 
        """
        
        smallword = word.lower()
        if smallword in self.mapper:
            return self.mapper[smallword]
        elif smallword in self.keepwords:
            return word
        elif self.primary.lookup(smallword):
            #print('{} in PRIMARY'.format(word))
            return word
        elif self.secondary.lookup(smallword):
            #print('{} in SECONDARY'.format(word))
            return word
        else:
            #print('{} not found'.format(word))
            return None
    
    def dict_verify(self, word):
        smallword = word.lower()
        if self.primary.lookup(smallword):
            return word
        elif self.secondary.lookup(smallword):
            return word

    def update(self, choice, newword, word):
        """
        updates the keepwords list and the mapper dictionary.
        """
        if choice in ['p', 'P']:
            self.mapper[word.lower()] = newword
        elif choice in ['n', 'N']:
            self.keepwords.append(newword.lower())

if __name__ == '__main__':
    testdict = Dictionary()
    print(testdict.secondary.table)