### 라이브러리

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```



### 경로 설정

```python
lsv_path = './210708_(18-20).xlsx'
lsv18 = pd.read_excel(lsv_path, sheet_name=2)
lsv19 = pd.read_excel(lsv_path, sheet_name=1)
lsv20 = pd.read_excel(lsv_path, sheet_name=0)
```



### 연도별 사분위 데이터프레임 구하는 함수

```python
def lsv_boxplot(lsv_mean, year):
    lsv_df = pd.DataFrame()
    iqr = np.percentile(lsv_mean['mean'],75) - np.percentile(lsv_mean['mean'],25)
    q1 = np.percentile(lsv_mean['mean'],25)
    q2 = np.percentile(lsv_mean['mean'],50)
    q3 = np.percentile(lsv_mean['mean'],75)

    lsv_df['최대'] = [max(lsv_mean['mean'])]
    lsv_df['최소'] = [min(lsv_mean['mean'])]
    lsv_df['최저한계치'] = [q1-(1.5*iqr)]
    lsv_df['제1사분위'] = [q1]
    lsv_df['제2사분위'] = [q2]
    lsv_df['제3사분위'] = [q3]
    lsv_df.index = ['{}년도 구성원 LSV'.format(year)]
    
    return lsv_df
```





### 사번을 기준으로 평가 점수 평균

```python
#2018년
lsv_18G = lsv18.groupby(lsv18['num'])
lsv18_mean = lsv_18G.mean()
new_lsv_18 = pd.DataFrame({
    'num':lsv18_mean.index.values,
    'mean':lsv18_mean.values.ravel()
})
new_lsv_18.to_excel('210708_LSV18.xlsx', index=False)
new_lsv_18

#2019년
lsv_19G = lsv19.groupby(lsv19['num'])
lsv19_mean = lsv_19G.mean()
new_lsv_19 = pd.DataFrame({
    'num':lsv19_mean.index.values,
    'mean':lsv19_mean.values.ravel()
})
new_lsv_19.to_excel('210708_LSV19.xlsx', index=False)
new_lsv_19

#2020년
lsv_20G = lsv20.groupby(lsv20['num'])
lsv20_mean = lsv_20G.mean()
new_lsv_20 = pd.DataFrame({
    'num':lsv20_mean.index.values,
    'mean':lsv20_mean.values.ravel()
})
new_lsv_20.to_excel('210708_LSV20.xlsx', index=False)
new_lsv_20
```



### 각 연도별 사분위 DataFrame 만들기

```python
# 2018년도
lsv_boxplot(new_lsv_18, 2018)

# 2019년도
lsv_boxplot(new_lsv_19, 2019)

# 2020년도
lsv_boxplot(new_lsv_20, 2020)
```



### 각 연도별 Boxplot 구현

```python
# 2018년도
plt.figure(figsize=(3,9))
plt.boxplot([new_lsv_18['mean']],
            labels=['18LSV'])
plt.show()

# 2019년도
plt.figure(figsize=(3,9))
plt.boxplot([new_lsv_19['mean']],
            labels=['19LSV'])
plt.show()

# 2020년도
plt.figure(figsize=(3,9))
plt.boxplot([new_lsv_20['mean']],
            labels=['20LSV'])
plt.show()
```

