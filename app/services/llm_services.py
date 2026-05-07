from langchain_groq import ChatGroq
from app.config.setting import Config

llm=ChatGroq(
    groq_api_key=Config.GROQ_API_KEY,
    model="llama-3.1-8b-instant"
    
    )

def get_ai_response(user_message):
    response =llm.invoke(user_message)
    return response.content

