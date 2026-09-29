import streamlit as st
#num input
num1=st.number_input("Enter number1",min_value=0)
num2=st.number_input("Enter number2",min_value=0)
st.write(num1)
st.write(num2)

#text_input
name=st.text_input('Enter your name')
st.write(name)

date=st.date_input('Enter date')
st.write(date)

btn=st.button('click')
print(btn)

if btn:
    st.write(num1)
    st.write(num2)
    print(num1+num2)
    st.write(name)
    st.write(date)


