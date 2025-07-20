
import streamlit as st

st.set_page_config(page_title="WhatsApp Template Enhancer", layout="centered")

st.title("🚀 WhatsApp Template Enhancer")

input_text = st.text_area("Paste your WhatsApp template message here:")

if st.button("Enhance Template") and input_text:
    st.subheader("🌐 Detected Language:")
    st.write("English")

    st.subheader("📂 Template Category:")
    st.write("Marketing")

    st.subheader("✅ Enhanced Template:")
    enhanced_template = '''Header: 🚂 Hey Subhadeep – Ready for Howrah?

Body: Complete booking your train tickets with us & get FLAT ₹600 OFF*!
🎟️ Trip Guarantee: Confirmed seat or 3× refund
❌ Free Cancellation: Zero penalty
Use Code: MMTBLACK'''
    st.code(enhanced_template, language='text')

    st.subheader("🔘 Quick Reply Buttons:")
    st.write("✅ Book My Ticket\n📍 Track Booking\n💬 Talk to Agent")

    st.subheader("📣 Utility Nudges:")
    st.write("⏰ Still on the fence? Your ₹600 OFF expires soon. (Send after 1 hour)")
    st.write("🕒 Train to Howrah departs tomorrow. Confirm now! (Send 24 hrs before trip)")
    st.write("🛤️ Final call: Boarding starts in 3 hrs! (Send 3 hrs before trip)")
