import streamlit as st

st.header('Division')
number1=st.number_input('Enter num 1',min_value=0)
number2=st.number_input('Enter num 2',min_value=1)

btn=st.button('Divison')
print(btn)

if btn:
    if number2!=0:
         s=number1/number2
         st.write("Division:",s)
