import streamlit as st

st.set_page_config(layout= "wide")

col1, col2 = st.columns(2)
with col1:
    st.image("images/peakpx.jpg" , width=600)

with col2:
    st.title("Chetan Lingareddy")
    content = """
    I am a master's Student in computer science from university of central missouri.
    """
    st.info(content)

content2= """
below are some web apps i have created using python , please feel free to contact me!
"""
st.write(content2)