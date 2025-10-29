import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

print("="*60)
print("MLOps Wine Quality Prediction - Model Training")
print("="*60)

# Load dataset
print("\n[1/5] Loading dataset...")
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
df = pd.read_csv(url, sep=';')

print(f"✓ Dataset loaded! Shape: {df.shape}")

# Prepare data
print("\n[2/5] Preparing data...")
X = df.drop('quality', axis=1)
y = df['quality']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"✓ Training: {len(X_train)}, Test: {len(X_test)}")

# Train model
print("\n[3/5] Training Random Forest...")
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)

# Evaluate
print("\n[4/5] Evaluating...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"✓ Accuracy: {accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save model
print("\n[5/5] Saving model...")
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✓ Model saved as model.pkl")
print("\n" + "="*60)
print("Training Complete! Next: python app.py")
print("="*60)
