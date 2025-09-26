from langchain.agents import load_tools
from smolagents import Tool, CodeAgent, InferenceClientModel, TransformersModel, LiteLLMModel



search_tool = Tool.from_langchain(load_tools(["serpapi"])[0])

model = InferenceClientModel(model_id="meta-llama/Llama-4-Scout-17B-16E-Instruct")

# model = LiteLLMModel(
#     model_id="ollama_chat/llama3:8b",
#     api_base="http://localhost:11434",
#     api_key="",
#     num_ctx=8192,
# )

agent = CodeAgent(tools=[search_tool], model=model)

agent.run("How many more blocks (also denoted as layers) are in BERT base encoder compared to the encoder from the architecture proposed in Attention is All You Need?")