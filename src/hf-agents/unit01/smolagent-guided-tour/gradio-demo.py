from smolagents import (
    load_tool,
    CodeAgent,
    InferenceClientModel,
    GradioUI
)

# Import tool from Hub
image_generation_tool = load_tool("m-ric/text-to-image", trust_remote_code=True)

model = InferenceClientModel(model_id="meta-llama/Llama-4-Scout-17B-16E-Instruct")

# Initialize the agent with the image generation tool
agent = CodeAgent(tools=[image_generation_tool], model=model)

GradioUI(agent).launch()