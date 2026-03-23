def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    
    counter = {}

    for char in s1:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    for char in s2:
        if char not in counter:
            return False
        counter[char] -= 1

    for value in counter.values():
        if value != 0:
            return False
    return True