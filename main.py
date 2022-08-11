from flask import Flask,render_template,request,url_for

import pickle
import numpy as np
model=pickle.load(open('RandomForest.pkl','rb'))

app=Flask(__name__)
count=0
@app.route('/',methods=['POST','GET'])
def home():
    return render_template('index.html')
@app.route('/result',methods=['POST','GET'])
def result():
    global count
    count+=1
    age=request.form.get('nameAge')
    height=request.form.get('nameHeight')
    weight = request.form.get('nameWeight')
    aphi= request.form.get('nameAp_hi')
    aplo = request.form.get('nameAp_lo')
    cholestrol = request.form.get('nameCholestrol')
    glucose = request.form.get('nameGlucose')
    gender = request.form.get('nameGender')
    smoke = 1 if request.form.get('nameSmoke')=='on' else 0
    alcohol = 1 if request.form.get('nameAlcohol')=='on' else 0
    active = 1 if request.form.get('nameActive')=='on' else 0
    features=[[age,height,weight,aphi,aplo,cholestrol,glucose,gender,smoke,alcohol,active]]
    npfeatures=np.array(features)
    score=model.predict(npfeatures)
    message="3123"
    if score==1:
        message='The Patient may have Cardio Vascular Disease'
    else:
        message="The Patient is safe from Cardio Vascular Disease"
    print(score)
    return render_template('index.html',score=message)

if __name__=='__main__':
    app.run(debug=True)

