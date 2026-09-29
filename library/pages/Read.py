import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

st.title("Book List")

b= BookListCreateRetrieveUpdateDelete()

record = b.list()
st.write("")
if record:
        st.table([record])
else:
        st.error("No record found")