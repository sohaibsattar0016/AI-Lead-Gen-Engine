# 🚀 Agentic AI Lead Generation Engine

An automated, end-to-end B2B lead generation system powered by **n8n** and **Streamlit**. This tool allows users to input a target industry and country, and the AI automatically scrapes Google and LinkedIn to find highly relevant company details, founder/CEO profiles, and their LinkedIn URLs.

## 🌟 Key Features
* **No-Code Backend Automation:** Built using n8n for seamless data flow and API handling.
* **Agentic Data Hunting:** Uses Serper API (Google Search) and targeted LinkedIn Dorking to find decision-makers.
* **Interactive Frontend:** A clean, user-friendly UI built with Streamlit.
* **Google Sheets Integration:** Automatically structures and saves the hunted data into a cloud spreadsheet.

## 🛠️ Tech Stack
* **Frontend:** Python, Streamlit
* **Backend Automation:** n8n (Dockerized)
* **APIs:** Serper.dev, Google Sheets API

## 🚀 Setup Instructions
1. Clone the repository.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt