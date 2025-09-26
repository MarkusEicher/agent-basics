import os
from huggingface_hub import InferenceClient

HF_TOKEN = os.environ.get("HF_TOKEN")

client = InferenceClient(model="meta-llama/Llama-4-Scout-17B-16E-Instruct")



output = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "The capital of France is"},
    ],
    stream=False,
    max_tokens=1024,
)
print(output.choices[0].message.content)