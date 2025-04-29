from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib

# loading model
model = joblib.load(open('models/logistic_regression_model.pkl', 'rb'))

# flask app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    features = request.form['feature']
    features = features.split(',')
    np_features = np.asarray(features, dtype=np.float32)

    # prediction
    pred = model.predict(np_features.reshape(1, -1))
    message = ['Cancerous' if pred[0] == 1 else 'Not Cancerouse']
    # print(message[0])
    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
