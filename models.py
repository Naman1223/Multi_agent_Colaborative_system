from langchain_openai import ChatOpenAI
from os import getenv
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import read_markdown_file

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
    model="gemini-3-flash-preview",)
    messages = [
        SystemMessage(content="You are a planning agent that can plan the given requirement and generate a detailed roadmap to complete the project step by step.The roadmap should be in bullet points."),
        HumanMessage(content=prompt)
    ]
    response = model.invoke(messages)
    return response.content

def UI_plan_llm(prompt):
    model = ChatGoogleGenerativeAI(
    api_key=google_api_key,
    model="gemini-3-flash-preview",)
    messages = [
        SystemMessage(content="You are a UI/UX designer. Generate a UI/UX plan for code based on the given requirement in React.You are free to use your imagination to create a ui based on the requirements content genrated should be in english and should be in a modern and responsive design"),
        HumanMessage(content=f"Original Requirement:\n{prompt}")
    ]
    response = model.invoke(messages)
    return response.content


def UI_llm(prompt):
    llm = ChatOpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    model="qwen/qwen3-coder:free",
    temperature=1.5,
    default_headers={
        "HTTP-Referer": "https://openrouter.ai/api/v1",  # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "openrouter.ai",  # Optional. Site title for rankings on openrouter.ai.
    } )
    messages = [
        SystemMessage(content="You are a UI/UX designer. Generate a UI/UX code based on the given requirement in React.Only return the code make sure not to return any other text apart from code also not include```jsx``` in the starting and  ending of the code. You are free to use your imagination to create a ui based on the requirements content genrated should be in english and should be in a modern and responsive design"),
        HumanMessage(content=f"Original Requirement:\n{prompt}")
    ]
    response = llm.invoke(messages)
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




def assinger_llm(plan,requirement):
    llm = ChatOpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    model="qwen/qwen3-coder:free",
    default_headers={
        "HTTP-Referer": "https://openrouter.ai/api/v1",  # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "openrouter.ai",  # Optional. Site title for rankings on openrouter.ai.
    } )
    messages = [
        SystemMessage(content="You are a senior business analyst. Assign the following project requirements to the roadmap."),
        HumanMessage(content=f"Plan: {plan}\n\nRequirement: {requirement}")
    ]
    response = llm.invoke(messages)
    return response.content