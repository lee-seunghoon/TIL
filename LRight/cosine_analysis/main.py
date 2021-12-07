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


# 잘못된 명령어 입력할 경우
class WrongAttributeException(Exception):
    pass


# 분석할 텍스트 데이터 불러오기
def load_data(BASE):
    # DB 데이터 로드 (REST API)
    # 자소서 문항 10가지 df 구성

    cnt = 1

    # 자소서 데이터 담을 df
    df = pd.DataFrame(columns=['h_id','name','q_1','q_2','q_3','q_4',
        'q_5','label','cosine','rank'])

    while True:
        try:
            res = requests.get(BASE+str(cnt)) # ==> api get 데이터 불러오기
            data = res.json()
            if data['h_id']: # ==> id 값이 있는 경우
                # ==> 불러온 json 데이터를 데이터프레임으로 변환
                new_df = pd.DataFrame().from_dict(data, orient='index').T
                # 전체 데이터 프레임을 만들기 위해 합치기
                df = pd.concat([df, new_df], axis=0)
                cnt += 1
        except: # id 값이 없을 경우 오류 나게끔 해서 무한 반복 중단
            print('id값 모두 추출 완료')
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
    cosine_df = prepro_data[['h_id', 'name']]

    # 불용어 사전
    stop_words = ['하는', '생각', '업무', '있는', '하여', '회사', '합니다', '하게', '지원', '하다', '있다',
                '되다', '되어다', '싶다', '이다', '입사', '자다', '위해', '않다', '가지', '많다', '보다',
                '귀사', '관련', '같다', '느끼다', '아니다', '히든', '그레이스', '오래', '근무', '문제', '정도', '분야',
                '통해', '채용', '요소', '어떻다', '만약', '때문', '그렇다', '하지만', '좋다', '일이']
    # 백터라이저
    count_vec = CountVectorizer(
        stop_words=stop_words,
        max_features=20,
        min_df=1
    )


    # 각 문항별 코사인 유사도 구하기
    for q in prepro_data.columns[2:7] :
        prepro_data[q].index = prepro_data['h_id']
        word, vec = count_analyze(prepro_data[q], count_vec)
        cos_df = cosine_extraction(count_vec, prepro_data[q], word)
        cosine_df = pd.merge(cosine_df, cos_df, on='h_id', how='left')

    # 코사인 유사도 평균 구하기
    cosine_df['mean'] = cosine_df.iloc[:,2:].mean(axis=1)

    # 랭킹순위 구하기
    cosine_df['rank'] = cosine_df['mean'].rank(ascending=False).astype(np.int64)

    return cosine_df


# 데이터 업데이트
def server_update(cosine_df, BASE):
    for num in cosine_df['h_id'].values:
        update = requests.patch(BASE+str(num), {'cosine':cosine_df['mean'][cosine_df['h_id']==num].values[0], 'rank':cosine_df['rank'][cosine_df['h_id']==num].values[0]})
        for key in np.array(list(update.json().keys()))[[0,1,-2,-1]]: 
            print(str(key) + ' : ' + str(update.json()[key]))
        print()

    # 실행 시각
    print(datetime.datetime.now())


def run(args):

    if args == 'jasosu':
        start = time.time()

        # DB 서버 url
        BASE = 'http://127.0.0.1:5000/text/'
        # 데이터 불러오기
        df = load_data(BASE)

        q = Queue()
        
        # 텍스트 전처리
        # 쓰레드 병렬 처리
        for col in df.columns[2:7]:
            thred = Process(target=text_preprocess, args=(df,col,q))    
            thred.start()
        
        for col in df.columns[2:7]:
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
    schedule.every().day.at('14:58').do(run, arg[1])

    while True:
        schedule.run_pending()
        time.sleep(1)    