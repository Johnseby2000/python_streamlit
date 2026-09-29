import streamlit as st
from streamlit.elements import write

st.header('BMI Calculator')
weight=st.number_input("Enter weight in kg:",min_value=1)
height=st.number_input("Enter height in cm:",min_value=1)

btn=st.button('bmi')
if btn:
     bmi=weight/(height/100)**2
     st.write('BMI is',bmi)
     if bmi < 18.5:
         st.write(bmi, 'is under weight')
     elif 18.5 <= bmi < 25:
         st.success( ' normal')
     elif 25 < bmi < 30:
         st.warning( ' overweight')
     elif bmi > 30:
         st.error( " obesity")

