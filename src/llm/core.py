from dataclasses import dataclass, asdict
from pydantic import BaseModel
from typing import List, Optional

from llama_index.core.prompts import PromptTemplate
from llama_index.core.output_parsers import PydanticOutputParser
from llama_index.core.program import LLMTextCompletionProgram
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import BaseTool


@dataclass
class LLMConfig:
    """Configuration for the LLM model."""

    model: str = "gpt-4o"
    api_key: Optional[str] = None
    temperature: float = 0
    project: Optional[str] = None
    location: Optional[str] = None
    base_url: Optional[str] = None
    max_tokens: Optional[int] = None

    @classmethod
    def from_dict(cls, config: dict) -> "LLMConfig":
        """Create LLMConfig from dictionary."""
        return cls(**config)

    def to_dict(self) -> dict:
        """Convert to dictionary, filtering None values."""
        config_dict = asdict(self)
        return {k: v for k, v in config_dict.items() if v is not None}

class CoreLLM:
    """CoreLLM class"""
    def __init__(self, llm_provider: type, config: LLMConfig, tools: Optional[List[BaseTool]] = None):
        self.config = config.to_dict()
        self.llm = llm_provider(**self.config)
        self.tools = tools or []
        self._agent = None

        if self.tools:
            self._agent = ReActAgent.from_tools(
                tools=self.tools, llm=self.llm, verbose=True, max_iterations=10
            )

    def evaluate(
        self, prompt: str, output_cls: type[BaseModel], **prompt_kwargs
    ) -> BaseModel:
        """Structured output method"""
        program = LLMTextCompletionProgram.from_defaults(
            output_cls=output_cls,
            output_parser=PydanticOutputParser(output_cls=output_cls),
            prompt=PromptTemplate(template=prompt),
            llm=self.llm,
            verbose=True,
        )
        return program(**prompt_kwargs)

    def chat(self, message: str) -> str:
        """Chat method that uses tools if available"""
        if self._agent:
            response = self._agent.chat(message)
            return str(response)
        else:
            # Fallback to simple completion
            response = self.llm.complete(message)
            return str(response)

    def add_tools(self, tools: List[BaseTool]):
        """Add tools and reinitialize agent"""
        self.tools.extend(tools)
        if self.tools:
            self._agent = ReActAgent.from_tools(
                tools=self.tools, llm=self.llm, verbose=True, max_iterations=10
            )

    def has_tools(self) -> bool:
        """Check if tools are available"""
        return len(self.tools) > 0
