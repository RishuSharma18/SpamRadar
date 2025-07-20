# 🛡️ SpamRadar – AI-Powered SMS Spam Detection App

**SpamRadar** is a smart and lightweight web app that classifies SMS messages as **Spam** or **Not Spam** using a trained Machine Learning model.  
Built with a clean and interactive **Streamlit UI**, it’s ideal for real-time classification, batch analysis, and recruiter portfolio demos.

## 🚀 Features

- ✅ Instant SMS Spam Detection (real-time message classification)
- 📂 Batch CSV Upload (analyze multiple messages at once)
- 📊 Confidence Score (how likely a message is spam)
- 🧠 Spam Trigger Word Highlighter (e.g., "win", "free", "offer")
- 🔐 Admin Panel to View Logged Predictions (secured with password)
- 🗂️ SQLite3 Logging (store message, prediction, confidence, timestamp)
- 📱 Responsive & Mobile-Friendly UI
- ☁️ 1-Click Deployable on Streamlit Cloud

## 📦 Dataset Used

- **Source**: [UCI SMS Spam Collection Dataset (via Kaggle)](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
- **Size**: 5,572 labeled SMS messages  
- **Classes**: `ham` (legit) and `spam`

## 🧠 ML Model & NLP Pipeline

- **Model**: Multinomial Naive Bayes (Scikit-learn)
- **Vectorization**: TF-IDF (with stopword removal)
- **Text Preprocessing**:
  - Lowercasing  
  - Removing digits and punctuation  
  - Whitespace cleanup

## 🎯 Model Performance

| Metric        | Value         |
|---------------|---------------|
| **Accuracy**  | `96.8%` ✅     |
| **Precision** | `100% (spam)` |
| **Recall**    | `77% (spam)`  |
| **F1-Score**  | `87% (spam)`  |

**Ham** messages are classified with perfect recall (100%)  
**Spam** messages are detected with high precision and balanced recall

## 🛠️ Tech Stack

| Layer          | Tools & Libraries               |
|----------------|---------------------------------|
| Language       | Python                          |
| ML Framework   | Scikit-learn                    |
| NLP Engine     | TF-IDF Vectorizer               |
| UI Framework   | Streamlit                       |
| Data Logging   | SQLite3                         |
| Deployment     | Streamlit Cloud                 |
| Version Control| Git + GitHub                    |


## 🗂️ Project Structure

SpamRadar/
```
├── app.py # Streamlit app
├── spam_classifier.ipynb # Notebook for model training & testing
├── spam_model.pkl # Trained Naive Bayes model
├── tfidf_vectorizer.pkl # TF-IDF vectorizer
├── spam.csv # Dataset file
├── requirements.txt # Python package dependencies
├── .gitignore # Files to ignore in Git
└── README.md # This file
```

## 🔐 Admin Panel (Secure Logging)
Admin panel lets you view all predictions logged in the database

Protected using:
`st.secrets["admin_password"]`

##  Live App Demo
🔗 [**SpamRadar** - click here](https://spamradar.streamlit.app/)

 ## 👨‍💻 Developer
[**Rishu Sharma**](https://github.com/RishuSharma18)  
 B.Tech CSE (Data Science) student| ML & Data Science Enthusiast
