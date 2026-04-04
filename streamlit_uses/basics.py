import streamlit as st
import numpy as np
import pandas as pd
import time as t

## image/logo
st.image("images/image.png")
## determine the title of app
st.title("Artificial Intelligence")

## header name
st.header("Machine Learning")

## subheader name
st.subheader("Deep Learning")

## information about the details
st.info("Information details of deep learning")

## warning message in yellow colour
st.warning("understand properly")

## error in red colour
st.error("wrong address")

## success appears in green colour
st.success("congrats you have done first project properly")

## write something in string as well as in range
st.write("students name")
st.write(range(20))


## markdown now
st.markdown("# Linear Regression")
st.markdown("## Linear Regression")
st.markdown("### Linear Regression")

## add emojis
st.markdown(":moon:")
st.markdown(":heart:")


## maths functon
st.latex(r''' a+b x^2 + c''')


                                     ## widgets
## checkbox to tick the relevant box
st.checkbox("Login")

## a button to click 
st.button("click")

## radio button to select any one out of given
st.radio("pick your gender",["Male","Female","Other"])

## selectbox 
st.selectbox("pick your course",["ML","AI","CYBERSECURITY"])

## select one out of given
st.multiselect("choose the department",["content","sales","marketing"])

## slide and find the relevant  option
st.select_slider("Rating",["Bad","Good","Excellent","Outstanding"])

## slider
st.slider("Enter your number", 0,100)

## to select any number between 0 to 100
st.number_input("Pick a number", 0,100)

## input box
st.text_input("Enter your email address")


## date and time 
st.date_input("starting date")
st.time_input("starting time")


## text_area
st.text_area("welocome to AI and ML World!")

## file upload
st.file_uploader("upload your file/folder")
st.color_picker("color")
st.progress(89)



                  ## spinner 
with st.spinner("just wait"):
    t.sleep(5)

st.balloons()


## sidebar details

st.sidebar.write("welcome to user details")
st.sidebar.text_input("mail address")
st.sidebar.text_input("password")
st.sidebar.button("submit")
st.sidebar.slider("details")

