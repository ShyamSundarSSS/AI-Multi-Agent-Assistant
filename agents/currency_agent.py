from llm import get_llm

from state import AgentState
from tools.currency_tool import convert_currency

def currency_agent(state: AgentState):
    llm = get_llm(temperature=0)

    prompt = f"""
Extract the following information.

Return ONLY in this format.

amount,from_currency,to_currency

Example

Convert 100 USD to INR

100,USD,INR

Convert 250 EUR to JPY

250,EUR,JPY

User:
{state["user_input"]}
"""

    response = llm.invoke(prompt).content.strip()

    amount, from_currency, to_currency = response.split(",")

    result = convert_currency(
        float(amount),
        from_currency,
        to_currency
    )

    return {
        "result": result
    }