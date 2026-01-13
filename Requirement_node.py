from typing import TypedDict , List 
from langgraph.graph import StateGraph ,START , END
from models import Reasoning_llm, Planning_llm, UI_llm, GapAnalysis_llm, RequirementUpdater_llm
from langgraph.checkpoint.memory import InMemorySaver
from tools import pdf_to_markdown
from rich.console import Console
from rich.markdown import Markdown

class AgentState(TypedDict):
    requirement: List[str]
    ask_user: List[str]
    question_count: int

requirement = pdf_to_markdown("BRD.pdf")

checkpointer = InMemorySaver()
graph = StateGraph(AgentState)

def requirement_node(state: AgentState) -> AgentState:
    """Create a in depth requirement for the given requirement which can be passed to the other nodes for planning"""
    requirement = Reasoning_llm(state['requirement'][-1])
    state['requirement'][-1] = requirement
    return state

def gap_analysis_node(state: AgentState) -> AgentState:
    """Analyze requirements for gaps"""
    current_requirement = state['requirement'][-1]
    
    question_count = state.get('question_count', 0)
    
    if question_count >= 3:
        state['ask_user'] = []
        return state

    analysis = GapAnalysis_llm(current_requirement)
    
    if "NO_GAPS" in analysis:
        state['ask_user'] = []
    else:
        state['ask_user'] = [analysis]
        state['question_count'] = question_count + 1
    return state

def human_feedback(state: AgentState) -> AgentState:
    """Get human feedback for the given requirement"""
    questions = state.get('ask_user', [])
    
    if questions:
        print(questions[0]) 
        feedback = input("\nPlease provide the missing details (or type 'skip'): ")
        if feedback.lower() == 'skip':
            state['requirement'].append("The user explicitely chose to skip providing details for: " + questions[0])
        else:
            state['requirement'].append(feedback) 
    else:
        feedback = input("Do you want to make any manual changes to the requirement?(y/n)")
        if feedback == "y":
            changes = input("Please enter the changes you want to make: ")
            state['requirement'].append(changes)
    return state

def update_requirement_node(state: AgentState) -> AgentState:
    """Update requirement with user feedback"""
    if len(state['requirement']) > 1:
        original = state['requirement'][-2] 
        feedback = state['requirement'][-1] 
        
        updated_req = RequirementUpdater_llm(original, feedback)
        state['requirement'] = [updated_req]
        
    return state

def should_continue(state: AgentState):
    """Decide whether to loop back or end"""
    if state.get('ask_user'):
        return "human_feedback"
    return END

graph.add_node("requirement_node", requirement_node)
graph.add_node("gap_analysis_node", gap_analysis_node)
graph.add_node("human_feedback", human_feedback)
graph.add_node("update_requirement_node", update_requirement_node)

graph.add_edge(START, "requirement_node")
graph.add_edge("requirement_node", "gap_analysis_node")

graph.add_conditional_edges(
    "gap_analysis_node",
    should_continue,
    {
        "human_feedback": "human_feedback",
        END: END
    }
)

graph.add_edge("human_feedback", "update_requirement_node")
graph.add_edge("update_requirement_node", "gap_analysis_node")

agent = graph.compile(checkpointer=checkpointer)
result = agent.invoke({"requirement": [requirement], "ask_user": [], "question_count": 0}, config={"configurable": {"thread_id": "1"}})
console = Console()
console.print(result['requirement'][-1])


def requirement_file():
    with open("requirement.md", "w", encoding="utf-8") as f:
        f.write(result['requirement'][-1])
requirement_file()
