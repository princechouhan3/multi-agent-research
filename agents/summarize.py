import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyADEQMvi9r5iNjCUZQZJZRBaFrMQSJoumc"))

# Use the Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash")

def run_summarize_agent(research_content: str) -> str:
    """
    Summarizes the research content into a concise and clear format.
    
    Args:
        research_content: The full text to be summarized.

    Returns:
        A summarized version of the input content.
    """
    prompt = f"""
    Summarize the following research information in a clear, concise, and professional way:

    {research_content}
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error during summarization: {str(e)}"
