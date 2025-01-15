"""
	load lm
"""

import os
os.environ["KERAS_BACKEND"] = "torch"
# os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

import keras_hub

def load_model(model_name):
    """
    Initialize model with optimizations for memory management.
    :param model_name: String containing pretrained model name
    :return: Optimized model
    """
    try:
        # Attempt to load the model with reduced precision and offloading
        model = keras_hub.models.CausalLM.from_preset(
            model_name,
            precision="int8",       # Use FP16 for lower memory usage
            device_map="auto",      # Auto map to GPU/CPU
            offload_folder="offload_cache"  # Offload to disk if needed
        )
    except Exception as e:
        raise RuntimeError(f"Failed to load model {model_name}: {e}")

    return model