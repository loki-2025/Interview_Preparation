def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    
    counter_s1 = {}
    counter_s2 = {}

    for char in s1:
        if char in counter_s1:
            counter_s1[char] += 1
        else:
            counter_s1[char] = 1

    for char in s2:
        if char in counter_s2:
            counter_s2[char] += 1
        else:
            counter_s2[char] = 1

    return counter_s1 == counter_s2