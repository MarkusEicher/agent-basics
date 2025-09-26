import os
from smolagents import CodeAgent, LiteLLMModel, TransformersModel, InferenceClientModel 
from huggingface_hub import list_models

# HF_TOKEN = os.environ.get("HF_TOKEN")



# Initialize a model (using Hugging Face Inference API)
model = TransformersModel(model_id="meta-llama/Llama-3.2-3B-Instruct")

# model = LiteLLMModel(
#     model_id="ollama_chat/llama3:8b",
#     api_base="http://localhost:11434",
#     api_key="",
#     num_ctx=8192,
# )

# Define a custom final answer check function
def is_integer(final_answer: str, agent_memory=None) -> bool:
    """Return True if final_answer is an integer."""
    try:
        int(final_answer)
        return True
    except ValueError:
        return False

# Initialize agent with custom final answer check
agent = CodeAgent(
    tools=[],
    # model=InferenceClientModel("meta-llama/Llama-4-Scout-17B-16E-Instruct"),
    model=model,
    final_answer_checks=[is_integer]
)

agent.run("Calculate the least common multiple of 3 and 7")
print(agent.logs)