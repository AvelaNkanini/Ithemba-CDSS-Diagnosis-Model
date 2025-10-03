import joblib
import pandas as pd

# -----------------------------
# Step 0: Load the trained model, label encoder, and feature columns
# -----------------------------
model = joblib.load("cancer_model.pkl")
le = joblib.load("label_encoder.pkl")
feature_columns = joblib.load("feature_columns.pkl")  # saved during training

# -----------------------------
# Step 1: Interactive prompt for user
# -----------------------------
print("Welcome to the Cancer Prediction Tool!")
print("Please enter your symptoms separated by commas (e.g., Cough, Chest pain, Weight loss):")
user_input = input("Symptoms: ")
input_symptoms = [s.strip() for s in user_input.split(",")]

user_sex = input("Enter your sex (Male/Female): ").strip()

# -----------------------------
# Step 2: Prepare input features
# -----------------------------
features = {symptom: 0 for symptom in feature_columns if symptom != 'Sex'}
for s in input_symptoms:
    if s in features:
        features[s] = 1
features['Sex'] = 0 if user_sex.lower() == "male" else 1

X_input = pd.DataFrame([features])

# Reorder columns exactly like training
X_input = X_input[feature_columns]

# -----------------------------
# Step 3: Make prediction
# -----------------------------
probs = model.predict_proba(X_input)[0]
predictions = {le.classes_[i]: float(probs[i]) for i in range(len(le.classes_))}

# -----------------------------
# Step 4: Show results
# -----------------------------
sorted_predictions = dict(sorted(predictions.items(), key=lambda x: x[1], reverse=True))

print("\nPredicted cancer types with probabilities:")
for cancer, prob in sorted_predictions.items():
    print(f"{cancer}: {prob:.2f}")
