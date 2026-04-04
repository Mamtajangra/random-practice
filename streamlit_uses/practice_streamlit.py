import streamlit as st
import time as t

st.title("Internet")
st.header("AI")
st.subheader("Machine Learning")
st.write("Definition of ML")

# Dropdown
st.selectbox("Choose any one", ["KNN", "Random Forest", "Logistic Regression"])

# Correct way for checkbox (single)
st.checkbox("Chosen by students")

# If you want multiple choices use multiselect
st.multiselect("Select students", [12, 34, 56, 89])

# Radio buttons
st.radio("Performance level", ["20", "38", "56", "79"])

# Multiselect (topics)
st.multiselect("Select multiple options", ["Cloud", "Deep Learning", "Cybersecurity"])

# Slider
st.slider("Enter your number", 0, 100)

# Number input with min & max
st.number_input("Enter any number", min_value=5, max_value=20)

# Date & time input
st.date_input("Opening date")
st.time_input("Entry time")

# Text area
st.text_area("Welcome to world website")

# Balloons with delay
t.sleep(2)
st.balloons()
