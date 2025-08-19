import google.generativeai as genai
import os
from dotenv import load_dotenv
from voice_io import speak , voice

load_dotenv()
api_key = os.getenv('ai-api-key')

def ai_query(query):
  
  genai.configure(
    api_key= api_key
  )
  model = genai.GenerativeModel(
    model_name= "gemini-1.5-flash",
    system_instruction="You are a helpful virtual assistant like a real human. You can answer questions, provide information, and assist with various tasks. Please respond in a friendly and short length. You will respond in the same as the user query language.",
    
    )
  response = model.generate_content(query)
  print(response.text)
  return response.text
