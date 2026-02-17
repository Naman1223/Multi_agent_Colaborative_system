# Multi-Agent Collaborative System

![Project Status](https://img.shields.io/badge/Status-Active-green)
![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)

## 🌟 Overview

The **Multi-Agent Collaborative System** is an advanced AI-driven platform designed to automate and enhance the software development lifecycle. By leveraging a team of specialized autonomous agents—Requirement Analyst, Gap Analysis Expert, Planner, User Proxy, and UI/UX Designer—this system transforms initial user ideas into detailed technical specifications, comprehensive project plans, and fully functional UI code.

Powered by **LangGraph** and state-of-the-art LLMs (OpenAI, Google Gemini, NVIDIA via OpenRouter), this collaborative framework ensures high-quality output through intelligent reasoning, iterative refinement, and human-in-the-loop validation.

## ✨ Key Features

- **🤖 Autonomous Requirement Engineering:** Analyzes raw user input (text or PDF) to generate structured, in-depth requirement documents.
- **🔍 Intelligent Gap Analysis:** Automatically identifies missing information, ambiguities, or inconsistencies and prompts the user for clarification.
- **🗣️ Human-in-the-Loop Feedback:** Interactive feedback mechanism (up to 3 iterations) to refine requirements based on user input, ensuring accuracy and completeness.
- **📅 Strategic Project Planning:** Creates detailed, step-by-step implementation roadmaps and task lists (`planning_node.py`).
- **🎨 AI-Powered UI/UX Design:** Generates modern, responsive React (JSX) code and UI plans based on finalized requirements (`UI_node.py`).
- **🖥️ Live Preview:** Instantly visualizes generated UIs using a local web view powered by Flask and PyWebView (`Webview.py`).
- **🔗 Multi-Model Integration:** Seamlessly integrates various high-performance models (GPT-4, Gemini Flash, NVIDIA Nemotron) for optimal performance across different tasks.

## 🏗️ System Architecture

The core of the system is built on a directed acyclic graph (DAG) using **LangGraph**, orchestrating the flow of information between agents:

1.  **Requirement Node:** Initial processing and expansion of user ideas.
2.  **Gap Analysis Node:** Critical evaluation of requirements to find missing details.
3.  **Human Feedback Node:** Interactive loop to gather user input on identified gaps.
4.  **Update Requirement Node:** Integration of user feedback into the master requirement document.
5.  **Planning Node:** Translating requirements into actionable roadmaps.
6.  **UI/UX Node:** Converting technical specs into visual designs and code.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- [Git](https://git-scm.com/)
- API Keys for:
    - OpenAI
    - Google Gemini
    - Groq (or OpenRouter)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Start-sys/Multi_agent_Colaborative_system.git
    cd Multi_agent_Colaborative_system
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in the root directory and add your API keys:
    ```env
    API_KEY=your_openai_api_key
    GOOGLE_API_KEY=your_google_api_key
    GROQ_API_KEY=your_groq_api_key
    ```

## 📖 Usage

Follow these steps to generate a project from scratch:

### 1. Generate Requirements
Run the requirement engineering module to start the process:
```bash
python Requirement_node.py
```
- Paste your initial project idea or requirements when prompted.
- The system will analyze gaps and ask clarifying questions.
- Once finalized, a `requirement.md` file will be generated.

### 2. Generate Project Plan
Create a detailed project plan and roadmap based on the requirements:
```bash
python planning_node.py
```
- This reads `requirement.md` and generates `plan.md` and `roadmap.md`.

### 3. Generate UI Code
After finalizing the roadmap, generate the UI:
```bash
python UI_node.py
```
- This reads `roadmap.md` and generates an `index.jsx` file with the React code.

### 4. Preview Application
To view the generated UI in a local window:
```bash
python Webview.py
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1.  Fork the project
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
