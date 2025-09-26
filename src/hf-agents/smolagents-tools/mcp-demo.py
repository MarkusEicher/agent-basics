from smolagents import MCPClient, CodeAgent, InferenceClientModel
from mcp import StdioServerParameters
import os

# Initialize a model (using Hugging Face Inference API)
model = InferenceClientModel("meta-llama/Llama-4-Scout-17B-16E-Instruct")

server_parameters = StdioServerParameters(
    command="uvx",  # Using uvx ensures dependencies are available
    args=["--quiet", "pubmedmcp@0.1.3"],
    env={"UV_PYTHON": "3.12", **os.environ},
)

with MCPClient(server_parameters, structured_output=True) as tools:
    agent = CodeAgent(tools=tools, model=model, add_base_tools=True)
    agent.run("Please find the latest research on COVID-19 treatment.")


# For Streamable HTTP-based MCP servers
# with MCPClient({"url": "http://127.0.0.1:8000/mcp", "transport": "streamable-http"}) as tools:
#     agent = CodeAgent(tools=tools, model=model, add_base_tools=True)
#     agent.run("Please find a remedy for hangover.")