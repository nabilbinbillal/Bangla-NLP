import os

def load_list(file):
    with open(file, "r", encoding="utf-8") as f:
        return set(f.read().splitlines())

DATA_DIR = os.path.join(os.path.dirname(__file__), "../../datasets/")
POS_WORDS = load_list(DATA_DIR + "positive_words.txt")
NEG_WORDS = load_list(DATA_DIR + "negative_words.txt")

def sentiment_analysis(tokens):
    pos_count = sum(1 for t in tokens if t in POS_WORDS)
    neg_count = sum(1 for t in tokens if t in NEG_WORDS)
    if pos_count > neg_count:
        return "POSITIVE"
    elif neg_count > pos_count:
        return "NEGATIVE"
    else:
        return "NEUTRAL"
