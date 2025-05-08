import nltk # type: ignore
import re
import string
import nltk # type: ignore
import pandas as pd
from nltk.corpus import stopwords # type: ignore
from nltk.stem import WordNetLemmatizer # type: ignore


stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_dataset(df):

    df = df.drop_duplicates(subset=['Text'], keep='first')
    return df

def preprocess_text(text):

    text = text.lower()

    text = re.sub(r"http\S+|www\S+|\@\w+|\#\w+|\d+", '', text)

    text = re.sub(f"[{re.escape(string.punctuation)}]", '', text)

    words =[word for word in text.split() if word not in stop_words]

    words = [lemmatizer.lemmatize(word) for word in words]

    return ' '.join(words)

