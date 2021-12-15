import requests
import pandas as pd
from lright_textanalysis import *
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# DB 서버 url
BASE = 'http://127.0.0.1:5000/text/'

cnt = 1
df = pd.DataFrame(columns=['h_id','name','q_1','q_2','q_3','q_4',
    'q_5','label','cosine','rank'])

while True:
    try:
        res = requests.get(BASE+str(cnt)) # ==> api get 데이터 불러오기
        data = res.json()
        if data['h_id']:
            # ==> 불러온 json 데이터를 데이터프레임으로 변환
            new_df = pd.DataFrame().from_dict(data, orient='index').T
            # 전체 데이터 프레임은 만들기 위해 합치기
            df = pd.concat([df, new_df], axis=0)
            cnt += 1
    except: # id 값이 없을 경우 오류 나게끔 해서 무한 반복 중단
        print('id값이 없어서 중지')
        break

#analitics = Text_analysis(df)
# q1 처리
q1_data = df['q_1']
q1_data.index = df['h_id'].values
prepro_q1 = q1_data.map(prepro_text)

# q2 처리
q2_data = df['q_2']
q2_data.index = df['h_id'].values
prepro_q2 = q2_data.map(prepro_text)

# 불용어 사전
stop_words0 = ['하는', '생각', '업무', '있는', '하여', '회사', '합니다', '하게', '지원', '하다', '있다',
               '되다', '되어다', '싶다', '이다', '입사', '자다', '위해', '않다', '가지', '많다', '보다',
               '귀사', '관련', '같다', '느끼다', '아니다', '히든', '그레이스', '오래', '근무', '문제', '정도', '분야',
               '통해', '채용', '요소', '어떻다', '만약', '때문', '그렇다', '하지만', '좋다', '일이']
count_vec0 = CountVectorizer(
    stop_words=stop_words0,
    max_features=20,
    min_df=1
)

q1_word, q1_vec = count_analyze(prepro_q1, count_vec0)

q1_cosine_df,q2_cosine_df = cosine_extraction(count_vec0, prepro_q1, prepro_q2, q1_word, df['name'].values)

print(q1_cosine_df[43:47])
print()
print(q2_cosine_df[43:47])
print()
#print(q1_cosine_df['rank'].values)
#print()
#print(q2_cosine_df['rank'].values)


# 업데이트 시 사용
for num in q1_cosine_df['id'].values[43:47]:
    update = requests.patch(BASE+str(num), {'cosine':q1_cosine_df['코사인 유사도'][q1_cosine_df['id']==num].values[0], 'rank':q1_cosine_df['rank'][q1_cosine_df['id']==num].values[0]})
    for key in np.array(list(update.json().keys()))[[0,1,-2,-1]]: 
        print(str(key) + ' : ' + str(update.json()[key]))
    print()