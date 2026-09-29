import streamlit as st
from streamlit.elements.widgets import number_input
from library_db import BookListCreateRetrieveUpdateDelete
st.title('Add New Record')

id=st.number_input("Enter book id",min_value=1)
title=st.text_input("enter book name")
author=st.text_input("enter author name")
price=st.number_input("Enter Book price",min_value=100)
pages=st.number_input("Enter Book pages",min_value=1)


l=st.selectbox('language',['English','French','Spanish','Hindi'])
st.write(l)

btn=st.button("Add")

if btn:
    n=BookListCreateRetrieveUpdateDelete()
    n.create(id,title,author,price,pages,l)
    st.success("Create record Successfully")

    # st.write("id:",id)
    # st.write("title:", title)
    # st.write("Author:", author)
    # st.write("Price:", price)
    # st.write("Pages:",pages)
    # st.write("Language:",l)





