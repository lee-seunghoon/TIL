# 사용 라이브러리

```python
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
```



# 사용자 정의 함수

```python
# batch_size 만큼 n_steps 길이의 여러 시계열 데이터 생성 
# 시계열 데이터(텍스트 문장과 같은 다른 시퀀스 데이터들도)는 입력 특성으로 3D 배열 [배치 크기, 타임 스텝 수, 차원 수]로 나타낸다 
def generate_time_series(batch_size, n_steps): 
    # random하게 0 ~ 1 사이의 실수를 3차원으로 만들어보겠습니다. 
    freq1, freq2, offsets1, offsets2 = np.random.rand(4, batch_size, 1) 
    
    # 시간축 데이터 생성 
    time = np.linspace(0,1,n_steps) 
    
    # 사인 곡선 1 
    series = 0.5 * np.sin((time - offsets1) * (freq1 * 10 + 10)) 
    
    # 사인 곡선 2 
    series += 0.2 * np.sin((time - offsets2) * (freq2 * 20 + 20)) 
    
    # noise data 
    series += 0.1 * (np.random.rand(batch_size, n_steps) - 0.5) 
    
    return series[...,np.newaxis].astype(np.float32)


# 모델 결과 시각화
def plot_graph(history, string):
    plt.plot(history.history[string])
    plt.plot(history.history['val_'+string], '')
    plt.xlabel('Epochs')
    plt.ylabel(string)
    plt.legend([string, 'val_'+string])
    plt.show()
```



# RNN 적용할 Sample Data 생성

```python
# 총 10000개의 시계열 데이터를 생성하고, 타입 스탭은 50 + 1 로 생성합니다. 
n_steps = 50 
series = generate_time_series(10000, n_steps+1) 

# train 학습 데이터(train_x)는 7000개로 구성하고 (7000, 50, 1) shape로 구성합니다.
# train 타겟 데이터(train_y)는 (7000, 1) shape로 구성
# 즉, RNN 모델은 input==3차원 / output==2차원
train_x, train_y = series[:7000, :n_steps], series[:7000, -1] 
val_x, val_y = series[7000:9000, :n_steps], series[7000:9000, -1] 
test_x, test_y = series[9000: , :n_steps], series[9000: , -1]
```



# SimpleRNN 구성

> - 평가 기준으로 MSE (최소 제곱 오차) 방식 적용
> - 최종 layer를 RNN으로 구성(은닉층이 포함, `하이퍼볼릭 탄젠트 함수`를 활성화 함수로 사용)
> - 이 방식은 앞에서 학습한 정보를 다음 모델이나, 신경망층에 전달하려 할 때 사용

```python
import tensorflow as tf

model = tf.keras.models.Sequential([
    tf.keras.layers.SimpleRNN(20, return_sequences=True, input_shape=[None, 1]),
    tf.keras.layers.SimpleRNN(20, return_sequences=True),
    tf.keras.layers.SimpleRNN(1)
])

model.compile(
    optimizer = tf.keras.optimizers.Adam(),
    loss = 'mse',
    metrics = ['mse']
)

history = model.fit(
    train_x,
    train_y,
    epochs=20,
    validation_data = (val_x, val_y)
)

# 최종 mse 값
print(history.history['val_mse'][-1])
# ==> 0.0038334811106324196
```



> - 수정 (다양한 활성화 함수를 사용할 수 있도록)
> - Dense Layer 대체

```python
import tensorflow as tf

model = tf.keras.models.Sequential([
    tf.keras.layers.SimpleRNN(20, return_sequences=True, input_shape=[None, 1]),
    # 마지막 Dense 층에 모든 정보를 전달하면서 다른 활성화 함수를 사용하기 위해 
    # RNN의 마지막 층은 return_sequences=True 를 지정하지 않습니다.
    tf.keras.layers.SimpleRNN(20),
    tf.keras.layers.Dense(1)
])

model.compile(
    optimizer = tf.keras.optimizers.Adam(),
    loss = 'mse',
    metrics = ['mse']
)

history = model.fit(
    train_x,
    train_y,
    epochs=20,
    validation_data = (val_x, val_y)
)
# 최종 mse 값
print(history.history['val_mse'][-1])
# ==> 0.0029193649534136057
```



# 여러 Time Step 값을 예측하는 방법



### 방법1

> - 하나씩 다음 time step을 예측한 후 그 예측값을 다시 입력값으로 활용해서 그 다음 time step을 예측
> - Test 하기 위해 새로운 Data 생성

```python
# 새로운 타임 스텝 예측
new_series = generate_time_series(1, n_steps + 10)

new_x, new_y = new_series[:, :n_steps], new_series[:, n_steps:]

x = new_x
for step_ahead in range(10):
    # 처음부터 하나씩 증가하면서 다음 타임 스텝을 예측 후 결과 값을 기존 값(3차원)에 추가할 수 있도록 shape 변환
    # 예측 값을 2차원 형태로 출력하기 때문
    recent_y_pred = model.predict(x[:, step_ahead:])[:, np.newaxis, :]
    x = np.concatenate([x, recent_y_pred], axis=1)

y_prd = x[:, n_steps:]

# MSE 값
np.mean(tf.keras.losses.mean_squared_error(new_y, y_prd))
# ==> 0.011365579
```



