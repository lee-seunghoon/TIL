# Practice - lemonade prediction



### 라이브러리 사용

```python
import tensorflow as tf
import pandas as pd
```



### 데이터 준비

```python
file = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
data = pd.read_csv(file)  #판다스로 csv데이터 읽어오는 코드 `pd.read_csv()`
data.head()
```



### 독립변수, 종속변수 설정

```python
독립 = data[['온도']]
종속 = data[['판매량']]
print(독립.shape, 종속.shape)
```



> `독립변수`가 `종속변수`에 미치는 영향을 분석하는 모델을 만든다.
>
> 이번 실습은 레모네이드 판매량(`종속변수`)과 온도(`독립변수`)와의 관계를 모델링한 후
>
> 학습시켜서 예측값을 추축한다.



### 모델을 만든다.

```python
X = tf.keras.layers.Input(shape=[1])	#독립변수가 1개라면 shape=[1]
Y = tf.keras.layers.Dense(1)(X)			#종속변수가 1개라면 Dense(1)
model = tf.keras.models.Model(X,Y)		#tensorlow, keras로 모델 만들기
model.compile(loss='mse')				#loss는... 아래쪽 결과에서 0으로 갈수록 좋은건데. 
```



### 모델을 학습시킨다.

```python
model.fit(독립,종속, epochs=1000, verbose=0)  # verbose=0 --> 학습하는 동안 그 내용 출력하지 않는 코드

# 출력값 --> <tensorflow.python.keras.callbacks.History at 0x7f6f77363978>

# 원래는 아래와 같은 과정 보여줌 (verbose=0 )
'''
Epoch 1/10
1/1 [==============================] - 0s 4ms/step - loss: 0.0014
Epoch 2/10
1/1 [==============================] - 0s 10ms/step - loss: 0.0014
Epoch 3/10
1/1 [==============================] - 0s 7ms/step - loss: 0.0014
Epoch 4/10
1/1 [==============================] - 0s 7ms/step - loss: 0.0014
Epoch 5/10
1/1 [==============================] - 0s 6ms/step - loss: 0.0014
Epoch 6/10
1/1 [==============================] - 0s 9ms/step - loss: 0.0014
Epoch 7/10
1/1 [==============================] - 0s 16ms/step - loss: 0.0014
Epoch 8/10
1/1 [==============================] - 0s 7ms/step - loss: 0.0014
Epoch 9/10
1/1 [==============================] - 0s 10ms/step - loss: 0.0014
Epoch 10/10
1/1 [==============================] - 0s 7ms/step - loss: 0.0014
<tensorflow.python.keras.callbacks.History at 0x7f6f772cd4e0>

'''
```



### 모델을 이용해서, 예측한다.

```python
model.predict([[2]])	#독립변수를 [] 안에 넣는거임

# 값 --> array([[4.435457]], dtype=float32) 
# 온도가 2도라면 레모네이드의 판매량은 4개 정도이다.
```

