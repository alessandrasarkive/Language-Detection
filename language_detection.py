import langid
import pandas as pd
from sklearn.metrics import accuracy_score

data = {
    'text': [
        "This is an English sentence.",
        "Esta es una oración en español.",
        "Das ist ein deutscher Satz.",
        "Another English example.",
        "Otro ejemplo en español.",
        "Noch ein deutscher Satz.",
        "For mig begyndte denne historie for 15 år siden",
        "对于我来说，这个故事是15年前开始的"
    ],
    'language': ['en', 'es', 'de', 'en', 'es', 'de', 'da','zh']
}

df = pd.DataFrame(data)

# langid
langid.set_languages(['en', 'es', 'de','da', 'zh'])

# Detect language function
def detect_lang(text):
    lang, conf = langid.classify(text)
    return lang

df['predicted_lang'] = df['text'].apply(detect_lang)

# Evaluate accuracy
accuracy = accuracy_score(df['language'], df['predicted_lang'])
print(f"Accuracy: {accuracy:.2f}")

print(df)





