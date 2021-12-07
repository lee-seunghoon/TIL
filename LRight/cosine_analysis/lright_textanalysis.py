# 사용 라이브러리
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from konlpy.tag import Okt
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# matplotlib 그래프 속성 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['figure.figsize'] = (12,16)
plt.rcParams['font.size'] = 20
# 그래프 그릴 때 마이너스(-) 부분도 표시해주기 (로그오즈비 표현을 위해 세팅)
plt.rcParams['axes.unicode_minus'] = False

# class Text_analysis:

#     # 초기화
#     def __init__(self, df):
#         self.df = df
#         pass

# 텍스트 전처리
def prepro_text(raw_data):

    # 특수기호, 영어, 숫자 제거
    prepro_texts = re.sub(r'[^가-힣]',' ',str(raw_data))
    # 형태소 분석기 생성
    okt = Okt()
    # 조사와 복수표현 등 필요없는 품사 tag 제거
    prepro_word = []
    for word, tag in okt.pos(prepro_texts):
        if tag not in ['Josa', 'Suffix']:
            prepro_word.append(word)
    # 어간 추출 적용
    # result = ' '.join(okt.morphs(' '.join(prepro_word), stem=True))

    # 어간 추출 X
    result = ' '.join(prepro_word)

    return result


# 빈도분석 후 결과 출력
def count_analyze(texts, count_vec, color='tab:blue', title='default'):
    
    count_vec.fit(texts)
    
    word_dict = sorted(count_vec.vocabulary_.items())
    idx2word = {idx:word for word, idx in word_dict}

    total_text = []
    total_text.append(' '.join(texts.values))

    count_matrix = count_vec.transform(total_text)

    count_word = []
    count_vector = []

    for i in range(10,0,-1):
        count_word.append(idx2word[(-count_matrix.toarray()[0]).argsort()[i-1]])
        count_vector.append(count_matrix.toarray()[0][(-count_matrix.toarray()[0]).argsort()[i-1]])

    # print(count_word)
    # print(count_vector)

    # plt.barh(count_word, count_vector, color=color)
    # plt.yticks(count_word)
    # plt.title(f'{title} 빈도 분석')
    # plt.show()

    return count_word, count_vector


# TF-IDF 생성 함수
def tfidf_analyze(fit_data, analysis_data, vec, color, title):
    vec.fit(fit_data)

    word_dict = sorted(vec.vocabulary_.items())
    idx2word = {idx:word for word, idx in word_dict}

    total_text = []
    total_text.append(' '.join(analysis_data.values))

    matrix = vec.transform(total_text)

    word = []
    vector = []
    if len(matrix.toarray()[0]) >= 5:
        for i in range(5,0,-1):
            word.append(idx2word[matrix.toarray()[0].argsort()[-i]])
            vector.append(matrix.toarray()[0][matrix.toarray()[0].argsort()[-i]])
    else:
        for i in range(len(matrix.toarray()[0]),0,-1):
            word.append(idx2word[matrix.toarray()[0].argsort()[-i]])
            vector.append(matrix.toarray()[0][matrix.toarray()[0].argsort()[-i]])

    print(word)
    print(vector)
    
    #plt.figure(figsize=(12,16))
    plt.barh(word, vector, color=color)
    plt.yticks(word)
    plt.title(f'{title} TF-IDF')
    plt.show()

    return word, vector


# 코사인 유사도 score 추출
def cosine_extraction(vec, fit_data, count_words):

    # label1인 데이터로 적합
    vec.fit(fit_data)

    # 빈도분석으로 뽑은 Top10 단어들 하나의 text로
    top10_word_vec = vec.transform([' '.join(count_words)])

    # 데이터 백터 변환
    fit_data_vec = vec.transform(fit_data)

    fit_data_cosine_sim = cosine_similarity(top10_word_vec, fit_data_vec)

    # label0_data_name = []
    # label1_data_name = []
    # for idx0 in new_data.index.values:
    #     label0_data_name.append(df['성명'][df['index']==idx0].values[0])

    # for idx1  in fit_data.index.values:
    #     label1_data_name.append(df['성명'][df['index']==idx1].values[0])

    cos_sim = 'cos' + str(fit_data.name[1:])

    fit_cosine_df = pd.DataFrame({
        'h_id' : fit_data.index.values,
        cos_sim : fit_data_cosine_sim[0]
    })
    #fit_cosine_df['코사인 유사도'] = fit_cosine_df['코사인 유사도'].map(lambda x: round(x,3))
    #fit_cosine_df['rank'] = fit_cosine_df['코사인 유사도'].rank(ascending=False).astype(np.int64)

    return fit_cosine_df