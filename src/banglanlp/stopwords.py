STOPWORDS_FILE = "datasets/stopwords.txt"

def load_stopwords():
    with open(STOPWORDS_FILE, encoding="utf-8") as f:
        stopwords = [line.strip() for line in f.readlines()]
    return set(stopwords)

STOPWORDS = load_stopwords()

def remove_stopwords(tokens):
    return [t for t in tokens if t not in STOPWORDS]
