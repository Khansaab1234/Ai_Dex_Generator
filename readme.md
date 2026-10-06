# ⚡ AI DAX Generator

An interactive, AI-powered tool built with **Streamlit** and **Google Gemini API** designed to help Power BI developers, Data Analysts, and Business Intelligence engineers generate, parse, and optimize complex **DAX (Data Analysis Expressions)** queries from plain English descriptions.

---

## 📌 Features

- **Natural Language to DAX**: Convert plain-English business logic into production-ready DAX expressions.
- **Formula Parsing & Explanation**: Breaks down complex measures into plain English for easier debugging and documentation.
- **Context-Aware Metadata**: Uses custom schema definitions (`metadata.json`) to suggest accurate table and column references.
- **Interactive UI**: Clean, responsive, and intuitive interface powered by Streamlit.
- **Modular Codebase**: Dedicated modules for prompt engineering, schema parsing, and API interactions.

---

## 🗂 Project Structure

```text
Ai Dex Generator/
│
├── .gitignore              # Ignores sensitive environment variables and venv
├── requirements.txt        # Python dependencies required to run the app
├── README.md               # Project documentation
├── app.py                  # Main Streamlit application entry point
├── parser.py               # Parsing and processing logic for DAX & metadata
├── prompts.py              # Prompt engineering templates for the Gemini model
├── metadata.json           # Schema definitions and data model references
├── test_gemini.py          # Testing script for Gemini API integration
│
└── .env                    # (Local only) Stores GEMINI_API_KEY
