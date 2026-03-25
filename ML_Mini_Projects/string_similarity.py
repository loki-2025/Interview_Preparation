def tokenize(text):
    """
    Convert input text into a list of lowercase word tokens.

    Args:
        text (str): Input text
    Returns:
        list: tokenized text
    """
    if not text:
        return []
    
    return text.lower().split()

def jaccard_similarity(tokens1, tokens2):
    """
    Computes jaccard similarity based on two tokens

    Args:
        tokens1 (list): tokens from first string
        tokens2 (list): tokens from second string
    Returns:
        float : Jaccard Similarity
    """
    
    set1 = set(tokens1)
    set2 = set(tokens2)

    intersection = set1.intersection(set2)
    union = set1.union(set2)
    if not union:
        return 0.0

    return len(intersection)/len(union)

def cosine_similarity(tokens1, tokens2):
    """
    Compute cosine similarity based on tokens of two texts

    Args:
        tokens1 (list): tokens from first text
        tokens2 (list): tokens from second text
    Returns:
        float: cosine similarity
    """
    import math

    freq1 = {}
    freq2 = {}
    for word in tokens1:
        if word in freq1:
            freq1[word] += 1
        else:
            freq1[word] = 1
    for word in tokens2:
        if word in freq2:
            freq2[word] += 1
        else:
            freq2[word] = 1
    vocab = freq1.keys() | freq2.keys()
    dot = 0
    sqr1 = 0
    sqr2 = 0
    
    for word in vocab:
        count1 = freq1.get(word,0)
        count2 = freq2.get(word,0)
        dot += count1 * count2
        sqr1 += count1 ** 2
        sqr2 += count2 ** 2
    
    magnitude1 = math.sqrt(sqr1)
    magnitude2 = math.sqrt(sqr2)
    
    if magnitude1 == 0.0 or magnitude2 == 0.0:
        return 0.0
    
    return dot / (magnitude2 * magnitude1)

def compare_texts(text1, text2):
    """
    Compares text strings based on cosine and jaccard similarity

    Args:
        text1 (str): First input string
        text2 (str): Second input string
    Returns:
        tuple:
            float: Jaccard similarity
            float: Cosine similarity
    """
    tokens1 = tokenize(text1)
    tokens2 = tokenize(text2)

    j_sim = jaccard_similarity(tokens1, tokens2)
    c_sim = cosine_similarity(tokens1, tokens2)

    return (j_sim, c_sim)