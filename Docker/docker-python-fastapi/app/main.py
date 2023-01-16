from typing import List
from fastapi import FastAPI, status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

##### Request body 정의 class #####
class ActionKeyword(BaseModel):
    keyword: str


class ExtractTotalLaw(BaseModel):
    lawSub: List[str]
    action: List[str]


class ExtractGuide(BaseModel):
    lawSub: List[str]
###################################

######### Default Setting #########
app=FastAPI()
dataload=DataLoad()
###################################

######### CORS Setting #########
# origins에는 protocal, domain, port만 등록한다.
origins = [
    # "http://192.168.0.13:3000", # url을 등록해도 되고
    "http://localhost:3000", # private 영역에서 사용한다면 *로 모든 접근을 허용할 수 있다.
    "http://localhost"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True, # cookie 포함 여부를 설정한다. 기본은 False
    allow_methods=["*"],    # 허용할 method를 설정할 수 있으며, 기본값은 'GET'이다.
    allow_headers=["*"],	# 허용할 http header 목록을 설정할 수 있으며 Content-Type, Accept, Accept-Language, Content-Language은 항상 허용된다.
)
###################################


#############Endpoint##############
@app.get("/healthcheck", status_code=status.HTTP_200_OK)
def health_check():
    """
    서버 상태 체크 및 인스턴스 구동 시작용
    response:\n
    {\n
        'healtcheck': 'Everything OK!'\n
    }
    """
    return {'healthcheck': 'Everything OK!'}


@app.get("/sub")
def get_law_sub():
    """
    전체 법령 주어 리스트를 반환
    """
    try:
        pass
    except Exception as e:
        return {"error":e}

@app.post("/keyword")
def select_action_from_keyword(search: ActionKeyword):
    """
    키워드 검색 로직을 통해 입력한 키워드와
    연관된 Action List 후보 5개 반환
    """
    try:
        pass
    except Exception as e:
        return {"error":e}

@app.post("/law")
def extract_law_from_sub_and_action_list(var: ExtractTotalLaw):
    """
    extract law
    """
    try:
        pass
    except Exception as e:
        return {"error":e}

@app.post("/post")
def extract_guide_url(var: ExtractGuide):
    """
    extract guide utl
    """
    try:    
        pass
    except Exception as e:
        return {"error":e}

