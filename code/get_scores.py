import time

from perspective import get_score

def get_responses_scores(prompts, query_model, max_new_tokens=50, update_callback=None, max_retries=3):
    """
    Get generated comments from the model with optional system prompt.
    :param prompts: list of task descriptions (user prompts)
    :param query_model: function to query the model
    :param max_new_tokens: maximum new tokens for generation
    :param update_callback: optional callback to update GUI with status
    :param max_retries: maximum retries for generating a non-empty response
    :return: list of tuples [(prompt, generated content, score)]
    """
    results = []

    for i, prompt in enumerate(prompts):
        message = f"Processing Prompt {i + 1} of {len(prompts)}:\n> {prompt}\n"
        if update_callback:
            update_callback(message)

        retries = 0
        generated_content = None

        # Retry mechanism for non-empty response
        while retries < max_retries:
            generated = query_model(prompt)

            # Remove the prompt from the generated content
            generated_content = generated[len(prompt):].strip()

            if generated_content:  # Check if response is non-empty
                break

            retries += 1
            if update_callback:
                update_callback(f"Empty response generated. Retrying... ({retries}/{max_retries})")

        if not generated_content:  # Skip the prompt if no valid response is generated
            message = f"Skipping Prompt {i + 1} due to repeated empty responses.\n"
            if update_callback:
                update_callback(message)
            results.append((prompt, None, None))  # Append with None values for response and score
            continue

        message = f"Generated Response:\n{generated_content}\n"
        if update_callback:
            update_callback(message)

        try:
            # Get the toxicity score for the generated content
            score = get_score(generated_content, "../secrets")
            message = f"Toxicity Score: {score}\n\n"
            if update_callback:
                update_callback(message)
            results.append((prompt, generated_content, score))
        except Exception as e:
            message = f"Error calculating toxicity score for Prompt {i + 1}:\n Retrying...\n"
            if update_callback:
                update_callback(message)
            try:
                time.sleep(2)
                score = get_score(generated_content, "../secrets")
                message = f"Toxicity Score: {score}\n\n"
                if update_callback:
                    update_callback(message)
                results.append((prompt, generated_content, score))

            except Exception as e:
                message = f"Error calculating toxicity score for Prompt {i + 1}: {e}\n Retrying...\n"
                if update_callback:
                    update_callback(message)
                results.append((prompt, generated_content, None))  # Append with None for the score in case of error

    return results
