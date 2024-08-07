import pandas as pd 
import numpy as np 
import streamlit as st
import joblib


Model = joblib.load('Model.h5')


def Predict(Gender, AGE, Urea, Cr, HbA1c, Chol, TG, HDL, LDL,VLDL, BMI):
    
    
    test = pd.DataFrame(data=[ [Gender, AGE, Urea, Cr, HbA1c, Chol, TG, HDL, LDL,VLDL, BMI] ] , 
                       columns=['Gender', 'AGE', 'Urea', 'Cr', 'HbA1c', 'Chol', 'TG', 'HDL', 'LDL','VLDL', 'BMI'])
    
    return Model.predict(test)



def main():
    
    Gender = st.selectbox(f'Select your Gender ', ['F' , 'M'])
    
    AGE = st.slider(f'Select your AGE ', min_value = 20.0, max_value = 80.0, step = 1.0 ,  )
    
    Urea = st.slider(f'Select your Urea ', min_value = 0.5, max_value = 39.0, step = 0.1)
    
    Cr = st.slider(f'Select your Cr ', min_value = 0.06, max_value = 8.0, step = 0.1 )
    
    HbA1c = st.slider(f'Select your HbA1c ', min_value = 0.9, max_value = 16.0, step = 1.0)
    
    Chol = st.slider(f'Select your Chol ', min_value = 0.0, max_value = 11.0, step = 1.0)
    
    TG = st.slider(f'Select your TG ', min_value = 0.3, max_value = 14.0, step = 0.1 , value = 10.0)
    
    HDL = st.slider(f'Select your HDL ', min_value = 0.2, max_value = 10.0, step = 0.1)
    
    LDL = st.slider(f'Select your LDL ', min_value = 0.3, max_value = 10.0, step = 0.1)
    
    VLDL = st.slider(f'Select your VLDL ', min_value = 0.1, max_value = 35.0, step = 1.0)
    
    BMI = st.slider(f'Select your BMI ', min_value = 19.0, max_value = 48.0, step = 1.0)
    
    if st.button('Predict'):
        
        ans = Predict(Gender, AGE, Urea, Cr, HbA1c, Chol, TG, HDL, LDL,VLDL, BMI)
        st.write(ans)
    
        
main()
