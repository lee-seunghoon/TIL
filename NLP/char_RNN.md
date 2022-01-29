# 라이브러리

```python
import numpy as np
import pandas as pd
import keras
from keras.preprocessing.text import Tokenizer
```



# 데이터 로드

> - sample로 셰익스피어 텍스트 활용(영어 text)
> - 한글 텍스트 데이터로 응용 활용

```python
sp_url = 'https://homl.info/shakespeare'
path = keras.utils.get_file('shakespeare.txt', sp_url)
with open(path) as f :
    shakespeare_text = f.read()
```



# 텍스트 정수 인코딩

```python
# 모든 텍스트 정수 인코딩
# keras의 토크나이저 사용
tokenizer = Tokenizer(char_level=True) # char_level=True ==> 단어 수준 인코딩 대신 글자 수준 인코딩 만든다
tokenizer.fit_on_texts(shakespeare_text)

# 이제 text 문장을  idx로 인코딩하거나
# Idx 값을 문자로 디코딩 할 수 있다
# 예시
print(tokenizer.texts_to_sequences(['Test'])) # ==> [[3, 2, 8, 3]]
print(tokenizer.sequences_to_texts([[3,2,8,3]])) # ==> ['t e s t']

# tokenizer가 담고 있는 고유한 글자 개수
char_len = len(tokenizer.word_index)
print(char_len) # ==> 39
# 전체 글자 개수
total_size = tokenizer.document_count
print(total_size) # ==> 1115394

# 전체 텍스트르 인코딩해서 각 글자를 idx로 변환
# 지금 tokenizer는 1부터 진행한다
# idx를 0부터 얻고자 1을 빼준다
# 문자열을 리스트에 넣어서 input 해준다
# 변수에 대괄호 씌워주면 차원이 한 차원 줄어든다
[encoding] = np.array(tokenizer.texts_to_sequences([shakespeare_text])) - 1
encoding
```