> - 그래프 그리기

```python
# 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'

# 그래프 그리기
plt.plot(range(50), new_x[0].reshape(-1), 'c.-')
plt.plot(range(50,60), new_y.reshape(-1), 'mo-')
plt.plot(range(50,60), y_prd.reshape(-1), 'bx-')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend(['학습','실제', '예측'])
plt.grid(True)
plt.show()
```

![output3](C:\Users\GOOD\Desktop\이승훈\Practice\RNN\output3.png)



> - 처음 만들었던 데이터에서 타겟 데이터만 살짝 수정 후 적용

```python
# 총 10000개의 시계열 데이터를 생성하고, 타입 스탭은 50 + 1 로 생성합니다. 
n_steps = 50 
series = generate_time_series(10000, n_steps+10) 

# train 데이터는 7000개로 구성하고 (7000, 50, 1) shape로 구성합니다.
# 타겟 데이터도 3차원으로 구성. 왜냐면 10개의 time step을 구하기 때문에 predict 하면 3차원으로 출력
train_x, train_y = series[:7000, :n_steps], series[:7000, -10:, 0] 
val_x, val_y = series[7000:9000, :n_steps], series[7000:9000, -10:, 0] # val_y ==> (2000, 10)
test_x, test_y = series[9000: , :n_steps], series[9000: , -10:, 0]

##################################################################

X = val_x 
for step_ahead in range(10):
    # 여기서 model 위에서 Dense(1) 로 출력한 model
    recent_y_pred = model.predict(X[:, step_ahead:])[:, np.newaxis, :]
    X = np.concatenate([X, recent_y_pred], axis=1)

Y_prd = X[:, n_steps:, 0]
# ==> (2000, 10)

# MSE
np.mean(tf.keras.losses.mean_squared_error(val_y, Y_prd))
# ==> 0.08856894
```



---



### 방법2

> - 하나씩 출력하는 게 아니라 한 번에 10번의 Time Step을 계산
> - 데이터도 이에 맞게 다시 구성
> - 마지막 Dense Layer에 10개 유닛 세팅
> - 성능이 좋음

```python
# 데이터 새롭게 구성
n_steps = 50 
series = generate_time_series(10000, n_steps+10) 
 
train_x, train_y = series[:7000, :n_steps], series[:7000, -10:, 0]     # train_y ==> (7000, 10)
val_x, val_y = series[7000:9000, :n_steps], series[7000:9000, -10:, 0] # val_y ==> (2000, 10)
test_x, test_y = series[9000: , :n_steps], series[9000: , -10:, 0]	   # test_y ==> (1000, 10)

# 새롭게 모델 구성
model = tf.keras.models.Sequential([
    tf.keras.layers.SimpleRNN(20, return_sequences=True, input_shape=[None, 1]),
    tf.keras.layers.SimpleRNN(20),
    # 다음 타임 스텝 10개를 한 번에 예측하기 위한 layer
    tf.keras.layers.Dense(10)
])

model.compile(
    optimizer = tf.keras.optimizers.Adam(),
    loss = 'mse',
    metrics = ['mse']
)

history = model.fit(
    train_x,
    train_y,
    epochs=20,
    validation_data = (val_x, val_y)
)

# 최종 mse 값
print(history.history['val_mse'][-1])
# ==> 0.008631878532469273
```



> - 모든 RNN Layer에서 나온 출력값을 모두 마지막 Dense Layer에 적용하기 위한 방법
> - 타겟 데이터도 차원 수를 10으로 맞춤

```python
# New 타겟 데이터
Y = np.empty((10000, n_steps, 10))
# Y.shape ==> (10000, 50, 10)

# 비어있는 Y에 값 채우기
for step in range(1, 10 +1):
    Y[:,:,step-1] = series[:, step:step+n_steps, 0]

Y_trin = Y[:7000] # ==> (7000, 50, 10)
Y_valid = Y[7000:9000] # ==> (2000, 50, 10)
Y_test = Y[9000:] # ==> (1000, 50, 10)

########################################################

# 모든 출력값 사용하는 새로운 모델
new_model = tf.keras.models.Sequential([
	tf.keras.layers.SimpleRNN(20, return_sequences=True, input_shape=[None,1]),
    tf.keras.layers.SimpleRNN(20, return_sequences=True),
    tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(10))
])

# 훈련 때는 모든 타임 스텝의 결과를 활용해서 MSE를 계산하는데 
# 최종 실제 모델 평가 결과는 마지막 타임 스텝의 출력에 대한 MSE만 계산하면 되서 사용자 정의 지표를 만들 필요가 있다.
def last_time_step_mse(y_true, y_pred):
    return tf.keras.metrics.mean_squared_error(y_true[:, -1], y_pred[:, -1])

new_model.compile(
    optimizer = tf.keras.optimizers.Adam(lr=0.01),
    loss = 'mse',
    metrics = [last_time_step_mse]
)

new_history = new_model.fit(
    train_x,
    Y_trin,
    epochs=20,
    validation_data = (val_x, Y_valid)
)

# 최종 mse 값
print(new_history.history['val_last_time_step_mse'][-1])
# ==> 0.006617669947445393
```



