# -*- coding: utf-8 -*-
from pydantic import BaseModel
class HeartBase(BaseModel):
    age: float 
    sex: float 
    cp: float 
    trestbps: float
    chol: float
    fbs: float
    restecg: float
    thalach: float
    exang: float
    oldpeak: float
    slope: float
    ca: float
    thal: float