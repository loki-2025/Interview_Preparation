def first_repeating_character(string):
    seen = set()

    for char in string:
        if char in seen:
            return char
        else:
            seen.add(char)
    return None