# AI Platform jupyter notebook

​	<목표>

- Tensorflow 2.x 학습 어플리케이션 만들고, 로컬에서 검사
- 클라우드의 단일 작업자 인스턴스에서 학습 작업 실행
- 모델 배포하여 예측
- 온라인 예측을 요청하고 응답 확인



## 실습 데이터 설명

- 미국 인구 조사 소득 데이터셋(https://archive.ics.uci.edu/ml/datasets/Census+Income)
- 소득 범주를 예측하는 분류 모델 빌드
- 소득 범주(label)
  - 50,000달러 초과
  - 50,000달러 이하



## Jupyter NoteBook 생성 및 Clone

1. `AI Platform` > `Dashboard` 클릭 후 `View notebook instances` 클릭

2. `New Notebook` 으로 생성

3. 설정 : `TensorFlow Enterprise` → `TensorFlow Enterprise 2.x(LTS 사용)` → `GPU 사용 안함`

4. 새 노트북 인스턴스 대화상자에서 연필 모양 아이콘 클릭하여 인스턴스 속성 편집

5. 인스턴스 이름은 미리 생성된 기본 이름 그대로 사용

6. 리전 : `us-central1`, 영역 : 선택한 리전의 영역(`us-central1-a`)

7. `Jupyter Lab` 열기

8. Terminal 에서 다음 명령어 입력(git 복제)

   ```cmd
   git clone https://github.com/GoogleCloudPlatform/training-data-analyst
   ```

9. `training-data-analyst/self-paced-labs/ai-platform-qwikstart` 으로 이동하여 `ai_platform_qwik_start.ipynb` 열기



## Code



### Step1. training data set 구축

- local 환경에 데이터 만들기

  ```python
  import os
  ```

  ```python
  %%bash
  
  mkdir data
  gsutil -m cp gs://cloud-samples-data/ml-engine/census/data/* data/
  ```

  ```python
  %%bash
  
  export TRAIN_DATA=$(pwd)/data/adult.data.csv
  export EVAL_DATA=$(pwd)/data/adult.test.csv
  ```



- 데이터 확인하기

  ```python
  %%bash
  
  head data/adult.data.csv
  ```

  

### Step2. local 환경에서 model train

- 로컬 훈련 작업을 통해 python 훈련 프로그램 가져오고, Cloud AI Platform 훈련 작업과 비슷한 환경에서 훈련 절차를 실행한다.



#### Step2.1 Local에서 실행할 파일 만들기

> - 3개의 파일 생성
> - 1번째 : `util.py` (데이터 전처리를 위한 utility 방법을 포함하고 있다.)
> - 2번째 : `model.py` (데이터 입력 세팅 및 모델 아키텍쳐)
> - 3번째 : `task.py` (모델 학습 및 평가)

```python
%%bash
mkdir -p trainer
touch trainer/__init__.py
```



- 1번째 `util.py` 생성 : 데이터 전처리(feature engineering) 코드

```python
얼얼절ㅇ%%writefile trainer/util.py
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
from six.moves import urllib
import tempfile

import numpy as np
import pandas as pd
import tensorflow as tf

# Storage directory
DATA_DIR = os.path.join(tempfile.gettempdir(), 'census_data')

# Download options.
DATA_URL = (
    'https://storage.googleapis.com/cloud-samples-data/ai-platform/census'
    '/data')
TRAINING_FILE = 'adult.data.csv'
EVAL_FILE = 'adult.test.csv'
TRAINING_URL = '%s/%s' % (DATA_URL, TRAINING_FILE)
EVAL_URL = '%s/%s' % (DATA_URL, EVAL_FILE)

# These are the features in the dataset.
# Dataset information: https://archive.ics.uci.edu/ml/datasets/census+income
_CSV_COLUMNS = [
    'age', 'workclass', 'fnlwgt', 'education', 'education_num',
    'marital_status', 'occupation', 'relationship', 'race', 'gender',
    'capital_gain', 'capital_loss', 'hours_per_week', 'native_country',
    'income_bracket'
]

# This is the label (target) we want to predict.
_LABEL_COLUMN = 'income_bracket'

# These are columns we will not use as features for training. There are many
# reasons not to use certain attributes of data for training. Perhaps their
# values are noisy or inconsistent, or perhaps they encode bias that we do not
# want our model to learn. For a deep dive into the features of this Census
# dataset and the challenges they pose, see the Introduction to ML Fairness
# Notebook: https://colab.research.google.com/github/google/eng-edu/blob
# /master/ml/cc/exercises/intro_to_fairness.ipynb
UNUSED_COLUMNS = ['fnlwgt', 'education', 'gender']

_CATEGORICAL_TYPES = {
    'workclass': pd.api.types.CategoricalDtype(categories=[
        'Federal-gov', 'Local-gov', 'Never-worked', 'Private', 'Self-emp-inc',
        'Self-emp-not-inc', 'State-gov', 'Without-pay'
    ]),
    'marital_status': pd.api.types.CategoricalDtype(categories=[
        'Divorced', 'Married-AF-spouse', 'Married-civ-spouse',
        'Married-spouse-absent', 'Never-married', 'Separated', 'Widowed'
    ]),
    'occupation': pd.api.types.CategoricalDtype([
        'Adm-clerical', 'Armed-Forces', 'Craft-repair', 'Exec-managerial',
        'Farming-fishing', 'Handlers-cleaners', 'Machine-op-inspct',
        'Other-service', 'Priv-house-serv', 'Prof-specialty', 'Protective-serv',
        'Sales', 'Tech-support', 'Transport-moving'
    ]),
    'relationship': pd.api.types.CategoricalDtype(categories=[
        'Husband', 'Not-in-family', 'Other-relative', 'Own-child', 'Unmarried',
        'Wife'
    ]),
    'race': pd.api.types.CategoricalDtype(categories=[
        'Amer-Indian-Eskimo', 'Asian-Pac-Islander', 'Black', 'Other', 'White'
    ]),
    'native_country': pd.api.types.CategoricalDtype(categories=[
        'Cambodia', 'Canada', 'China', 'Columbia', 'Cuba', 'Dominican-Republic',
        'Ecuador', 'El-Salvador', 'England', 'France', 'Germany', 'Greece',
        'Guatemala', 'Haiti', 'Holand-Netherlands', 'Honduras', 'Hong',
        'Hungary',
        'India', 'Iran', 'Ireland', 'Italy', 'Jamaica', 'Japan', 'Laos',
        'Mexico',
        'Nicaragua', 'Outlying-US(Guam-USVI-etc)', 'Peru', 'Philippines',
        'Poland',
        'Portugal', 'Puerto-Rico', 'Scotland', 'South', 'Taiwan', 'Thailand',
        'Trinadad&Tobago', 'United-States', 'Vietnam', 'Yugoslavia'
    ]),
    'income_bracket': pd.api.types.CategoricalDtype(categories=[
        '<=50K', '>50K'
    ])
}


def _download_and_clean_file(filename, url):
    """Downloads data from url, and makes changes to match the CSV format.

    The CSVs may use spaces after the comma delimters (non-standard) or include
    rows which do not represent well-formed examples. This function strips out
    some of these problems.

    Args:
      filename: filename to save url to
      url: URL of resource to download
    """
    temp_file, _ = urllib.request.urlretrieve(url)
    with tf.io.gfile.GFile(temp_file, 'r') as temp_file_object:
        with tf.io.gfile.GFile(filename, 'w') as file_object:
            for line in temp_file_object:
                line = line.strip()
                line = line.replace(', ', ',')
                if not line or ',' not in line:
                    continue
                if line[-1] == '.':
                    line = line[:-1]
                line += '\n'
                file_object.write(line)
    tf.io.gfile.remove(temp_file)


def download(data_dir):
    """Downloads census data if it is not already present.

    Args:
      data_dir: directory where we will access/save the census data
    """
    tf.io.gfile.makedirs(data_dir)

    training_file_path = os.path.join(data_dir, TRAINING_FILE)
    if not tf.io.gfile.exists(training_file_path):
        _download_and_clean_file(training_file_path, TRAINING_URL)

    eval_file_path = os.path.join(data_dir, EVAL_FILE)
    if not tf.io.gfile.exists(eval_file_path):
        _download_and_clean_file(eval_file_path, EVAL_URL)

    return training_file_path, eval_file_path


def preprocess(dataframe):
    """Converts categorical features to numeric. Removes unused columns.

    Args:
      dataframe: Pandas dataframe with raw data

    Returns:
      Dataframe with preprocessed data
    """
    dataframe = dataframe.drop(columns=UNUSED_COLUMNS)

    # Convert integer valued (numeric) columns to floating point
    numeric_columns = dataframe.select_dtypes(['int64']).columns
    dataframe[numeric_columns] = dataframe[numeric_columns].astype('float32')

    # Convert categorical columns to numeric
    cat_columns = dataframe.select_dtypes(['object']).columns
    dataframe[cat_columns] = dataframe[cat_columns].apply(lambda x: x.astype(
        _CATEGORICAL_TYPES[x.name]))
    dataframe[cat_columns] = dataframe[cat_columns].apply(lambda x: x.cat.codes)
    return dataframe


def standardize(dataframe):
    """Scales numerical columns using their means and standard deviation to get
    z-scores: the mean of each numerical column becomes 0, and the standard
    deviation becomes 1. This can help the model converge during training.

    Args:
      dataframe: Pandas dataframe

    Returns:
      Input dataframe with the numerical columns scaled to z-scores
    """
    dtypes = list(zip(dataframe.dtypes.index, map(str, dataframe.dtypes)))
    # Normalize numeric columns.
    for column, dtype in dtypes:
        if dtype == 'float32':
            dataframe[column] -= dataframe[column].mean()
            dataframe[column] /= dataframe[column].std()
    return dataframe


def load_data():
    """Loads data into preprocessed (train_x, train_y, eval_y, eval_y)
    dataframes.

    Returns:
      A tuple (train_x, train_y, eval_x, eval_y), where train_x and eval_x are
      Pandas dataframes with features for training and train_y and eval_y are
      numpy arrays with the corresponding labels.
    """
    # Download Census dataset: Training and eval csv files.
    training_file_path, eval_file_path = download(DATA_DIR)

    # This census data uses the value '?' for missing entries. We use
    # na_values to
    # find ? and set it to NaN.
    # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv
    # .html
    train_df = pd.read_csv(training_file_path, names=_CSV_COLUMNS,
                           na_values='?')
    eval_df = pd.read_csv(eval_file_path, names=_CSV_COLUMNS, na_values='?')

    train_df = preprocess(train_df)
    eval_df = preprocess(eval_df)

    # Split train and eval data with labels. The pop method copies and removes
    # the label column from the dataframe.
    train_x, train_y = train_df, train_df.pop(_LABEL_COLUMN)
    eval_x, eval_y = eval_df, eval_df.pop(_LABEL_COLUMN)

    # Join train_x and eval_x to normalize on overall means and standard
    # deviations. Then separate them again.
    all_x = pd.concat([train_x, eval_x], keys=['train', 'eval'])
    all_x = standardize(all_x)
    train_x, eval_x = all_x.xs('train'), all_x.xs('eval')

    # Reshape label columns for use with tf.data.Dataset
    train_y = np.asarray(train_y).astype('float32').reshape((-1, 1))
    eval_y = np.asarray(eval_y).astype('float32').reshape((-1, 1))

    return train_x, train_y, eval_x, eval_y
```



- 2번째, `model.py`

> - 데이터 파이프라인을 위한 `tf.data API` 사용
> - `Keras Sequential API`를 사용한 model 코드
> - 입력층으로 DNN 사용하고, 추가로 3개 layer를 쌓는데 `Relu` function을 사용한다.
> - 이진분류이기 때문에 activation은 `sigmoid`로 진행

```python
%%writefile trainer/model.py
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf


def input_fn(features, labels, shuffle, num_epochs, batch_size):
    """Generates an input function to be used for model training.

    Args:
      features: numpy array of features used for training or inference
      labels: numpy array of labels for each example
      shuffle: boolean for whether to shuffle the data or not (set True for
        training, False for evaluation)
      num_epochs: number of epochs to provide the data for
      batch_size: batch size for training

    Returns:
      A tf.data.Dataset that can provide data to the Keras model for training or
        evaluation
    """
    if labels is None:
        inputs = features
    else:
        inputs = (features, labels)
    dataset = tf.data.Dataset.from_tensor_slices(inputs)

    if shuffle:
        dataset = dataset.shuffle(buffer_size=len(features))

    # We call repeat after shuffling, rather than before, to prevent separate
    # epochs from blending together.
    dataset = dataset.repeat(num_epochs)
    dataset = dataset.batch(batch_size)
    return dataset


def create_keras_model(input_dim, learning_rate):
    """Creates Keras Model for Binary Classification.

    The single output node + Sigmoid activation makes this a Logistic
    Regression.

    Args:
      input_dim: How many features the input has
      learning_rate: Learning rate for training

    Returns:
      The compiled Keras model (still needs to be trained)
    """
    Dense = tf.keras.layers.Dense
    model = tf.keras.Sequential(
        [
            Dense(100, activation=tf.nn.relu, kernel_initializer='uniform',
                  input_shape=(input_dim,)),
            Dense(75, activation=tf.nn.relu),
            Dense(50, activation=tf.nn.relu),
            Dense(25, activation=tf.nn.relu),
            Dense(1, activation=tf.nn.sigmoid)
        ])

    # Custom Optimizer:
    # https://www.tensorflow.org/api_docs/python/tf/train/RMSPropOptimizer
    optimizer = tf.keras.optimizers.RMSprop(lr=learning_rate)

    # Compile Keras model
    model.compile(
        loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    return model
```



- 3번째 `task.py`

> - `tf.distribute.MirroredStrategy() ` 를 활용해서 분산 방식으로 학습이 가능하다.
> - 훈련된 모델은 `Tensorflow SavedModel format`으로 저당된다.

```python
%%writefile trainer/task.py
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os

from . import model
from . import util

import tensorflow as tf


def get_args():
    """Argument parser.

    Returns:
      Dictionary of arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--job-dir',
        type=str,
        required=True,
        help='local or GCS location for writing checkpoints and exporting '
             'models')
    parser.add_argument(
        '--num-epochs',
        type=int,
        default=20,
        help='number of times to go through the data, default=20')
    parser.add_argument(
        '--batch-size',
        default=128,
        type=int,
        help='number of records to read during each training step, default=128')
    parser.add_argument(
        '--learning-rate',
        default=.01,
        type=float,
        help='learning rate for gradient descent, default=.01')
    parser.add_argument(
        '--verbosity',
        choices=['DEBUG', 'ERROR', 'FATAL', 'INFO', 'WARN'],
        default='INFO')
    args, _ = parser.parse_known_args()
    return args


def train_and_evaluate(args):
    """Trains and evaluates the Keras model.

    Uses the Keras model defined in model.py and trains on data loaded and
    preprocessed in util.py. Saves the trained model in TensorFlow SavedModel
    format to the path defined in part by the --job-dir argument.

    Args:
      args: dictionary of arguments - see get_args() for details
    """

    train_x, train_y, eval_x, eval_y = util.load_data()

    # dimensions
    num_train_examples, input_dim = train_x.shape
    num_eval_examples = eval_x.shape[0]

    # Create the Keras Model
    keras_model = model.create_keras_model(
        input_dim=input_dim, learning_rate=args.learning_rate)

    # Pass a numpy array by passing DataFrame.values
    training_dataset = model.input_fn(
        features=train_x.values,
        labels=train_y,
        shuffle=True,
        num_epochs=args.num_epochs,
        batch_size=args.batch_size)

    # Pass a numpy array by passing DataFrame.values
    validation_dataset = model.input_fn(
        features=eval_x.values,
        labels=eval_y,
        shuffle=False,
        num_epochs=args.num_epochs,
        batch_size=num_eval_examples)

    # Setup Learning Rate decay.
    lr_decay_cb = tf.keras.callbacks.LearningRateScheduler(
        lambda epoch: args.learning_rate + 0.02 * (0.5 ** (1 + epoch)),
        verbose=True)

    # Setup TensorBoard callback.
    tensorboard_cb = tf.keras.callbacks.TensorBoard(
        os.path.join(args.job_dir, 'keras_tensorboard'),
        histogram_freq=1)

    # Train model
    keras_model.fit(
        training_dataset,
        steps_per_epoch=int(num_train_examples / args.batch_size),
        epochs=args.num_epochs,
        validation_data=validation_dataset,
        validation_steps=1,
        verbose=1,
        callbacks=[lr_decay_cb, tensorboard_cb])

    export_path = os.path.join(args.job_dir, 'keras_export')
    tf.keras.models.save_model(keras_model, export_path)
    print('Model exported to: {}'.format(export_path))



if __name__ == '__main__':
    strategy = tf.distribute.MirroredStrategy()
    with strategy.scope():
        args = get_args()
        tf.compat.v1.logging.set_verbosity(args.verbosity)
        train_and_evaluate(args)

```



#### 2.2 : python 학습 프로그램을 이용하여 로컬 환경에서 학습 진행

> - 위 작업을 GCP 클라우드 AI Platform 위에서 돌리더라도 코드는 거의 비슷하다
> - 아래 코드에서 output directory 명확히 지정해줘야 한다.
> - 그래서 학습된 모델이 지정된 dir에 잘 저장될 수 있도록 세팅!
> - 현재 verbosity 값을 default값으로 turn off 돼 있다. 만약 세팅 희망하면 `--verbosity=DEBUG` 세팅하면 된다.

```python
%%bash

MODEL_DIR=output
gcloud ai-platform local train \
	--module-name trainer.task \
    --package-path trainer/ \
    --job-dir $MODEL_DIR \
    -- \
    --train-files $TRAIN_DATA \
    --eval-files $EVAL_DATA \
    --train-steps 1000 \
    --eval-steps 100
```



> - 모델 결과가 output 폴더에 잘 저장됐는지 확인.

```python
%%bash

ls output/keras_export/
```



#### 2.3 : 입력 데이터 전처리 파이프라인

> - 새로운 입력데이터도 학습 데이터와 동일한 전처리과정이 필요하다. 학습데이터와 input의 shape이 동일해야한다.
> - 학습 시간과 예측 시간이 거의 동일하게 이뤄지는 전처리 파이프라인을 원할 것이다.
> - 아래 코드에서는 eval-data에서 random으로 추출한 데이터를 보여준다.



> - raw 데이터를 전처리하는 과정 확인

```python
from trainer import utill
_, _, eval_x, eval_y = util.load_data()

prediction_input = eval_x.sample(5)
prediction_targets = eval_y[prediction_input.index]
```



> - 전처리 완료된 input 데이터 확인
> - 범주형 컬럼 데이터는 전처리 코드에서 학습데이터에 적용한 그대로 이미 적용돼 있음
> - 연속형 컬럼 데이터(예:age)는 z-score로 정규화진행
> - 몇몇 컬럼(필드)은 빠졌음

```python
print(prediction_input)
```



> - 예측할 input 데이터를 new line으로 json 파일 저장

```python
import json

with open('test.json', 'w') as json_file:
    for row in prediction_input.values.tolist():
        json.dump(row, json_file)
        json_file.write('\n')
```



> - `test.json` 파일 확인

```python
%%bash

cat test.json
```



#### 2.4 예측을 위해 학습된 모델 사용하기

> - 로컬환경에서 사용하는걸로 이해하기

```python
%%bash

gcloud ai-platform local predict \
	--model-dir output/keras_export/ \
    --json-instances ./test.json
```



### Step3. 클라우드 상에서 모델 사용하기

> - 변수 설정하기

```python
%% bash

export PROJECT=$(gcloud config list project --format "value(core.project)")
echo "Your current GCP Project Name is: "${PROJECT} 
```

```python
PROJECT = "위에서 나온 PROJECT 이름 입력"
BUCKET_NAME=PROJECT+"-aiplatform"
REGION="us-central1"
```

```python
os.environ["PROJECT"]= PROJECT
os.environ["BUCKET_NAME"]= BUCKET_NAME
os.environ["REGION"]= REGION
os.environ["TFVERSION"]= "2.1"
os.environ["PYTHONVERSION"]= "3.7"
```



#### 3.1 Cloud Storage bucket

> - ai-platform 클라우드에서 모들을 training하고 prediction하려면 Google Cloud Storage(GCS)에 액세스해야 한다.
> - `BUCKET_NAME`을 활용하여 버킷을 만들고, 로컬에 저장한 데이터를 복사한다.

```python
%%bash

if ! gsutil ls | grep -q gs://${BUCKET_NAME}; then
    gsutil mb -l ${REGION} gs://${BUCKET_NAME}
fi
gsutil cp -r data gs://$BUCKET_NAME/data
```



> - Set the TRAIN_DATA and EVAL_DATA variables to point to the files:

```python
%%bash

export TRAIN_DATA=gs://$BUCKET_NAME/data/adult.data.csv
export EVAL_DATA=gs://$BUCKET_NAME/data/adult.test.csv
```



> - gsutil을 활용해서 test.json 파일을 GCS로 복사

```python
%%bash

gsutil cp test.json gs://$BUCKET_NAME/data/test.json
```



> - TEST_JSON이란 변수를 위 파일경로로 point 설정
>   (Set the TEST_JSON variable to point to that file:)

```python
%%bash

export TEST_JSON=gs://$BUCKET_NAME/data/test.json
```



#### 3.2 GCP에서 싱글 인스턴스 학습기 구동하기

> - basic tier의 싱글 인스턴스 사용한다.
> - job id 생성을 위해 날짜와 시간 사용
> - output 경로를 `OUTPUT_PATH` 변수에 세팅.
> - output 경로는 job id로 지정해주면 좋은 모델 체크포인트 개념이라서 
> - 전체 학습 로그를 확인하고 싶다면 `--verbosity` 에 `DEBUG` 값을 부여

```python
%%bash

JOB_ID=census_$(date -u +%y%m%d_%H%M%S)
OUTPUT_PATH=gs://$BUCKET_NAME/$JOB_ID \
    --job-dir $OUTPUT_PATH \
    --runtime-version $TFVERSION \
    --python-version $PYTHONVERSION \
    --module-name trainer.task \
    --package-path trainer/ \
    --region $REGION \
    -- \
    --train-files $TRAIN_DATA \
    --eval-files $EVAL_DATA \
    --train-steps 1000 \
    --eval-steps 100 \
    --verbosity DEBUG
```

> - 작업 상태를 확인하고 싶다면 아래 명령어로 확인 가능
>   `$ gcloud ai-platform jobs describe census_220228-090128`
>   `$ gcloud ai-platform jobs stream-logs $JOB_ID`



> - 위에서 생성한 job_id로 환경변수 설정

```python
os.environ['JOB_ID']='census_220228_090128'
```



#### 3.3 모델 배포 및 예측

> - 짧은 기간 동안 수많은 예측 요청이 들어오면 AI_Platform에 배포해서 서빙하는 것이 유용하다.



> - AI Platform 모델 만들기

```python
os.environ['MODEL_NAME']='census1'
```

```python
%%bash

gcloud ai-platform models create $MODEL_NAME --regions=$REGION
```

<출력확면>

```output
Using endpoint [https://ml.googleapis.com/]
Created ai platform model [projects/qwiklabs-gcp-04-45199dabb29d/models/census1].
```



> - `MODEL_BINARIES` 변수에 추출된 학습 모델 binaries 전체 경로를 입력해준다. ($OUTPUT_PATH/keras_export/)
> - 모델의 version v1을 만들어서 학습 모델 배포하기

```python
%%bash

OUTPUT_PATH=gs://$BUCKET_NAME/$JOB_ID
MODEL_BINARIES=$OUTPUT_PATH/keras_export/
gcloud ai-platform versions create v1 \
--model $MODEL_NAME \
--origin $MODEL_BINARIES \
--runtime-version $TFVERSION \
--python-version $PYTHONVERSION \
--region=global
```



> - 모델 배포하는 데 몇 분 소요되며
> - 아래 명령어를 통해 배포된 모델 리스트를 확인할 수 있다.

```python
%%bash

gcloud ai-platform models list
```



#### 3.4 배포한 모델에 예측 요청 보내기

> - `test.json` 파일을 이용하여 예측 요청을 보낸다.
> - response에는 예측값이 포함돼 있다.

```python
%%bash

gcloud ai-platform predict \
--model $MODEL_NAME
--version v1
--json-instances ./test.json \
--region global
```

<출력결과>

```output
DENSE_4
[0.31581780314445496]
[0.5926693677902222]
[0.00038980727549642324]
[0.03884931281208992]
[6.94881018716842e-05]
Using endpoint [https://ml.googleapis.com/]
```

> - AI Platform은 배치 예측을 지원한다. 하지만 이번 프로젝트에선 다루지 않는다. 추가로 찾아보길 추천
