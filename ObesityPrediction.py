# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 11:46:39 2024

@author: Smart AI Labs
"""

import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

classifier= pickle.load(open("C:/Users/Smart AI Labs/Desktop/AI jupyter notebook/Obesity Prediction/trained_model.sav", 'rb'))

with st.sidebar:
    
    selected= option_menu("Obesity Prediction System",
                          [" Obesity Prediction System"],
                         
                          icons= ['file-medical-fill'],
                          default_index=0)
    

st.title("Obesity Prediction using ML")

Age = st.text_input("Age")
Gender = st.text_input("Gender")
Height = st.text_input('Height')
Weight = st.text_input('Weight')
BMI = st.text_input('BMI value')
PhysicalActivityLevel = st.text_input('Physical Activity Level')



prediction = ''
    
    
    
if st.button('Obesity Prediction'):
    prediction = classifier.predict([[Age, Gender, Height, Weight, BMI, PhysicalActivityLevel ]])    
    label_mapping = {
       0: "Normal weight",
       1: "Obese",  
       2: "Overweight",
       3: "Underweight",
       }
    prediction_label = label_mapping.get(prediction[0], "Unknown")
    st.success(f"The person is {prediction_label}")