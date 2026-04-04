import streamlit as st
st.title("HELLO ,WORLD!")                          ## title of app
st.write("Welcome to your first streamlit app")      ## write something below the title 

if st.button("click me!"):                           ## check there is any button if yess then press
    st.success("You clicked the button")             ## if you pressed you got success


    ## run = streamlit run hello_app.py