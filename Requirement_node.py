from typing import TypedDict , List 
from langgraph.graph import StateGraph ,START , END
from models import Reasoning_llm,Planning_llm , UI_llm
from langgraph.checkpoint.memory import InMemorySaver
from tools import pdf_to_markdown
from rich.console import Console
from rich.markdown import Markdown
class AgentState(TypedDict):
    requirement: List[str]

requirement = pdf_to_markdown("BRD.pdf")

def requirement_node(state: AgentState) -> AgentState:
    """Create a plan for the given requirement"""
    requirement = Reasoning_llm(state['requirement'][-1])
    state['requirement'].append(requirement)
    return state

checkpointer= InMemorySaver()
graph = StateGraph(AgentState)
graph.add_node("requirement_node", requirement_node)
graph.add_edge(START, "requirement_node")
graph.add_edge("requirement_node", END)
agent = graph.compile(checkpointer=checkpointer)
result = agent.invoke({"requirement": [requirement]}, config={"configurable": {"thread_id": "1"}})
console = Console()
console.print(result['requirement'][-1])

