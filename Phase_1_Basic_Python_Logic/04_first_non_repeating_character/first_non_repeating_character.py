def first_non_repeating_character(string):
    counter = {}
    for char in string:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    for item, value in counter.item():
        if value == 1:
            return item
    return None