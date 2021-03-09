# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 12:57:15 2021

@author: prana
"""

from flask import Flask, request
import numpy as np
import flasgger
from flasgger import Swagger
from pickle import load
import pickle
import streamlit as st

load_model=pickle.load(open('gram_model_dt.sav','rb'))

app=Flask(__name__)
Swagger(app)


@app.route('/',methods=["Get"])
def predict():
    
    """Price Prediction for Tomato in Karnataka
    
    ---
    parameters:
                                
      - name: district
        in: query
        type: number
        description: "0-19"
        required: true
      - name: market
        in: query
        type: number
        description: "0-58"
        required: true
      - name: variety
        in: query
        type: number
        description: "0=Hybrid 1=Normal" 
        required: true
      - name: day
        in: query
        type: number
        description: "0-30"
        required: true
      - name: month
        in: query
        type: number
        description: "0-11"
        required: true
      - name: year
        in: query
        type: number
        description: ""
        required: true
    responses:                        
        200:                        
            description: The output values
    """    
    i1=request.args.get('district')
    
    i2=request.args.get('market')
    
    i3=request.args.get('variety')
    
    i4=request.args.get('day')
    
    i5=request.args.get('month')
    
    i6=request.args.get('year')
    
    prediction=load_model.predict([[i1,i2,i3,i4,i5,i6]])
    print(prediction)
    return "Hello The answer is"+str(prediction)









if __name__=='__main__':
    app.run( debug=True)