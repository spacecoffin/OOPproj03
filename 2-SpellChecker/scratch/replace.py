suggestion_list = []

for i in range(len(word)):
    while len(suggestion_list) < 10:
        


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