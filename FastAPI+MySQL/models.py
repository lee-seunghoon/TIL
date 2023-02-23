from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database_connent import Base


class NER(Base):
    """
    NER 테이블 모델
    """
    __tablename__ = "ner"
    id = Column(Integer, primary_key=True, index=True)
    catchform_id = Column(Integer, index=True)
    catchform_question_id = Column(Integer)
    original_content = Column(String)
    analysis_response = Column(String)
    user_input_content = Column(String)
    register_date = Column(String, index=True)

    #es_table = relationship("ES", back_populates="ner_table")


class ES(Base):
    """
    ES 테이블 모델
    """
    __tablename__ = "es"
    id = Column(Integer, primary_key=True, index=True)
    catchform_id = Column(Integer, index=True)
    original_content = Column(String)
    analysis_response = Column(String)
    final_result = Column(String)
    custom_purpose = Column(String)
    register_date = Column(String, index=True)
    
    # 이 기능을 사용하기 위해서는 ForeignKey setting 필요함
    # ner_table = relationship("NER", back_populates="es_table")

