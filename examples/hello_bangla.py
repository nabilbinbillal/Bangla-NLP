from banglanlp.tokenization import tokenize
from banglanlp.stopwords import remove_stopwords
from banglanlp.pos import pos_tag
from banglanlp.ner import ner_tag
from banglanlp.sentiment import sentiment_analysis

text = "রবীন্দ্রনাথ ঢাকায় গান গাইলেন। আজ আবহাওয়া খুব সুন্দর।"

# Tokenization
tokens = tokenize(text)
print("Tokens:", tokens)

# Stopwords
filtered = remove_stopwords(tokens)
print("After stopword removal:", filtered)

# POS tagging
pos_results = pos_tag(filtered)
print("POS tagging:", pos_results)

# NER tagging
ner_results = ner_tag(filtered)
print("NER tagging:", ner_results)

# Sentiment analysis
sentiment = sentiment_analysis(filtered)
print("Sentiment:", sentiment)
