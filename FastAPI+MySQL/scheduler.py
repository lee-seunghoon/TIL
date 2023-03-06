"""
1. 매일 어제 데이터를 백엔드 서버로부터 받는다

2. 매월 1일 전월 데이터 전체를 불러와서 csv로 변환 후 GCS에 저장
"""
import os
import re
import json
import requests
from logger import logger
from pytz import timezone
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler


# Test
def get_ner_data():
    url = "http://127.0.0.1:8000/ner/get"
    res = requests.get(url, timeout=5)
    data = res.json()
    data_len = len(data)
    logger.info(f"총 데이터 개수 : {data_len}")
    return data
#######


def test_print_background():
    logger.info('test')


def insert_ner_data(datas):
    """
    수집항목 피드백 데이터 DB 추가 삽입
    """
    if datas:
        url = "http://127.0.0.1:8000/ner/create"
        headers={'Content-Type': 'application/json'}
        final_result=[]
        for data in datas:
            res = requests.post(url, data=json.dumps(data), headers=headers, timeout=5)
            result = res.json()
            final_result.append(result)
            print("result code : " + str(res.status_code))
            print(result)
        return final_result
    else:
        return datas


def insert_es_data(datas):
    """
    수집목적 피드백 데이터 DB 추가 삽입
    """
    if datas:
        url = "http://127.0.0.1:8000/es/create"
        headers={'Content-Type': 'application/json'}
        final_result=[]
        for data in datas:
            res = requests.post(url, data=json.dumps(data), headers=headers, timeout=5)
            result = res.json()
            final_result.append(result)
            print("result code : " + str(res.status_code))
            print(result)
        return final_result
    else:
        return datas


# 1. 매일 어제 데이터를 백엔드 서버로부터 받아서 DB에 저장한다.
def get_daily_nlp_data():
    # backend_url = "https://dev.catchsecu.com/api/nlp_data" #! backend 통신 url 수정 필요!
    # res = requests.get(backend_url, timeout=5)
    # datas = res.json()
    datas = {
            "NER": [
                {
                    "catchform_id": 111,
                    "catchform_question_id": 11,
                    "original_content": "test",
                    "analysis_response": "test",
                    "user_input_content": "test",
                    "register_date": "2023-02-19 15:49:53"
                }
            ],
            "ES": [
                {
                    "catchform_id": 112,
                    "original_content": "test",
                    "analysis_response": "test",
                    "final_result": "test",
                    "custom_purpose": "test",
                    "register_date": "2023-02-18 02:58:16"
                }
            ]
        }

    # NER insert
    ner_result = insert_ner_data(datas["NER"])
    ner_len = len(ner_result)
    logger.info(f"{ner_len}개 NER Data instert Success!! ")

    # ES insert
    es_result = insert_es_data(datas["ES"])
    es_len = len(es_result)
    logger.info(f"{es_len}개 ES Data instert Success!! ")


def convert_camel_to_snake(datas):
    if datas:
        for dict_data in datas:
            for key in dict_data.copy().keys():
                if key in dict_data.keys():
                    new_key = re.sub(r'(?<!^)(?=[A-Z])', '_', key).lower()
                    dict_data[new_key] = dict_data.pop(key)
        return datas
    else:
        return datas


def get_nlp_from_backend():
    backend_url = "https://staging.catchsecu.com/api/nlp/feedback"
    X_API_KEY = os.environ["X_API_KEY"]
    header = {"X-API-KEY": X_API_KEY}
    today = datetime.now(timezone('Asia/Seoul')).strftime("%Y-%m-%d")
    params = {'request_at': today}
    res = requests.get(backend_url, headers=header, params=params)
    datas = res.json()

    ner_datas = convert_camel_to_snake(datas["ner"])
    es_datas = convert_camel_to_snake(datas["es"])

    # NER insert
    ner_result = insert_ner_data(ner_datas)
    ner_len = len(ner_result)
    logger.info(f"{ner_len}개 NER Data instert Success!! ")

    # ES insert
    es_result = insert_es_data(es_datas)
    es_len = len(es_result)
    logger.info(f"{es_len}개 ES Data instert Success!! ")


# 2. 매월 1일 전월 데이터 전체를 불러와서 csv로 변환 후 GCS에 저장한다.


# Scheduler
def main_BlockingScheduler():
    sched = BlockingScheduler({'apscheduler.timezone': 'Asia/Seoul'})
    sched.add_job(get_daily_nlp_data, 'cron', month='1-12', day='20', hour='16', minute='50', id='test1')
    sched.start()


def main_BackgroundScheduler():
    sched = BackgroundScheduler(daemon=True, timezone='Asia/Seoul')
    sched.start()
    sched.add_job(get_daily_nlp_data, 'cron', month='1-12', day='20', hour='17', minute='37', id='back_test1')


def main_interval_back():
    sched = BackgroundScheduler({'apscheduler.timezone': 'Asia/Seoul'})
    sched.start()
    sched.add_job(test_print_background, 'interval', seconds=2, id='1')


if __name__ == "__main__" :
    get_nlp_from_backend()
