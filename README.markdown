# Phishing Email Detector

An AI-powered tool to detect phishing emails using NLP and machine learning, built with Python, Scikit-learn, and Streamlit.

## Features
- Preprocesses email text using TF-IDF vectorization.
- Trains a Random Forest model for email classification.
- Deploys an interactive Streamlit web app for real-time detection.
- Achieves over 90% accuracy on the test dataset.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/phishing-email-detector.git
   cd phishing-email-detector
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/subhajournal/phishingemails) and place `Phishing_Email.csv` in the `data` folder.

## Usage
1. Train the model:
   ```bash
   python train_model.py
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Open the provided URL in your browser, enter an email text, and click "Detect" to classify it as phishing or safe.

## Dataset
- Source: [Phishing Email Detection Dataset](https://www.kaggle.com/datasets/subhajournal/phishingemails)
- Contains email text and labels ("Safe Email" or "Phishing Email").

## Project Structure
```
phishing-email-detector/
├── data/
│   └── Phishing_Email.csv
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```

