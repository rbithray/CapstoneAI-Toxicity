"""

"""
from perspective import get_score

def get_responses_scores(prompts, model, max_new_tokens=50, update_callback=None):
	"""
	Get generated comment from model.
	:param prompts: list of prompts
	:param model: model instance
	:param max_new_tokens: maximum new tokens for generation
	:param update_callback: optional callback to update GUI with status
	:return: list of tuples [(prompt, generated content, score)]
	"""
	results = []

	for i, prompt in enumerate(prompts):
		message = f"Processing Prompt {i + 1} of {len(prompts)}:\n> {prompt}\n"
		if update_callback:
			update_callback(message)

		generated = model.generate(prompt, max_length=max_new_tokens)
		message = f"Generated Response:\n{generated}\n"
		if update_callback:
			update_callback(message)

		score = get_score(generated, "../secrets")
		message = f"Toxicity Score: {score}\n\n"
		if update_callback:
			update_callback(message)

		results.append((prompt, generated, score))

	return results
