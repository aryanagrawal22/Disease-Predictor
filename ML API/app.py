# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:40:41 2020

@author: win10
"""

# 1. Library imports
import uvicorn
import base64
import numpy as np
import matplotlib.pyplot as plt
from fastapi import FastAPI
from StrokeBase import StrokeBase
from HeartBase import HeartBase
from HepatitisBase import HepatitisBase
import pickle
# 2. Create the app object
app = FastAPI()

pickle_heart = open("./Model/heart_disease_model.pkl","rb")
classifier_heart = pickle.load(pickle_heart)

pickle_stroke = open("./Model/stroke_model.pkl","rb")
classifier_stroke = pickle.load(pickle_stroke)

pickle_hepatitis = open("./Model/liver_disease_model_hepatitis.pkl","rb")
classifier_hepatitis = pickle.load(pickle_hepatitis)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
#@app.get('/{name}')
#def get_name(name: str):
#    return {'Welcome To Krish Youtube Channel': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict_heart')
def predict_heartbase(data:HeartBase):
    data = data.dict()
    age = data['age']
    sex = data['sex']
    cp = data['cp']
    trestbps = data['trestbps']
    chol = data['chol']
    fbs = data['fbs']
    restecg = data['restecg']
    thalach = data['thalach']
    exang = data['exang']
    oldpeak = data['oldpeak']
    slope = data['slope']
    ca = data['ca']
    thal = data['thal']
    
    
    barWidth = 0.25
    fig = plt.subplots(figsize =(12, 8))
 
    # set height of bar
    Normal = [120, 180, 130, 0]
    Diagnosed = [trestbps, chol, thalach, oldpeak]
 
    # Set position of bar on X axis
    br1 = np.arange(len(Normal))
    br2 = [x + barWidth for x in br1]
    
    # Make the plot
    plt.bar(br1, Normal, color ='g', width = barWidth,
            edgecolor ='grey', label ='Normal')
    plt.bar(br2, Diagnosed, color ='r', width = barWidth,
            edgecolor ='grey', label ='Diagnosed')
 
    # Adding Xticks
    plt.xlabel('Parameters', fontweight ='bold', fontsize = 15)
    plt.ylabel('Values', fontweight ='bold', fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(Normal))],
        ['trestbps', 'chol', 'thalach', 'oldpeak'])
 
    plt.legend()
    plt.savefig("./output.jpg")
    with open("output.jpg", "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())
    
    
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier_heart.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    if(prediction[0]==1):
        prediction = 1
    else:
        prediction = 0
    return {
        'prediction': prediction,
        'image': converted_string
    }

@app.post('/predict_stroke')
def predict_strokebase(data:StrokeBase):
    data = data.dict()
    gender = data['gender']
    age = data['age']
    hypertension = data['hypertension']
    heart_disease = data['heart_disease']
    ever_married = data['ever_married']
    work_type = data['work_type']
    Residence_type = data['Residence_type']
    avg_glucose_level = data['avg_glucose_level']
    bmi = data['bmi']
    smoking_status = data['smoking_status']
    
    
    barWidth = 0.25
    fig = plt.subplots(figsize =(12, 8))
 
    # set height of bar
    Normal = [90, 23]
    Diagnosed = [avg_glucose_level, bmi]
 
    # Set position of bar on X axis
    br1 = np.arange(len(Normal))
    br2 = [x + barWidth for x in br1]
    
    # Make the plot
    plt.bar(br1, Normal, color ='g', width = barWidth,
            edgecolor ='grey', label ='Normal')
    plt.bar(br2, Diagnosed, color ='r', width = barWidth,
            edgecolor ='grey', label ='Diagnosed')
 
    # Adding Xticks
    plt.xlabel('Parameters', fontweight ='bold', fontsize = 15)
    plt.ylabel('Values', fontweight ='bold', fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(Normal))],
        ['Average Glucose Level', 'BMI'])
 
    plt.legend()
    plt.savefig("./output.jpg")
    with open("output.jpg", "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())
    
    
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier_stroke.predict([[gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status]])
    if(prediction[0]==1):
        prediction=1
    else:
        prediction=0
    return {
        'prediction': prediction,
        'image': converted_string
    }


@app.post('/predict_hepatitis')
def predict_hepatitisbase(data:HepatitisBase):
    data = data.dict()
    Age=data['Age']
    Sex=data['Sex']
    ALB=data['ALB']
    ALP=data['ALP']
    ALT=data['ALT']
    AST=data['AST']
    BIL=data['BIL']
    CHE=data['CHE']
    CHOL=data['CHOL']
    CREA=data['CREA']
    GGT=data['GGT']
    PROT=data['PROT']
    
    
    barWidth = 0.25
    fig = plt.subplots(figsize =(12, 8))
 
    # set height of bar
    Normal = [42, 70, 20, 25, 10, 8, 3, 105, 15, 70]
    Diagnosed = [ALB, ALP, ALT, AST, BIL, CHE, CHOL, CREA, GGT, PROT]
 
    # Set position of bar on X axis
    br1 = np.arange(len(Normal))
    br2 = [x + barWidth for x in br1]
    
    # Make the plot
    plt.bar(br1, Normal, color ='g', width = barWidth,
            edgecolor ='grey', label ='Normal')
    plt.bar(br2, Diagnosed, color ='r', width = barWidth,
            edgecolor ='grey', label ='Diagnosed')
 
    # Adding Xticks
    plt.xlabel('Parameters', fontweight ='bold', fontsize = 15)
    plt.ylabel('Values', fontweight ='bold', fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(Normal))],
        ["ALB", "ALP", "ALT", "AST", "BIL", "CHE", "CHOL", "CREA", "GGT", "PROT"])
 
    plt.legend()
    plt.savefig("./output.jpg")
    with open("output.jpg", "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())
    
    
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier_hepatitis.predict([[Age, Sex, ALB, ALP, ALT, AST, BIL, CHE, CHOL, CREA, GGT, PROT]])
    if(prediction[0]==1):
        prediction=1
    else:
        prediction=0
    return {
        'prediction': prediction,
        'image': converted_string
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload