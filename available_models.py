from dotenv import load_dotenv
import google.generativeai as genai
import os
from config import GOOGLE_API_KEY

load_dotenv()

genai.configure(api_key=GOOGLE_API_KEY)

for model in genai.list_models():
    print(model.name)