import streamlit as st
import pandas

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
st.caption(content2)

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
