from langchain_openai import ChatOpenAI
from os import getenv
from dotenv import load_dotenv

load_dotenv()
api_key=getenv("API_KEY")
def Reasoning_llm(prompt):
    llm = ChatOpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    model="nvidia/nemotron-3-nano-30b-a3b:free",
    default_headers={
        "HTTP-Referer": "https://openrouter.ai/api/v1",  # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "openrouter.ai",  # Optional. Site title for rankings on openrouter.ai.
    } )
    response = llm.invoke(prompt)
    return response.content

print(Reasoning_llm("How can i create a chatbot?"))