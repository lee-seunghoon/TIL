import os

from slack import WebClient
from slack.errors import SlackApiError

import logging
logging.basicConfig(level=logging.DEBUG)

slack_test_token = os.environ.get("SLACK_API_TOKEN", None)
print("Slack OAuth token :", slack_test_token)

client = WebClient(token=slack_test_token)

try:
	res=client.chat_postMessage(
		channel="ai-catchform-error",
		text="test"
	)
except SlackApiError as e:
	assert e.response["error"]
