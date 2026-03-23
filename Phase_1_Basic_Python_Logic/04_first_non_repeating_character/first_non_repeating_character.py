def first_non_repeating_character(string):
    counter = {}
    for char in string:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    for char in string:
        if counter[char] == 1:
            return char
    return None