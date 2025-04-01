import streamlit as st
import re
from send_email import send_email

st.header("Contact Me")

#st.form is used to make form components
with st.form(key = 'email_forms'):
    user_email = st.text_input("Enter your Email Address")
    raw_message = st.text_area("Enter your message")
    
     # Validate email format
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    is_valid_email = re.match(email_pattern, user_email)

    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Message:
{raw_message}
"""

    submit_button = st.form_submit_button("Submit")

    if submit_button:
        if not is_valid_email:
            st.error("Please enter a valid email address.")
        elif not raw_message.strip():
            st.error("Message field cannot be empty.")
        else:
            send_email(message)
            st.success(f"✅ Email sent successfully! We will respond to {user_email} soon.")