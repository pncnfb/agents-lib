from llama_index.tools.duckduckgo import DuckDuckGoSearchToolSpec

class WeatherAgent:
    def __init__(self, llm: any):
        self.llm = llm
        self.prompt_template =  """ You are a weather assistant. Help the user understand the weather in the city they asked about.\n"
                                    User Query: {query}\n
                                    Search Results:\n{search_results}\n\n
                                    Summarize the weather conditions in a clear and friendly way.
                                    Only answer with no follow up questions
                                """

        self.search_tool = DuckDuckGoSearchToolSpec()

    def query(self, query_text: str) -> str:
        search_results = self.search_tool.duckduckgo_full_search(query=query_text)

        prompt = self.prompt_template.format(
            query=query_text,
            search_results=search_results
        )

        response = self.llm.complete(prompt)

        return response
