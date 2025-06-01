import os
from google.cloud import aiplatform
from google.oauth2 import service_account
from vertexai.generative_models._generative_models import (
    HarmBlockThreshold,
    HarmCategory,
)
from llama_index.llms.google_genai import GoogleGenAI
from .base import BaseLLM

class GoogleLLM(BaseLLM):
    """
    GoogleLLM Class
    """
    def __init__(self, config):
        super().__init__(config)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.config["GCP_JSON_CREDS_PATH"]

    def get_llm(self):
        """Returns a LLamaIndex Google LLM"""

        return GoogleGenAI(
            vertexai_config={"project": self.config["GCP_PROJECT_ID"], "location": self.config["GCP_REGION"]},
            model=self.config["MODEL"],
            temperature=float(self.config["TEMPERATURE"]),
            max_retries=int(self.config["MAX_RETRIES"]),
            max_tokens=int(self.config["MAX_TOKENS"]),
            safety_settings={
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_UNSPECIFIED: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            },
        )
