from abc import ABC, abstractmethod
from typing import Any
from pydantic import BaseModel

from llama_index.core.prompts import PromptTemplate
from llama_index.core.output_parsers import PydanticOutputParser
from llama_index.core.program import LLMTextCompletionProgram


class BaseLLM(ABC):
    def __init__(self, config: dict):
        self.config = config
        self.llm = self.get_llm()

    @abstractmethod
    def get_llm(self) -> Any:
        pass

    def evaluate(self, prompt: str, output_cls: type[BaseModel], **prompt_kwargs) -> BaseModel:

        program = LLMTextCompletionProgram.from_defaults(
            output_cls=output_cls,
            output_parser=PydanticOutputParser(output_cls=output_cls),
            prompt=PromptTemplate(template=prompt),
            llm=self.llm,
            verbose=True,
        )

        return program(**prompt_kwargs)
