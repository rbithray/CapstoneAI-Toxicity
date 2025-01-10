"""
	Get toxicity-score from PerspectiveAPI
"""
from googleapiclient import discovery
import json

def get_score(text, token_file):
	"""
		Use PerspectiveAPI to get toxicity-score
		:param text: Content to be analysed
		:param token_file: Token file
		:return: PerspectiveAPI toxicity-score
	"""

	with open("secrets") as f:
		api_key = list(json.load(f)["PerspectiveAPI"].values())[0]

	client = discovery.build(
		"commentanalyzer",
		"v1alpha1",
		developerKey=api_key,
		discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
		static_discovery=False,
	)

	analyze_request = {
		'comment': {'text': text},
		'requestedAttributes': {'TOXICITY': {}}
	}
	score = client.comments().analyze(body=analyze_request).execute()["attributeScores"]['TOXICITY']["summaryScore"][
	"value"]

	return score
