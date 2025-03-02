import streamlit as st

# Corrected `page_icon` instead of `project_icon`
st.set_page_config(page_title="Growth Mindset Project", page_icon="🌟")

st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("Welcome to Your Growth Journey")
st.write("Welcome to Your Growth Journey means you are starting a path of learning, improvement, and success. It's about growing your skills, gaining new experiences, and becoming a better version of yourself step by step. 🚀")

# Quote Section
st.header("Today's Growth Mindset Quote")
st.write("Success is not final.")

# User Input Section
st.header("What is Your Challenge?")
user_input = st.text_input("Describe a challenge you are facing:")

# Condition to Display Message
if user_input:
    st.success(
        f"You are facing: {user_input}. Keep pushing forward towards your goal! 💪")
else:
    st.warning("Tell us about your challenge.")
