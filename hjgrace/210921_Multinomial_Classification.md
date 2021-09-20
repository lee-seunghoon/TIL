# Multinomial Classification (Multi-Class)

- 다중 분류
- Label의 Class가 3개 이상을 의미
- ex) 조직의 6가지 유형을 분류 / 동식물의 다양한 유형을 분류 등
- multinomial로 모델을 구성할 때 맞는 하이퍼파라미터를 찾아보자



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

