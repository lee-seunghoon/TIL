# BMI Data Multinomial Classification

> - Tensor 1.x 버전 사용
> - activation function : **`softmax`**



#### `Module`

```python
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt
```



#### `Data Preprocessing`

```python
# Raw Data Loading
df = pd.read_csv('../data/bmi.csv', skiprows=3)

# Data 전처리
# df.isnull().sum() # ==> 결측치 없습니다.

fig = plt.figure()

label_fig = fig.add_subplot(1,3,1)
height_fig = fig.add_subplot(1,3,2)
weight_fig = fig.add_subplot(1,3,3)

label_fig.set_title('Label')
height_fig.set_title('Height')
weight_fig.set_title('Weight')

label_fig.boxplot(df['label'])
height_fig.boxplot(df['height'])
weight_fig.boxplot(df['weight'])

fig.tight_layout()
plt.show()

# 결측치 이상치 모두 존재 안합니다.
```

![image-20210317225943262](md-images/image-20210317225943262.png)

```python
x_data = df.drop('label', axis=1, inplace=False).values
t_data = df['label'].values

# 모든 독립변수 data(x_data)를 정규화
scaler = MinMaxScaler()
scaler.fit(x_data)

# label data one-hot encoding
sess = tf.Session()
onhot_t_data = sess.run(tf.one_hot(t_data, depth=3))
```





#### `Data Split`

```python
# train_test_data split
train_x_data, test_x_data, onehot_train_t_data, onehot_test_t_data =\
train_test_split(x_data, onhot_t_data, test_size=0.3, random_state=0)

# 정규화된 train & test 독립변수
norm_train_x_data= scaler.transform(train_x_data)
norm_test_x_data= scaler.transform(test_x_data)

# onehot t_data
# onehot_train_t_data & onehot_test_t_data
```



#### `Tensor Graph`

```python
# Tensor Graph 구성
X = tf.placeholder(shape=[None,2], dtype=tf.float32)
T = tf.placeholder(shape=[None,3], dtype=tf.float32)

W = tf.Variable(tf.random.normal([2,3], name='weight'))
b = tf.Variable(tf.random.normal([3], name='weight'))

# hypothesis
logit = tf.matmul(X,W) + b
H = tf.nn.softmax(logit)

# loss
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logit, labels=T))

# train
train = tf.train.GradientDescentOptimizer(learning_rate=1e-4).minimize(loss)

sess.run(tf.global_variables_initializer())

# Accuracy Tensor
argmax_result = tf.argmax(H,1)
correct = tf.cast(tf.equal(argmax_result, tf.argmax(T,1)),
                  dtype=tf.float32)
accuracy = tf.reduce_mean(correct)
```



#### `batch & learn_function` 

```python
# batch 설정
epochs_num = 10000
batch_size = 100

# 학습 함수
def learning(sess, x_data, t_data):
    print('######### 학습 시작 ############')
    for step in range(epochs_num):
        
        batch_data = int(x_data.shape[0]/batch_size)
        for batch in range(batch_data):
            batch_x = x_data[batch*batch_size:(batch+1)*batch_size]
            batch_t = t_data[batch*batch_size:(batch+1)*batch_size]
            
            _, loss_val = sess.run([train,loss], feed_dict={X:batch_x, T:batch_t})

        if step % 1000 == 0:
            print('Loss : {}'.format(loss_val))
    print('######### 학습 종료 ############')
```



#### `KFold Validation`

```python
cv=5
result=[]
kf = KFold(n_splits=cv, shuffle=True)

for train_data_idx, val_data_idx in kf.split(norm_train_x_data):
    train_x = norm_train_x_data[train_data_idx]
    train_t = onehot_train_t_data[train_data_idx]
    
    val_x = norm_train_x_data[val_data_idx]
    val_t = onehot_train_t_data[val_data_idx]
    
    learning(sess,train_x,train_t)
    
    result.append(sess.run(accuracy, feed_dict={X:val_x, T:val_t}))
    
print('각 fold별 accurcy =', result)
print('validation accuracy =', np.mean(result))
```

![image-20210317230313630](md-images/image-20210317230313630.png)



#### `Final Accuracy`

```python
# test_data로 구한 최종 Accuracy
print('최종 Accurcay :', sess.run(accuracy, feed_dict={X:scaler.transform(test_x_data), T:onehot_test_t_data}))
```

![image-20210317230354974](md-images/image-20210317230354974.png)