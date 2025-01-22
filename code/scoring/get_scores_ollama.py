from perspective import get_score

def get_responses_scores(prompts, query_model, max_new_tokens=50, update_callback=None):
    """
    Get generated comments from the model with optional system prompt.
    :param prompts: list of task descriptions (user prompts)
    :param query_model: function to query the model
    :param max_new_tokens: maximum new tokens for generation
    :param update_callback: optional callback to update GUI with status
    :return: list of tuples [(prompt, generated content, score)]
    """
    results = []

    for i, prompt in enumerate(prompts):
        message = f"Processing Prompt {i + 1} of {len(prompts)}:\n> {prompt}\n"
        if update_callback:
            update_callback(message)

        # Query the model
        generated = query_model(prompt)

        # Remove the prompt from the generated content
        generated_content = generated[len(prompt):].strip()

        message = f"Generated Response:\n{generated_content}\n"
        if update_callback:
            update_callback(message)

        # Get the toxicity score for the generated content
        score = get_score(generated_content, "../secrets")
        message = f"Toxicity Score: {score}\n\n"
        if update_callback:
            update_callback(message)

        results.append((prompt, generated_content, score))

    return results
