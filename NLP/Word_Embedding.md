# Word Embedding

> - 자연어 단어들을 기계(컴퓨터)가 이해할 수 있는 숫자로 벡터화 시키는 행위
> - 워드 임베딩으로 잘 표현된 벡터들은 계산이 가능하고, 다양한 모델이 input  값으로 사용 가능



## Encoding(인코딩)

> - embedding 과 비슷한 과정을 의미한다.
> - 기계가 바로 이해할 수 없는 자연어들을 기계가 이해할 수 있는 숫자로 변환해주는 작업
> - 텍스트 인코딩에서는 주로, `정수 인코딩` 과 `원핫 인코딩`을 사용한다.



### 정수 Encoding

#### 1. dictionary를 이용한 정수 encoding

> - 직접 정수 encode 구현

```python
text = '작은 일도 무시하지 않고 최선을 다해야 한다. 작은 일에도 최선을 다하면 정성스럽게 된다.'

# 띄어쓰기를 기준으로 token 구성
tokens = [token for token in text.split(' ')]
# 중복 값 제거
unique_tokens = set(tokens)
# 다시 list로
unique_tokens = list(unique_tokens)

# token과 index key:value로 dictionary 만들기
tokens2idx = {token:idx for idx, token in enumerate(unique_tokens)}

# encoding
encode = [tokens2idx[token] for token in tokens]
encode # ==> [3, 8, 0, 9, 6, 7, 5, 3, 4, 6, 10, 1, 2]
```



#### 2. Keras 활용 정수 encoding

> - keras에서 텍스트 전처리를 위한 라이브러리 지원
> - 단어에 정수 레이블 부여
> - 자동으로 빈도 수가 높은 단어는 낮은 index값을 부여

```python
from tensorflow.keras.preprocessing.text import Tokenizer

text = '작은 일도 무시하지 않고 최선을 다해야 한다. 작은 일에도 최선을 다하면 정성스럽게 된다.'

tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])
print(tokenizer.word_index)
# ==> {'작은': 1, '최선을': 2, '일도': 3, '무시하지': 4, '않고': 5, '다해야': 6, '한다': 7, '일에도': 8, '다하면': 9, '정성스럽게': 10, '된다': 11}

encoding = tokenizer.texts_to_sequences([text])[0]
print(encoding)
# ==> [1, 3, 4, 5, 2, 6, 7, 1, 8, 2, 9, 10, 11]
```



