import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "../../datasets/nouns_verbs.txt")

def pos_tag(tokens):
    """Simple offline POS tagging using predefined words."""
    pos_dict = {}
    # Format of nouns_verbs.txt:
    # word\tPOS
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                word, tag = line.strip().split("\t")
                pos_dict[word] = tag

    return [(t, pos_dict.get(t, "X")) for t in tokens]
