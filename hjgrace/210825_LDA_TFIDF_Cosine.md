## 라이브러리

```python
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from konlpy.tag import Okt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from matplotlib import font_manager, rc
import warnings
warnings.filterwarnings(action='ignore')

# LDA용 라이브러리
from sklearn.decomposition import LatentDirichletAllocation

# cosine_simmility
from sklearn.metrics.pairwise import linear_kernel
```



## 그래프 폰트 설정

```python
plt.rcParams['font.size'] = 20
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['figure.figsize'] = (16,18)
```



## 함수 모음



#### LDA 함수

```python
def topic_divide(new_df, vectorizer, lda):
    feature_vec = vectorizer.fit_transform(new_df)
    lda =  lda.fit(feature_vec)
    feature_names = vectorizer.get_feature_names()
    
    for idx, topic in enumerate(lda.components_):
        print('{}번째 토픽'.format(idx+1))
        topic_word_idx = (-topic).argsort()
        top20_idx = topic_word_idx[:10]

        if idx == 0:
            topic1 = [(feature_names[i], round(topic[i],2)) for i in top20_idx]
            print(topic1)
            topic1_word = []
            topic1_lda = []
            for word, num in topic1[::-1]:
                topic1_word.append(word)
                topic1_lda.append(num)

        elif idx==1:
            topic2 = [(feature_names[i], round(topic[i],2)) for i in top20_idx]
            print(topic2)
            topic2_word = []
            topic2_lda = []
            for word, num in topic2[::-1]:
                topic2_word.append(word)
                topic2_lda.append(num)

        elif idx==2:
            topic3 = [(feature_names[i], round(topic[i],2)) for i in top20_idx]
            print(topic3)
            topic3_word = []
            topic3_lda = []
            for word, num in topic3[::-1]:
                topic3_word.append(word)
                topic3_lda.append(num)

        elif idx==3:
            topic4 = [(feature_names[i], round(topic[i],2)) for i in top20_idx]
            print(topic4)
            topic4_word = []
            topic4_lda = []
            for word, num in topic4[::-1]:
                topic4_word.append(word)
                topic4_lda.append(num)

    return topic1_word, topic1_lda, topic2_word, topic2_lda, topic3_word, topic3_lda, topic4_word, topic4_lda
```



#### Tfidf & 코사인유사도

```python
def tfidf_cosine(topic_word, total_text, raw_df):
    total_word = ' '.join(topic_word[:-11:-1])
    tfidf = TfidfVectorizer(max_features=500, min_df=100, stop_words=stop_words)
    new_text = pd.Series(total_word)
    all_docs = total_text.append(new_text)
    tfidf_matrix = tfidf.fit_transform(all_docs)
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    cosin_num = []
    select_text = []
    for i in np.arange(-1,-7,-1):
        num = cosine_sim[-1][cosine_sim[-1][:-1].argsort()[i]]
        text = raw_df.iloc[cosine_sim[-1][:-1].argsort()[i]]
        cosin_num.append(num)
        select_text.append(text)

    new_df = pd.DataFrame({
        '대표 문장' :  select_text,
        '코사인 유사도': cosin_num
    })
    return  new_df
```



## LDA 생성

```python
# 토픽 수 : 4개
# 기본 학습 방법('online') 대신 조금 느리지만 성능이 더 좋은 'batch' 사용
# 모델 성능을 위해 max_iter 증가 (기본값==10)
# 참고로 max_iter는 최대 반복수라고 생각하면 됨. 중간에 알고리즘으로 값이 수렴할 경우 멈춤
lda = LatentDirichletAllocation(
    n_components = 4, 
    learning_method = 'batch',
    max_iter= 30
)
```

