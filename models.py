from langchain_openai import ChatOpenAI
from os import getenv
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
api_key=getenv("API_KEY")
google_api_key=getenv("GOOGLE_API_KEY")
groq_api_key=getenv("GROQ_API_KEY")

from langchain_core.messages import SystemMessage, HumanMessage

def Reasoning_llm(prompt_user):
    llm = ChatOpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    model="nvidia/nemotron-3-nano-30b-a3b:free",
    default_headers={
        "HTTP-Referer": "https://openrouter.ai/api/v1",  # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "openrouter.ai",  # Optional. Site title for rankings on openrouter.ai.
    } )
    messages = [
        SystemMessage(content="You are a reasoning agent that can reason about the given requirement and generate a detailed requirement to complete the project."),
        HumanMessage(content=prompt_user)
    ]
    response = llm.invoke(messages)
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

import time

def GapAnalysis_llm(requirement):
    llm = ChatOpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    model="nvidia/nemotron-3-nano-30b-a3b:free",
    default_headers={
        "HTTP-Referer": "https://openrouter.ai/api/v1",  # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "openrouter.ai",  # Optional. Site title for rankings on openrouter.ai.
    } )
    messages = [
        SystemMessage(content="You are a senior business analyst. Analyze the following project requirements. Identify any missing critical information (e.g., tech stack, design preferences, timeline, target audience, specific features). If gaps exist, list up to 3 most important questions to ask the stakeholder to clarify them. If the requirement is comprehensive enough to start planning, respond with 'NO_GAPS'."),
        HumanMessage(content=requirement)
    ]
    response = llm.invoke(messages)
    return response.content

def RequirementUpdater_llm(original_requirement, user_feedback):
    llm = ChatOpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    model="nvidia/nemotron-3-nano-30b-a3b:free",
    default_headers={
        "HTTP-Referer": "https://openrouter.ai/api/v1",  # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "openrouter.ai",  # Optional. Site title for rankings on openrouter.ai.
    } )
    messages = [
        SystemMessage(content="You are a requirement manager. Update the original project requirement document based on the user's feedback. Ensure the new information is integrated smoothly and the document remains coherent."),
        HumanMessage(content=f"Original Requirement:\n{original_requirement}\n\nUser Feedback:\n{user_feedback}")
    ]
    response = llm.invoke(messages)
    return response.content
