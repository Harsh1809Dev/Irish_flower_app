import pandas as pd
import numpy as np
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from PIL import Image

def app():
    st.set_option('deprecation.showfileUploaderEncoding', False)

    st.title("Iris Flower Identifier")

    st.header("Identify whether the plant is Setosa, Versicolor or Virginica by simply providing sepal length, sepal width , petal length and petal width")
    st.title("")
    sepal_length = st.number_input("Enter sepal length")
    if sepal_length < 0:
        st.error("Invalid sepal length! Length can't be negative")
    sepal_width = st.number_input("Enter sepal width")
    if sepal_width < 0 :
        st.error("Invalid sepal width ! Width can't be negative")
    petal_length = st.number_input("Enter petal length")
    if petal_length < 0 :
        st.error("Invalid petal length ! Length can't be negative")
    petal_width = st.number_input("Enter petal width")
    if petal_width < 0:
        st.error("Invalid petal width ! Width can't be negative")

    if st.button("Click here to identify the flower type"):
        iris_dataset= load_iris()
        X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)
        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(X_train, y_train)
        X_pred = np.array([[sepal_length,sepal_width,petal_length,petal_width]])
        y_pred = knn.predict(X_pred)
        flower_pred = iris_dataset['target_names'][y_pred]
        flower_type = flower_pred[0]
        st.write("Flower is : Iris-",flower_type)
        if flower_type == 'versicolor':
            image = Image.open('versicolor.jpg')
            st.image(image,caption="IRIS VERSICOLOR",use_column_width=True)
        if flower_type == 'setosa':
            image_setosa = Image.open('setosa.jpg')
            st.image(image_setosa,caption="IRIS SETOSA",use_column_width=True)
        if flower_type == 'virginica':
            image_virginica = Image.open('virginica.jpg')
            st.image(image_virginica,caption="IRIS VIRGINICA",use_column_width=True)