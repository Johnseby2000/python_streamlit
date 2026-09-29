import streamlit as st
from streamlit.elements.widgets import number_input
from blood import blood_donor
st.title('Add New Record')
id=st.number_input('Enter donor id',min_value=1)
name=st.text_input('enter donor name')
bloodgroup=st.text_input('enter blood_group')
phone=st.text_input('enter donors number')
city=st.text_input('enter donor_city')
last_donation=st.text_input('enter last_donation')
btn=st.button("Add Donor")
if btn:
    n=blood_donor()
    n.create(id,name,bloodgroup,phone,city,last_donation)
    st.success("Created record Successfully")
