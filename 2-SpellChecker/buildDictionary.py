def buildDictionary (fNames):
    """
    Reads the files from which the dictionary is to be constructed.
    Each new word in the file of two or more alphabetic characters
    is included in the dictionary unless it is a proper noun.
    """
    
    # Discard capitalized words that do not start a sentence.
    # Begins a sentence = the non-whitespace character immediately
    # preceding the first letter is a period.
    
    dictionary = []
    period_flag = False
    for afile in fNames.split():
        file = open(afile, 'r')
        try:
            wordch = []
            while True:
                char = file.read(1)
                if not char:               # check if end-of-file
                    if len(wordch) >=2:
                        aword = ''.join(wordch)
                        if aword not in dictionary:
                            dictionary.append(aword) 
                    break
                elif char.isalpha():
                    wordch.append(char)
                elif len(wordch) >= 2:
                    aword = ''.join(wordch)
                    if not aword.istitle():
                        if aword.lower() not in dictionary:
                            dictionary.append(aword.lower())
                    elif period_flag:
                        print("{}: capitalized but begins".format(aword))
                        if aword.lower() not in dictionary:
                            dictionary.append(aword.lower())
                    else:
                        print("\t{} not added bc capitalized".format(aword))
                    wordch = []
                    period_flag = False
                    if not char.isspace():
                        if char is '.':        # check for end of sentence
                            period_flag = True
                        else:
                            period_flag = False
                else:
                    if not char.isspace():
                        if char is '.':        # check for end of sentence
                            period_flag = True
                        else:
                            period_flag = False
                    wordch = []
        finally:
            file.close()

    return dictionary


def writetofile (dictionary, outfile="words.dat"):
    """
    Write the dictionary words to the file outfile
    """

    file = open(outfile, 'w')
    try:
        dictionary.sort()
        for aword in dictionary:
            file.write(aword)
            file.write('\n')
    finally:
        file.close()

if __name__ == '__main__':
    fNames = input("Enter the file names to build dictionary: ")
    writetofile(buildDictionary (fNames))
    # alice.txt  carol.txt  gulliver.txt  hyde.txt  treasure.txt  war.txt

