from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('clf_rf.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        Age = int(request.form['Age'])
        Anaemia1=request.form['Anaemia']
        if (Anaemia1=='Yes'):
            Anaemia=1
        else:
            Anaemia=0
        
        creatinine_phosphokinase=float(request.form['creatinine_phosphokinase'])

        Diabetes1=request.form['diabetes']
        if Diabetes1=='Yes':
            Diabetes=1
        else:
            Diabetes=0

        
        ejection_fraction=float(request.form['ejection_fraction'])
        High_blood_pressure1=request.form['high_blood_pressure']
        if High_blood_pressure1=='Yes':
            high_blood_pressure=1
        else:
             high_blood_pressure=0
             
        platelets=float(request.form['platelets'])
        serum_creatinine=float(request.form['serum_creatinine'])
        serum_sodium=float(request.form['serum_sodium'])

        Sex1=request.form['sex']
        if Sex1=='Male':
            sex=1
        else:
            sex=0
        
        smoking1=request.form['smoking']
        if smoking1=='Yes':
            smoking=1
        else:
            smoking=0
        time=float(request.form['time'])
        prediction=model.predict([[Age,Anaemia,creatinine_phosphokinase,Diabetes,ejection_fraction,high_blood_pressure,platelets,serum_creatinine,serum_sodium,sex,smoking,time]])
        output=round(prediction[0],2)
        if output==0:
            return render_template('index.html',prediction_text="patient not going to die!")
        else:
            return render_template('index.html',prediction_text="Sorry,Patient will die!")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=False)

