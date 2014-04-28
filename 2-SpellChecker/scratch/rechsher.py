def string_hash(string):
    hash_val = 0
    for char in string:
        hash_val *= 26
        hash_val += ord(char) - 97
    return hash_val

def mod_hash(string, table_size):
    hash_val = 0
    for char in string:
        hash_val *= 26
        hash_val += ord(char) - 97
    return hash_val % table_size

def multmod_hash(string, table_size):
    hash_val = 0
    for char in string:
        hash_val *= 26
        hash_val += ord(char) - 97
        # avoid int overflow by taking mod M at the end of each iteration
        hash_val = hash_val % table_size
    return hash_val