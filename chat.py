import google.generativeai as genai
import config

genai.configure(api_key=config.GEMINI_API_KEY)

def chatbot(input):
    if input:
        messages = [
            {"role": "system", "content": "You are Agro-Sahayak, an AI assistant specialized in agriculture. Provide expert insights on farming, crops, soil health, pest control, and market trends. Do not answer any questions related to other fields except Agriculture. Keeps the replies short and simple untill user asks you to explain in detail."},
            {"role": "user", "content": input}
        ]

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(input)
        
        return response.text