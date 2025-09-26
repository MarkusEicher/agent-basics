# !pip install 'smolagents[toolkit]'
from smolagents import WebSearchTool

search_tool = WebSearchTool()
print(search_tool("Who's the current president of Russia?"))