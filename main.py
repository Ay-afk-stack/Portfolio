import streamlit as st

st.set_page_config(layout = "wide")

col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.png",width = 300)

with col2:
    st.title("Ayush Pakhrin")
    content = """Hi, I am Ayush Pakhrin! I'm an aspiring Python developer on a journey to master coding and problem-solving. With a passion for learning and a curiosity for how things work, I'm exploring Python's versatility in web development, data analysis, automation, and beyond. This portfolio showcases my progress, projects, and the challenges I've tackled along the way."""
    st.info(content)

content2= """Below you can find some of the apps I have built in Python. Feel Free to contact me!"""

st.write(content2)