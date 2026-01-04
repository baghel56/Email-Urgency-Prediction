import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import os

# Load data
df = pd.read_csv("Milestone-3_Urgency-prediction/data/sample_urgency_emails.csv")

X = df["subject"] + " " + df["body"]
y = df["urgency"]

# Vectorization
vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
X_vec = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# ✅ CREATE results folder if not exists
os.makedirs("Milestone-3_Urgency-prediction/results", exist_ok=True)

# ✅ SAVE model and vectorizer
joblib.dump(model, "Milestone-3_Urgency-prediction/results/urgency_model.pkl")
joblib.dump(vectorizer, "Milestone-3_Urgency-prediction/results/urgency_vectorizer.pkl")

print("✅ Model and vectorizer saved successfully")
