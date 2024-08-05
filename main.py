import streamlit as st
from langchain_helper import get_few_shot_db_chain
import os

st.title("Claims Center: Database Q&A 💡")

question = st.text_input("Question: ")

if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)






