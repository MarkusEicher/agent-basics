from smolagents import Tool, CodeAgent, InferenceClientModel



image_generation_tool = Tool.from_space(
    "black-forest-labs/FLUX.1-schnell",
    name="image_generator",
    description="Generate an image from a prompt"
)

# image_generation_tool("A sunny beach")

model = InferenceClientModel(model_id="meta-llama/Llama-4-Scout-17B-16E-Instruct")
agent = CodeAgent(tools=[image_generation_tool], model=model)

agent.run(
    "Improve this prompt, then generate an image of it.", additional_args={'user_prompt': 'A rabbit wearing a space suit'}
)