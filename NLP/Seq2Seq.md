# Sequence 2 Sequence 모델



## 데이터

> - KorQuAD_v1.0
>   - Training 질의응답쌍 60,407개
>   - Test 질의 응답쌍 5,774개
> - 어르신 대화 데이터
>   - AI_hub 일상 대화 데이터 + 웰니스 건강 대화 데이터

---



> - KorQuAD_v1.0 데이터

```python
import json
import pandas as pd

# 데이터 불러오기
with open('/content/drive/MyDrive/Colab Notebooks/TF-IDF_Test/KorQuAD_v1.0_train.json', 'r', encoding='utf8') as f :
    contents = f.read() # string type
    json_data = json.loads(contents)

# 질문, 응답 쌍 데이터프레임 만들기
question = []
answer = []
for i in range(1420):
    first =  len(json_data['data'][i]['paragraphs'])
    for j in range(first):
        second = len(json_data['data'][i]['paragraphs'][j]['qas'])
        for k in range(second):
            q = json_data['data'][i]['paragraphs'][j]['qas'][k]['question']
            a = json_data['data'][i]['paragraphs'][j]['qas'][k]['answers'][0]['text']
            question.append(q)
            answer.append(a)
            
df = pd.DataFrame({
    'question' : question,
    'answer' : answer
})

df      
```

![image-20210615204631981](md-images/image-20210615204631981.png)



> - 어르신 대화 데이터

```python
chat_data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/TF-IDF_Test/new_chat_data.csv', encoding='utf8')
chat_data
```

![image-20210615210601967](md-images/image-20210615210601967.png)



> - KorQuAD_v1.0 데이터 + 어르신 대화 데이터

```python
new_data = pd.concat([df, chat_data], ignore_index=True)
new_data
```

![image-20210615210932429](md-images/image-20210615210932429.png)



## 데이터 전처리

```python
# 라이브러리
import os
import re
import json
import numpy as np
import pandas as pd
from tqdm import tqdm
from konlpy.tag import Okt

# 설정
FILTERS = "([~.,!?\"';:)(])"
PAD = '<PAD>'   # ==> 어떤 의미도 없는 패딩 토큰
STD = '<SOS>'   # ==> 시작 토큰을 의미
END = '<END>'   # ==> 종료 토큰을 의미
UNK = '<UNK>'   # ==> 사전에 없는 단어 의미

PAD_INDEX = 0
STD_INDEX = 1
END_INDEX = 2
UNK_INDEX = 3

MARKER =[PAD, STD, END, UNK]
CHANGE_FILTER =re.compile(FILTERS)

MAX_SEQUENCE =35  # 우리 모델에서 사용할 문장 최대 길이
```



> - 데이터 불러오기

```python
def load_data(path):
    data_df = pd.read_csv(path, header=0)
    question, answer = list(data_df['question']), list(data_df['answer'])
    return question, answer
```



> - 단어 전처리

```python
def data_tokenizer(data):
    words = []
    for s in data :
        sentence = re.sub(CHANGE_FILTER, "", s)
        for word in sentence.split():
            words.append(word)
    return [word for word in words if word]
```



> - 한글 텍스트 형태소 단위 토크나이징

```python
def prepro_morphlized(data):
    morph_analyzer = Okt()
    result_data = []
    for seq in tqdm(data):
        morphlized_seq = " ".join(morph_analyzer.morphs(seq.replace(' ', '')), stem=True)
        result_data.append(morphlized_seq)

    return result_data
```



> - 단어 사전 만들기

```python
def load_vocab(path, vocab_path, tokenize_as_morph=False):
    vocab_list = []
	
    # 단어 사전 저장할 폴더 없을 경우
    if not os.path.exists(vocab_path):
        if (os.path.exists(path)):
            data_df = pd.read_csv(path, encoding='utf-8')
            question, answer = list(data_df['question']), list(data_df['answer'])

            if tokenize_as_morph :
                question = prepro_morphlized(question)
                answer = prepro_morphlized(answer)

            data = []
            data.extend(question)
            data.extend(answer)

            words = data_tokenizer(data)
            words = list(set(words))
            words[:0] = MARKER

        with open(vocab_path, 'w', encoding='utf-8') as vocab_file:
            for word in words:
                vocab_file.write(word + '\n')

    with open(vocab_path, 'r', encoding='utf-8') as vocab_file:
        for line in vocab_file:
            vocab_list.append(line.strip())  # ==> strip() : 양쪽 공백 모두 삭제

    word2idx, idx2word = make_vocab(vocab_list)

    return word2idx, idx2word, len(word2idx)

def make_vocab(vocab_list):
    # key : 단어 , value : 인덱스 ==> 딕셔너리 만든다
    word2idx = {word:idx for idx, word in enumerate(vocab_list)}

    # key : 인덱스 , value : 단어 ==> 딕셔너리 만든다
    idx2word = {idx:word for idx, word in enumerate(vocab_list)}

    return word2idx, idx2word
```

