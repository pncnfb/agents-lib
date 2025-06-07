from llama_index.llms.anthropic import Anthropic
from llms.base import BaseLLM


class AnthropicLLM(BaseLLM):
    """
    AnthropicLLM Class
    """

    def get_llm(self):
        """Returns a LLamaIndex Anthropic LLM"""
        return Anthropic(**self.config)
