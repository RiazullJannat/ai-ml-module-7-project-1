from google import genai
from dotenv import load_dotenv
import os


#loading the environment variable

load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")

#initialize client
client = genai.Client(api_key=api_key)


#note generator 
def generate_note(images):
    res =client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, "Summarize the picture in note format at max 100 words, make sure add necessary markdown to differentiate different section"]
    )
    return res.text

#audio generator
def generate_audio(text):
    pass

#quiz generator
def generate_quiz(images,difficulty):
    pass 