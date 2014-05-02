def buildDictionary (fNames):
    """
    Reads the files from which the dictionary is to be constructed.
    Each new word in the file of two or more alphabetic characters is
    included in the dictionary. 
    """
    dictionary = {}
    for afile in fNames.split():
        file = open(afile, 'r')
        try:
            wordch = []
            apostrophe_count = 0
            period_flag = False
            while True:
                char = file.read(1)
                if not char:               # check if end-of-file
                    if (len(wordch) - apostrophe_count) >= 2:
                        aword = ''.join(wordch)
                        if apostrophe_count >= 1:
                            if aword[-1] is "'":
                                aword = aword[:-1] # strip trailing apostrophes
                        if not aword.replace("'", "").istitle() or period_flag:
                            if aword.lower() not in dictionary:
                                dictionary[aword.lower()] = 1
                            elif aword.lower() in dictionary:
                                dictionary[aword.lower()] += 1
                    break
                elif char.isalpha():
                    wordch.append(char)
                elif char is "'":
                    if wordch: # don't begin words with apostrophes
                        wordch.append(char)
                        apostrophe_count += 1
                else:
                    # don't count apostrophes toward length of word
                    if (len(wordch) - apostrophe_count) >= 2:
                        aword = ''.join(wordch)
                        if apostrophe_count >= 1:
                            if aword[-1] is "'":
                                aword = aword[:-1] # strip trailing apostrophes
                                
                        # don't write capitalized words unless they
                        # begin a sentence:
                        if not aword.replace("'", "").istitle() or period_flag:
                            if aword.lower() not in dictionary:
                                dictionary[aword.lower()] = 1
                            elif aword.lower() in dictionary:
                                dictionary[aword.lower()] += 1
                                
                        wordch = []
                        apostrophe_count = 0
                        period_flag = False
                        if not char.isspace():
                            if char is '.':        # check for end of sentence
                                period_flag = True
                    else:
                        wordch = []
                        if not char.isspace():
                            if char is '.':        # check for end of sentence
                                period_flag = True
                            else:
                                period_flag = False
        finally:
            file.close()
            dict_sort = []
            for key in dictionary.keys():
                word_with_count = []
                word_with_count.append(dictionary[key])
                word_with_count.append(key)
                dict_sort.append(word_with_count)
            dict_sort.sort()
            dict_sort.reverse()

    return dict_sort


def writetofile (dictionary, outfile="words.dat"):
    """
    Write the dictionary words to the file outfile
    """

    file = open(outfile, 'w')
    try:
        # dictionary.sort()
        for aword in range(len(dictionary)):
            file.write(dictionary[aword][1])
            file.write('\n')
    finally:
        file.close()

if __name__ == '__main__':
    fNames = input("Enter the file names to build dictionary: ")
    writetofile(buildDictionary (fNames))

