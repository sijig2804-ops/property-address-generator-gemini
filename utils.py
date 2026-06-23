import json
import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

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
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Generate valid JSON only."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response["choices"][0]["message"]["content"]

    return json.loads(content)
