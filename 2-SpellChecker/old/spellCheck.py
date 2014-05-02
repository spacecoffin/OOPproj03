from dictionary import Dictionary

"""
class SpellChecker:
    def __init__(self):
        self.adict = Dictionary()
    
    def statistics(self):
        
        self.stats_dict = {}
        for index in range(self.adict.primary.table_size):
            #print('index {}'.format(index))
            length = len(self.adict.primary.list[index])
            #print(self.adict.primary.list[index])
            #print(length)
            count = self.stats_dict.get(length, None)
            #print(count)
            if count:
                self.stats_dict[length] += 1
            else:
                self.stats_dict[length] = 1
        
        #print(self.stats_dict.items())
        
        
        bday_dict = {}
        month_list = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
                      'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
        for month in month_list:
            bday_dict[month] = []
        
        for bday in self.bday_list:
            bday_dict[bday[0]].append(bday[1])
        
        for month in month_list:
            print("{}".format(month.capitalize()), end=' ')
            
            for day in range(1, 32):
                if day in bday_dict[month]:
                    print("{}({})".format(
                        day, bday_dict[month].count(day)), end=' ')                
            print()
        """

def askuser(word):
    """
    if the word is not found in the dictionary, user imput is
    requested
    """
    
    print (('\n\t\t\t%s\n') % word)

    query = 'replace(R), replace all(P), ignore(I), ignore all(N), exit(E): '

    choice = input(query).lower()
    while choice not in ['r','p','i','n','e']:
        choice = input(query).lower()        

    newword = word
    if choice in  ['R','r','P','p']:
        newword = input ('Replacement word: ')
        
        # REPLACEMENT BIT UP HERE

    return (choice, newword)
    
def spellcheckandoutput(text="mytext"):
    """
    reads words from the file to be spell-checked and checks if the word
    is in the dictionary. If not, user is queried for input. The
    output is written to the file.
    """
    adict = Dictionary()
    infile = open(text, 'r')
    outfile = open(text+".out", 'w')

    def processinput(choice, newword, word):
        """
        update the dictionary based on the user input.
        If the user wants to exit, copy the rest of the input file to
        the output
        """
        if choice in ['p','P','n','N']:
            adict.update(choice,newword, word)
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
                    newword = adict.verify(word)
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
                newword = adict.verify(word)
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

