import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyADEQMvi9r5iNjCUZQZZRBaFrMQSJoumC"))

# Initialize the Gemini model (1.5 Flash is faster for research-style queries)
model = genai.GenerativeModel("models/gemini-1.5-flash")

def run_research_agent(topic: str) -> str:
    """
    Given a topic, this function uses Gemini to gather in-depth research content.
    Returns a string with gathered information.
    """
    prompt = f"""
    You are a helpful research assistant. Your task is to conduct thorough research on the topic: "{topic}".
    Provide a structured summary that includes:
    - Introduction
    - Key Concepts
    - Recent Developments
    - Use Cases or Applications
    - Sources (if available)

    Write in a clear and concise manner suitable for generating a report later.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error in Research Agent: {str(e)}"
