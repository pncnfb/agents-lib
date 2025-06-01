import langwatch

from globals import google_llm
from agents import WebSearchAgent

agent = WebSearchAgent(google_llm)

@langwatch.trace(name="websearch_mcp_check")
def ask_agent(query):
    return agent.query(query)

response = ask_agent("What is mcp protocol?")

print(response)
