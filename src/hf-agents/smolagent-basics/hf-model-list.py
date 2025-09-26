from huggingface_hub import list_models

# Using the list_models function directly
# task = "text-classification"

# most_downloaded_model = next(iter(list_models(filter=task, sort="downloads", direction=-1)))
# print(most_downloaded_model.id)

# Using it as a custom tool with smolagents @tool decorator
from smolagents import tool

@tool
def model_download_tool(task: str) -> str:
    """
    This is a tool that returns the most downloaded model of a given task on the Hugging Face Hub.
    It returns the name of the checkpoint.

    Args:
        task: The task for which to get the download count.
    """
    most_downloaded_model = next(iter(list_models(filter=task, sort="downloads", direction=-1)))
    return most_downloaded_model.id

# Now using the tool with a smolagents agent
from smolagents import CodeAgent, TransformersModel, InferenceClientModel
# model = TransformersModel(model_id="meta-llama/Llama-3.2-3B-Instruct")
agent= CodeAgent(
    tools=[model_download_tool], 
    model=InferenceClientModel("meta-llama/Llama-4-Scout-17B-16E-Instruct"))
agent.run(
    "Can you give me the name of the most downloaded model for 'text-to-video'?"
)