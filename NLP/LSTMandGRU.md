# LSTM 

```python
model = keras.models.Sequential([
    keras.layers.LSTM(20, return_sequence=True, input_shape=[None, 1]),
    keras.layers.LSTM(20, return_sequence=True)
    keras.layers.TimeDistributed(keras.layers.Dense(10))
])
```



# GRU

```python
model = keras.models.Sequential([
    keras.layers.Conv1D(filter=20, kernel_size=4, strides=2, padding='valid', input_shape=[None, 1]),
    keras.layers.GRU(20, return_sequences=True),
    keras.layers.GRU(20, return_sequences=True),
    keras.layers.TimeDistributed(keras.layers.Dense(10))
])
```

