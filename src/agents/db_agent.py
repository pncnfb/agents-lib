from llm import CoreLLM

class DatabaseAgent(CoreLLM):
    """Specialized agent for database operations with structured outputs"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.has_tools():
            raise ValueError("DatabaseAgent requires tools to be configured")

        self.base_prompt = """
        - You are a database assistant.
        - Use the available database tools to answer the question accurately.
        - Always use tools to get real data instead of making assumptions.
        - Return always the query used
        """

    def __call__(self, request: str) -> str:
        return self.chat(message=f"{self.base_prompt} \nThis is the request:\n{request}")