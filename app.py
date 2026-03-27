import streamlit as st
import json
import os

# 1. Function to load your JSON data
def load_data():
    # Path to your JSON file
    data_path = os.path.join("data", "aktu_data.json")
    with open(data_path, "r") as f:
        return json.load(f)

# 2. Page Config
st.set_page_config(page_title="AKTU OneStop", page_icon="🎓")
st.title("🎓 AKTU OneStop")

# 3. Load the data
try:
    data = load_data()
    
    # 4. Sidebar Selections
    st.sidebar.header("Filter Search")
    # This automatically gets the subject names from your JSON keys!
    subject_list = list(data.keys())
    selected_subject = st.sidebar.selectbox("Select Subject", subject_list)

    # 5. Display the Content
    st.header(f"Important Topics for: {selected_subject}")
    
    # Loop through the units in the selected subject
    for unit, topics in data[selected_subject].items():
        with st.expander(f"📌 {unit}"):
            for topic in topics:
                st.write(f"- {topic}")
                
    st.info("💡 Pro-tip: Focus on these topics to cover 80% of the question paper!")

except Exception as e:
    st.error("Wait! We're still updating the library. Please check back in a bit!")
    # This helps you debug if the file path is wrong
    st.write(f"Error details: {e}")
