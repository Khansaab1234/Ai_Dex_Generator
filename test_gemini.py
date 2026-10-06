import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

question = input("Ask your DAX question: ")

response = client.models.generate_content(
    model="models/gemini-flash-latest",
    contents=question
)

print("\nAI Response:\n")
print(response.text)
