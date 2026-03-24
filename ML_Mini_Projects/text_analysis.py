def character_frequency(string):
    """
    This function computes character counts in a string
    Args:
        string (str): Input String
    Returns:
        dict: character counts
    """
    char_count = {}

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    if char_count:
        return char_count
    else:
        return {}
def character_probability(freq_dict):
    """
    Compute probability distribution from character frequency counts.
    Args:
        freq_dict (dict): Mapping of characters to their frequency counts
    Returns:
        dict: probability of each unique character
    """
    if not freq_dict:
        return {}

    probability_map = {}
    total_count = sum(freq_dict.values())
    for key, value in freq_dict.items():
        probability_map[key] = value / total_count
    
    return probability_map

def calculate_entropy(prob_dict):
    """
    Computes the entropy of a string

    Args:
        prob_dict (dict): Probability map of each unique character
    Returns:
        float: Entropy of the string 
    """
    import math
    if not prob_dict:
        return 0.0    
    entropy = 0
    for value in prob_dict.values():
        if value > 0:    
            entropy -= value * math.log2(value)

    return entropy

def analyze_text(string):
    """
    Analyze input string by computing character frequency, probability distribution, and entropy.

    Args:
        string (str): Input String to test
    Returns:
        tuple:
            dict: Character frequency map
            dict: Character probability distribution
            float: Entropy of the string
    """
    
    char_count = character_frequency(string)
    probability_map= character_probability(freq_dict = char_count)   
    entropy = calculate_entropy(prob_dict=probability_map)
    return char_count, probability_map, entropy