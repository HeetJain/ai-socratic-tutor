import streamlit as st

st.title("Ai-socratic-tutor")
st.write("[bold]your own friendly neighbourhood Lupa ")
st.write("Namaste Duniya")

if "message" not in st.session_state:
    st.session_state.message = [{"role":"ai","content":"Hello my name is lupa"}]

for msg in st.session_state.message:
     with st.chat_message(msg["role"]):
         st.write(msg["content"])


input = st.chat_input("enter you question here")

if input:
    st.session_state.message.append({"role":"user","content":input})
    with st.chat_message("user"):
        st.write(input)



    bot_reply=f"You asked: {input}, right now?.But, I am not connected to any api because my non coders friend haven't made one yet"
    st.session_state.message.append({"role":"ai","content": bot_reply})
    with st.chat_message("ai"):
        st.write(bot_reply)
