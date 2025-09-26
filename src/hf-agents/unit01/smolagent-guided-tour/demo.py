import os
from smolagents import CodeAgent, TransformersModel # InferenceClientModel LiteLLMModel

# HF_TOKEN = os.environ.get("HF_TOKEN")

# Initialize a model (using Hugging Face Inference API)
model = TransformersModel(model_id="HuggingFaceTB/SmolLM-135M-Instruct")

# model = LiteLLMModel(
#     model_id="ollama_chat/gpt-oss:20b",
#     api_base="http://localhost:11434",
#     api_key="",
#     num_ctx=8192,
# )

# Create an agent with no tools
agent = CodeAgent(
    tools=[],
    model=model,
)

# Run the agent with a task
# result = agent.run("What is the current weather in Paris?")
# print(result)

agent.run(
    "Could you give me the 118th number in the Fibonacci sequence?",
)