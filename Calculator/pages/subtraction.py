import streamlit as st

st.header('Subtraction')
number1=st.number_input('Enter num 1',min_value=0)
number2=st.number_input('Enter num 2',min_value=0)

btn=st.button('sub')
print(btn)

if btn:
    s=number1-number2
    st.write("subtract:",s)