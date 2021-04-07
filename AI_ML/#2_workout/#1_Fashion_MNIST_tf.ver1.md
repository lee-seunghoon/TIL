# Fashion-MNIST 필답 수행평가



### 1. Multinomial Classification 구현 후 정확도 측정

### 2. Deep Neural Network(DNN) 구현 후 정확도 측정

### 3. Convolutional Neural Network(CNN) 구현 후 정확도 측정

---



### `<1. Multinomial Classification 구현 후 정확도 측정>`

```python
# 1. Multinomial Classification 구현
# Logistic regression

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

# raw_data
train_raw_df = pd.read_csv('../kaggle_data/fashion/fashion-mnist_train.csv')
test_raw_df = pd.read_csv('../kaggle_data/fashion/fashion-mnist_test.csv')

train_x_data = train_raw_df.drop('label', axis=1, inplace=False).values
test_x_data = test_raw_df.drop('label', axis=1, inplace=False).values

# print(train_x_data.shape) ==> (60000, 784)
# print(test_x_data.shape) ==> (10000, 784)

# 정규화
scaler = MinMaxScaler()
scaler.fit(train_x_data)
norm_train_x_data = scaler.transform(train_x_data)
norm_test_x_data = scaler.transform(test_x_data)

# one-hot
sess = tf.Session()
onehot_train_t_data = sess.run(tf.one_hot(train_raw_df['label'], depth=10))
onehot_test_t_data = sess.run(tf.one_hot(test_raw_df['label'], depth=10))

#############################################################################

# Tensor Graph

X = tf.placeholder(shape=[None, 784], dtype=tf.float32)
T = tf.placeholder(shape=[None, 10], dtype=tf.float32)

W = tf.Variable(tf.random.normal([784,10]))
b = tf.Variable(tf.random.normal([10]))

logit = tf.matmul(X,W) + b
H = tf.nn.softmax(logit)

loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logit, labels=T))

train = tf.train.GradientDescentOptimizer(learning_rate=1e-2).minimize(loss)

#############################################################################
sess.run(tf.global_variables_initializer())

batch_size = 1000
epochs = 5000
# batch & learning_func
def learning(sess, x_data, t_data):
    for step in range(epochs):
        total_bath = int(x_data.shape[0]/batch_size)
        for i in range(total_bath):
            train_x_data = x_data[i*batch_size:(i+1)*batch_size]
            train_t_data = t_data[i*batch_size:(i+1)*batch_size]
            
            _, loss_val = sess.run([train, loss], feed_dict={X:train_x_data, T:train_t_data})
            
        if step % 500 == 0:
            print('loss 값 :', loss_val)

# accuracy 측정
predict = tf.argmax(H,1)
correct = tf.cast(tf.equal(predict,tf.argmax(T,1)), dtype=tf.float32)
accuracy = tf.reduce_mean(correct)
#############################################################################

learning(sess, norm_train_x_data, onehot_train_t_data)

print('최종 accuracy :', sess.run(accuracy, feed_dict={X:norm_test_x_data, T:onehot_test_t_data}))
'''
loss 값 : 8.898512
loss 값 : 0.89644825
loss 값 : 0.72407943
loss 값 : 0.63567483
loss 값 : 0.57887965
loss 값 : 0.5390306
loss 값 : 0.509436
loss 값 : 0.4865125
loss 값 : 0.46830767
loss 값 : 0.45360684
최종 accuracy : 0.8347
'''
```

