import streamlit as st
import pywhatkit as kit
st.title('Whatsapp Message Sender App')
phone_number =st.text_input('Receiver Mobile No.')
message = st.text_area('Message')
hour=st.number_input(label="Set Hour", min_value=0, max_value=24, value="min")
minute=st.number_input(label="Set Minutes", min_value=0, max_value=59, value="min")
if st.button("Send Message"):
    try:
        kit.sendwhatmsg(phone_number, message,hour,minute)
        print("Message scheduled successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")