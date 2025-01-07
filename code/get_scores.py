from llms.llama import llama
from llms.gemma import gemma
from llms.BLOOM import BLOOM
from llms.mistral import mistral
from perspective import get_score

def get_responses_scores(prompts, models, max_new_tokens=50):
	results = {}
	for model in models:
		lm =
		for prompt in prompts:

			# Generate text
			response = llm.generate(prompt)
			# Get toxicity score
			score = get_score(response, max_new_tokens)
			# Save result
			results[prompt][model] = {"response": response, "score": score}
		#
		# # Get responses
		# llama_response = get_llama(prompt, max_new_tokens)
		# gemma_response = get_gemma(prompt, max_new_tokens)
		# bloom_response = get_BLOOM(prompt, max_new_tokens)
		# mistral_response = get_mistral(prompt, max_new_tokens)
		#
		# # Get scores
		# llama_score = score(llama_response)
		# gemma_score = score(gemma_response)
		# bloom_score = score(bloom_response)
		# mistral_score = score(mistral_response)

		# append result
		# results[prompt] = {"llama": [llama_response, llama_score],
		#             "gemma": [gemma_response, gemma_score],
		#             "BLOOM": [bloom_response, bloom_score],
		#             "mistral": [mistral_response,mistral_score]}

	return results