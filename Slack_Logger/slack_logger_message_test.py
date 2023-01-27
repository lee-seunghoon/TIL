"""
Slack Logger 라이브러리 활용하여 log message 발송
pip install slack-logger
"""
import os
import logging
from slack_logger import SlackHandler, SlackFormatter
from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

"""
uwsgi 활용하여 배포할 경우 환경변수는 wsgi.ini 파일에 아래와 같이 정의 돼 있어야 한다.
[uwsgi]
...
env=SLACK_WEBHOOK_URL=https://hooks.slack.com/services/T04...
env=FLASK_ENV=dev
"""
# 위에서 정의된 변수를 아래와 같이 불러와야 한다.
SLACK_WEBHOOK_URL = os.environ["SLACK_WEBHOOK_URL"]
FLASK_ENV = os.environ["FLASK_ENV"]

# log level setting
if FLASK_ENV.lower() == "dev":
    LOG_LEVEL = logging.DEBUG
elif FLASK_ENV.lower() == "prod":
    LOG_LEVEL = logging.INFO

logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
        datefmt='%m/%d/%Y %H:%M:%S',
        level=LOG_LEVEL
    )

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Slack Handler setting
sh = SlackHandler(username='logger',
                  icon_emoji=":alert",
                  url=SLACK_WEBHOOK_URL)
sh.setLevel(logging.DEBUG)

f = SlackFormatter()
sh.setFormatter(f)
logger.addHandler(sh)

# flask error handler setting
# 4XX or 50X error 발생 시 작동
@app.errorhandler(HTTPException)
def error_handling_500(error):
    result = {
                "error_code" : error.code,
                "description" : error.description,
                "message" : str(error)
            }
    logger.error(str(result))
    return jsonify(result)

logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")
