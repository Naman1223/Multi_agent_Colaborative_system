from typing import TypedDict , List 
from langgraph.graph import StateGraph ,START , END
from models import Reasoning_llm,Planning_llm , UI_llm

class AgentState(TypedDict):
    requirement: List[str]

user_input = input("Enter your requirement: ")
def reasoning_node(state: AgentState) -> AgentState:
    # Extract the latest requirement or input
    input_text = state['requirement'][-1]
    reasoning = UI_llm(input_text)
    state['requirement'].append(reasoning)
    return state

graph = StateGraph(AgentState)
graph.add_node("reasoning_node", reasoning_node)
graph.add_edge(START, "reasoning_node")
graph.add_edge("reasoning_node", END)
agent = graph.compile()
result = agent.invoke({"requirement": [user_input]})
print(result)

