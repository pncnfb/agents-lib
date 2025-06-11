import asyncio
from llama_index.llms.anthropic import Anthropic

# from llama_index.llms.google_genai import GoogleGenAI
from llama_index.tools.mcp import BasicMCPClient, McpToolSpec
from globals import CONFIG

from llm.core import LLMConfig
from agents import DatabaseAgent


async def setup_mcp_tools():
    """Setup MCP tools"""
    local_client = BasicMCPClient(
        command_or_url="uvx",
        args=["postgres-mcp"],
        env={
            "DATABASE_URI": f"postgres://{CONFIG["db"]["usr"]}:{CONFIG["db"]["psw"]}@{CONFIG["db"]["host"]}/{CONFIG["db"]["db_name"]}"
        },
    )

    mcp_tool = McpToolSpec(client=local_client)
    tools = await mcp_tool.to_tool_list_async()
    return tools


async def main():

    print("Database Agent with MCP Tools")
    tools = await setup_mcp_tools()

    db_agent = DatabaseAgent(
        llm_provider=Anthropic,
        config=LLMConfig.from_dict(CONFIG["anthropic"]),
        tools=tools,
    )

    print("Getting schemas:")
    schemas = db_agent("Give me the name of all schemas")
    print(f"{schemas}\n")

    print("Getting tables:")
    tables = db_agent("Give me the name of all tables in schema 'public'")
    print(f"{tables}\n")

    print("Query data:")
    tables = db_agent("Give me the number of films per release year in netflix titles table")
    print(f"{tables}\n")


if __name__ == "__main__":
    asyncio.run(main())
