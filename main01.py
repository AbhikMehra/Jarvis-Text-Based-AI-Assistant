import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file.")

genai.configure(api_key=api_key)

# Choose a valid model from your list
model_name = "models/gemini-2.0-flash"
model = genai.GenerativeModel(model_name)
chat = model.start_chat(history=[])

def completion(message):
    response = chat.send_message(message)
    reply = response.text
    print(f"Jarvis: {reply}")

if __name__ == "__main__":
    print("Jarvis: Hi, I am Jarvis. How may I help you?")
    while True:
        user_input = input("User: ")
        completion(user_input)

