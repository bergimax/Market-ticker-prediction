# # LOAD A MODEL
import pickle
from flask import Flask
from flask import request
from flask import jsonify

model_file = 'mid_term_model.bin'

with open(model_file, 'rb') as f_in: #wb=write, rb=read
    dv, model = pickle.load(f_in) 

app = Flask('market_prediction')

@app.route('/predict', methods=['POST'])

#create data to test it

def predict():
  market = request.get_json()

  X = dv.transform([market])
  y_pred = model.predict(X)

  result = {
     "market_probability": float(y_pred),
     "commodity": int(y_pred)
  }

  return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)