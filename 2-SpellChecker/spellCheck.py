from dictionary import Dictionary

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

    return (choice,newword)
    
def spellcheckandoutput(text="mytext"):
    """
    reads words from the file to be spell-checked and checks if the word
    is in the dictionary. If not, user is queried for input. The
    output is written to the file.
    """
    dict = Dictionary()
    infile = open(text, 'r')
    outfile = open(text+".out", 'w')

    def processinput(choice, newword, word):
        """
        update the dictionary based on the user input.
        If the user wants to exit, copy the rest of the input file to
        the output
        """
        if choice in ['p','P','n','N']:
            dict.update(choice,newword, word)
        elif choice in ['e','E']:
            for line in infile:
                outfile.write(line)
            
    try:
        wordch = []
        while True:
            char = infile.read(1)
            if not char:
                if len(wordch) > 0:
                    word = ''.join(wordch)
                    newword = dict.verify(word)
                    if newword is None:
                        choice, newword = askuser(word)
                        outfile.write(newword)
                        processinput(choice,newword, word)
                    else: outfile.write(newword)
                break
            elif char.isalpha():
                wordch.append(char)
            elif len(wordch) == 0:
                outfile.write(char)
            else:
                word = ''.join(wordch)
                newword = dict.verify(word)
                if newword is None:
                    choice,newword = askuser(word)
                    outfile.write(newword)
                    outfile.write(char)
                    processinput(choice,newword,word)
                else:
                    outfile.write(newword); outfile.write(char)
                wordch = []
    finally:
        infile.close()
        outfile.close()
            
    
if __name__ == '__main__':
    query = 'Name of the document to be spell-checked: '
    spellcheckandoutput(input(query))

