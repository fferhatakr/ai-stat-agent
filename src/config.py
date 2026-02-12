import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()

def get_llm():
    
    api_key = os.getenv("GROQ_API_KEY")
    if api_key is None:
        raise Exception("Hata: .env dosyasında GROQ_API_KEY eksik!")

    
    llm = ChatGroq(
        temperature=0, 
        model_name="llama-3.1-8b-instant", 
        groq_api_key=api_key
    )
    
    return llm