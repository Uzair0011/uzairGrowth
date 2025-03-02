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

# Reflecting on Learning
st.header("Reflect on Your Learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"Great insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experiences helps you grow! Share your difficulties.")

# Achievements
st.header("Celebrate Your Wins!")
achievement = st.text_area("Share something you've recently accomplished:")

if achievement:
    st.success(f"Amazing! You achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share one now!")

# Footer
st.write("- - -")
st.write("Keep believing in yourself, growth is a journey! 🚀")
st.write("**Created By Uzair Ahmed**")
