# 🛡️ SpamRadar – AI-powered SMS Spam Classifier App

SpamRadar is a lightweight, intelligent web app that classifies text messages as **Spam** or **Not Spam** using machine learning.  
It uses a **Multinomial Naive Bayes** model trained on SMS spam dataset, wrapped inside a clean and responsive **Streamlit interface** — ideal for real-time usage, batch prediction, and recruiter demos.

---

## 🚀 Features

✅ Real-time SMS spam classification  
📂 CSV Upload to scan multiple messages  
📊 Prediction confidence percentage  
🧠 Spam trigger-word highlighter (e.g., “win”, “free”, “offer”)  
🔐 Admin panel (password-protected) to view prediction logs  
🗂️ SQLite3 logging of predictions with timestamps  
📱 Mobile-friendly responsive layout  
🌐 Deployable on **Streamlit Cloud** instantly

---

## 📦 Dataset Used

- **Source**: [UCI SMS Spam Collection Dataset (via Kaggle)](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
- 5,572 labeled SMS messages (ham/spam)

---

## 🧠 Model & NLP Pipeline

- **Model**: Multinomial Naive Bayes
- **Vectorization**: TF-IDF (stopwords removed)
- **Preprocessing**:
  - Lowercasing
  - Digit and punctuation removal
  - Extra space stripping

---

## 🎯 Model Performance

| Metric        | Value         |
|---------------|---------------|
| **Accuracy**  | `96.8%` ✅     |
| **Precision** | `100% (spam)` |
| **Recall**    | `77% (spam)`  |
| **F1-Score**  | `87% (spam)`  |

📈 Ham messages: 100% recall  
📉 Spam messages: Balanced recall to reduce false negatives

---

## 🧰 Tech Stack

| Layer          | Tools/Libraries                   |
|----------------|-----------------------------------|
| Language       | Python                            |
| Web Framework  | Streamlit                         |
| ML Model       | Naive Bayes (Scikit-learn)        |
| Vectorization  | TF-IDF (Scikit-learn)             |
| Database       | SQLite3                           |
| Deployment     | Streamlit Cloud                   |
| Version Control| Git + GitHub                      |

---

## 🗂️ Project Structure

SpamRadar/
│
├── app.py # Streamlit app
├── spam_classifier.ipynb # Notebook for model training & testing
├── spam_model.pkl # Trained Naive Bayes model
├── tfidf_vectorizer.pkl # TF-IDF vectorizer
├── spam.csv # Dataset file
├── requirements.txt # Python package dependencies
├── .gitignore # Files to ignore in Git
└── README.md # This file

## 🔐 Admin Panel (Secure Logging)
Admin panel lets you view all predictions logged in the database

Protected using:
`st.secrets["admin_password"]`

## 🌍 Live App Demo
🔗 Click to Open Live App

👨‍💻 Developer
Rishu Sharma
🎓 B.Tech CSE | ML & Data Science Enthusiast
