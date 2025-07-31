import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

# Load dataset
def load_data(file_path):
    df = pd.read_csv(file_path)
    df = df[['Email Text', 'Email Type']].dropna()
    df['label'] = df['Email Type'].apply(lambda x: 1 if 'Phishing' in x else 0)
    return df['Email Text'], df['label']

# Preprocess text
def preprocess_text(text):
    if isinstance(text, str):
        text = re.sub(r'\W', ' ', text.lower())
        text = re.sub(r'\s+', ' ', text).strip()
        stop_words = set(stopwords.words('english'))
        text = ' '.join(word for word in text.split() if word not in stop_words)
        return text
    return ''

# Main function
def train():
    # Load and preprocess data
    X, y = load_data('data/Phishing_Email.csv')
    X = X.apply(preprocess_text)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create pipeline
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=5000)),
        ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
    ])

    # Train model
    pipeline.fit(X_train, y_train)

    # Evaluate
    y_pred = pipeline.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print(classification_report(y_test, y_pred))

    # Save model
    with open('phishing_model.pkl', 'wb') as f:
        pickle.dump(pipeline, f)

if __name__ == '__main__':
    train()