import os

class Dictionary:
    """
    Maintains the following lists.
      words: list of dictionary words.
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
        self.words = [w.rstrip('\n') for w in file.readlines()]
        self.words.append('a'); self.words.append('i')
        self.mapper = {}
        self.keepwords = []

    def verify(self, word):
        """
        check if the word is in the dictionary or in 'keepwords'. If
        so, word is returned. If not, we check if the user has a
        mapping defined for the word. If so, the replacement word is
        returned. 
        """
        
        smallword= word.lower()
        if smallword in self.mapper:
           return self.mapper[smallword]
        elif smallword in self.keepwords or smallword in self.words:
            return word
        else: return None

    def update(self, choice, newword, word):
        """
        updates the keepwords list and the mapper dictionary.
        """
        if choice in ['p', 'P']:
            self.mapper[word.lower()] = newword
        elif choice in ['n', 'N']:
            self.keepwords.append(newword)

    


