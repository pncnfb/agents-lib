from configparser import ConfigParser

# import langwatch

from llms.providers.anthropic import AnthropicLLM
from llms.providers.google import GoogleLLM

config = ConfigParser()
config.read("config.ini")

# langwatch.setup(api_key=config["LANGWATCH"]["api_key"])

LLM = AnthropicLLM(config["ANTHROPIC"])
# LLM = GoogleLLM(config["GOOGLE"])
