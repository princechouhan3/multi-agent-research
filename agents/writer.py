import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyADEQMvi9r5iNjCUZQZJZRBaFrMQSJoumc"))

# Initialize Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash")

def run_writer_agent(topic: str, summary: str) -> str:
    """
    Write a detailed report using the topic and summarized research.
    """
    prompt = f"""
    Write a comprehensive, professional report on the following topic using the summary provided.

    Topic: {topic}

    Summary:
    {summary}

    The report should include:
    - An engaging introduction
    - A well-structured main body with insights
    - A clear and concise conclusion
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
