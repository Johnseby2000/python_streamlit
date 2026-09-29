import streamlit as st
from streamlit.elements.widgets import checkbox
import datetime as date
st.title('Student Register Form')
name=st.text_input("Enter your name:")
age=st.number_input("Enter your age:",min_value=1,max_value=100)
d=st.date_input("DOB",min_value=date.date(1990,1,1),
                             max_value=date.date.today(),
                             value=date.date(2006,1,1) )

email=st.text_input("Enter your email:")

g=st.radio('Gender',['Male','Female'])
st.write(g)

c=st.selectbox('Course',['Python','Dotnet','Java'])
st.write(c)

b=st.button('Register')

if b:
    st.write("Name:",name)
    st.write("Age:", age)
    st.write("Dob:",d )
    st.write("email:", email)
    st.write("Gender:",g)
    st.write("Course:",c)




