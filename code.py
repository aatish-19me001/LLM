import streamlit as st
from google import genai
st.markdown(
  """
  <h1 style='text-align: center;'> AADHI's AI WORLD</h1>
  <p style='text-align: center; font-size:18px;'>
    How Can I Help You :) !.
  </p>
  """,
  unsafe_allow_html=True,
)
robo = genai.Client(api_key=st.secrets["MY_API_KEY"])
mychat = robo.chats.create(model="gemini-flash-lite-latest")
#Placeholder for the response
response_placeholder = st.empty()

question = st.text_input("", placeholder="Enter your question here...")

col1, col2, col3 = st.columns([4, 1, 4])

with col2:
  send =st.button("Send")

if send:
  response = mychat.send_message(question)
  response_placeholder.write(response.text)
