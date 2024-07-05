"""
Entry point for the Outsmart Arena LLM Battle
"""

from interfaces.llms import LLM
from dotenv import load_dotenv


def main():
    load_dotenv()
    llm = LLM.for_model_name("gpt-3.5-turbo")
    result = llm.send("You are a helpful assistant", "What's 2+2?", 100)
    print(result)
    llm = LLM.for_model_name("claude-3-haiku-20240307")
    result = llm.send("You are a helpful assistant", "What's 2+2?", 100)
    print(result)
    llm = LLM.for_model_name("gemini-pro")
    result = llm.send("You are a helpful assistant", "What's 2+2?", 10)
    print(result)


if __name__ == "__main__":
    main()
