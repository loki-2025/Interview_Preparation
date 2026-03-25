def compress_string(string):
    """
    Compress a string based on number of repetetive characters
    Args:
        string (str): Input string
    Returns:
        str: compressed string
        
    """
    if not string:
        return string
    result = []
    count = 1
    for idx in range(1, len(string)):
        if string[idx] == string[idx-1]:
            count += 1
            
        else:
            result.append(string[idx-1])
            result.append(str(count))
            count = 1
    result.append(string[-1])
    result.append(str(count))
    compressed_string = ''.join(result)
    return compressed_string if len(compressed_string) < len(string) else string