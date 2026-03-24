def is_palindrome(string):
    """
    Computes if a given string is palindrome or not

    Args:
        string (str): Input String
    Returns:
        True, if string is palindrome
        False, otherwise
    """
    cleaned = []
    for char in string:
        if char.isalnum():
            cleaned.append(char)
    l = len(cleaned)
    for i in range( l // 2):
        if cleaned[i] != cleaned[l-1-i]:
            return False
    return True