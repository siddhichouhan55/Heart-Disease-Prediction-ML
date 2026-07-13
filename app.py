from flask import Flask, render_template, request
import os
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, "HeartDiseasePredictionn.pkl")

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found: {model_path}")

with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    features = [
        float(request.form['HighBP']),
        float(request.form['HighChol']),
        float(request.form['CholCheck']),
        float(request.form['BMI']),
        float(request.form['Smoker']),
        float(request.form['Stroke']),
        float(request.form['Diabetes']),
        float(request.form['PhysActivity']),
        float(request.form['Fruits']),
        float(request.form['Veggies']),
        float(request.form['HvyAlcoholConsump']),
        float(request.form['AnyHealthcare']),
        float(request.form['NoDocbcCost']),
        float(request.form['GenHlth']),
        float(request.form['MentHlth']),
        float(request.form['PhysHlth']),
        float(request.form['DiffWalk']),
        float(request.form['Sex']),
        float(request.form['Age']),
        float(request.form['Education']),
        float(request.form['Income'])
    ]

    prediction = model.predict([features])

    if prediction[0] == 1:
        result = "⚠ High Risk of Heart Disease"
        color = "red"
    else:
        result = "✅ Low Risk of Heart Disease"
        color = "green"

    return render_template("index.html",
                           prediction_text=result,
                           color=color)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting server on http://127.0.0.1:{port}")
    app.run(host="127.0.0.1", port=port, debug=False, use_reloader=False)

