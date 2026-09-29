import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete
st.title('Welcome to Library App')
b=BookListCreateRetrieveUpdateDelete()
tab1,tab2,tab3,tab4,tab5=st.tabs(['ADD','READ','RETRIEVE','UPDATE','DELETE'])
with tab1:
    st.write('APP')
with tab2:
    st.write('READ')
with tab1:
    st.write('RETRIEVE)
with tab1:
    st.write('APP')
with tab1:
    st.write('APP')