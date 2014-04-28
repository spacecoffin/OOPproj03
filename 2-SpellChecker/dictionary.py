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

class HashTableDict:
    def __init__(self, size=5003):
        self.list=[['']]*size
        self.table_size = size
        
    def lookup(self, key):
        # call self.hash(key) to get index
        index = self.make_hash(key)
        # find the correct key at that bucket
        if key in self.list[index]:
            return key
        else:
            return None
    
    def insert(self, key):
        # call self.hash(key) to get index
        index = self.make_hash(key)
        # insert new key-value pair to that bucket.
        #print('key is {}'.format(key))
        if self.list[index][0]:                       # resolve collisions
            #print('collision at {}'.format(index))
            self.list[index].append(key)
            #print(self.list[index])
        else:
            self.list[index][0] = key
        
    def make_hash(self, word):
        hash_val = 0
        for char in word:
            hash_val *= 26
            hash_val += ord(char) - 97
            # avoid int overflow by taking mod M at the end of each iteration
            hash_val = hash_val % self.table_size
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
        file.seek(0)
        line_count -= 500
        line_count //= 2
        line_count = abs(line_count) # fix so that small words.dat works
        line_count = nextPrime(line_count)
            
        self.primary = HashTableDict(size=5003)
        self.secondary = HashTableDict(size=line_count)
        
        current_line = 0
        while current_line < 500:
            word = file.readline()
            word = word.rstrip('\n')
            self.primary.insert(word)
            current_line += 1
        
        for word in file:
            word = word.rstrip('\n')
            self.secondary.insert(word)
        #print(self.primary.list)
        #print(self.secondary.list)
        #print(line_count)
            
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
            print('{} in PRIMARY'.format(word))
            return word
        elif self.secondary.lookup(smallword):
            print('{} in SECONDARY'.format(word))
            return word
        else:
            print('{} not found'.format(word))
            return None

    def update(self, choice, newword, word):
        """
        updates the keepwords list and the mapper dictionary.
        """
        if choice in ['p', 'P']:
            self.mapper[word.lower()] = newword
        elif choice in ['n', 'N']:
            self.keepwords.append(newword)