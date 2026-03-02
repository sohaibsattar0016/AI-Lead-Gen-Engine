import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables securely from .env file
load_dotenv()

# Page configuration
st.set_page_config(page_title="AI Lead Generation Engine", page_icon="🤖", layout="centered")

# Header section
st.title("🚀 AI Lead Generation Engine")
st.markdown("**Automated B2B Lead Hunter**")
st.write("Enter your target market and let our AI Agent hunt for the best leads.")

st.divider()

# Input fields for the client
col1, col2 = st.columns(2)
with col1:
    industry = st.text_input("🎯 Target Industry", "Software")
    
with col2:
    # Expanded Dropdown for better UI (Top 15+ Countries)
    countries_list = [
        "United States", 
        "United Kingdom", 
        "Canada", 
        "Australia", 
        "Germany", 
        "United Arab Emirates", 
        "Singapore", 
        "Netherlands", 
        "Switzerland", 
        "France", 
        "Japan", 
        "South Korea", 
        "Saudi Arabia", 
        "Brazil", 
        "South Africa", 
        "India",
        "Pakistan"
    ]
    country = st.selectbox("🌍 Target Country", countries_list)

st.divider()

# Fetch Webhook URL securely from the .env file
WEBHOOK_URL = os.getenv("WEBHOOK_URL").strip().replace('"', '').replace("'", "")

# Generate Button
if st.button("Generate Leads", type="primary", use_container_width=True):
    # Safety check if .env is missing
    if not WEBHOOK_URL:
        st.error("⚠️ Webhook URL is missing! Please configure your .env file.")
    else:
        with st.spinner(f"AI is hunting for {industry} leads in {country}... Please wait."):
            
            # Data payload for n8n
            payload = {
                "Industry": industry,
                "Country": country
            }
            
            try:
                # Sending request to n8n webhook
                response = requests.post(WEBHOOK_URL, json=payload)
                
                if response.status_code == 200:
                    st.success(f"✅ Leads for {industry} in {country} successfully generated! Check your Google Sheet.")
                    st.balloons()
                else:
                    st.error(f"⚠️ System busy or error occurred. Status Code: {response.status_code}")
            except Exception as e:
                st.error(f"Error connecting to AI Engine: {e}")

# Footer
st.markdown("---")
st.caption("Developed by Sohaib Sattar | AI & Automation Specialist")