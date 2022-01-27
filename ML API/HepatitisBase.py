# -*- coding: utf-8 -*-
from pydantic import BaseModel
class HepatitisBase(BaseModel):    
    Age:int
    Sex:int
    ALB:float
    ALP:float
    ALT:float
    AST:float
    BIL:float
    CHE:float
    CHOL:float
    CREA:float
    GGT:float
    PROT:float
