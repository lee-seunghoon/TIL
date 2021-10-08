## 라이브러리

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
```



## 데이터 로드

```python
path = './retirement_prediction.csv'
df = pd.read_csv(path)
```



## 데이터 정보 및 분포 파악

```python
df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 14999 entries, 0 to 14998
Data columns (total 10 columns):
 #   Column                 Non-Null Count  Dtype  
---  ------                 --------------  -----  
 0   satisfaction_level     14999 non-null  float64
 1   last_evaluation        14999 non-null  float64
 2   number_project         14999 non-null  int64  
 3   average_montly_hours   14999 non-null  int64  
 4   time_spend_company     14999 non-null  int64  
 5   Work_accident          14999 non-null  int64  
 6   left                   14999 non-null  int64  
 7   promotion_last_5years  14999 non-null  int64  
 8   department             14999 non-null  object 
 9   salary                 14999 non-null  object 
dtypes: float64(2), int64(6), object(2)
memory usage: 1.1+ MB
'''
```

```python
# 결측치 확인
df.isna().sum()
'''
satisfaction_level       0
last_evaluation          0
number_project           0
average_montly_hours     0
time_spend_company       0
Work_accident            0
left                     0
promotion_last_5years    0
department               0
salary                   0
dtype: int64
'''
```

```python
df.describe()
'''
	satisfaction_level	last_evaluation	number_project	average_montly_hours	time_spend_company	Work_accident	left	promotion_last_5years
count	14999.000000	14999.000000	14999.000000	14999.000000	14999.000000	14999.000000	14999.000000	14999.000000
mean	0.612834	0.716102	3.803054	201.050337	3.498233	0.144610	0.238083	0.021268
std	0.248631	0.171169	1.232592	49.943099	1.460136	0.351719	0.425924	0.144281
min	0.090000	0.360000	2.000000	96.000000	2.000000	0.000000	0.000000	0.000000
25%	0.440000	0.560000	3.000000	156.000000	3.000000	0.000000	0.000000	0.000000
50%	0.640000	0.720000	4.000000	200.000000	3.000000	0.000000	0.000000	0.000000
75%	0.820000	0.870000	5.000000	245.000000	4.000000	0.000000	0.000000	0.000000
max	1.000000	1.000000	7.000000	310.000000	10.000000	1.000000	1.000000	1.000000
'''

```

```python
# 문자열 데이터 분포 확인
df.describe(include='O')
'''
	  department	salary
count	   14999	 14999
unique	      10	     3
top	       sales	   low
freq		4140	  7316
'''
```

```python
# salary 컬럼 확인
df['salary'].value_counts()
'''
low       7316
medium    6446
high      1237
Name: salary, dtype: int64
'''
```

```python
# department 컬럼 확인
df['department'].value_counts()
'''
sales          4140
technical      2720
support        2229
IT             1227
product_mng     902
marketing       858
RandD           787
accounting      767
hr              739
management      630
Name: department, dtype: int64
'''
```



## 이상치 확인

```python
# 박스플랏으로 이상치 확인
# satisfaction_level 변수를 제외하고 나머지 독립변수 8개를 한번에 확인하기

# 도화지를 그린다
fig = plt.figure(figsize=(10, 12))

# 기본 도화지 위에 세부 도화지를 세팅한다
# 행렬의 개념으로 가로 2줄(행) 세로 3줄(열)로 세팅한다, 그리고 이 도화지가 몇번째 위치할지 정해준다.
# add_subplot(행, 열, 위치)
x1 = fig.add_subplot(2,3,1)
x2 = fig.add_subplot(2,3,2)
x3 = fig.add_subplot(2,3,3)
x4 = fig.add_subplot(2,3,4)
x5 = fig.add_subplot(2,3,5)
x6 = fig.add_subplot(2,3,6)

# 각 도화지에 bboxplot 그려준다
x1.boxplot(df['last_evaluation'])
x2.boxplot(df['number_project'])
x3.boxplot(df['average_montly_hours'])
x4.boxplot(df['time_spend_company'])
x5.boxplot(df['Work_accident'])
x6.boxplot(df['promotion_last_5years'])

plt.tight_layout()
plt.show()
```



## 데이터 전처리

```python
# 독립변수 데이터 인코딩
# 1. salary
encoding_map = {'low':0,
                'medium':1,
                'high':2}

df['salary'] = df['salary'].map(encoding_map)

# 값 확인
df['salary'].value_counts()
'''
0    7316
1    6446
2    1237
Name: salary, dtype: int64
'''
```

```python
# 2. department

# 손쉽게 인코딩 해주는 라이브러리
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
encoder.fit(df['department'])
encoding_class = encoder.transform(df['department'])
encoding_class
# array([7, 7, 7, ..., 8, 8, 8])
```

```python
# 데이터 분리

# 독립변수(설명변수)
x_data = df.drop('left', axis=1, inplace=False)

# 종속변수(결과변수)
y_data = df['left']

# train test data 분리
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(x_data, y_data, test_size=0.3, stratify=y_data, random_state=0)
```

