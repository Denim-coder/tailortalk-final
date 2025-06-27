import streamlit as st
import requests

st.title("📅 TailorTalk - Meeting Scheduler")

user_input = st.text_input("🗣️ Say something to book a slot (e.g. 'Book a meeting tomorrow at 4 PM'):")

if user_input:
    with st.spinner("Talking to the calendar agent..."):
        try:
            response = requests.post("http://localhost:8000/chat/", json={"user_input": user_input})
            response.raise_for_status()
            st.success(response.json()["response"])
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Backend error: {e}")
        except ValueError:
            st.error("❌ Could not decode response.")
