# Multinomial Classification (Multi-Class)

- 다중 분류
- Label의 Class가 3개 이상을 의미
- ex) 조직의 6가지 유형을 분류 / 동식물의 다양한 유형을 분류 등
- multinomial로 모델을 구성할 때 맞는 하이퍼파라미터를 찾아보자



## Multi-Nomial Logistic 통계분석 (MNLogit)

> - statsmodels.api.MNLogit()

```python
# 라이브러리
import statsmodels.api as sm

# 독립변수 x / 종속변수 y 라고 가정
# 종속변수가 다항분류인 데이터의 상관관계를 확인하기 윟새 MNLogit 생성
logit_model = sm.MNLogit(y, sm.add_constant(x))
result = logit_model.fit()

# 분석 결과 보고서 확인
result.summary()

# 또다른 형태의 2차보고서(?) 확인
result.summary2()
```



## VIF

> - 10을 초과하면 다중공선성이 있다고 판단한다.
> - 5를 초과할 경우 다중공선선의 위험이 있다고 판단한다.

```python
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

# VIF 값 확인할 독립변수 데이터
x_data = df.iloc[:,1:] # 예시

# VIF를 표현한 데이터프레임 생성
vif_df = pd.DataFrame()

# 컬럼명으로 독립변수명을 설정
vif_df['features'] = x_data.columns

# statsmodels 라이브러리에서 variance_influence_factor 모듈을 활용한다.
# 독립변수들 간의 관계를 확인하는 게 다중공선성이라서 독립변수만 입력한다.
vif_df['VIF'] = [variance_influence_factor(x_data.values, i) for i in range(x_data.shape[1])]
```





## Logistic Regression

> - `multi_class` = 'ovr'
>   - `one vs rest` 방식을 의미
>   - 각 클래스를 분류할 이진분류의 직선을 그린 후
>   - 교차하는 부분을 각 class의 데이터와 거리를 구해
>   - 가장 가까운 영역을 그 class의 영역으로 설정하는 방식
>   - 단점은 모든 데이터를 활용해 거리를 구해야 해서 데이터가 많다면 시간이 오래걸림

```python
from sklearn.linear_model import LogisticRegrssion

# C는 규제 강도를 설정하는 하이퍼파라미터 (penalty 파라미터와 연관있음) - 과적합을 해소하기 위해 사용 (0.001 ~ 100 정도까지 다양하게 테스트 필요)
# class_weight == Label의 class가 골고루 분포돼 있는 게 아니라, 편향적으로 분포돼 있을경우 'balanced' 사용
# multi_class == 'auto' / 'ovr' / 'multinomial' 사용
# solver == 최적화를 위한 알고리즘 {‘newton-cg’, ‘lbfgs’, ‘liblinear’, ‘sag’, ‘saga’}, default=’lbfgs’
# 		적은 데이터셋에 대해서는 ‘liblinear’가 좋은 선택이다.
#		반대로 큰 데이터셋이 대해서는 ‘sag’, ‘saga’ 알고리즘이 더 빠르다
# 		다중분류에 있어서는 ‘newton-cg’, ‘lbfgs’, ‘sag’, ‘saga’ 알고리즘만 가능하다
# 		‘liblinear’는 one-versus-rest(ovr) 방식에 적합하다.
#		‘newton-cg’, ‘lbfgs’, ‘sag’, ‘saga’ 알고리즘은 L2 penalty를 다루든가 아니면 아예 없다.

logit_model = LogisticRegression(C=1,
                                 class_weight='balanced',
                                 multi_class='ovr',
                                 n_jobs=-1,
                                 solver='lbfgs')
```



## Decision Tree

