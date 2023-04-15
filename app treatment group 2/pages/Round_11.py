import streamlit as st
from PIL import Image

st.header("Guess the City")
st.write("Round 11/17")
st.write("Where has this Google Streetview picture been taken?")
image=Image.open('Bild11.png')
st.image(image)
if "current" not in st.session_state:
    st.session_state.current = None

if "A" not in st.session_state:
    st.session_state.T = False

A = st.button("What do you guess AI?")

if A:
    st.session_state.current = "A"

if st.session_state.current != None:
    if st.session_state.current == "A":
        st.session_state.A = True
        st.write("My Guess is: **Berlin**. In particular, the colored areas below have helped me for my guess.")
        image=Image.open("Bild11L.png")
        st.image(image)
        st.write("**Your guess:** What do you think? Where has this Google Streetview picture been taken?")
        T = st.button("Tel Aviv")
        J = st.button("Jerusalem")
        B = st.button("Berlin")
        H = st.button("Hamburg")
        if T:
            st.write("Your Guess is **Tel Aviv**.")
            st.markdown('<a href="/Round_12" target="_self">Next Round</a>', unsafe_allow_html=True)
        if J:
            st.write("Your Guess is **Jerusalem**.")
            st.markdown('<a href="/Round_12" target="_self">Next Round</a>', unsafe_allow_html=True)
        if B:
            st.write("Your Guess is **Berlin**.")
            st.markdown('<a href="/Round_12" target="_self">Next Round</a>', unsafe_allow_html=True)
        if H:
            st.write("Your Guess is **Hamburg**.")
            st.markdown('<a href="/Round_12" target="_self">Next Round</a>', unsafe_allow_html=True)

