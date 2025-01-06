import torch
from transformers import BloomTokenizerFast, BloomForCausalLM

def generate_text_with_bloom(prompt: str, max_new_tokens: int = 50) -> str:
    """
    Generates text using the BLOOM model, completing the given prompt.
    """
    model_name = "bigscience/bloom-3b"  # (smaller than the full 176B model)
    print(f"Loading model: {model_name}")
    
    tokenizer = BloomTokenizerFast.from_pretrained(model_name)
    model = BloomForCausalLM.from_pretrained(model_name)
    
    # If you have a GPU, uncomment:
    # model.to("cuda")
    
    # Tokenize the prompt
    inputs = tokenizer(prompt, return_tensors="pt")
    # If GPU is available:
    # inputs = {k: v.to("cuda") for k, v in inputs.items()}

    # Generate text
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            top_k=50,
            temperature=0.7
        )
    
    # Decode to a string
    completed_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return completed_text

if __name__ == "__main__":
    # Example prompt
    prompt = "The sky was a deep shade of"
    
    # Generate and print completion
    generated_text = generate_text_with_bloom(prompt)
    print("\n=== Generated Completion ===")
    print(generated_text)
