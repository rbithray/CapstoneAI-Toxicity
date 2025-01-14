"""
	load lm
"""

import os
os.environ["KERAS_BACKEND"] = "torch"
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

import keras_hub

def load_model(model_name):
	"""
	Initialise model with optimisations to reduce memory usage.
	:param model_name: String containing pretrained model name
	:return: Optimized model
	"""

	try:
		# Use a smaller precision (FP16) for reduced memory usage
		model = keras_hub.models.CausalLM.from_preset(
			model_name,
			precision="int8"  # Change to "int8" if supported for even lower memory
		)
	except Exception as e:
		raise RuntimeError(f"Failed to load model {model_name}: {e}")

	return model