```python
# 1. Multinomial Classification 구현 후 정확도 측정
# K-Fold CV
# Local Jupyter Notebook

import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import KFold
from sklearn.metrics import classification_report

# raw data
df = pd.read_csv('../kaggle_data/fashion/fashion-mnist_train.csv')
# display(df.head(), df.shape)

# 결측치, 이상치 처리
# 우리 data는 없다.

# 데이터 확인 (이미지 확인)
img_data = df.drop('label', axis=1, inplace=False).values

fig = plt.figure(figsize=(15,10))
fig_img = []

for i in range(10):
    fig_img.append(fig.add_subplot(2,5,i+1))
    fig_img[i].imshow(img_data[i].reshape(28,28), cmap='gray')
    
plt.tight_layout
plt.show()

# train - test split
x_data_train, x_data_test, t_data_train, t_data_test =\
train_test_split(df.drop('label', axis=1, inplace=False), df['label'], 
                 test_size=0.3, random_state=0)

# 정규화(Normalization)
scaler = MinMaxScaler()
scaler.fit(x_data_train)
x_data_train_norm = scaler.transform(x_data_train)
x_data_test_norm = scaler.transform(x_data_test)

# one-hot encoding
sess = tf.Session()
t_data_train_onehot = sess.run(tf.one_hot(t_data_train, depth=10))
t_data_test_onehot = sess.run(tf.one_hot(t_data_test, depth=10))

#Data 전처리 끝

# Placeholder
X = tf.placeholder(shape=[None, 784], dtype=tf.float32)
T = tf.placeholder(shape=[None, 10], dtype=tf.float32)

# Weight & bias
# He's 초기법 적용
W = tf.get_variable('weight', shape=[784,10],
                   initializer= tf.contrib.layers.variance_scaling_initializer())
b = tf.Variable(tf.random.normal([10]))

# Linear Regression ==> Softmax
logit = tf.matmul(X,W) + b
H = tf.nn.softmax(logit)

# loss
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logit, labels=T))

# train
train = tf.train.GradientDescentOptimizer(learning_rate=1e-2).minimize(loss)

sess.run(tf.global_variables_initializer())

# batch & learn
batch_size = 512
epochs = 1000
def learning(sess, x_data, t_data):
    for step in range(epochs):
        
        total_batch = int(x_data.shape[0]/batch_size)
        for i in range(total_batch):
            train_x_data = x_data[i*batch_size : (i+1)*batch_size]
            train_t_data = t_data[i*batch_size : (i+1)*batch_size]

            _,loss_val = sess.run([train, loss], feed_dict={X:train_x_data, T:train_t_data})
        
        if step % 500 == 0 :
            print('loss 값 :', loss_val)
        
# 평가
predict = tf.argmax(H,1)
correct = tf.cast(tf.equal(predict, tf.argmax(T,1)), dtype=tf.float32)
accuracy = tf.reduce_mean(correct)

#KFold
cv = 5
kf_accuracy = []
kf = KFold(n_splits=cv, shuffle=True)
for train_data_idx, val_data_idx in kf.split(x_data_train_norm):
    train_x_data = x_data_train_norm[train_data_idx]
    train_t_data = t_data_train_onehot[train_data_idx]
    
    val_x_data = x_data_train_norm[val_data_idx]
    val_t_data = t_data_train_onehot[val_data_idx]
    
    learning(sess, train_x_data, train_t_data)
    
    kf_accuracy.append(sess.run(accuracy, feed_dict={X:val_x_data, T:val_t_data}))

print('Total kf accuracy :', kf_accuracy)
print('Total accuracy :', np.mean(kf_accuracy))

'''
Total kf accuracy : [0.78690475, 0.8247619, 0.83488095, 0.83738095, 0.8477381]
Total accuracy : 0.82633334
'''
```

```python
# train data에서 split한 test data로 accuracy 측정
first_result = classification_report(t_data_test, 
                                     sess.run(tf.argmax(H,1), feed_dict={X:x_data_test_norm}))
print('첫번째 Accuracy 결과 :\n', first_result)
'''
첫번째 Accuracy 결과 :
               precision    recall  f1-score   support

           0       0.76      0.78      0.77      1799
           1       0.96      0.96      0.96      1843
           2       0.72      0.75      0.73      1808
           3       0.83      0.85      0.84      1849
           4       0.73      0.75      0.74      1765
           5       0.91      0.91      0.91      1786
           6       0.61      0.55      0.58      1787
           7       0.91      0.91      0.91      1789
           8       0.93      0.92      0.93      1795
           9       0.94      0.93      0.93      1779

    accuracy                           0.83     18000
   macro avg       0.83      0.83      0.83     18000
weighted avg       0.83      0.83      0.83     18000
'''

# 최종 test data로 accuracy 측정
test_df = pd.read_csv('../kaggle_data/fashion/fashion-mnist_test.csv')

test_x_data = test_df.drop('label', axis=1, inplace=False).values
test_t_data = test_df['label'].values
test_x_data_norm = scaler.transform(test_x_data)

final_result = classification_report(test_t_data,
                                     sess.run(tf.argmax(H,1), feed_dict={X:test_x_data_norm}))
print('최종 Accuracy 결과 :\n', final_result)
'''
최종 Accuracy 결과 :
               precision    recall  f1-score   support

           0       0.77      0.80      0.78      1000
           1       0.95      0.97      0.96      1000
           2       0.74      0.72      0.73      1000
           3       0.83      0.86      0.85      1000
           4       0.74      0.77      0.75      1000
           5       0.90      0.90      0.90      1000
           6       0.62      0.57      0.59      1000
           7       0.89      0.89      0.89      1000
           8       0.93      0.91      0.92      1000
           9       0.91      0.92      0.92      1000

    accuracy                           0.83     10000
   macro avg       0.83      0.83      0.83     10000
weighted avg       0.83      0.83      0.83     10000

'''
```



