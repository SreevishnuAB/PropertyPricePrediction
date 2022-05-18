from flask import Flask, request, jsonify
from model import Model
import logging
import os

port = int(os.environ.get('PORT', 3000))
logging.basicConfig(level='INFO')

app = Flask(__name__)
model = Model.get_instance()

@app.route('/health', methods=['GET'])
def health():
  return jsonify({"status": "OK"})

@app.route('/describe', methods=['GET'])
def describe():
  return model.data.describe().to_json()

@app.route('/predict', methods=['POST'])
def predict():
  data = request.get_json()
  # logging.info(data)
  prediction = model.predict(data)
  logging.info(prediction)
  return jsonify({"predicted price": prediction.tolist()})

@app.route('/update-model', methods=['POST'])
def update_model():
  data = request.get_json()
  logging.info(f"data {data}")
  model.add_data(data)
  return jsonify({"response": "model updated"})
  # return jsonify({"error": "model could not be updated"}), 500

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=port)
  