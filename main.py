import pywhatkit as py
import streamlit as st

st.markdown("""<style>
.css-fblp2m{
visibility: hidden;
}</style>""", unsafe_allow_html=True)

st.title("Whatsapp Message Automate ")
st.image('/Users/aqibsiddiqui/Desktop/untitled folder/WhatsApp.png', width=50)
st.markdown("----")
st.text("Hi!! I can help you to stay in touch with your contacts even when you're busy")

with st.form("Detail", clear_on_submit=True):
    pno = st.text_input("Enter the number you want to send message with country code:")
    message = st.text_input("Enter the message you want to send:")
    col1, col2 = st.columns(2)
    hour = col1.text_input("Hours")
    minute = col2.text_input("Minute")
    button = st.form_submit_button("Submit")

    if button:
        if pno == "" or message == "" or hour == "" or minute == "":
            st.warning("Please fill all the details")
        else:
            st.success("Successfully submitted")
            py.sendwhatmsg(pno, message, int(hour), int(minute))
