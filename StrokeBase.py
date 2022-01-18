# -*- coding: utf-8 -*-
from pydantic import BaseModel
class StrokeBase(BaseModel):    
    gender:int
    age:float
    hypertension:int
    heart_disease:int
    ever_married:int
    work_type:int
    Residence_type:int
    avg_glucose_level:float
    bmi:float
    smoking_status:int