---



### `2. Deep Neural Network(DNN) 구현 후 정확도 측정`

```python
# 2. Deep Neural Network(DNN) 구현 후 정확도 측정

# Google Colab 이용

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report

# Data 전처리

# Train Data
train_data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/kaggle_data/fashion/fashion-mnist_train.csv')

# Data split
x_data_train, x_data_val, t_data_train, t_data_val =\
train_test_split(train_data.drop('label', axis=1, inplace=False), train_data['label'], 
                 test_size=0.3, random_state=0)

# 정규화
scaler = MinMaxScaler()
scaler.fit(x_data_train)
norm_train_x_data = scaler.transform(x_data_train)
norm_val_x_data = scaler.transform(x_data_val)

# one-hot
sess = tf.Session()
onehot_train_t_data = sess.run(tf.one_hot(t_data_train, depth=10))
onehot_val_t_data = sess.run(tf.one_hot(t_data_val, depth=10))

# Data 전처리 끝

# DNN Tensor

# Input Layer
X = tf.placeholder(shape=[None, 784], dtype=tf.float32)
T = tf.placeholder(shape=[None, 10], dtype=tf.float32)

# hidden layer_1
W1 = tf.get_variable('W1', shape=[784, 128],
                     initializer=tf.contrib.layers.xavier_initializer())
b1 = tf.Variable(tf.random.normal([128]))

layer_1 = tf.matmul(X, W1) + b1
relu_1 = tf.nn.relu(layer_1)

# hidden layer_2
W2 = tf.get_variable('W2', shape=[128, 64],
                     initializer=tf.contrib.layers.xavier_initializer())
b2 = tf.Variable(tf.random.normal([64]))

layer_2 = tf.matmul(relu_1, W2) + b2
relu_2 = tf.nn.relu(layer_2)

# output layer
W3 = tf.get_variable('W3', shape=[64, 10],
                     initializer=tf.contrib.layers.xavier_initializer())
b3 = tf.Variable(tf.random.normal([10]))

logit = tf.matmul(relu_2, W3) + b3
H = tf.nn.softmax(logit)

# loss
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logit, labels=T))

# train
train = tf.train.GradientDescentOptimizer(learning_rate=1e-2).minimize(loss)

# Accuracy
predict = tf.argmax(H,1)
correct = tf.cast(tf.equal(predict, tf.argmax(T,1)),dtype=tf.float32)
accuracy = tf.reduce_mean(correct)

sess.run(tf.global_variables_initializer())

###############################################################################

batch_size = 128
epochs = 1000

def learning(sess, x_data, t_data):
    for step in range(epochs):

        batch = int(x_data.shape[0]/batch_size)
        for i in range(batch):
            x_data_train = x_data[i*batch_size : (i+1)*batch_size]
            t_data_train = t_data[i*batch_size : (i+1)*batch_size]
        
            _, loss_val = sess.run([train, loss], feed_dict={X:x_data_train, T:t_data_train})

        if step % 100 == 0:
            print('loss 값 :', loss_val)

# 학습
learning(sess, norm_train_x_data, onehot_train_t_data)

# 평가
result = sess.run(accuracy, feed_dict={X:norm_val_x_data, T: onehot_val_t_data})
print('최종 accuracy :', result)

'''
loss 값 : 0.89500195
loss 값 : 0.3271907
loss 값 : 0.20197906
loss 값 : 0.11328979
loss 값 : 0.0668103
loss 값 : 0.041395705
loss 값 : 0.02384229
loss 값 : 0.012476339
loss 값 : 0.0071329046
loss 값 : 0.004524871
최종 accuracy : 0.8764
'''
```

