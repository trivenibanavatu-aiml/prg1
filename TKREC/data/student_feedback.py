import streamlit as st

# App title and description
st.title("Student Feedback Form")
st.write("Please provide your feedback for the class session.")

# Input widgets
name = st.text_input("Enter your name")

subject = st.selectbox("Select a subject", ["Math", "Science", "English", "History"])

rating = st.slider("Rate the session", min_value=1, max_value=10)

comments = st.text_area("Any additional comments")

# Submit button
if st.button("Submit"):
    if name and subject and rating:
        st.success("Thank you for your feedback!")
        st.write("**Submitted Details:**")
        st.write(f"Name: {name}")
        st.write(f"Subject: {subject}")
        st.write(f"Rating: {rating}/10")
        st.write(f"Comments: {comments}")
    else:
        st.warning("Please fill in all the required fields.")