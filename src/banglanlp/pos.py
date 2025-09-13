def pos_tag(tokens):
    """
    Simple offline POS tagging for experiments
    """
    tags = []
    for word in tokens:
        if word.endswith("া") or word.endswith("ি"):
            tags.append((word, "NOUN"))
        elif word.endswith("ে") or word.endswith("ো"):
            tags.append((word, "VERB"))
        else:
            tags.append((word, "X"))
    return tags
