import os
import joblib
import pandas as pd
from flask import Flask, request, jsonify

app = Flask("SuperKart")

# Load the serialized model
model_path = os.path.join("backend_files", "superkart_model.joblib")
model = joblib.load(model_path)

# Define a route for the home page
@app.get('/')
def home():
    return "Welcome to the SuperKart System"

@app.route('/v1/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        # Convert single instance payload to a DataFrame row
        df = pd.DataFrame([data])
        prediction = model.predict(df)[0]
        return jsonify({"prediction": float(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/v1/predictbatch', methods=['POST'])
def predict_batch():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        # Read the uploaded CSV data
        df = pd.read_csv(file)
        predictions = model.predict(df)

        # Map predictions back to indexes
        result = {str(i): float(pred) for i, pred in enumerate(predictions)}
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
