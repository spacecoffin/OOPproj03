from dictionary import Dictionary

class SpellChecker:
    def __init__(self):
        self.adict = Dictionary()
    
    def statistics(self):
        self.stats_dict = {}
        for index in range(self.adict.primary.size):
            length = len(self.adict.primary.table[index])
            count = self.stats_dict.get(length, None)
            if count:
                self.stats_dict[length] += 1
            else:
                self.stats_dict[length] = 1
        max_length = max(self.stats_dict.keys())
        
        print('\nStats on Primary Dictionary', '-'*31, sep='\n')
        print('Length', ' '*9, 'Number of Lists', sep='')
        
        for list_length in range(max_length+1):
            list_total = self.stats_dict[list_length]
            print('{}{:<3}{}{:>5}'.format(
                ' '*3, list_length, ' '*12, list_total))
        
        self.stats_dict = {}
        for index in range(self.adict.secondary.size):
            length = len(self.adict.secondary.table[index])
            count = self.stats_dict.get(length, None)
            if count:
                self.stats_dict[length] += 1
            else:
                self.stats_dict[length] = 1
        max_length = max(self.stats_dict.keys())
        
        print('\nStats on Secondary Dictionary', '-'*31, sep='\n')
        print('Length', ' '*9, 'Number of Lists', sep='')
        
        for list_length in range(max_length+1):
            list_total = self.stats_dict[list_length]
            print('{}{:<3}{}{:>5}'.format(
                ' '*3, list_length, ' '*12, list_total))
    
    def askuser(word):
        """
        if the word is not found in the dictionary, user input is
        requested
        """
        
        print (('\n\t\t\t%s\n') % word)
    
        query = 'replace(R), replace all(P), ignore(I), ignore all(N), exit(E): '
    
        choice = input(query).lower()
        while choice not in ['r','p','i','n','e']:
            choice = input(query).lower()        
    
        newword = word
        if choice in  ['R','r','P','p']:
            suggestion_list = []
            for index in word:
                while len(suggestion_list) < 10:
                    if self.adict.primary.lookup(word[index+1:]):
                    
                
            
            #newword = input ('Replacement word: ')
            
            # REPLACEMENT BIT UP HERE
            
    
        return (choice, newword)
    
    def spellcheck(self, text="mytext"):
        """
        reads words from the file to be spell-checked and checks if the word
        is in the dictionary. If not, user is queried for input. The
        output is written to the file.
        """
        infile = open(text, 'r')
        outfile = open(text+".out", 'w')
    
        def processinput(choice, newword, word):
            """
            update the dictionary based on the user input.
            If the user wants to exit, copy the rest of the input file to
            the output
            """
            if choice in ['p','P','n','N']:
                self.adict.update(choice,newword, word)
            elif choice in ['e','E']:
                for line in infile:
                    outfile.write(line)
                
        try:
            wordch = []
            #apostrophe_count = 0
            while True:
                char = infile.read(1)
                if not char:
                    if len(wordch) > 0:
                        word = ''.join(wordch)
                        if word[-1] is "'":
                            word = word[:-1] # strip trailing apostrophes
                        newword = self.adict.verify(word)
                        if newword is None:
                            choice, newword = askuser(word)
                            outfile.write(newword)
                            processinput(choice, newword, word)
                        else:
                            outfile.write(newword)
                    break
                elif char.isalpha():
                    wordch.append(char)
                elif char is "'":
                    if wordch: # don't begin words with apostrophes
                        wordch.append(char)
                        #apostrophe_count += 1
                elif len(wordch) == 0:
                    outfile.write(char)
                    # not done this
                else:
                    word = ''.join(wordch)
                    if word[-1] is "'":
                        word = word[:-1] # strip trailing apostrophes
                    newword = self.adict.verify(word)
                    if newword is None:
                        choice, newword = askuser(word)
                        outfile.write(newword); outfile.write(char)
                        processinput(choice, newword, word)
                    else:
                        outfile.write(newword); outfile.write(char)
                    wordch = []
        finally:
            infile.close()
            outfile.close()

if __name__ == '__main__':
    query = 'Name of the document to be spell-checked: '
    spellcheckandoutput(input(query))

