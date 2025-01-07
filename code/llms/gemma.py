import os
os.environ["KERAS_BACKEND"] = "torch"  # Or "tensorflow" or "jax"!
import torch
import keras
import keras_hub
import numpy as np

gemma_lm = keras_hub.models.GemmaCausalLM.from_preset("gemma_7b_en")


gemma_lm.generate(prompt, max_length=max_length)

print(gemma_gen_response(gemma_lm, prompt="gemma"))