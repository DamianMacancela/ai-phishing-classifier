ai-phishing-classifier
======================

*a basic NLP-based phishing email classifier*

**ai-phishing-classifier** uses classic Machine Learning to distinguish between legitimate emails and phishing attempts based on textual content. Built as a foundational exploration of spam filtering before moving into complex Deep Learning models.

### How it works
1. **TF-IDF:** Transforms raw email text into numerical vectors, weighting words by their statistical significance across the dataset.
2. **Naive Bayes:** Uses the Multinomial Naive Bayes algorithm to classify the vectors.

### Usage

```bash
git clone https://github.com/DamianMacancela/ai-phishing-classifier.git
cd ai-phishing-classifier
pip install -r requirements.txt
```
Run the testing scripts in `src/` to classify sample `.eml` files or train a custom dataset.

### License
MIT
