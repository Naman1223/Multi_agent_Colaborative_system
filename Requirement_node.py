from typing import TypedDict , List 
from langgraph.graph import StateGraph ,START , END
from models import Reasoning_llm,Planning_llm , UI_llm
from langgraph.checkpoint.memory import InMemorySaver
import tools
class AgentState(TypedDict):
    requirement: List[str]

requirement = tools.pdf_to_markdown("")

def requirement_node(state: AgentState) -> AgentState:
    state['requirement'].append(requirement)
    return state

checkpointer= InMemorySaver()
graph = StateGraph(AgentState)
graph.add_node("requirement_node", requirement_node)
graph.add_edge(START, "requirement_node")
graph.add_edge("requirement_node", END)
agent = graph.compile(checkpointer=checkpointer)
result = agent.invoke({"requirement": [requirement]}, config={"configurable": {"thread_id": "1"}})
print(result)
