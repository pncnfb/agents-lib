import json
import toml

#import langwatch
#langwatch.setup(api_key=config["langwatch"]["api_key"])

CONFIG = toml.load("config.toml")

with open(file="mcp_servers_config.json", mode="r", encoding="utf-8") as f:
    MCP_SERVERS = json.load(f)["mcpServers"]

