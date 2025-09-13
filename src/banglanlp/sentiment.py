def load_dataset(file_path):
    with open(file_path, encoding="utf-8") as f:
        return set([line.strip() for line in f.readlines()])

POSITIVE_WORDS = load_dataset("datasets/positive_words.txt")
NEGATIVE_WORDS = load_dataset("datasets/negative_words.txt")

def sentiment_analysis(tokens):
    score = 0
    for t in tokens:
        if t in POSITIVE_WORDS:
            score += 1
        elif t in NEGATIVE_WORDS:
            score -= 1
    if score > 0:
        return "POSITIVE"
    elif score < 0:
        return "NEGATIVE"
    else:
        return "NEUTRAL"
