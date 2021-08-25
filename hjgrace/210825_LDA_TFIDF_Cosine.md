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
def topic_divide(new_df, vectorizer):
    feature_vec = vectorizer.fit_transform(new_df)
    lda =  LatentDirichletAllocation(n_components=4, random_state=0).fit(feature_vec)
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

