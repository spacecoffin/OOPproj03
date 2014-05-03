suggestion_list = []

if len(suggestion_list) < 10:
    # Swapped consecutive letter check
    for i in range(len(word)-1):
        if self.adict.dict_verify(word[:i] + word[i+1] + word[i] + word[i+2:]):
            suggestion_list.append(
                word[:i] + word[i+1] + word[i] + word[i+2:])
if len(suggestion_list) < 10:
    # Extra letter check
    for i in range(len(word)):
        if self.adict.dict_verify(word[:i] + word[i+1:]):
            suggestion_list.append(word[:i] + word[i+1:])
if len(suggestion_list) < 10:
    # Substituted letter check
    for i in range(len(word)):
        for l in range(26):
            if self.adict.dict_verify(word[:i] + chr(l+97) + word[i+1:]):
                suggestion_list.append(word[:i] + chr(l+97) + word[i+1:])
if len(suggestion_list) < 10:
    # Missing letter check
    for i in range(len(word)+1):
        for l in range(26):
            if self.adict.dict_verify(word[:i] + chr(l+97) + word[i:]):
                suggestion_list.append(word[:i] + chr(l+97) + word[i:])

# EXTRA
# word[:i] + word[i+1:]
#for i in range(len(word)):
#    print('Extra: {}'.format(word[:i] + word[i+1:]))

# SWAP
# word[:i] + word[i+1] + word[i] + word[i+2:]
#for i in range(len(word)-1):
#	print('Swap: {}'.format(word[:i] + word[i+1] + word[i] + word[i+2:]))

# MISSING
# word[:i] + [a-z] + word[i:]
#for i in range(len(word)+1):
#	for l in range(26):
#		print(word[:i] + chr(l+97) + word[i:])

# SUB
# word[:i] + [a-z] + word[i+1]
#for i in range(len(word)):
#    for l in range(26):
#        print(word[:i] + chr(l+97) + word[i+1:])

"""
if True:
    # Swapped consecutive letter check
    for i in range(len(word)-1):
        print('Swap: {}'.format(word[:i] + word[i+1] + word[i] + word[i+2:]))
    # Extra letter check
    for i in range(len(word)):
        print('Extra: {}'.format(word[:i] + word[i+1:]))
    # Substituted letter check
    for i in range(len(word)):
        for l in range(26):
            print('Subbed: {}'.format(word[:i] + chr(l+97) + word[i+1:]))
    # Missing letter check
    for i in range(len(word)+1):
        for l in range(26):
            print('Missing: {}'.format(word[:i] + chr(l+97) + word[i:]))
"""