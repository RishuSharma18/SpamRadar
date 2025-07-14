import streamlit as st
import pandas as pd
import string
import re
import joblib
import sqlite3
from datetime import datetime

st.set_page_config(page_title="SpamRadar", page_icon="🛡️")
st.markdown("""
<style>
.big-font { font-size:22px !important; font-weight: bold; color: #004080; }
[data-testid="stSidebar"] {
    background-color: #F0F2F6;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="big-font">🛡️ Welcome to <strong>SpamRadar</strong> — Your Smart Message Defender!</p>', unsafe_allow_html=True)


# ---------------- Model Load ----------------
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")


# ---------------- Trigger Words ----------------
spam_keywords = ['free', 'win', 'click', 'offer', 'buy', 'urgent', 'cash', 'prize', 'congratulations']


# ---------------- SQLite DB Setup ----------------
conn = sqlite3.connect('predictions.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT,
    prediction TEXT,
    confidence REAL,
    timestamp TEXT
)
''')
conn.commit()


# ---------------- Helper Functions ----------------
def clean_text(msg):
    msg = msg.lower()
    msg = re.sub(r'\d+', '', msg)
    msg = msg.translate(str.maketrans('', '', string.punctuation))
    return msg.strip()

def highlight_triggers(msg):
    for word in spam_keywords:
        msg = re.sub(rf"\b({word})\b", r"**:red[\1]**", msg, flags=re.IGNORECASE)
    return msg

def predict_message(msg):
    cleaned = clean_text(msg)
    vec = vectorizer.transform([cleaned])
    pred = model.predict(vec)[0]
    proba = model.predict_proba(vec)[0][1]
    return pred, round(proba * 100, 2)

def log_prediction(msg, result, confidence):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO history (message, prediction, confidence, timestamp) VALUES (?, ?, ?, ?)",
                   (msg, result, confidence, timestamp))
    conn.commit()


# ---------------- Message Prediction ----------------
st.markdown("## 🔎 Predict a Message")
user_input = st.text_area("✍️ Enter your message here:")

if st.button("🔍 Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        prediction, confidence = predict_message(user_input)
        log_prediction(user_input, "SPAM" if prediction == 1 else "NOT SPAM", confidence)

        st.markdown("#### 📤 Your Message:")
        st.markdown(highlight_triggers(user_input), unsafe_allow_html=True)

        st.success("✅ Prediction: NOT SPAM" if prediction == 0 else "🚫 Prediction: SPAM")
        st.info(f"📊 Confidence: `{confidence}%` spam")


# ---------------- Inbox Simulation ----------------
st.markdown("---")
st.markdown("## 📱 Simulate Your Inbox")

uploaded_file = st.file_uploader("Upload CSV with `message` column")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        if 'message' not in df.columns:
            st.error("CSV must have a 'message' column.")
        else:
            df['clean'] = df['message'].apply(clean_text)
            vecs = vectorizer.transform(df['clean'])
            df['Prediction'] = model.predict(vecs)
            df['Confidence'] = (model.predict_proba(vecs)[:, 1] * 100).round(2)

            for i, row in df.iterrows():
                st.markdown(f"**📨 {row['message']}**")
                st.markdown(f"{'🚫' if row['Prediction']==1 else '✅'} Confidence: {row['Confidence']}%", unsafe_allow_html=True)
                st.markdown("---")

    except Exception as e:
        st.error("Something went wrong: " + str(e))


# ---------------- Admin Login ----------------
is_admin = False
with st.expander("🔐 Admin Login", expanded=False):
    admin_key = st.text_input("Enter admin key to unlock advanced features:", type="password")
    if admin_key == st.secrets["admin_password"]:  #  Setting my secret key
        is_admin = True
        st.success("✅ Admin mode activated.")


# ---------------- Admin History Panel ----------------
if is_admin:
    st.markdown("## 📂 Prediction History (Admin Only)")
    if st.checkbox("📜 Show Saved Predictions"):
        history_df = pd.read_sql_query("SELECT * FROM history ORDER BY id DESC", conn)
        st.dataframe(history_df)


# ---------------- Footer ----------------
st.markdown("""
<hr style="border:0.5px solid #ccc" />

<div style="text-align:center; padding:10px 0; font-size:14px;">
    🛡️ <strong>SpamRadar</strong> &nbsp;|&nbsp; Developed with ❤️ by <a href="https://github.com/your-username" target="_blank">Rishu Sharma</a>
</div>
""", unsafe_allow_html=True)

