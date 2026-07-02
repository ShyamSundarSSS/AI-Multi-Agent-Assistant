from langgraph.graph import StateGraph, START, END

from state import AgentState

from agents.router import router_agent
from agents.weather_agent import weather_agent
from agents.currency_agent import currency_agent
from agents.general_agent import general_agent


graph = StateGraph(AgentState)


graph.add_node("router", router_agent)
graph.add_node("weather", weather_agent)
graph.add_node("currency", currency_agent)
graph.add_node("general", general_agent)


graph.add_edge(START, "router")


def route(state: AgentState):
    return state["agent"]


graph.add_conditional_edges(
    "router",
    route,
    {
        "weather": "weather",
        "currency": "currency",
        "general": "general"
    },
)


graph.add_edge("weather", END)
graph.add_edge("currency", END)
graph.add_edge("general", END)


app = graph.compile()