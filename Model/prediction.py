import pickle
import pandas as pd
import numpy as np
import sklearn

with open('Model/rainfall_trained_model.pkl', 'rb') as file:
    model_data = pickle.load(file)

model = model_data["model"]
feature_name = model_data["feature_name"]

version = '1.0.0'

class_labels = [str(label) for label in model.classes_.tolist()]

def predict_output(user_input: dict):
    df = pd.DataFrame([user_input])

    predicted_class = model.predict(df)[0]
    probabilities = model.predict_proba(df)[0]

    confidence = float(np.max(probabilities))
    class_probs = {str(label): float(prob) for label, prob in zip(class_labels, probabilities)}

    return {
        "predicted_category": str(predicted_class),
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }
