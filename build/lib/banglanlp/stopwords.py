import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "../../datasets/stopwords.txt")

def remove_stopwords(tokens):
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        stopwords = set(f.read().splitlines())
    return [t for t in tokens if t not in stopwords]
