from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "google/gemma-2b-it"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype=torch.float32
)

print("Model loaded successfully!")
prompt = "Explain smart farming in simple words."

inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=100)

print("\nAI Response:\n")
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
