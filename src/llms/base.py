from abc import ABC, abstractmethod

class BaseLLM(ABC):
    def __init__(self, config: dict):
        self.config = config

    @abstractmethod
    def get_llm(self):
        pass
