import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd 

app = Flask(__name__)
## Load the model
regmodel = pickle.load(open('regmodel.pkl','rb'))
scaler = pickle.load(open('scaling.pkl','rb'))
## First Route(basically a home page/landing page for your web app)
@app.route('/')
def home():
    return render_template('home.html')

## Api to send data and get predictions
@app.route('/predict_api', methods=["POST"])
def predict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    scaled_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
    regression.predict(scaled_data)
    print(output[0])
    return jsonify(output[0])

## Page to get the data and display prediction
@app.route('/predict',methods=['POST'])
def predict():
    data = [float(val) for val in request.form.values()]
    final_input = scaler.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output = regmodel.predict(final_input)[0]
    return render_template("home.html", prediction_text="The House Price Prediction is {}".format(output))

if __name__=="__main__":
    app.run(debug=True)