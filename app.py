from flask import Flask, render_template, request, jsonify
import requests
import pickle
import numpy as np
import sklearn




app = Flask(__name__)

filenme = pickle.load(open("heart_prediction_model.pkl","rb"))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

 
@app.route('/predict',methods = ['POST'])
def predict():
    if request.method == 'POST':
        
        age = int(request.form['age'])
        
        oldpeak = int(request.form['oldpeak'])
        
        ca = int(request.form['ca'])
        
        cp=(request.form["cp"])
        if(cp == "typical_angina"):
            typical_angina = 1
            atypical_angina = 0
            non_anginal_pain = 0
        elif(cp == "atypical_angina"):
            typical_angina = 0
            atypical_angina = 1
            non_anginal_pain = 0
        else:
            typical_angina = 0
            atypical_angina = 0
            non_anginal_pain = 1
        
        sex=(request.form["sex"])
        if(sex=='Male'):
            Male=1
            female=0
        else:
             Male=0
             female=1
             
        
            
        trtbps=float(request.form['trtbps'])
        
        chol=float(request.form['chol']) 
        
        fbs= (request.form["fbs"])
        if (fbs=="true"):
            yes = 1
            no = 0
        else:
            yes=0
            no=1
            
        rest_ecg = (request.form["rest_ecg"])
        if (rest_ecg=="normal"):
            normal = 1
            having_STT_wave_abnormality = 0
            ventricular_hypertrophy_by_Estes_criteria = 0
        elif (rest_ecg==" having_STT_wave_abnormality"):
            normal = 0
            having_STT_wave_abnormality = 1
            ventricular_hypertrophy_by_Estes_criteria = 0
        else:
            normal = 0
            having_STT_wave_abnormality = 0
            ventricular_hypertrophy_by_Estes_criteria = 1
        
        thalach=float(request.form['thalach'])
        
        exang= (request.form["exang"])
        if (exang=="true"):
            yes = 1
            no = 0
        else:
            yes=0
            no=1
        
        
            
       
        
       
        
        
        
        
            
        data = np.array([[age,sex,cp,trtbps,chol,fbs,rest_ecg,thalach,exang,ca,oldpeak]])    
        my_prediction=filenme.predict(data)
         
        return render_template("result.html", contprediction = my_prediction)
if __name__=="__main__":
    app.run(debug=True)




