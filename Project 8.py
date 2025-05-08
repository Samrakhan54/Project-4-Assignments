# BMI Calculator using Streamlit

import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("Enter your weight (kg):")
height = st.number_input("Enter your height (m):")

if weight > 0 and height > 0:
    bmi = weight / (height * height)
    st.write("Your BMI is:", round(bmi, 2))
    if bmi < 18.5:
        st.write("You are underweight.")
    elif bmi < 25:
        st.write("You have a normal weight.")
    else:
        st.write("You are overweight.")
