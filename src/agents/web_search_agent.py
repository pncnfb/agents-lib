from typing import List
import requests
from bs4 import BeautifulSoup
from llama_index.tools.duckduckgo import DuckDuckGoSearchToolSpec
from models.web_search import SingleSourceRes, WebResponseAugmented

class WebSearchAgent:
    """
    WebSearchAgent Class
    """
    def __init__(self, llm: any):
        self.llm = llm
        self.prompt_template = (
            "You are a web assistant. Based on the following information from web search, "
            "provide a bullet-point summary of the most relevant facts and insights about the user's query.\n\n"
            "User Query: {query}\n\n"
            "Scraped Info:\n{scraped_info}\n\n"
            "Respond with only bullet points. No extra explanation, no questions."
        )

        self.search_tool = DuckDuckGoSearchToolSpec()

    def query(self, query_text: str) -> WebResponseAugmented:
        search_results = self.search_tool.duckduckgo_full_search(query=query_text)

        references: List[SingleSourceRes] = []
        scraped_info_parts = []

        for result in search_results:
            title = result.get("title", "No title")
            href = result.get("href")
            if not href:
                continue
            page_text = self.scrape_page_text(href)
            references.append(SingleSourceRes(text=page_text[:300] + "...", link=href))
            scraped_info_parts.append(f"### {title}\n{page_text}")

        scraped_info = "\n\n".join(scraped_info_parts)

        return self.llm.evaluate(
            prompt=self.prompt_template,
            output_cls=WebResponseAugmented,
            query=query_text,
            scraped_info=scraped_info
        )
        #return WebResponseAugmented(response=response_text, references=references)

    def scrape_page_text(self, url: str, max_chars: int = 1000) -> str:
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")

            texts = soup.stripped_strings
            page_text = " ".join(texts)

            return page_text[:max_chars] + "..." if len(page_text) > max_chars else page_text
        except Exception as e:
            return f"[Error loading {url}: {e}]"
