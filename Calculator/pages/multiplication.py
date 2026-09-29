import streamlit as st

st.header('Multiplication')
number1=st.number_input('Enter num 1',min_value=0)
number2=st.number_input('Enter num 2',min_value=0)

btn=st.button('Product')
print(btn)

if btn:
    s=number1/number2
    st.write("Product:",s)