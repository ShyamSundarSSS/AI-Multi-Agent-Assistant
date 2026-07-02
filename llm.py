import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


def get_llm(
    model: str = "llama-3.3-70b-versatile",
    temperature: float = 0,
):
    """
    Returns a configured Groq LLM.

    Args:
        model: Name of the Groq model.
        temperature: Controls randomness in the model's responses.

    Returns:
        ChatGroq instance.
    """

    return ChatGroq(
        model=model,
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=temperature,
    )