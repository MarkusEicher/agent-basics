from smolagents import MCPClient, CodeAgent, InferenceClientModel
from mcp import StdioServerParameters
import os

# Initialize a model (using Hugging Face Inference API)
model = InferenceClientModel("meta-llama/Llama-4-Scout-17B-16E-Instruct")

# Initialize server parameters
server_parameters = StdioServerParameters(
    command="uvx",
    args=["--quiet", "pubmedmcp@0.1.3"],
    env={"UV_PYTHON": "3.12", **os.environ},
)

# Manually manage the connection
try:
    mcp_client = MCPClient(server_parameters)
    tools = mcp_client.get_tools()

    # Use the tools with your agent
    agent = CodeAgent(tools=tools, model=model, add_base_tools=True)
    result = agent.run("What are the recent therapeutic approaches for Alzheimer's disease?")

    # Process the result as needed
    print(f"Agent response: {result}")
finally:
    # Always ensure the connection is properly closed
    mcp_client.disconnect()