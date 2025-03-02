# pip install streamlit
import streamlit as st

st.set_page_config(page_title="growth mindset project", project_icon="🌟")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("Welcome to Your Growth Journey")
st.write("Welcome to Your Growth Journeys  means you are starting a path of learning, improvement, and success. Its about growing your skills, gaining new experiences, and becoming a better version of yourself step by step. 🚀")

# quote section
st.header("Today Growth Mindset Quote")
st.write("Success is not Final")

st.header("Whats is your Challenge")
user_input = st.text_input("Describe a challenge you are facing ")

# condition
if user_input:
    st.success(
        f" you are facing: {user_input}. Keep pushing forward towards your goal!")
else:
    st.warning("Tell us about your challenge")

# reflexing
st.header("Relection of your learning")
reflection = st.text_area("Write your reflextion outcome:")

if reflection:
    st.success(f"Great insight! Your reflection:{reflection}")
else:
    st.info("Reflecting on past experience help you grow! shre your difficulties")

# acheivement
st.header("Celebrate Your Wins!")
acheivement = st.text_area("Share something your are recently accomlished")

if acheivement:
    st.success(f"Amazing! You acheived:{acheivement}")
else:
    st.info("Big or small, every acheivement counts! share one now")

# footer
st.write("- - -")
st.write("Keep believing in yourself. Growth is a journey, not a destination!")
st.write("**Create by Uzair Ahmed**")
