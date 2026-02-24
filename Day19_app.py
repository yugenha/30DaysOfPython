import re
from Data.stop_words import stop_words

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def remove_support_words(text):
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

def text_similarity(text1, text2):
    text1 = remove_support_words(clean_text(text1))
    text2 = remove_support_words(clean_text(text2))
    words = set(text1.split()).union(set(text2.split()))
    vec1 = [1 if word in text1 else 0 for word in words]
    vec2 = [1 if word in text2 else 0 for word in words]
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = sum(a * a for a in vec1) ** 0.5
    magnitude2 = sum(b * b for b in vec2) ** 0.5
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    return dot_product / (magnitude1 * magnitude2)