> - `max_depth` : 트리의 최대 깊이를 의미하며, default값인 `None`으로 설정되면 클래스 분류를 완변하게 할 때까지 노드를 분할하면서 모델을 구성한다. `과적합(overfitting)`을 방지하기 위해 설정하는 경우가 많다.
> - `min_samples_split` : 각 노드가 만들어질 때 사용할 데이터 비율을 설정하는 파라미터이고, 0.1 ~ 1 의 단위로 세팅한다.
> - `min_samples_leaf` : 마지막 노드들을 리프노드라고 하는데, 이 리프노드에서 사용할 최소 데이터 수를 세팅하는 파러미터를 의미한다.
> - `max_features` : 최적의 모델을 구성하기 위해, feature(독립변수)를 최대 몇개까지 사용할 지 정하는 파라미터다.

```python
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(
	max_depth = 20,
    min_samples_split = 0.5,
    min_samples_leaf = 0.5,
    max_features = 50
)

clf.fit(train_x, train_y)

train_score = clf.score(train_x, train_y)
test_score = clf.score(train_x, train_y)

print('train accuracy :', train_score)
print('test accuracy :', test_score)
```



## XGboost 특징

> - Tree 계열 알고리즘을 활용한 앙상블 학습 모델
> - 최적의 성능을 보이는 `GradientBoosting`의 느린 속도를 보완하면서 동일한 퍼포먼스를 보여주는 모델 
> - `오버피팅(과대적합)` 문제를 효율적으로 해결하는 모델 
> - 모델 내부적으로 보유한 교차검증 시스템을 활용해서 최대 반복횟수 세팅을 통해 `early stop`이 가능함(무한정 학습하지 않음)



## XGboost 하이퍼파라미터

> - **learning_rate** : 학습률을 의미하면 0~1까지의 숫자 입력 가능  
> - **n_estimators** : 랜덤포레스트에서 트리 모델 개수를 지정하는 것과 같이, 생성할 weak learner 즉, 약한 학습 분류기의 개수를 세팅하는 파라미터 
> - **min_child_weight** : 오버피팅을 규제하기 위해 튜닝하며, 관측치에 대한 가중치 합의 최소를 의미, 수가 커질수록 under fitting 가능성 높음, 범위는 0 ~ ∞ 
> - **max_depth** : 트리 기반의 파라미터와 동일한 의미를 가지며, 0을 지정하면 깊이의 제한이 없고, 너무 크면 오버피팅 문제를 불러오기 때문에 통상 3~ 10정도까지 세팅하는 경우가 많음, 범위는 0 ~ ∞ 
> - **gamma** : leaf node의 추가 분할을 결정하기 위한 최소손실 감소값을 의미, 값이 클수록 오버피팅 감소효과, 범위는 마찬가지로 0 ~ ∞ 
> - **objective**     
>   1) 회귀일 경우 = 'reg:linear'    
>   2) 이진분류일 경우 = 'binary:logistic'    
>   3) 다중분류이면서 class를 그대로 return 하고 싶을 경우 = 'multi:softmax'    
>   4) 다중분류이면서 각 class에 속할 확률을 return 하고 싶을 경우 = 'multi:softprob'

```python
import xgboost as xgb

model = xgb.XGBoostClassifier(
    n_estimators=200, # 100이 default 값
	objective='binary:logistic',
    n_jobs=-1,
    random_state=0
)
model.fit(train_x,
          train_y,
          eval_metric = 'error' # 이진분류일 경우 ==> 'error','logloss' 주로 사용
								# 다중분류일 경우 ==> 'merror','mlogloss' 주로 사용
          eval_set=[(test_x, test_y)],
          early_stopping_rounds=50)
```





## DNN

```python
# 라이브러리
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import LabelEncoder

# DNN 모델 구성
model = Sequential()
model.add(Dense(64, input_dim=128, activation='relu')) # ==> input_dim은 독립변수의 개수(feature의 개수)
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(6, activation='softmax'))

# 모델 컴파일
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# 모델 적합
model.fit(train_x, train_y, epochs=20, batch_size=64)

# 정확도 점수
model.evaluate(test_x, text_y)[1]

```

