# BanglaNLP v0.1

BanglaNLP is an open-source Python toolkit for Bengali language processing. It provides essential NLP functionalities for Bangla, designed to work **offline with editable datasets**, making it beginner-friendly and easy to extend.

---

## 🔹 Features

- **Tokenization:** Split Bangla text into individual words.  
- **Stopword Removal:** Remove common Bangla stopwords for clean text processing.  
- **POS Tagging (Offline):** Rule-based part-of-speech tagging (NOUN, VERB, unknown).  
- **Named Entity Recognition (NER, Offline):** Detect names, locations, and organizations using simple word lists.  
- **Sentiment Analysis (Offline):** Classify Bangla text as positive, negative, or neutral using keyword-based scoring.  
- **Editable Datasets:** All stopwords, names, locations, organizations, and sentiment words are stored in `datasets/` and can be customized easily.  
- **Example Scripts:** `examples/hello_bangla.py` demonstrates all features together.  
- **Modular & Expandable:** Structured to allow future integration of pretrained models (Hugging Face, BanglaBERT) and additional NLP features.  

---

## 🔹 Installation

Clone the repository and install the package in **editable mode**:

```bash
git clone 
cd Bangla-NLP
pip install -e .
