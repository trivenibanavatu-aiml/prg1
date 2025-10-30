import streamlit as st
st.text("Hello, world!")
st.text("Hello, world!")
st.text("TKREC")
st.image(image="./images/images.jpg",width=300)


data = {
  "employees": [
    {
      "firstName": "John",
      "lastName": "Doe",
      "age": 30,

      "skills": ["JavaScript", "HTML", "CSS"]
    },
    {
      "firstName": "Anna",
      "lastName": "Smith",
      "age": 25,

      "skills": ["Python", "SQL"]
    }
  ],
  "location": {
    "city": "New York",
    "country": "USA"
  }
} 
st.dataframe(data)
st.json(data)
st.table(data)
