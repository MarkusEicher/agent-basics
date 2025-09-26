from smolagents.local_python_executor import LocalPythonExecutor
from smolagents import CodeAgent, TransformersModel, InferenceClientModel, LiteLLMModel
import os


custom_executor = LocalPythonExecutor([])


HF_TOKEN = os.environ.get("HF_TOKEN")

# Initialize a model (using Hugging Face Inference API)
# model = InferenceClientModel("meta-llama/Llama-4-Scout-17B-16E-Instruct")

# Initialize a model using the Transformers local inference interface
# model = TransformersModel(model_id="meta-llama/Llama-3.2-3B-Instruct")


model = LiteLLMModel(
    model_id="ollama_chat/llama3:8b",
    api_base="http://localhost:11434",
    api_key="",
    num_ctx=8192,
)

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

# agent.run("Calculate the least common multiple of 3 and 7")

# Utilisty for pretty printing errors
def run_capture_exception(command: str):
    try:
        custom_executor(harmful_command)
    except Exception as e:
        print("ERROR:\n", e)

# Undefined command just do not work
# harmful_command="!echo Bad command"
# run_capture_exception(harmful_command)

# Imports like os will not be performed unless explicitly added to `additional_authorized_imports`
# harmful_command="import os; exit_code = os.system('echo Bad command')"
# run_capture_exception(harmful_command)

# harmful_command="import random; random._os.system('echo Bad command')"
# run_capture_exception(harmful_command)

harmful_command="""
while True:
    pass
"""
run_capture_exception(harmful_command)