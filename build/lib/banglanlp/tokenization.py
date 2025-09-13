def tokenize(text):
    """
    Simple Bangla word tokenizer
    """
    import re
    text = re.sub(r"[।,.!?]", " ", text)  # remove punctuations
    tokens = text.strip().split()
    return tokens
