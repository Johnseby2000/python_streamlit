import streamlit as st

from library_db import BookListCreateRetrieveUpdateDelete
st.title('Update')

id=st.number_input("Enter book id",min_value=1)
title=st.text_input("enter book name")
author=st.text_input("enter author name")
price=st.number_input("Enter Book price",min_value=100)
pages=st.number_input("Enter Book pages",min_value=1)
lan=st.selectbox('language',['English','French','Spanish','Hindi'])
st.write(lan)

btn=st.button("Update")

if btn:
    n=BookListCreateRetrieveUpdateDelete()
    n.update(id,title, author, price, pages, lan)
    st.success("Updated record Successfully")




