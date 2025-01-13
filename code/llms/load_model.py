"""
	load lm
"""

import os
os.environ["KERAS_BACKEND"] = "torch"
import setuptools.dist
import torch
import keras
import keras_hub

def load_model(model_name):
	"""
	initialise model
	:param model_name: string containing pretrained model name
	:return: model
	"""
	if torch.cuda.is_available():
		device = "cuda"
	else:
		device = "cpu"

	model = keras_hub.models.CausalLM.from_preset(model_name).to(device)

	return model