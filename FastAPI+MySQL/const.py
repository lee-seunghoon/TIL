import os
import logging

LOG_LEVEL = logging.INFO
SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL", None)