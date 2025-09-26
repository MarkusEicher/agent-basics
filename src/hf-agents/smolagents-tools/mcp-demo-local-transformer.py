from smolagents import MCPClient, CodeAgent, InferenceClientModel, TransformersModel, ChatMessage
from mcp import StdioServerParameters
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os

class LocalTransformersModel:
    def __init__(self, model_name: str):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.pad_token_id = self.tokenizer.eos_token_id

    def generate(self, messages: list[ChatMessage], **kwargs) -> ChatMessage:
        # Optional: nutze stop_sequences, max_tokens etc. aus kwargs
        stop_sequences = kwargs.get("stop_sequences", [])
        max_tokens = kwargs.get("max_tokens", 512)

        # Prompt zusammenbauen
        prompt = "\n".join([msg.content for msg in messages])

        inputs = self.tokenizer(prompt, return_tensors="pt", padding=True)
        input_ids = inputs["input_ids"]
        attention_mask = inputs["attention_mask"]

        # Generierung
        outputs = self.model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            pad_token_id=self.pad_token_id,
            max_new_tokens=max_tokens,
        )

        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Optional: rudimentäres Stop-Handling
        for stop in stop_sequences:
            if stop in response:
                response = response.split(stop)[0].strip()

        return ChatMessage(role="assistant", content=response)

# Initialize a model using the Huggingface InferenceClientModel
# model = InferenceClientModel("meta-llama/Meta-Llama-3-8B-Instruct")
# Initialize a model using the Transformers local inference interface
model = LocalTransformersModel("meta-llama/Llama-3.2-3B-Instruct")

server_parameters = StdioServerParameters(
    command="uvx",  # Using uvx ensures dependencies are available
    args=["--quiet", "pubmedmcp@0.1.3"],
    env={"UV_PYTHON": "3.12", **os.environ},
)

with MCPClient(server_parameters, structured_output=True) as tools:
    agent = CodeAgent(tools=tools, model=model, add_base_tools=True)
    agent.run("Please find the latest research on COVID-19 treatment.")