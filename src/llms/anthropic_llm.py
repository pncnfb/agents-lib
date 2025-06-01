from llama_index.llms.anthropic import Anthropic
from .base import BaseLLM

class AnthropicLLM(BaseLLM):
    """
    AnthropicLLM Class
    """
    def get_llm(self):
        """Returns a LLamaIndex Anthropic LLM"""
        return Anthropic(model=self.config["MODEL"], api_key=self.config["ANTHROPIC_API_KEY"])


