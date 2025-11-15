import json
import random
import numpy as np
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
import pickle

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# Load intents
with open('intents.json') as file:
    data = json.load(file)

# Prepare data
corpus = []
labels = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        tokens = nltk.word_tokenize(pattern.lower())
        lemmatized = [lemmatizer.lemmatize(word) for word in tokens]
        corpus.append(' '.join(lemmatized))
        labels.append(intent['tag'])

# Encode labels
le = LabelEncoder()
y = le.fit_transform(labels)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save model, vectorizer, and label encoder
with open('chatbot_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

with open('label_encoder.pkl', 'wb') as f:
    pickle.dump(le, f)

print("Training complete. Model saved as chatbot_model.pkl")
print("Vectorizer saved as vectorizer.pkl")
