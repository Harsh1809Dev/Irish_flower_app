import streamlit as st
from PIL import Image

def app():
    st.title("How to use model")
    st.write("It is very simple to identify whether the plant is Iris Setosa, Iris Versicolor or Iris Virginica using the inbuilt model")
    st.write("Steps for using the model : ")
    st.write("1. Measure the length and width of Petal and Sepal in centimetres.")
    image_sepal_petal = Image.open('sepal_petal.png')
    st.image(image_sepal_petal,use_column_width=True)
    st.write("For eg. sepal length and width are 6.5 cm and 3.0 cm, respectively. And petal length and width are 5.8 cm and 2.2 cm, respectively")
    st.write("2. Provide the data to the model.")   
    image_input = Image.open('input.png')
    st.image(image_input,use_column_width=True)
    st.write("3. After providing th data to the model simply click on  the '***Click here to identify the flower type***' button in the model section.")
    image_button = Image.open('button.png')
    image_button = st.image(image_button,use_column_width=True)
    st.write("4. The model will tell what type of plant is.")
    image_flower_pred = Image.open('flower_pred.png')
    st.image(image_flower_pred,use_column_width=True)
    st.title("")
    st.write("**Video guide for using the application for identification: **")
    video_file = open('home.mkv','rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.title("")
    st.title("")
    st.title("")
    st.write("***ALERT : do not enter negative value otherwise the model will show an error***")
    image_error = Image.open("error.png")
    st.image(image_error,use_column_width=True)