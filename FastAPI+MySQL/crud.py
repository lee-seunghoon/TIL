from datetime import date
from sqlalchemy.orm import Session
import models, schemas


def get_ner(db: Session, today = date.today().strftime("%Y-%m")):
    """
    NER 데이터 조회
    현재 년월(ex. 2023-02)을 필터링 기준으로 활용하여 전체 데이터 조회 
    """
    return db.query(models.NER).filter(models.NER.register_date.like(today+"%")).all()


def create_ner(db: Session, ner: schemas.NerCreate):
    """
    새로운 NER 피드백 데이터 DB 추가
    """
    db_ner = models.NER(
        catchform_id=ner.catchform_id,
        catchform_question_id=ner.catchform_question_id,
        original_content=ner.original_content,
        analysis_response=ner.analysis_response,
        user_input_content=ner.user_input_content,
        register_date=ner.register_date
    )
    db.add(db_ner)
    db.commit()
    db.refresh(db_ner)
    return db_ner


def get_es(db: Session, today = date.today().strftime("%Y-%m")):
    """
    ES 데이터 조회
    현재 년월(ex. 2023-02)을 필터링 기준으로 활용하여 전체 데이터 조회 
    """
    return db.query(models.ES).filter(models.ES.register_date.like(today+"%")).all()


def create_es(db: Session, es: schemas.ES):
    """
    새로운 ES 피드백 데이터 DB 추가
    """
    db_es= models.ES(
        catchform_id = es.catchform_id,
        original_content = es.original_content,
        analysis_response = es.analysis_response,
        final_result = es.final_result,
        custom_purpose = es.custom_purpose,
        register_date = es.register_date
    )
    db.add(db_es)
    db.commit()
    db.refresh(db_es)
    return db_es
