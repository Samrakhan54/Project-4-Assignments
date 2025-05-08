# Simple Website with Streamlit

import streamlit as st

st.title("My First Streamlit Website")

st.write("Welcome to my site! This is made using Python and Streamlit.")

name = st.text_input("What's your name?")
if name:
    st.write("Hello", name + " 👋")

st.write("Thanks for visiting!")
