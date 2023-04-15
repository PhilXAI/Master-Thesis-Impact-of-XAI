import streamlit as st
from PIL import Image

st.header("Guess the City")
st.write("Round 11/17")
st.write("Where has this Google Streetview picture been taken?")
image=Image.open('Bild11.png')
st.image(image)
st.write("**Your guess:** What do you think? Where has this Google Streetview picture been taken?")
if "current" not in st.session_state:
    st.session_state.current = None

if "T" not in st.session_state:
    st.session_state.T = False

if "J" not in st.session_state:
    st.session_state.J = False

if "B" not in st.session_state:
    st.session_state.J = False

if "H" not in st.session_state:
    st.session_state.J = False

T = st.button("Tel Aviv")
J = st.button("Jerusalem")
B = st.button("Berlin")
H = st.button("Hamburg")

if T:
    st.session_state.current = "T"
if J:
    st.session_state.current = "J"
if B:
    st.session_state.current = "B"
if H:
    st.session_state.current = "H"

if st.session_state.current != None:

    if st.session_state.current == "T":
        st.session_state.T = True    
        st.session_state.J = False
        st.session_state.B = False
        st.session_state.H = False
        st.write("Your Guess is **Tel Aviv**.")
        A = st.button("What do you guess AI?")
        if A:
            st.write("My Guess is: **Berlin**. In particular, the colored areas below have helped me for my guess.")
            image=Image.open("Bild11L.png")
            st.image(image)
            st.markdown('<a href="/Round_12" target="_self">Next Round</a>', unsafe_allow_html=True)

    elif st.session_state.current == "J":
        st.session_state.T = False
        st.session_state.J = True
        st.session_state.B = False
        st.session_state.H = False
        st.write("Your Guess is **Jerusalem**.")
        A = st.button("What do you guess AI?")
        if A:
            st.write("My Guess is: **Berlin**. In particular, the colored areas below have helped me for my guess.")
            image=Image.open("Bild11L.png")
            st.image(image)
            st.markdown('<a href="/Round_12" target="_self">Next Round</a>', unsafe_allow_html=True)
    
    elif st.session_state.current == "B":
        st.session_state.T = False
        st.session_state.J = False
        st.session_state.B = True
        st.session_state.H = False
        st.write("Your Guess is **Berlin**.")
        A = st.button("What do you guess AI?")
        if A:
            st.write("My Guess is: **Berlin**. In particular, the colored areas below have helped me for my guess.")
            image=Image.open("Bild11L.png")
            st.image(image)
            st.markdown('<a href="/Round_12" target="_self">Next Round</a>', unsafe_allow_html=True)

    else:
        st.session_state.T = False
        st.session_state.J = False
        st.session_state.B = False
        st.session_state.H = True
        st.write("Your Guess is **Hamburg**.")
        A = st.button("What do you guess AI?")
        if A:
            st.write("My Guess is: **Berlin**. In particular, the colored areas below have helped me for my guess.")
            image=Image.open("Bild11L.png")
            st.image(image)
            st.markdown('<a href="/Round_12" target="_self">Next Round</a>', unsafe_allow_html=True)
