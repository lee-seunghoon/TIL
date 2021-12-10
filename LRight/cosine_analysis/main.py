# 라이브러리
import requests
import pandas as pd
from lright_textanalysis import *
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import schedule
import sys
import time
import datetime
from multiprocessing import Process, Queue
from threading import Thread
import json


# 잘못된 명령어 입력할 경우
class WrongAttributeException(Exception):
    pass


# 분석할 텍스트 데이터 불러오기
def load_data(BASE):
    # DB 데이터 로드 (REST API)
    # 자소서 문항 10가지 df 구성

    cnt = 1

    # 자소서 데이터 담을 df
    df = pd.DataFrame(columns=['id','name','q_1','q_2','q_3'])

    while True:
        try:
            get_data ={
                'userId':cnt,
                'include':[
                    'cosine'
                    ]
                }
            header = {'Content-Type': 'application/json'}
            # ==> api 데이터 post 방식으로 불러오기
            res = requests.post(BASE+'user', json.dumps(get_data), headers=header) 
            result = res.json()

            # db에서 api로 받아온 결과 필요한 데이만 추출
            userId = result['result']['user'][0]['userId']
            name = result['result']['user'][0]['lastName'] + result['result']['user'][0]['firstName']
            q_1 = result['result']['user'][0]['cosine']['questions'][0]['data']
            q_2 = result['result']['user'][0]['cosine']['questions'][1]['data']
            q_3 = result['result']['user'][0]['cosine']['questions'][2]['data']

            # 추출한 데이터로 새로운 데이터프레임 만들기
            cos_df = pd.DataFrame({
                'id' : [userId],
                'name' : [name],
                'q_1' : [q_1],
                'q_2' : [q_2],
                'q_3' : [q_3]
            })

            # 기존 데이터프레임과 합치기
            df = pd.concat([df, cos_df])

            cnt += 1
            
        except: # id 값이 없을 경우 오류 나게끔 해서 무한 반복 중단
            print('데이터 추출 완료')
            break
    
    return df


# 텍스트 전처리
def text_preprocess(df, text, queue):
    df[text] = df[text].map(prepro_text)
    queue.put(df[text])
    return df[text]


# 코사인 유사도 구하기
def extract_cosine(prepro_data):

    # 코사인 유사도 담을 df 구성
    cosine_df = prepro_data[['id', 'name']]

    # 불용어 사전
    stop_words = ['하는', '생각', '업무', '있는', '하여', '회사', '합니다', '하게', '지원', '하다', '있다',
                '되다', '되어다', '싶다', '이다', '입사', '자다', '위해', '않다', '가지', '많다', '보다',
                '귀사', '관련', '같다', '느끼다', '아니다', '히든', '그레이스', '오래', '근무', '문제', '정도', '분야',
                '통해', '채용', '요소', '어떻다', '만약', '때문', '그렇다', '하지만', '좋다', '일이']
    
    # 백터라이저
    count_vec = CountVectorizer(
        stop_words=stop_words,
        # max_features=20,
        min_df=2
    )

    # 각 문항별 코사인 유사도 구하기
    for q in prepro_data.columns[2:] :
        prepro_data[q].index = prepro_data['id']
        word, vec = count_analyze(prepro_data[q], count_vec)
        cos_df = cosine_extraction(count_vec, prepro_data[q], word)
        cosine_df = pd.merge(cosine_df, cos_df, on='id', how='left')

    # 코사인 유사도 평균 구하기
    cosine_df['mean'] = cosine_df.iloc[:,2:].mean(axis=1)

    # 랭킹순위 구하기
    cosine_df['rank'] = cosine_df['mean'].rank(ascending=False).astype(np.int64)

    # 랭킹순위 정렬
    cosine_df.sort_values(by='rank', axis=0, ascending=True, inplace=True)

    return cosine_df


# 데이터 업데이트
def server_update(cos_df, BASE):
    for i in cos_df['id'].values:
        cos_sim = float(cos_df['mean'][cos_df['id']==i].values[0])
        rank = int(cos_df['rank'][cos_df['id']==i].values[0])
        update_data =[{
            "userId": i,
            "cosine": cos_sim,
            "rank": rank
            }]
        header = {'Content-Type': 'application/json'}
        update_res = requests.put(BASE+'cosine/update', json.dumps(update_data), headers=header)
        # for key in np.array(list(update_res.json().keys()))[[0,1,-2,-1]]: 
        #     print(str(key) + ' : ' + str(update_res.json()[key]))
        print(update_res.status_code)

    # 실행 시각
    print(datetime.datetime.now())


def run(args):

    if args == 'jasosu':
        start = time.time()

        # DB 서버 url
        BASE = 'http://localhost:3100/api/v1/'
        # 데이터 불러오기
        df = load_data(BASE)

        q = Queue()
        
        # 텍스트 전처리
        # 쓰레드 병렬 처리
        for col in df.columns[2:]:
            thred = Process(target=text_preprocess, args=(df,col,q))    
            thred.start()
        
        for col in df.columns[2:]:
            df[col] = pd.Series(q.get())
            
        # 코사인 유사도 추출
        cosine = extract_cosine(df)

        # 서버 update
        server_update(cosine, BASE)

        end = time.time()
        print('\n총실행시간 :', round(end-start), '초')
    
    elif args == 'pyungpan':
        pass

    else: 
        raise WrongAttributeException(f"Not Listed option")


if __name__ == '__main__':

    # command 명령어에서 입력해준 파라미터 받기
    arg = sys.argv

    # schedule.do() 안에 함수와 함께 넣을 인자값 부여
    schedule.every().day.at('10:59').do(run, args=arg[1])

    while True:
        schedule.run_pending()
        time.sleep(1)    