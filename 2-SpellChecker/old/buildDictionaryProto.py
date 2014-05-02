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
    apostrophe_count = 0
    occurrences = 0
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
                elif char is "'":
                    wordch.append(char)
                    apostrophe_count += 1
                elif (len(wordch) - apostrophe_count) >= 2:
                    aword = ''.join(wordch)
                    
                    # This apostrophe scheme will break the istitle check.
                    
                    if apostrophe_count >= 1:
                        #print("Word w apostrophe: {}".format(aword))
                        if aword[0] is "'":
                            #print("Word w leading apostrophe: {}".format(aword))
                            aword = aword[1:]
                        if aword[-1] is "'":
                            #print("Word w trailing apostrophe: {}".format(aword))
                            aword = aword[:-1]
                        #print("\tDe-leadtrailed: {}".format(aword))
                        
                    if not aword.istitle():
                        if aword.lower() not in dictionary:
                            dictionary.append(aword.lower())
                        elif aword.lower() not in mult_dict:
                            mult_dict[aword.lower()] = 2
                        else:
                            occurrences = mult_dict.get(aword.lower())
                            occurrences += 1
                            mult_dict[aword.lower()] = occurrences
                    elif period_flag:
                        #print("{}: capitalized but begins".format(aword))
                        if aword.lower() not in dictionary:
                            dictionary.append(aword.lower())
                        elif aword.lower() not in mult_dict:
                            mult_dict[aword.lower()] = 2
                        else:
                            occurrences = mult_dict.get(aword.lower())
                            occurrences += 1
                            mult_dict[aword.lower()] = occurrences
                    #else:
                        #print("\t{} not added bc capitalized".format(aword))
                    wordch = []
                    period_flag = False
                    apostrophe_count = 0
                    if not char.isspace():
                        if char is '.':        # check for end of sentence
                            period_flag = True
                else:
                    if not char.isspace():
                        if char is '.':        # check for end of sentence
                            period_flag = True
                        else:
                            period_flag = False
                    wordch = []
                    apostrophe_count = 0
        finally:
            file.close()

    return dictionary


def writetofile (dictionary, mult_dict, outfile="words.dat"):
    """
    Write the dictionary words to the file outfile
    """

    file = open(outfile, 'w')
    try:
        dictionary.sort()
        
        # YOU ARE HERE, figuring out how to input the 500 most occurring words
        # first
        # This scheme is likely no good 
        max_occurrences = max(mult_dict.values())
        for n in range(max_occurrences):
            occurrences = max_occurrences - n
            to_write = [word for word in mult_dict.keys()
                        if mult_dict[word] == occurrences]
            for word in to_write:
                file.write(word)
                file.write('\n')
        
        for aword in dictionary:
            file.write(aword)
            file.write('\n')
    finally:
        file.close()

if __name__ == '__main__':
    mult_dict = {}
    fNames = input("Enter the file names to build dictionary: ")
    writetofile(buildDictionary (fNames), mult_dict)
    # alice.txt  carol.txt  gulliver.txt  hyde.txt  treasure.txt  war.txt

