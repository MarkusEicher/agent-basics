from smolagents import CodeAgent, InferenceClientModel, WebSearchTool, TransformersModel

model = InferenceClientModel("meta-llama/Llama-4-Scout-17B-16E-Instruct")
# model = TransformersModel(model_id="meta-llama/Llama-3.2-3B-Instruct")

web_agent = CodeAgent(
    tools=[WebSearchTool()],
    model=model,
    name="web_search_agent",
    description="Runs web searches for you. Give it your query as an argument."
)

manager_agent = CodeAgent(
    tools=[], model=model, managed_agents=[web_agent]
)

manager_agent.run("Who is the CEO of Hugging Face?")