```python
# val_data accuracy
val_report = classification_report(t_data_val,
                                 sess.run(predict, feed_dict={X:norm_val_x_data}))
print(val_report)
'''
              precision    recall  f1-score   support

           0       0.82      0.78      0.80      1799
           1       0.97      0.97      0.97      1843
           2       0.76      0.85      0.80      1808
           3       0.89      0.87      0.88      1849
           4       0.80      0.78      0.79      1765
           5       0.96      0.93      0.95      1786
           6       0.68      0.68      0.68      1787
           7       0.93      0.94      0.94      1789
           8       0.97      0.94      0.95      1795
           9       0.94      0.96      0.95      1779

    accuracy                           0.87     18000
   macro avg       0.87      0.87      0.87     18000
weighted avg       0.87      0.87      0.87     18000
'''

# 최종 accuracy 측정
test_data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/kaggle_data/fashion/fashion-mnist_test.csv')

test_x_data = test_data.drop('label', axis=1, inplace=False).values
norm_test_x_data = scaler.transform(test_x_data)
test_t_data = test_data['label'].values

final_report = classification_report(test_t_data,
                                 sess.run(predict, feed_dict={X:norm_test_x_data}))
print(final_report)
'''
              precision    recall  f1-score   support

           0       0.81      0.86      0.83      1000
           1       0.98      0.98      0.98      1000
           2       0.79      0.83      0.81      1000
           3       0.89      0.88      0.88      1000
           4       0.82      0.82      0.82      1000
           5       0.96      0.94      0.95      1000
           6       0.75      0.68      0.71      1000
           7       0.93      0.94      0.93      1000
           8       0.96      0.96      0.96      1000
           9       0.93      0.96      0.94      1000

    accuracy                           0.88     10000
   macro avg       0.88      0.88      0.88     10000
weighted avg       0.88      0.88      0.88     10000
'''
```

---



### `3. Convolutional Neural Network(CNN) 구현 후 정확도 측정`

