def most_frequent_character(string):
    counter = {}

    for char in string:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    
    max_freq = 0
    most_frequent_character = None
    for char in string:
        if counter[char] > max_freq:
            max_freq = counter[char]
            most_frequent_character = char
    return most_frequent_character
     
