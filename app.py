import json
import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from prompts import SYSTEM_PROMPT
from parser import parse_ai_response



with open("metadata.json","r") as file:
    metadata = json.load(file)

st.sidebar.title("AI DAX Assistant")
st.sidebar.write("Powered by Gemini")
st.sidebar.success("Model: Gemini Flash Latest")
st.sidebar.subheader("Metadata")
st.sidebar.success("Loaded Successfully")
st.sidebar.write(f"Model: {metadata['model_name']}")
st.sidebar.write(f"Tables: {len(metadata['tables'])}")
st.sidebar.write(f"Relationships: {len(metadata['relationships'])}")
st.sidebar.write(f"Measures: {len(metadata['measures'])}")

# Load environment variables
load_dotenv()
# Create Gemini client
client = genai.Client(
api_key=os.getenv("GEMINI_API_KEY")
)
st.title("AI DAX Assistant")

question = st.text_area("Enter your DAX question:")

prompt = f"""
{SYSTEM_PROMPT}

========================================================
POWER BI DATA MODEL
========================================================

Model Name:
{metadata["model_name"]}

Description:
{metadata["description"]}

Complete Metadata:
{metadata}

========================================================
USER QUESTION
========================================================

{question}

========================================================
RULES

1. Use ONLY metadata provided.

2. Respect relationships.

3. Never invent columns.

4. Never invent tables.

5. Reuse existing measures whenever possible.

6. Use date columns for Time Intelligence.

7. Use Fact and Dimension tables appropriately.

========================================================
"""

if st.button("Generate DAX"):
    if prompt.strip():
        with st.spinner("Generating optimized DAX..."):
            response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )
            parsed_response = parse_ai_response(response.text)

            st.subheader("Generated DAX")
            st.code(
    parsed_response["Formula"],
    language="sql"
)