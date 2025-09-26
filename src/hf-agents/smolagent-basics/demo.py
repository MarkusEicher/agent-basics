import os
from smolagents import CodeAgent, TransformersModel, InferenceClientModel, LiteLLMModel

HF_TOKEN = os.environ.get("HF_TOKEN")

# Initialize a model (using Hugging Face Inference API)
model = InferenceClientModel("meta-llama/Llama-4-Scout-17B-16E-Instruct")

# Initialize a model using the Transformers local inference interface
# model = TransformersModel(model_id="meta-llama/Llama-3.2-3B-Instruct")

# model = LiteLLMModel(
#     model_id="ollama_chat/llama3:8b",
#     api_base="http://localhost:11434",
#     api_key="",
#     num_ctx=8192,
# )

# Create an agent with no tools
agent = CodeAgent(
    tools=[],
    model=model,
    # additional_authorized_imports="sympy",
    # instructions="At each step, you should write everything out to a file called stepthoughts.txt. Create the file if it does not exist."
)

# Run the agent with a task

# result = agent.run("What is the current weather in Paris?")
# print(result)

agent.run(
    "Could you give me the 118th number in the Fibonacci sequence?",
)

# print(agent.prompt_templates["system_prompt"])