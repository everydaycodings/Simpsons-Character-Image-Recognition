import streamlit as st
from helper import predict

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

st.title("Simpsons Recognision System")
st.sidebar.title("Hello World")

file_type = ['png', 'jpg']
uploaded_file = st.sidebar.file_uploader("Upload Your WhatsApp Group Exported (without Media) txt file",type=file_type)


if uploaded_file is not None:
    st.header("The Image you have choose is of: ")
    st.image(uploaded_file)
    with open("cache/"+ uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    predict = predict(uploaded_file.name)
    st.header(predict)