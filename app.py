import streamlit as st
import numpy as np
import pandas as pd

st.title("The app title")

st.page_link("app.py", label="Home", icon="⚽️")
st.page_link("pages/profile.py", label="My profile")

st.write("Hello **world**!")

chart_data = pd.DataFrame(
    np.random.randn(20, 3), 
    columns=['a', 'b', 'c']
    )

st.write(chart_data)

st.link_button('Click me', 'https://www.baidu.com')
