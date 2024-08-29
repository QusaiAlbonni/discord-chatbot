from google import generativeai as genai
from settings import GEMINI_KEY
from sql import Conversation
from typing import Iterable

genai.configure(api_key=GEMINI_KEY)
genai.GenerationConfig.temperature = 0.4

model = genai.GenerativeModel(model_name='gemini-1.5-pro-latest')


def generate_response(conversation_history: Iterable[Conversation]):
    history = []
    for conversation in conversation_history:
        if conversation.role == 'bot':
            role = 'model'
        else:
            role = 'user'
        history.append(
            {
                'role': role,
                'parts': [conversation.message_content]
            }
        )
    response = model.generate_content(contents=history)

    return response
