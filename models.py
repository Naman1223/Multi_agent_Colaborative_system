from langchain_openai import ChatOpenAI
from os import getenv
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
api_key=getenv("API_KEY")
google_api_key=getenv("GOOGLE_API_KEY")
groq_api_key=getenv("GROQ_API_KEY")

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


def Planning_llm(prompt):
    model = ChatGoogleGenerativeAI(
    api_key=google_api_key,
    model="gemini-2.0-flash-exp",)
    response = model.invoke(prompt)
    return response.content

def UI_llm(prompt):
    llm = ChatOpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    model="qwen/qwen3-coder:free",
    default_headers={
        "HTTP-Referer": "https://openrouter.ai/api/v1",  # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "openrouter.ai",  # Optional. Site title for rankings on openrouter.ai.
    } )
    response = llm.invoke(prompt)
    return response.content
