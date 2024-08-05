import streamlit as st
from query_data import query_rag
import os

st.title("Claims Center: Ask your questions 💡")
question = st.text_input("Question: ")

if question:
    
    response,sources = query_rag(question)
    try:
        st.header("Answer")
        #st.write(response)
        st.write(response.generations[0][0].text)
        text=sources[0]
        first_backslash_index = text.find('\\')
        first_colon_index = text.find(':', first_backslash_index)

        # Extract the middle part without the colon
        middle_part = text[first_backslash_index + 1:first_colon_index]
        st.header("Source")
        st.write(middle_part)
    except KeyError as e:
        st.error(f"KeyError: {e} key is missing in the data structure.")

    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")





