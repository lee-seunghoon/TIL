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



### 사분위 DataFrame 만들기

```python
# 18년도 예시
lsv18_df = pd.DataFrame()
lsv18_df['최대'] = [max(new_lsv_18['mean'])]
lsv18_df['최소'] = [min(new_lsv_18['mean'])]
lsv18_df['제1분위'] = [np.percentile(new_lsv_18['mean'],25)]
lsv18_df['제2분위'] = [np.percentile(new_lsv_18['mean'],50)]
lsv18_df['제3분위'] = [np.percentile(new_lsv_18['mean'],75)]
lsv18_df.index = ['2018년도 구성원 LSV']
lsv18_df
```



### Boxplot 구현

```python
plt.figure(figsize=(3,9))
plt.boxplot([new_lsv_18['mean']],
            labels=['18LSV'])
plt.show()
```

