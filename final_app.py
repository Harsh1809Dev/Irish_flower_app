import model
import info
import help
import home
import streamlit as st

PAGES = {
    "Home": home,
    "Information about flowers": info,
    "Identify flower": model,
    "Help": help
}

st.sidebar.title('**NAVIGATION**')
selection = st.sidebar.radio("Go To", list(PAGES.keys()))
page = PAGES[selection]
page.app()