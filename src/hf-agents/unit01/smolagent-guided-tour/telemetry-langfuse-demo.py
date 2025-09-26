import os
from smolagents import CodeAgent, InferenceClientModel

# -- Langfuse OpenTelemetry Setup --
# According to the Hugging Face guide, we set up environment variables
# for Langfuse and then instrument smolagents.

# IMPORTANT: Replace these with your self-hosted Langfuse details.
# For self-hosted instances, the public and secret keys might not be required
# depending on your setup, but the LANGFUSE_HOST is essential.
os.environ["LANGFUSE_PUBLIC_KEY"] = os.environ.get("LANGFUSE_PUBLIC_KEY", "pk-lf-...")
os.environ["LANGFUSE_SECRET_KEY"] = os.environ.get("LANGFUSE_SECRET_KEY", "sk-lf-...")
# Point this to your local docker instance, default is http://localhost:3000
os.environ["LANGFUSE_HOST"] = os.environ.get("LANGFUSE_HOST", "http://localhost:3000")

# Instrument the smolagents library to automatically create traces
from openinference.instrumentation.smolagents import SmolagentsInstrumentor
SmolagentsInstrumentor().instrument()

# Optional: Verify connection with Langfuse server
from langfuse import get_client
langfuse = get_client()
if langfuse.auth_check():
    print("✅ Langfuse client is authenticated and ready!")
else:
    print("⚠️ Authentication failed. Please check your Langfuse credentials and host.")
# -- End of Langfuse Setup --


# Ensure your Hugging Face token is set as an environment variable
HF_TOKEN = os.environ.get("HF_TOKEN")
if not HF_TOKEN:
    print("Warning: HF_TOKEN environment variable not set. The InferenceClientModel may fail.")

# Initialize a model (using Hugging Face Inference API)
model = InferenceClientModel("meta-llama/Meta-Llama-3-8B-Instruct")


# Create an agent with no tools
agent = CodeAgent(
    tools=[],
    model=model,
)

# Run the agent with a task
print("\nRunning agent with Langfuse telemetry enabled...")
agent.run(
    "Could you give me the 118th number in the Fibonacci sequence?",
)

print("\n✅ Agent execution finished!")
print(f"Navigate to {os.environ['LANGFUSE_HOST']} to inspect your run in Langfuse.")