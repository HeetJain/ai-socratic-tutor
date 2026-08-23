import streamlit as st
import requests 
st.set_page_config("Luna Tutor",layout="wide")
menu = st.sidebar.radio("Select View:", ["🎓 Student Tutor", "📈 Teacher Dashboard"])

if menu == "🎓 Student Tutor":
    st.title("Ai-socratic-tutor ")
    st.markdown("##### your own friendly AI Tutor Luna ")

    url = "https://api.dify.ai/v1/chat-messages"

    headers={   
        "Authorization": "Bearer app-mekNBLa1G4oFbLCwY7u6bv8P",
       "Content-type" : "application/json"
    }


    if "message" not in st.session_state:
        st.session_state.message = [{"role":"ai","content":"Hello my name is Luna: your AI tutor how can i help you"}]

    for msg in st.session_state.message:
         with st.chat_message(msg["role"]):
             st.write(msg["content"])


    input = st.chat_input("enter you question here")

    if input:
        st.session_state.message.append({"role":"user","content":input})
        with st.chat_message("user"):
            st.write(input)
        payload={
            "inputs":{},
            "query":input,
            "response_mode":"blocking",
            "user":"Student"
        }
        try:
         response = requests.post(url,headers=headers,json=payload,timeout=40)

         response_data = response.json()

         if "answer" in response_data:
            bot_reply = response_data["answer"]
         else:
            bot_reply = f"API Error: {response_data}"
        except requests.exceptions.Timeout:
            st.write("Request timeout. The server is taking too long to think")
        except requests.exceptions.RequestException as e:
            st.write(f"Request failed {e}")


        st.session_state.message.append({"role":"ai","content":bot_reply})
        with st.chat_message("ai"):
            st.write(bot_reply)

else:

    st.header("Classroom Insights")
    

    col1, col2, col3 = st.columns(3)
    col1.metric("Active Students", "42", "+3 this week")
    col2.metric("Questions Asked", "128", "High Engagement")
    col3.metric("Struggling Concept", "Acid,Bases and salts", "-12% accuracy")
    
    st.divider()
    
    st.subheader("Weekly Topic Confusion")
    # A simple bar chart using fake data
    chart_data = {"Gravity": 45, "Fractions": 80, "Photosynthesis": 20}
    st.bar_chart(chart_data)


