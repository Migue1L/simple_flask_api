from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = [data.get('files_changed', 0), data.get('lines_added', 0), data.get('lines_removed', 0)]
    pred = model.predict([features])[0]
    prob = model.predict_proba([features])[0][pred]
    return jsonify({"prediction": int(pred), "confidence": float(prob)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)