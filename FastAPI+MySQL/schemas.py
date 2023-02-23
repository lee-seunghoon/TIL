from typing import Union
from pydantic import BaseModel


class NER(BaseModel):
    id: int
    catchform_id: int
    catchform_question_id: int
    original_content: Union[str, None]
    analysis_response: Union[str, None]
    user_input_content: Union[str, None]
    register_date: str

    class Config:
        orm_mode = True


class NerCreate(BaseModel):
    catchform_id: int
    catchform_question_id: int
    original_content: Union[str, None]
    analysis_response: Union[str, None]
    user_input_content: Union[str, None]
    register_date: str

    class Config:
        orm_mode = True


class ES(BaseModel):
    id: int
    catchform_id: int
    original_content: Union[str, None]
    analysis_response: Union[str, None]
    final_result: Union[str, None]
    custom_purpose: Union[str, None]
    register_date: str

    class Config:
        orm_mode = True


class EsCreate(BaseModel):
    catchform_id: int
    original_content: Union[str, None]
    analysis_response: Union[str, None]
    final_result: Union[str, None]
    custom_purpose: Union[str, None]
    register_date: str

    class Config:
        orm_mode = True
