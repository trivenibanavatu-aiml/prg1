import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Student Performance Visualizer")
st.write("Upload a CSV file containing student performance data.")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Raw Data")
    st.dataframe(df)

    st.subheader("Line Chart - Subject Marks Over Time")
    st.line_chart(df.set_index("Month")[["Math", "Science", "English"]])

    st.subheader("Bar Chart - Total Marks per Student")
    df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
    st.bar_chart(df.set_index("Name")["Total"])

    st.subheader("Scatterplot - Math vs Science")
    st.scatter_chart(df[["Math", "Science"]])

    st.subheader("Custom Chart using matplotlib and st.pyplot")
    fig, ax = plt.subplots()
    ax.plot(df["Month"], df["English"], marker='o', color='green', label="English Marks")
    ax.set_title("English Performance Over Months")
    ax.set_xlabel("Month")
    ax.set_ylabel("Marks")
    ax.legend()
    st.pyplot(fig)
