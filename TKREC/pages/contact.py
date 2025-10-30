import streamlit as st
st.text("Contact Information")
st.title("Interactive Feedback Form ")

st.text_input("Enter  Name")
st.text_input("Enter Emailid")
st.text_input("Enter Mobile Number")  
st.text_input("Message")

if st.button("Submit"):
    st.success("Submitted successfully!")
    st.snow()
st.write("Thank you for your Feedback!")
























