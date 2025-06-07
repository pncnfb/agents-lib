import os
from vertexai.generative_models._generative_models import (
    HarmBlockThreshold,
    HarmCategory,
)
from llama_index.llms.google_genai import GoogleGenAI
from llms.base import BaseLLM


def config_to_dict(config):
    return {k: v for k, v in config.items()}


class GoogleLLM(BaseLLM):
    """
    GoogleLLM Class
    """

    def __init__(self, config):
        config = config_to_dict(config)
        config["temperature"] = float(config["temperature"])
        config["max_tokens"] = int(config["max_tokens"])
        config["max_retries"] = int(config.get("max_retries", 3))
        super().__init__(config)

    def get_llm(self):
        """Returns a LLamaIndex Google LLM"""

        return GoogleGenAI(
            **self.config,
            safety_settings={
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_UNSPECIFIED: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            },
        )
