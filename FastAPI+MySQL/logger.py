"""
슬랙 메세지 발송
- NLP DB insert 성공 여부 정보
- NLP DB insert 데이터 개수
- NLP DB insert 시기
"""
import sys
import logging
from pytz import timezone
from datetime import datetime
from const import LOG_LEVEL, SLACK_WEBHOOK_URL
from slack_logger import SlackHandler, SlackFormatter


tz = timezone('Asia/Seoul')

# convert time zone method
def timetz(*args):
    return datetime.now(tz).timetuple
logging.Formatter.converter = timetz

# logging init
logging.basicConfig(
    format="[%(asctime)s] %(levelname)-8s in %(name)s: %(message)s",
    level=LOG_LEVEL,
    stream=sys.stdout,
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

# Add slack handler
slack_handler = SlackHandler(username="slack_logger",
                             icon_emoji=":alert_slow",
                             url=SLACK_WEBHOOK_URL)
slack_format = SlackFormatter()
slack_handler.setFormatter(slack_format)
logger.addHandler(slack_handler)