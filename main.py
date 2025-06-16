"""D&D Knowledge Navigator - Main server entry point."""

from fastmcp import FastMCP

from tools import register_tools

app: FastMCP = FastMCP("D&D 5e Knowledge Base")
register_tools(app)
app.run(transport="stdio")
