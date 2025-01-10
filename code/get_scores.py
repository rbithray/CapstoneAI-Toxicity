"""

"""
from perspective import get_score

def get_responses_scores(prompts, model, max_new_tokens=50):
	"""
	Get generated comment from model
	:param prompts: list of prompts
	:param model: model
	:param max_new_tokens:
	:return: dict of {prompt: (gennerated content, score)}
	"""
	results = {}

	for i, prompt in enumerate(prompts):
		print(f"Prompt {i + 1} of {len(prompts)}\n")
		print(f"> {prompt}\n")
		generated = model.generate(prompt, max_length=50)
		print(f"{generated}\n")
		score = get_score(generated)
		results[prompt] = (generated, score)

	return results