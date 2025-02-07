import streamlit as st
import pandas

st.set_page_config(layout= "wide")

col1, col2 = st.columns(2)
with col1:
    st.image("images/peakpx.jpg" , width=600)

with col2:
    st.title("Chetan Lingareddy")
    About = """
    I am a master's Student in computer science from university of central missouri.
    """
    st.info(About)



Projects= """
Below are some web applications , I have created using python along with their source codes.
"""
st.caption(Projects)

col3,empty_col, col4 = st.columns([1.5,0.5,1.5])

df= pandas.read_csv("data.csv", sep = ";")
with col3:
    for index,  row in df[:10].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({"https://github.com/ChetanLingareddy/Todo_public"})")


with col4:
    for index,  row in df[10:].iterrows():
        st.subheader(row["title"])
        st.write ( row["description"] )
        st.image ( "images/" + row["image"] )
        st.write(f"[Source Code]({row['url']})")
