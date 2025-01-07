"""
	Get toxicity-score from PerspectiveAPI
"""
from googleapiclient import discovery


def get_score(text):
	api_key = 'AIzaSyCjE67SsBOuJ6CIrGrhUtEtynezRnanNm0'

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
