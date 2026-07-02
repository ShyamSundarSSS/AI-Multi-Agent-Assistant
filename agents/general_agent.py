from llm import get_llm

from state import AgentState

def general_agent(state: AgentState):
    llm = get_llm(
    temperature=0.3
)

    response = llm.invoke(state["user_input"]).content

    return {
        "result": response
    }