# import streamlit as st
# from streamlit.elements.widgets import number_input
#
# from library_db import BookListCreateRetrieveUpdateDelete
# st.title('Delete')
#
# id=st.number_input("Enter book id",min_value=1)
# btn=st.button("Delete")
#
# if btn:
#     n=BookListCreateRetrieveUpdateDelete()
#     record=n.delete(id)
#     print(record)
#     if record:
#         st.success("Deleted record Successfully")
#     else:
#         st.error("No record found")
import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

st.title("Delete Book")

n = BookListCreateRetrieveUpdateDelete()

book_id = st.number_input(
    "Enter Book ID",
    min_value=1,
    step=1
)

if st.button("Delete"):
    result = n.delete(int(book_id))

    if result:
        st.success("Record deleted successfully")
    else:
        st.error("No record found")