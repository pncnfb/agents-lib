from globals import LLM
from agents import WebSearchAgent

agent = WebSearchAgent(LLM)

print(agent.query("What is mcp protocol?"))
