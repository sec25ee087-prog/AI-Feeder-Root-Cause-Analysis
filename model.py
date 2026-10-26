from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

DATA_PATH = Path(__file__).parent / "data" / "sample_data.csv"
FEATURES = ["voltage_v", "current_a", "temperature_c"]

def load_data():
    data = pd.read_csv(DATA_PATH)
    required = FEATURES + ["label"]
    missing = [col for col in required if col not in data.columns]
    if missing:
        raise ValueError(f"Dataset is missing required columns: {missing}")
    return data

def train_model(data):
    X = data[FEATURES]
    y = data["label"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight="balanced")
    model.fit(X_train, y_train)
    score = accuracy_score(y_test, model.predict(X_test))
    return model, score

def predict_cause(model, voltage_v, current_a, temperature_c):
    sample = pd.DataFrame([{
        "voltage_v": voltage_v,
        "current_a": current_a,
        "temperature_c": temperature_c,
    }], columns=FEATURES)
    probabilities = model.predict_proba(sample)[0]
    index = probabilities.argmax()
    return model.classes_[index], float(probabilities[index])
