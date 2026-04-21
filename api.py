from google import genai
from dotenv import load_dotenv
import os, io
from gtts import gTTS


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
    audio_buffer = io.BytesIO()
    speech = gTTS(text, lang='en', slow=False)
    speech.write_to_fp(audio_buffer)
    return audio_buffer

#quiz generator
def generate_quiz(images,difficulty):
    res = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, f"Generate a quiz based on the image with {difficulty} difficulty level. Return the quiz in json format with fields: question, options, and correct_answer. Make sure use markdown to differentiate the options."]
    )
    return res.text