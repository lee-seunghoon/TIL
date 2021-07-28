# 비지도 학습

> - 사이킷런을 이용한 비지도 학습
> - k-평균 군집화 (K-means Clustering) : 데이터 안에서 대표하는 군집의 중심을 찾는 알고리즘
> - 군집화(Clustering)란 : 데이터를 특성에 따라 여러 집단으로 나누는 방법



## k-평균 군집화

> - k개만큼의 중심을 임의로 설정
> - 모든 데이터를 가장 가까운 중심에 할당
> - 같은 중심에 할당된 데이터들을 하나의 군집으로 판단
> - 각 군집 내 데이터들을 가지고 군집의 중심을 새로 구해서 업데이트
> - 이후 또 다시 가까운 중심에 할당되고 위 과정을 반복
> - 반복은 할당되는 데이터에 변화가 없을 때까지 이뤄진다.
> - 반복 종료되면 각 데이터가 마지막으로 할당된 중심에 따라 군집이 나뉨



## 실습 (붓꽃 데이터 군집화)

#### 라이브러리

```python
from sklean.cluster import KMeans
k_means = KMeans(n_cluster=3) # n_cluster = 군집의 개수 (k)
```
