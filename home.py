import streamlit as st
import base64
def app():
    st.set_option('deprecation.showfileUploaderEncoding', False)

    st.title("Iris Flower Identifier")
    st.write("Identify whether the plant is Iris Setosa, Iris Versicolor or Iris Virginica.")

    file_ = open("home.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="home gif">',
        unsafe_allow_html=True,
    )

    st.write("Iris flower identifier helps you idenitfy whether the plant is an Iris Setosa, Iris Versicolor or Iris virgininca on the basis of length and width of petal and sepal with accuracy upto 97%.")
