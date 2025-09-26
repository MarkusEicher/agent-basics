import os
from smolagents import CodeAgent, InferenceClientModel

# -- Phoenix OpenTelemetry Setup --
# According to the Hugging Face guide, we import and initialize Phoenix
# to trace the agent's execution.
from phoenix.otel import register
from openinference.instrumentation.smolagents import SmolagentsInstrumentor

# Register Phoenix as the OpenTelemetry endpoint
register()
# Instrument the smolagents library to automatically create traces
SmolagentsInstrumentor().instrument()
# -- End of Phoenix Setup --


# Ensure your Hugging Face token is set as an environment variable
HF_TOKEN = os.environ.get("HF_TOKEN")
if not HF_TOKEN:
    print("Warning: HF_TOKEN environment variable not set. The InferenceClientModel may fail.")

# Initialize a model (using Hugging Face Inference API)
# The model identifier has been updated to a known valid one.
model = InferenceClientModel("meta-llama/Meta-Llama-3-8B-Instruct")


# Create an agent with no tools
agent = CodeAgent(
    tools=[],
    model=model,
)

# Run the agent with a task
print("Running agent with Phoenix telemetry enabled...")
agent.run(
    "Could you give me the 118th number in the Fibonacci sequence?",
)

print("\n✅ Agent execution finished!")
print("Navigate to http://127.0.0.1:6006/ to inspect your run in Phoenix.")