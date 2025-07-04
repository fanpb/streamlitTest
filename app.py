import streamlit as st

st.title("The app title")

st.page_link("app.py", label="Home", icon="⚽️")
st.page_link("pages/profile.py", label="My profile")

st.write("Hello **world**!")
