from smolagents import MCPClient, CodeAgent, InferenceClientModel

model = InferenceClientModel("meta-llama/Llama-4-Scout-17B-16E-Instruct")

# Using the weather server with structured output
from mcp import StdioServerParameters

server_parameters = StdioServerParameters(
    command="python",
    args=["/home/markus/projects/agent-basics/src/hf-agents/smolagents-tools/weather-demo/weather.py"]
)

with MCPClient(server_parameters, structured_output=True) as tools:
    agent = CodeAgent(tools=tools, model=model)
    result = agent.run("What is the temperature in Tokyo in Fahrenheit?")
    print(result)