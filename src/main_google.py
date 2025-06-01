from globals import google_llm
from agents import TestAgent
import langwatch

from llama_index.core.llms import ChatMessage

# Create agent
agent = TestAgent(google_llm)

# --- Standard sync call ---
@langwatch.trace(name="test_sync")
def run_sync():
    print("---- SYNC ----")
    return agent.query("Tell me something about 'prompt engineering'?")

# --- Async call (if supported by agent/LLM) ---
@langwatch.trace(name="test_async")
async def run_async():
    print("---- ASYNC ----")
    if hasattr(google_llm, "achat"):
        return await google_llm.achat(
            messages=[
                ChatMessage(role="user", content="Explain the concept of retrieval augmented generation.")
            ]
        )

# --- Multi-turn chat ---
@langwatch.trace(name="test_chat")
def run_chat():
    print("---- CHAT ----")
    if hasattr(google_llm, "chat"):
        messages = [
            ChatMessage(role="user", content="What is the capital of France?"),
            ChatMessage(role="assistant", content="The capital of France is Paris."),
            ChatMessage(role="user", content="And what is its population?")
        ]
        return google_llm.chat(messages)


# --- Main entry ---
if __name__ == "__main__":
    #run_sync()
    run_chat()
    #asyncio.run(run_async())
