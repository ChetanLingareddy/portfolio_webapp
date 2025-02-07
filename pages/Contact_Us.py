import streamlit as st

from send_email import email

st.header("Contact Me")

with st.form(key = "email_message"):
    user_email = st.text_input("enter your E-mail")
    raw_message = st.text_area("Enter your message")
    message = f"""\
Subject: mail from {user_email}
From: {user_email}
{raw_message}"""
    button = st.form_submit_button("submit")
    if button:
        email(message)
        st.info("Your E-mail has been sent successfully")

