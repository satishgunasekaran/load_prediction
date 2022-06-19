from opcode import opname
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():

    features = [np.round(float(x),2) for x in request.form.values()]
    final_features = [features]




    print(final_features)
    
    prediction = model.predict(final_features)

    prediction = np.round(prediction, 2)[0]


    print(prediction)

    return render_template('index.html', prediction = prediction)

if __name__ == "__main__":
    app.run(debug=True)