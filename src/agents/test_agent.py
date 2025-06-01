from llama_index.core import PromptTemplate

class TestAgent:
    def __init__(self, llm: any):
        self.llm = llm
        self.prompt_template = PromptTemplate(
            "Answer the following question in an extremely formal and professional tone:\n\nQuestion: {query}"
        )

    def query(self, user_input: str) -> str:
        prompt = self.prompt_template.format(query=user_input)
        response = self.llm.complete(prompt)
        return response.text.strip()