```python
# 3. Convolutional Neural Network(CNN) 구현 후 정확도 측정

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split


# Train Data
train_data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/kaggle_data/fashion/fashion-mnist_train.csv')

# Data_split
x_data_train, x_data_val, t_data_train, t_data_val =\
train_test_split(train_data.drop('label', axis=1, inplace=False), train_data['label'], 
                 test_size=0.3, random_state=0)

# 정규화
scaler = MinMaxScaler()
scaler.fit(x_data_train)
norm_train_x_data = scaler.transform(x_data_train)
norm_val_x_data = scaler.transform(x_data_val)

# one-hot
sess = tf.Session()
onehot_train_t_data = sess.run(tf.one_hot(t_data_train, depth=10))
onehot_val_t_data = sess.run(tf.one_hot(t_data_val, depth=10))

# Data 전처리 끝

# CNN 그래프

# Input Layer
X = tf.placeholder(shape=[None, 784], dtype=tf.float32)
T = tf.placeholder(shape=[None, 10], dtype=tf.float32)

# Convolution
# 입력데이터 형태부터 수정 ==> 4차원
# -1, 28, 28, 1
x_img = tf.reshape(X, [-1, 28, 28, 1])

# 1st conv layer
# filter(kernal)
W1 = tf.Variable(tf.random.normal([3,3,1,32]))
L1 = tf.nn.conv2d(x_img,
                  W1,
                  strides=[1,1,1,1],
                  padding='SAME') # ==> 워낙 Data size가 작기 때문에 (28,28) 유지해줘도 pooling에서 절반으로 줄어든다.
L1 = tf.nn.relu(L1) # ==> (?, 28, 28, 32)

# 1st pooling
P1 = tf.nn.max_pool(L1,
                    ksize=[1,2,2,1],
                    strides=[1,2,2,1],
                    padding='SAME')
print(P1.shape) # ==> (?, 14, 14, 32) # ==> ksize와 strides (2,2) 때문에 반으로 줄어든다.

# 2nd conv layer
W2 = tf.Variable(tf.random.normal([3,3,32,64]))
L2 = tf.nn.conv2d(P1,
                  W2,
                  strides=[1,1,1,1],
                  padding='SAME')
L2 = tf.nn.relu(L2) # ==> (?, 14, 14, 64)

# 2nd pooling
P2 = tf.nn.max_pool(L2,
                    ksize=[1,2,2,1],
                    strides=[1,2,2,1],
                    padding='SAME')

# convolution 끝
#######################################################

# FC Layer로 들어가기 위한 shape 조정
# 4차원 ==> 2차원
conv_img = tf.reshape(P2, [-1, 7 * 7 * 64])

# FC Layer
W3 = tf.get_variable('weight3', shape=[7 * 7 * 64, 256],
                     initializer=tf.contrib.layers.variance_scaling_initializer())
b3 = tf.Variable(tf.random.normal([256]))

input_layer_ = tf.nn.relu(tf.matmul(conv_img, W3) + b3)
input_layer = tf.nn.dropout(input_layer_, rate=0.4)

# Output Layer (Dense)
W4 = tf.get_variable('weight4', shape=[256, 10],
                     initializer=tf.contrib.layers.variance_scaling_initializer())
b4 = tf.Variable(tf.random.normal([10]))

logit = tf.matmul(input_layer, W4) + b4
H = tf.nn.softmax(logit)

# tensor layer graph 끝
#######################################################

# loss
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logit, labels=T))

# train
train = tf.train.GradientDescentOptimizer(learning_rate=1e-2).minimize(loss)

# Accuracy
predict = tf.argmax(H,1)
correct = tf.cast(tf.equal(predict, tf.argmax(T,1)),dtype=tf.float32)
accuracy = tf.reduce_mean(correct)

sess.run(tf.global_variables_initializer())

###################################################################################
batch_size = 128
epochs = 1000

for step in range(epochs):

    batch = int(norm_train_x_data.shape[0]/batch_size)
    for i in range(batch):
        x_data_train = norm_train_x_data[i*batch_size : (i+1)*batch_size]
        t_data_train = onehot_train_t_data[i*batch_size : (i+1)*batch_size]
    
        _, loss_val = sess.run([train, loss], feed_dict={X:x_data_train, T:t_data_train})

    if step % 100 == 0:
        print('loss 값 :', loss_val)
        
'''
loss 값 : 1.010111
loss 값 : 0.13795377
loss 값 : 0.044796802
loss 값 : 0.09336342
loss 값 : 0.070253745
loss 값 : 0.011469511
loss 값 : 0.011740573
loss 값 : 0.01297378
loss 값 : 0.018714555
loss 값 : 0.009353402
'''
```

```python
# val_data accuracy
val_report = classification_report(t_data_val.values,
                                 sess.run(predict, feed_dict={X:norm_val_x_data}))
print(val_report)
'''
              precision    recall  f1-score   support

           0       0.81      0.88      0.84      1799
           1       0.99      0.97      0.98      1843
           2       0.85      0.85      0.85      1808
           3       0.89      0.92      0.90      1849
           4       0.83      0.83      0.83      1765
           5       0.98      0.95      0.97      1786
           6       0.76      0.70      0.73      1787
           7       0.94      0.96      0.95      1789
           8       0.98      0.97      0.98      1795
           9       0.96      0.96      0.96      1779

    accuracy                           0.90     18000
   macro avg       0.90      0.90      0.90     18000
weighted avg       0.90      0.90      0.90     18000
'''

# test_data accuracy
test_data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/kaggle_data/fashion/fashion-mnist_test.csv')
norm_test_x_data = scaler.transform(test_x_data)
test_t_data = test_data['label'].values

final_report = classification_report(test_t_data,
                                 	sess.run(predict, feed_dict={X:norm_test_x_data}))
print(final_report)
'''
              precision    recall  f1-score   support

           0       0.81      0.88      0.84      1000
           1       0.98      0.98      0.98      1000
           2       0.87      0.83      0.85      1000
           3       0.89      0.93      0.91      1000
           4       0.85      0.85      0.85      1000
           5       0.98      0.95      0.97      1000
           6       0.77      0.70      0.73      1000
           7       0.94      0.95      0.94      1000
           8       0.98      0.97      0.98      1000
           9       0.95      0.97      0.96      1000

    accuracy                           0.90     10000
   macro avg       0.90      0.90      0.90     10000
weighted avg       0.90      0.90      0.90     10000
'''
```

