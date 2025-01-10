import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# My Hugging Face token
HF_TOKEN = "my token"

# Loading the model
model = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mistral-7B-v0.1", 
    token=HF_TOKEN,
    device_map="auto",  # Automatically place model on available GPU(s) or CPU
    torch_dtype="auto",  # Adjust dtype for optimal performance (e.g., float16 on GPU)
)

tokenizer = AutoTokenizer.from_pretrained(
    "mistralai/Mistral-7B-v0.1", 
    token=HF_TOKEN
)

# Finishing a sentence
text = "Hello my name is"
inputs = tokenizer(text, return_tensors="pt")

outputs = model.generate(**inputs, max_new_tokens=20)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))

def generate_text(prompt, model, tokenizer, max_length=50):
    """Generate text from a prompt using the Mixtral model."""
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        inputs.input_ids,
        max_length=max_length,
        do_sample=True,  # Use sampling for creative text generation
        top_k=50,        # Limit to top-k sampling for diversity
        top_p=0.95,      # Use nucleus sampling for probabilistic responses
        temperature=0.7, # Adjust creativity; lower for deterministic, higher for varied responses
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
