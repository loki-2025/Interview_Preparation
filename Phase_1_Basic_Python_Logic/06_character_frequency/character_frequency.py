def character_frequency(string):
    """
    This function calculates frequency of the character in a string
    
    Args:
        param1 (str): Input String
    Returns:
        dict: Mapping of character to its frequency count
    """
    counter = {}
    for char in string:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    
    return counter