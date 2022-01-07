import streamlit as st
import helper

st.set_page_config(
     page_title="Simpsons Recognision System",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://github.com/everydaycodings/Anima-Recommendation-System-WebApp#readme',
         'Report a bug': "https://github.com/everydaycodings/Anima-Recommendation-System-WebApp/issues/new/choose",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
)

st.sidebar.title("Hello World")

file_type = ['png', 'jpg']
uploaded_file = st.sidebar.file_uploader("Upload Your WhatsApp Group Exported (without Media) txt file",type=file_type)


if uploaded_file is not None:
    pass