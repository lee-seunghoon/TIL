## 전체 데이터(25,000개) ImageDataGenerator를 이용하여 모델 구현 후 Accuracy 측정

- history 객체를 이용하여 train loss, accuracy와 validation loss, accuracy 비교



### `Image Generator 생성`

```python
import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 전체 경로
base_dir = '/content/drive/MyDrive/Colab Notebooks/CAT_DOG/cat_dog_full'

# 각 용도별 경로
train_path = os.path.join(base_dir, 'train')
val_path = os.path.join(base_dir, 'validation')
test_path = os.path.join(base_dir, 'test')

# 각 용도별 generator
train_gen = ImageDataGenerator(rescale=1/255)
val_gen = ImageDataGenerator(rescale=1/255)
test_gen = ImageDataGenerator(rescale=1/255)

# 각 이미지 generator
train_img_gen = train_gen.flow_from_directory(train_path,
                                             target_size=(150,150),
                                             batch_size=20,
                                             classes=['cats', 'dogs'],
                                             class_mode='binary')
val_img_gen = val_gen.flow_from_directory(val_path,
                                             target_size=(150,150),
                                             batch_size=20,
                                             classes=['cats', 'dogs'],
                                             class_mode='binary')
test_img_gen = test_gen.flow_from_directory(test_path,
                                             target_size=(150,150),
                                             batch_size=20,
                                             classes=['cats', 'dogs'],
                                             class_mode='binary')
'''
Found 14000 images belonging to 2 classes.
Found 6000 images belonging to 2 classes.
Found 5000 images belonging to 2 classes.
'''

for x_data, t_data in train_img_gen:
    print(x_data.shape)
    print(t_data)

    plt.imshow(x_data[0])
    plt.show()

    break

```

![image-20210408183309516](md-images/image-20210408183309516.png)



### `CNN Model 구성`

```python
# CNN Layer 구성

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Dropout, Conv2D, MaxPooling2D
from tensorflow.keras.optimizers import Adam

model = Sequential()

# conv layer 구성
model.add(Conv2D(filters=32,
                 kernel_size=(3,3),
                 padding='same',
                 activation='relu',
                 input_shape=(150,150,3)))
# maxpooling
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(filters=64,
                 kernel_size=(3,3),
                 padding='same',
                 activation='relu'))
model.add(Conv2D(filters=64,
                 kernel_size=(3,3),
                 padding='same',
                 activation='relu'))
# maxpooling
model.add(MaxPooling2D(pool_size=(2,2)))

# DNN Layer
model.add(Flatten())

model.add(Dropout(rate=0.5))

model.add(Dense(64, activation='relu'))

model.add(Dense(1, activation='sigmoid'))

print(model.summary())
'''
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 150, 150, 32)      896       
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 75, 75, 32)        0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 75, 75, 64)        18496     
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 75, 75, 64)        36928     
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 37, 37, 64)        0         
_________________________________________________________________
flatten (Flatten)            (None, 87616)             0         
_________________________________________________________________
dropout (Dropout)            (None, 87616)             0         
_________________________________________________________________
dense (Dense)                (None, 64)                5607488   
_________________________________________________________________
dense_1 (Dense)              (None, 1)                 65        
=================================================================
Total params: 5,663,873
Trainable params: 5,663,873
Non-trainable params: 0
_________________________________________________________________
None
'''
```



#### `compile & fit`

```python
# compile
model.compile(optimizer=Adam(1e-4),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# fit
history = model.fit(train_img_gen,
          steps_per_epoch=700,
          epochs=20,
          verbose=1,
          validation_data=val_img_gen,
          validation_steps=300)

'''
Epoch 20/20
700/700 [==============================] - 77s 110ms/step - loss: 0.0678 - accuracy: 0.9777 - val_loss: 0.6891 - val_accuracy: 0.8000
'''
```



#### `Graph`

```python
train_loss = history.history['loss']
val_loss = history.history['val_loss']

train_accuracy = history.history['accuracy']
val_accuracy = history.history['val_accuracy']

fig = plt.figure(figsize=(20,5))
loss_graph = fig.add_subplot(1,2,1)
acc_graph = fig.add_subplot(1,2,2)

loss_graph.plot(train_loss, c='r', label='train_loss')
loss_graph.plot(val_loss, c='b', label='val_loss')
loss_graph.legend()

acc_graph.plot(train_accuracy, c='r', label='train_accuracy')
acc_graph.plot(val_accuracy, c='b', label='val_accuracy')
acc_graph.legend()

plt.tight_layout()
plt.show()
```

![image-20210408183510454](md-images/image-20210408183510454.png)



#### `Accuracy`

```python
# accuracy 측정
test_loss, test_acc = model.evaluate(test_img_gen, verbose=1)
print('test data의 accuracy :', test_acc)
'''
250/250 [==============================] - 1165s 5s/step - loss: 0.6974 - accuracy: 0.7964
test data의 accuracy : 0.7964000105857849
'''
```

