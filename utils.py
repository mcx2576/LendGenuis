import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def remove_punctuation(text):
    """Remove punctuation marks from the text"""
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator)

def remove_numbers(text):
    """Remove numbers from the text"""
    return re.sub(r'\d+', '', text)

def convert_to_lowercase(text):
    """Convert text to lowercase"""
    return text.lower()

def remove_stopwords(text):
    """Remove stopwords from the text"""
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word.casefold() not in stop_words]
    return ' '.join(filtered_text)

def lemmatize_text(text):
    """Lemmatize the text"""
    lemmatizer = WordNetLemmatizer()
    word_tokens = word_tokenize(text)
    lemmatized_text = [lemmatizer.lemmatize(word) for word in word_tokens]
    return ' '.join(lemmatized_text)

def clean_text(text):
    """Apply multiple text cleaning functions to the text"""
    text = remove_punctuation(text)
    text = remove_numbers(text)
    text = convert_to_lowercase(text)
    # text = remove_stopwords(text)
    text = lemmatize_text(text)
    return text
