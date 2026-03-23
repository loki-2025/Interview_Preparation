def index_of_non_repetetive_character(string):
    counter = {}
    for char in string:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    for i, char in enumerate(string):
        if counter[char] == 1:
            return i
    return -1
