import google.generativeai as genai
import os
from dotenv import load_dotenv
import html

load_dotenv()

class GeminiChat:
    def __init__(self):
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        
    def get_response(self, message):
        try:
            # Add system prompt for simpler responses
            prompt = f"Please give a simple, clear, and brief answer. Use everyday language that's easy to understand. Keep it conversational and friendly.\n\nUser question: {message}"
            
            response = self.model.generate_content(prompt)
            # Decode HTML entities for clean display
            clean_text = html.unescape(response.text)
            return clean_text
        except Exception as e:
            return "Sorry, something went wrong. Please try again."