import streamlit as st
from src.extraction import load_data

st.set_page_config(layout="wide")

def main():

    df = load_data()

if __name__ == "main":
    main()
