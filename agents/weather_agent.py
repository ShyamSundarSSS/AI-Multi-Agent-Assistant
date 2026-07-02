from llm import get_llm
from state import AgentState
from tools.weather_tool import get_weather

def weather_agent(state: AgentState):
    llm = get_llm(temperature=0)

    prompt = f"""
Extract ONLY the city name.

Examples:

Weather in Chennai
Chennai

Temperature in Delhi
Delhi

Will it rain in Mumbai?
Mumbai

User:
{state["user_input"]}
"""

    city = llm.invoke(prompt).content.strip()

    result = get_weather(city)

    return {
        "result": result
    }