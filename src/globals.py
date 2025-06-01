from configparser import ConfigParser

import langwatch

from llms.anthropic_llm import AnthropicLLM
from llms.google_llm import GoogleLLM

config = ConfigParser()
config.read("config.ini")

langwatch.setup(api_key=config["LANGWATCH"]["API_KEY"])

anthropic_llm = AnthropicLLM(config["ANTHROPIC_LLM"]).get_llm()
google_llm = GoogleLLM(config["GOOGLE_LLM"]).get_llm()
