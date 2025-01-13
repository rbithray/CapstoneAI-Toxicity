import os
os.environ["KERAS_BACKEND"] = "tensorflow"  # "torch", "tensorflow", or "jax"!
#import torch
import keras
import keras_hub

def init_gemma():
	"""
		initialise gemma lm
		:return: Gemma model object
	"""
	if torch.cuda.is_available():
		device = "cuda"
	else:
		device = "cpu"

	gemma_lm = keras_hub.models.GemmaCausalLM.from_preset("gemma2_2b_en").to(device)

	return gemma_lm

print("Gemma2 7b\n")

gemma_lm = init_gemma()

while True:
	prompt = input("> ")
	if prompt == "exit":
		break

	print("Gemma: " + gemma_lm.generate(prompt, max_length=100))


