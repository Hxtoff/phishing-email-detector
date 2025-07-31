import streamlit as st
import pickle
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

# Load model
with open('phishing_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Preprocess text
def preprocess_text(text):
    if isinstance(text, str):
        text = re.sub(r'\W', ' ', text.lower())
        text = re.sub(r'\s+', ' ', text).strip()
        stop_words = set(stopwords.words('english'))
        text = ' '.join(word for word in text.split() if word not in stop_words)
        return text
    return ''

# Streamlit app
st.title("Phishing Email Detector")
st.write("Enter an email text to check if it's phishing or safe.")

email_text = st.text_area("Email Content", height=200)
if st.button("Detect"):
    if email_text:
        processed_text = preprocess_text(email_text)
        prediction = model.predict([processed_text])[0]
        probability = model.predict_proba([processed_text])[0][1]
        if prediction == 1:
            st.error(f"This email is likely a PHISHING email (Confidence: {probability:.2%})")
        else:
            st.success(f"This email is likely SAFE (Confidence: {1-probability:.2%})")
    else:
        st.warning("Please enter an email text.")