from smolagents import CodeAgent, TransformersModel, InferenceClientModel, LiteLLMModel
import os

HF_TOKEN = os.environ.get("HF_TOKEN")

# Initialize a model (using Hugging Face Inference API)
# model = InferenceClientModel("meta-llama/Llama-4-Scout-17B-16E-Instruct")

# Initialize a model using the Transformers local inference interface
model = TransformersModel(model_id="meta-llama/Llama-3.2-3B-Instruct")


# model = LiteLLMModel(
#     model_id="ollama_chat/llama3:8b",
#     api_base="http://localhost:11434",
#     api_key="",
#     num_ctx=8192,
# )

with CodeAgent(model=model, tools=[], executor_type="docker") as agent:
    agent.run("Can you give me the 100th Fibonacci number?") 