import streamlit as st

st.title("Ai-socratic-tutor")
st.write("[bold]your own friendly neighbourhood Lupa ")
st.write("Namaste Duniya")
input = st.chat_input("Type Your message here")

if "message" not in st.session_state:
    user = st.chat_message("role",avatar="ai").write("Hi my name is Lupa. How may i help you?")
    
if input:
    st.write(f"the user is saying {input}")
