import re
import json
import requests
import crud, schemas
from typing import List
from logger import logger
from database_connent import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from pytz import timezone


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


ner_router = APIRouter(
    prefix='/ner',
    tags=["ner"],
    # dependencies=[Depends(get_db)],
    # responses={404: {"description": "Not Found"}}
)

es_router = APIRouter(
    prefix="/es",
    tags=["es"],
)


schedule_router = APIRouter(
    prefix="/api",
    tags=["es"],
)


@ner_router.get("/get", response_model=List[schemas.NER])
def read_ner_data(db: Session = Depends(get_db)):
    data = crud.get_ner(db)     # ==> db.query 타입의 결과
    return data


@ner_router.post("/create", response_model=schemas.NER)
def insert_ner_data(ner: schemas.NerCreate, db: Session = Depends(get_db)):
    return crud.create_ner(db=db, ner=ner)


@es_router.get("/get", response_model=List[schemas.ES])
def read_es_data(db: Session = Depends(get_db)):
    data = crud.get_es(db)
    return data


@es_router.post("/create", response_model=schemas.ES)
def insert_es_data(es: schemas.EsCreate, db: Session = Depends(get_db)):
    return crud.create_es(db=db, es=es)


@schedule_router.get("/daily_insert")
def daily_feedback_to_db(db: Session = Depends(get_db)):
    # Get feedback data from BackEnd DB
    # backend_url = "http://test.com/api/nlp/feedback"
    # X_API_KEY = os.environ["X_API_KEY"]
    # header = {"X-API-KEY":X_API_KEY}
    # today = datetime.now(timezone('Asia/Seoul')).strftime("%Y-%m-%d")
    # params = {'request_at':today}
    # res = requests.get(backend_url, headers=header, params=params)
    # datas = res.json()

    datas = {
        'es': [
            {'catchformId': 1111,
             'originalContent': 'test',
             'analysisResponse': 'test',
             'finalResult': 'test',
             'customPurpose': 'test',
             'registerDate': '2023-02-21 14:39:17'}
        ],
        'ner': [
            {'catchformId': 3057,
             'catchformQuestionId': 2893,
             'originalContent': '전화번호',
             'analysisResponse': '{"originalText":"전화번호","analysisText":"[전화번호:NOR-B(97.2%)]","nlpAnalysisExtractDtos":[{"keyword":"전화번호","label":"NOR","probability":0.972}]}',
             'userInputContent': '{"personalInformationType":"IDENTIFICATION","userInputContent":"번호"}',
             'registerDate': '2023-02-21 14:39:32'}
        ]
    }

    ner_datas = json.dumps(convert_camel_to_snake(datas["ner"]))
    es_datas = json.dumps(convert_camel_to_snake(datas["es"]))

    # NER insert
    ner_results = []
    for ner_data in ner_datas:
        ner_result = crud.create_ner(db=db, ner=ner_data)
        ner_result.append(ner_results)
    ner_len = len(ner_results)
    logger.info(f"{ner_len}개 NER Data instert Success!! ")

    # ES insert
    es_results = []
    for es_data in es_datas:
        es_result = crud.create_es(db=db, es=es_data)
        es_results.append(es_result)
    es_len = len(es_results)
    logger.info(f"{es_len}개 ES Data instert Success!! ")

    result = {
        "NER": ner_results,
        "ES": es_results
    }

    return result
