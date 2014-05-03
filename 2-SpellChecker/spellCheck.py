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
        print()
    
    def ver_mis(self, word, ver='y'):
    # Missing letter function
        for i in range(len(word)+1):
            for l in range(26):
                temp_word = word[:i] + chr(l+97) + word[i:]
                if ver is 'y':
                    if self.adict.dict_verify(temp_word):
                        yield temp_word
                elif ver is 'n':
                    yield temp_word
    
    def ver_sub(self, word, ver='y'):
    # Substituted letter function
        for i in range(len(word)):
            for l in range(26):
                temp_word = word[:i] + chr(l+97) + word[i+1:]
                if ver is 'y':
                    if self.adict.dict_verify(temp_word):
                        yield temp_word
                elif ver is 'n':
                    yield temp_word
    
    def ver_ext(self, word, ver='y'):
    # Extra letter function
        for i in range(len(word)):
            temp_word = word[:i] + word[i+1:]
            if ver is 'y':
                if self.adict.dict_verify(temp_word):
                    yield temp_word
            elif ver is 'n':
                yield temp_word
    
    def ver_swp(self, word, ver='y'):
    # Swapped consecutive letter function
        for i in range(len(word)-1):
            temp_word = word[:i] + word[i+1] + word[i] + word[i+2:]
            if ver is 'y':
                if self.adict.dict_verify(temp_word):
                    yield temp_word
            elif ver is 'n':
                yield temp_word
    
    def askuser(self, word):
        """
        if the word is not found in the dictionary, user input is
        requested
        """
        
        print (('\n\t\t\t"%s" is unknown.\n') % word)
    
        query = 'replace(R), replace all(P), ignore(I), ignore all(N), exit(E): '
    
        choice = input(query).lower()
        while choice not in ['r','p','i','n','e']:
            choice = input(query).lower()        
    
        newword = word
        # YOURE DOING THE TITLECASE THING
        if choice in  ['R','r','P','p']:
            self.suggestion_list = []
                
            # Missing letter check
            for i in range(len(word)+1):
                for l in range(26):
                    temp_word = word[:i] + chr(l+97) + word[i:]
                    if self.adict.dict_verify(temp_word)\
                    and not temp_word in self.suggestion_list:
                        self.suggestion_list.append(temp_word)
            
            # Substituted letter check
            for i in range(len(word)):
                for l in range(26):
                    temp_word = word[:i] + chr(l+97) + word[i+1:]
                    if self.adict.dict_verify(temp_word)\
                    and not temp_word in self.suggestion_list:
                        self.suggestion_list.append(temp_word)
                
            # Extra letter check
            for i in range(len(word)):
                temp_word = word[:i] + word[i+1:]
                if self.adict.dict_verify(temp_word) \
                and not temp_word in self.suggestion_list:
                    self.suggestion_list.append(temp_word)
                
            # Swapped consecutive letter check
            for i in range(len(word)-1):
                temp_word = word[:i] + word[i+1] + word[i] + word[i+2:]
                if self.adict.dict_verify(temp_word) \
                and not temp_word in self.suggestion_list:
                    self.suggestion_list.append(temp_word)
            
            if len(self.suggestion_list) < 10:
                for dist1 in self.ver_mis(word, ver='n'):
                    for dist2 in self.ver_mis(dist1):
                        if not dist2 in self.suggestion_list:
                            self.suggestion_list.append(dist2)
                    for dist2 in self.ver_sub(dist1):
                        if not dist2 in self.suggestion_list:
                            self.suggestion_list.append(dist2)
                    for dist2 in self.ver_ext(dist1):
                        if not dist2 in self.suggestion_list:
                            self.suggestion_list.append(dist2)
                    for dist2 in self.ver_swp(dist1):
                        if not dist2 in self.suggestion_list:
                            self.suggestion_list.append(dist2)
                for dist1 in self.ver_sub(word, ver='n'):
                    for dist2 in self.ver_mis(dist1):
                        if not dist2 in self.suggestion_list:
                            self.suggestion_list.append(dist2)
                    for dist2 in self.ver_sub(dist1):
                        if not dist2 in self.suggestion_list:
                            self.suggestion_list.append(dist2)
                    for dist2 in self.ver_ext(dist1):
                        if not dist2 in self.suggestion_list:
                            self.suggestion_list.append(dist2)
                    for dist2 in self.ver_swp(dist1):
                        if not dist2 in self.suggestion_list:
                            self.suggestion_list.append(dist2)
                for dist1 in self.ver_ext(word, ver='n'):
                    for dist2 in self.ver_mis(dist1):
                        if not dist2 in self.suggestion_list:
                            self.suggestion_list.append(dist2)
                    for dist2 in self.ver_sub(dist1):
                        if not dist2 in self.suggestion_list:
                            self.suggestion_list.append(dist2)
                    for dist2 in self.ver_ext(dist1):
                        if not dist2 in self.suggestion_list:
                            self.suggestion_list.append(dist2)
                    for dist2 in self.ver_swp(dist1):
                        if not dist2 in self.suggestion_list:
                            self.suggestion_list.append(dist2)
                for dist1 in self.ver_swp(word, ver='n'):
                    for dist2 in self.ver_mis(dist1):
                        if not dist2 in self.suggestion_list:
                            self.suggestion_list.append(dist2)
                    for dist2 in self.ver_sub(dist1):
                        if not dist2 in self.suggestion_list:
                            self.suggestion_list.append(dist2)
                    for dist2 in self.ver_ext(dist1):
                        if not dist2 in self.suggestion_list:
                            self.suggestion_list.append(dist2)
                    for dist2 in self.ver_swp(dist1):
                        if not dist2 in self.suggestion_list:
                            self.suggestion_list.append(dist2)
            
            # Prune the list to contain exactly 10 words.
            self.suggestion_list = self.suggestion_list[:10]
            
            for item in range(len(self.suggestion_list)):
                print('( {} ) {}'.format(item, self.suggestion_list[item]))
            print('( {} ) Use my replacement'.format(len(self.suggestion_list)))
            
            while True:
                replace_choice = int(input('Your choice:  '))
                if replace_choice == len(self.suggestion_list):
                    newword = input('Replacement word: ')
                    break
                elif replace_choice < len(self.suggestion_list):
                    newword = self.suggestion_list[replace_choice]
                    break
                else:
                    print('Choose an option in the range 0-{}'.format(
                        len(self.suggestion_list)))
            
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
                            choice, newword = self.askuser(word)
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
                        choice, newword = self.askuser(word)
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

