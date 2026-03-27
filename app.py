import streamlit as st

# Title of the Web App
st.title("🎓 AKTU OneStop")
st.subheader("Your Intelligent Exam Companion")

# Sidebar for Navigation
st.sidebar.header("Navigation")
branch = st.sidebar.selectbox("Select your Branch", ["CS", "IT", "ME", "CE", "EC"])
semester = st.sidebar.selectbox("Select Semester", ["1", "2", "3", "4", "5", "6", "7", "8"])

# Main Content
st.write(f"### Welcome {branch} Student! (Semester {semester})")
st.info("Select a subject below to see high-frequency exam topics.")

# Example Subject Dropdown
subject = st.selectbox("Choose a Subject", ["Data Structures", "Discrete Structures", "Computer Organization"])

if subject == "Data Structures":
    st.write("#### 🔥 High Priority Topics (Based on last 5 years):")
    st.write("- **Unit 1:** Sparse Matrix, Linked List Reversal")
    st.write("- **Unit 2:** Stack using Queue, Postfix Evaluation")
    st.success("Tip: Focus on Unit 1 and 3 for maximum marks!")
