import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("student performance visualizer")
st.write("upload CSV file to visualize student performance")
#uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
uploaded_file = "data/Data_visualization.csv"
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
    st.subheader("tail of the data ")
    st.data_editor(df.tail(10))
    st.subheader("head of the data ")
    st.data_editor(df.head(10))
    st.subheader("statistical summary of the data ")    
    st.write(df.describe())
    st.info(df)
    st.snow()

    