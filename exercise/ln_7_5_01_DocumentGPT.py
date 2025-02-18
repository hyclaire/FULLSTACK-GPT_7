
import streamlit as st
import time

st.set_page_config(
    page_title="DocumentGPT",
    page_icon="📑"
)

st.title("Document GPT")

def send_message(message, role, save=True):
    with st.chat_message(role):
        st.write(message)
        if save:
            st.session_state["messages"].append({"message": message, "role": role})

# save the data into session_state to keep the history
# to repaint the whole page
# if we refresh it, the session state will be gone... 
if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    send_message(message["message"], message["role"], save=False)

message = st.chat_input("Send a message to the ai")

if message:
    send_message(message, "human")
    time.sleep(2)
    send_message(f"You said: {message}", "ai" ) 