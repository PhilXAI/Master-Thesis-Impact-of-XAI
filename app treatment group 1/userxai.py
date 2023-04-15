import streamlit as st
st.header("Demographic and Sociographic Questions")
st.write("**Please answer the following questions before the actual task starts.**")
option = st.selectbox("What best describes your gender?",("male", "female", "diverse"))

st.text_input("What is your nationality?")

st.text_input("What is your year of birth?")

st.text_input("What is your highest educational qualification?")

st.write("Which of the following cities have you visited?")
genre = st.radio("Berlin", ('Yes', "No"))
genre = st.radio("Hamburg", ('Yes', "No"))
genre = st.radio("Tel Aviv", ('Yes', "No"))
genre = st.radio("Jerusalem", ('Yes', "No"))

st.write("**Thank you. Now click the button bellow to start the game.**")
st.markdown('<a href="/Round_1" target="_self">Let\'s start</a>', unsafe_allow_html=True)