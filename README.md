# Language-Detection
This project uses the langid library to detect the language of text samples and evaluates accuracy with scikit-learn. It supports English, Spanish, German, Danish, and Chinese. A small dataset is used to demonstrate detection performance and print results in a clear, tabular format.

## Language Detection with Langid

### Overview

This project demonstrates how to use the [`langid`](https://github.com/saffsd/langid.py) library to automatically detect the language of a given text. It evaluates the model's performance using a small multilingual dataset and calculates accuracy using `scikit-learn`.

---

### Features

- Detects languages from text using `langid`
- Supports English (`en`), Spanish (`es`), German (`de`), Danish (`da`), and Chinese (`zh`)
- Compares predictions against true labels
- Calculates overall accuracy using `accuracy_score`

---

### Sample Dataset

The dataset includes 8 sample sentences in:
- 🇬🇧 English  
- 🇪🇸 Spanish  
- 🇩🇪 German  
- 🇩🇰 Danish  
- 🇨🇳 Chinese

Each sentence is labeled with its correct language code.

---

### How to Run

1. **Install dependencies** (if not already installed):

```bash
pip install langid scikit-learn pandas
```

2. **Run the script**:

```bash
python detect_language.py
```

3. **Output**:
- Prints the accuracy score
- Displays a table with original text, true language, and predicted language

---

### 📦 Dependencies

- `langid`
- `pandas`
- `scikit-learn`

---

### Example Output

```
Accuracy: 1.00
                               text language predicted_lang
0     This is an English sentence.       en              en
1  Esta es una oración en español.       es              es
2     Das ist ein deutscher Satz.       de              de
3       Another English example.       en              en
4     Otro ejemplo en español.       es              es
5     Noch ein deutscher Satz.       de              de
6  For mig begyndte denne historie... da              da
7         对于我来说，这个故事是15年前开始的       zh              zh
