"""
Slack Logger 라이브러리 활용하여 log message 발송
pip install slack-logger
"""
import os
import logging
from slack_logger import SlackHandler, SlackFormatter

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Slack Handler setting
sh = SlackHandler(username='logger',
                  icon_emoji=":robot_face",
                  url="https://hooks.slack.com/services/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")
sh.setLevel(logging.DEBUG)

f = SlackFormatter()
sh.setFormatter(f)
logger.addHandler(sh)

logger.debug("debug message")
logger.info("info message")
logger.warn("warning message")
logger.error("error message")
logger.critical("critical message")
