from llm import get_llm

from state import AgentState

def router_agent(state: AgentState):
    llm = get_llm(
    temperature=0
)
    prompt = f"""
    You are an intelligent routing assistant.

    Your task is to classify the user's request into ONLY ONE category.

    Possible categories:

    weather
    currency
    general

    Rules:

    - Questions about weather, temperature, rain, humidity, forecast, climate -> weather

    - Questions about converting currencies, exchange rates, money conversion -> currency

    - EVERYTHING ELSE -> general

    Return ONLY ONE WORD.

    User:
    {state["user_input"]}
    """

    response = llm.invoke(prompt).content.strip().lower()

    return {
        "agent": response
    }