# Random Forest(랜덤 포레스트)

> - Decision Tree (의사결정 나무) 단점 : 오버피팅
>   - 가지치기(Pruning) 방법을 통해 최소화 
>   - 오버피팅을 해결하기 위해 랜덤 포레스트 활용



## 정의

> - 다양한 Decision Tree 모델을 `앙상블` 기법으로 전체 모델 구성
> - 각 Decision Tree 모델로부터 분류 결과를 취합해서 결론 취합
>   - 가장 많이 나온 값을 최종 예측값 
> - 하나의 특징을 예측하기 위한 다양한 요소(`Feature`) 를 사용하는 것이 정확도를 높임
> - But, 다양한 요소(`Feature`)로 인해 오버피팅!



## 앙상블

> - 다수의 학습 알고리즘을 사용



## 배깅 (Bagging)

> - 랜덤 포레스트 모델에서 각 Decision Tree를 생성하는 프로세스
> - 학습 데이터에서 임의 개수만큼 랜덤으로 선택해서 Decision Tree 만들기
> - 각 Decision Tree 만들 때마다 임의의 데이터를 사용하는데 이때 중요한 것은 `중복` 을 허용!
> - ex) 1000개의 행이 있는 가방에서 임의로 100개를 뽑아 첫 번째 트리를 만들고 100개의 행은 가방에 도로 집어 넣는다. 그리고 다시 1000개의 행에서 임의로 100개를 뽑아 두 번째 트리를 만든 후 다시 가방에 집어 넣는다...



## Bagging Features

> - 각 Tree에 다양성을 주기 위해 사용될 특성(Feature)들을 제한
> - 각 분할에서 전체 속성들 중 일부만 고려하여 트리를 작성
>   - 총 속성이 25개면 랜덤으로 5개, 즉 전체 속성 개수의 제곱근만큼 선택!
>   - ex. 일부 속성만을 활용해서 정보 획득량이 가장 높은 기준으로 데이터 분할



## 사이킷런 파라미터

- `n_estimators` : Random Forest 안 Decision Tree 개수
  - n_estimators는 클수록 좋다.
  - Decision Tree가 많을수록 더 깔끔한 Decision Boundary 나옴.
  - Default = 10
- `max_features` : 무작위로 선택할 Feature 개수
  - max_features = n_features이면 30개의 feature 중 30개의 feature 모두 선택
  - bootstrap = True이면 30개의 feature에서 복원 추출로 30개 추출
    - 특성 선택의 무작위성이 없어진거지 샘플링의 무작위성을 그대로
  - 그러므로, max_features 값이 크면 각 Decision Tree가 매우 비슷해짐
  - 반대로, max_features 값이 작아지면 각 Decision Tree가 달라지면서 오버피팅 문제 해결
  - max_features는 일반적으로 Default 값 사용
- `max_depth` : 트리의 깊이를 의미
- `min_samples_leaf` : 리프노드가 되기 위한 최소한의 샘플 데이터 수
- `min_samples_split` : 노드를 분할하기 위한 최소한의 데이터 수
- `max_leaf_nodes` : 리프노드의 최대 개수

