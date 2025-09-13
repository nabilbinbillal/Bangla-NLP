# BanglaNLP v0.1

**BanglaNLP** is a free, open-source Python toolkit for **Bengali Natural Language Processing (Bangla NLP)**. Designed for developers, researchers, students, and hobbyists, BanglaNLP provides essential **offline NLP functionalities** for Bangla text, including **tokenization, stopword removal, part-of-speech tagging (POS), named entity recognition (NER), and sentiment analysis**. All datasets are **editable**, making it easy for anyone to customize and expand.  

Whether you are building **Bangla chatbots, text analysis tools, sentiment classifiers, or research projects**, BanglaNLP provides a modular and beginner-friendly foundation.

---

## 🔹 Key Features

1. **Tokenization**
   - Split Bangla sentences into individual words.  
   - Supports basic punctuation handling.  
   - Example:
     ```python
     from banglanlp.tokenization import tokenize
     tokens = tokenize("আমি বাংলায় গান গাই।")
     print(tokens)  # Output: ['আমি', 'বাংলায়', 'গান', 'গাই']
     ```

2. **Stopword Removal**
   - Remove common Bangla stopwords to clean text for further NLP tasks.  
   - Editable `datasets/stopwords.txt` allows you to add/remove words.  
   - Example:
     ```python
     from banglanlp.stopwords import remove_stopwords
     filtered = remove_stopwords(tokens)
     print(filtered)  # Output: ['বাংলায়', 'গান', 'গাই']
     ```

3. **POS Tagging (Offline)**
   - Rule-based tagging for **NOUN, VERB, and unknown words (X)**.  
   - Example:
     ```python
     from banglanlp.pos import pos_tag
     pos_results = pos_tag(filtered)
     print(pos_results)  # Output: [('বাংলায়', 'X'), ('গান', 'X'), ('গাই', 'VERB')]
     ```

4. **Named Entity Recognition (NER)**
   - Detect **person names, locations, and organizations** using simple lists in `datasets/`.  
   - Fully editable for improved coverage.  
   - Example:
     ```python
     from banglanlp.ner import ner_tag
     ner_results = ner_tag(filtered)
     print(ner_results)  # Output: [('বাংলায়', 'O'), ('গান', 'O'), ('গাই', 'O')]
     ```

5. **Sentiment Analysis**
   - Classify Bangla text as **POSITIVE, NEGATIVE, or NEUTRAL** using keyword-based scoring.  
   - Datasets: `positive_words.txt` and `negative_words.txt`.  
   - Example:
     ```python
     from banglanlp.sentiment import sentiment_analysis
     sentiment = sentiment_analysis(filtered)
     print(sentiment)  # Output: POSITIVE
     ```

6. **Editable Datasets**
   - All datasets are stored in the `datasets/` folder:  
     - `stopwords.txt` – Common Bangla stopwords  
     - `names.txt` – Person names  
     - `locations.txt` – Cities and towns  
     - `organizations.txt` – Institutions  
     - `positive_words.txt` – Positive sentiment words  
     - `negative_words.txt` – Negative sentiment words  

7. **Example Scripts**
   - `examples/hello_bangla.py` demonstrates full usage of tokenization, stopword removal, POS, NER, and sentiment analysis.  

8. **Modular & Expandable**
   - Designed for future integration with **pretrained models (BanglaBERT, Hugging Face models)**, **text summarization**, **translation**, and **speech processing**.

---

## 🔹 Installation

Install in editable mode to work with your own edits:

```bash
# Clone the repository
git clone https://github.com/nabilbinbillal/Bangla-NLP.git
cd Bangla-NLP

# Install the package in editable mode
pip install -e .
