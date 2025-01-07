from llms.llama import get_llama
from llms.gemma import get_gemma
from llms.BLOOM import get_BLOOM
from llms.mistral import get_mistral
from perspective import score

def get_responses_scores(prompts, model, max_new_tokens=50):
	results = {}
	for model in models:
		for prompt in prompts:
			llm = model["model"]
			name = model["name"]

			response = llm
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
		results[prompt] = {"llama": [llama_response, llama_score],
		            "gemma": [gemma_response, gemma_score],
		            "BLOOM": [bloom_response, bloom_score],
		            "mistral": [mistral_response,mistral_score]}

	return results