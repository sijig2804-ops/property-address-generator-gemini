import json
import streamlit as st
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_addresses(state, count):

    prompt = f"""
Generate {count} realistic U.S. residential property records.

State: {state}

Return ONLY valid JSON.

Schema:

[
  {{
    "Street Number":"",
    "Street Name":"",
    "City":"",
    "State":"",
    "County":"",
    "Zip Code":"",
    "Property Type":"",
    "Square Feet":"",
    "Year Built":""
  }}
]

Requirements:
- No duplicate addresses
- Realistic city names
- Realistic county names

- Property Type must be one of:
  Single Family
  Condo
  Townhome
  Multi Family

- Square Feet should be realistic:
  Condo: 600-1800
  Townhome: 1200-2500
  Single Family: 1500-5000
  Multi Family: 2500-10000

- Year Built should be between 1950 and current year

Return ONLY the JSON array.
"""

    response = model.generate_content(prompt)

    content = response.text.strip()

    # Remove markdown if Gemini wraps JSON in code blocks
    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    return json.loads(content)
