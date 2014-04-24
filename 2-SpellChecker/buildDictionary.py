def buildDictionary (fNames):
    """
    Reads the files from which the dictionary is to be constructed.
    Each new word in the file of two or more alphabetic characters is
    included in the dictionary. 
    """
    dictionary = []
    for afile in fNames.split():
        file = open(afile, 'r')
        try:
            wordch = []
            apostrophe_count = 0
            while True:
                char = file.read(1)
                if not char:               # check if end-of-file
                    if len(wordch) >=2:
                        aword = ''.join(wordch)
                        if aword not in dictionary:
                            dictionary.append(aword) 
                    break
                elif char.isalpha():
                    wordch.append(char.lower())
                elif char is "'":
                    if wordch:
                        wordch.append(char)
                        apostrophe_count += 1
                elif (len(wordch) - apostrophe_count) >= 2:
                    aword = ''.join(wordch)
                    if apostrophe_count >= 1:
                        if aword[-1] is "'":
                            aword = aword[:-1]
                        if aword.replace("'", "") not in dictionary:
                            dictionary.append(aword)
                    else:
                        if aword not in dictionary:
                            dictionary.append(aword)
                    wordch = []
                    apostrophe_count = 0
                else:
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
