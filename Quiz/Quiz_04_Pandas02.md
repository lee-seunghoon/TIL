# Pandas 연습문제.02 



## Q1

```txt
displ(배기량)이 4 이하인 자동차와 5 이상인 자동차 중 어떤 자동차의 hwy(고속도로 연비)가 평균적으로 더 높은지 확인하세요.
```

* 정답 코드

  ```python
  import numpy as np
  import pandas as pd
  
  mpg_data = pd.read_csv('mpg.txt')
  hwy_4 = mpg_data[mpg_data['displ']<=4.0]['hwy'].mean()
  hwy_5 = mpg_data[mpg_data['displ']>=5.0]['hwy'].mean()
  
  print('배기량 4이하인자동차 :',hwy_4)
  # ==> 배기량 4이하인자동차 : 25.96319018404908
  print('배기량 5이상인자동차 :',hwy_5)
  # ==> 배기량 5이상인자동차 : 18.07894736842105
  ```
  
  



## Q2

```txt
자동차 제조 회사에 따라 도시 연비가 다른지 알아보려고 한다. 
"audi"와 "toyota" 중 어느 manufacturer(제조회사)의 cty(도시 연비)가 평균적으로 더 높은지 확인하세요.
```

* 정답 코드

  ```python
  import numpy as np
  import pandas as pd
  
  mpg_data = pd.read_csv('mpg.txt')
  df = mpg_data['cty'].groupby(mpg_data['manufacturer'])
  audi_cty_mean = df.get_group('audi').mean()
  toyota_cty_mean = df.get_group('toyota').mean()
  
  print('audi의도시연비평균 :', audi_cty_mean)
  # ==> audi의도시연비평균 : 17.61111111111111
  print('toyota의도시연비평균 :', toyota_cty_mean)
  # ==> toyota의도시연비평균 : 18.529411764705884
  ```



## Q3

```txt
"chevrolet", "ford", "honda" 자동차의 고속도로 연비 평균을 알아보려고 한다. 
이 회사들의 데이터를 추출한 후 hwy(고속도로 연비) 평균을 구하세요.
```

* 정답 코드

  ```python
  import numpy as np
  import pandas as pd
  
  mpg_data = pd.read_csv('mpg.txt')
  df = mpg_data['hwy'].groupby(mpg_data['manufacturer'])
  
  chevrolet_hwy_mean = df.get_group('chevrolet')
  ford_hwy_mean = df.get_group('ford')
  honda_hwy_mean = df.get_group('honda')
  
  #Series도 concatenation으로 연결 가능!
  df_connect = pd.concat([chevrolet_hwy_mean, ford_hwy_mean, honda_hwy_mean],axis=0)
  print('hwy(고속도로 연비) 평균 :',df_connect.mean())
  # ==> hwy(고속도로 연비) 평균 : 22.50943396226415
  ```



## Q4

```txt
"audi"에서 생산한 자동차 중에 어떤 자동차 모델의 hwy(고속도로 연비)가 높은지 알아보려고 한다. "audi"에서 생산한 자동차 중 hwy가 1~5위에 해당하는 자동차의 데이터를 출력하세요.
```

* 정답코드

  ```python
  import numpy as np
  import pandas as pd
  
  mpg_data = pd.read_csv('mpg.txt')
  df = mpg_data['hwy'].groupby(mpg_data['manufacturer'])
  audi_hwy_ascend = df.get_group('audi').sort_values(ascending=False).head()
  print(mpg_data.iloc[audi_hwy_ascend.index,:])
  
  '''
  manufacturer       model  displ  year  cyl       trans drv  cty  hwy fl  \
  2         audi          a4    2.0  2008    4  manual(m6)   f   20   31  p   
  3         audi          a4    2.0  2008    4    auto(av)   f   21   30  p   
  0         audi          a4    1.8  1999    4    auto(l5)   f   18   29  p   
  1         audi          a4    1.8  1999    4  manual(m5)   f   21   29  p   
  9         audi  a4 quattro    2.0  2008    4  manual(m6)   4   20   28  p   
  
       class  
  2  compact  
  3  compact  
  0  compact  
  1  compact  
  9  compact  
  '''
  ```
  
  

## Q5

```txt
mpg 데이터는 연비를 나타내는 변수가 2개입니다. 
두 변수를 각각 활용하는 대신 하나의 통합 연비 변수를 만들어 사용하려 합니다. 
평균 연비 변수는 두 연비(고속도로와 도시)의 평균을 이용합니다. 
회사별로 "suv" 자동차의 평균 연비를 구한후 내림차순으로 정렬한 후 1~5위까지 데이터를 출력하세요.
```

* 정답 코드

  ```python
  import numpy as np
  import pandas as pd
  
  mpg_data = pd.read_csv('mpg.txt')
  suv_data = mpg_data[mpg_data['class']=='suv']
  new_df = suv_data[['cty','hwy']].groupby(suv_data['manufacturer'])
  avg_fuel_efficiency = new_df.mean().mean(axis=1).sort_values(ascending=False)
  display(avg_fuel_efficiency)
  
  '''
  manufacturer
  subaru        21.916667
  toyota        16.312500
  nissan        15.875000
  mercury       15.625000
  jeep          15.562500
  ford          15.333333
  chevrolet     14.888889
  lincoln       14.166667
  land rover    14.000000
  dodge         13.928571
  dtype: float64
  '''
  
  ```



## Q6

```txt
mpg 데이터의 class는 "suv", "compact" 등 자동차의 특징에 따라 일곱 종류로 분류한 변수입니다. 
어떤 차종의 도시 연비가 높은지 비교하려 합니다. 
class별 cty 평균을 구하고 cty 평균이 높은 순으로 정렬해 출력하세요.
```

* 정답 코드

  ```python
  import numpy as np
  import pandas as pd
  
  mpg_data = pd.read_csv('mpg.txt')
  class_df = mpg_data['cty'].groupby(mpg_data['class'])
  display(class_df.mean().sort_values(ascending=False))
  
  '''
  class
  subcompact    20.371429
  compact       20.127660
  midsize       18.756098
  minivan       15.818182
  2seater       15.400000
  suv           13.500000
  pickup        13.000000
  Name: cty, dtype: float64
  '''
  ```
  
  

## Q7

```txt
어떤 회사 자동차의 hwy(고속도로 연비)가 가장 높은지 알아보려 합니다. 
hwy(고속도로 연비) 평균이 가장 높은 회사 세 곳을 출력하세요.
```

* 정답 코드

  ```python
  import numpy as np
  import pandas as pd
  
  mpg_data = pd.read_csv('mpg.txt')
  hwy_df = mpg_data['hwy'].groupby(mpg_data['manufacturer'])
  hwy_df_mean = hwy_df.mean().sort_values(ascending=False)
  display(hwy_df_mean[:3])
  
  '''
  manufacturer
  honda         32.555556
  volkswagen    29.222222
  hyundai       26.857143
  Name: hwy, dtype: float64
  '''
  ```
  
  

## Q8

```txt
어떤 회사에서 "compact" 차종을 가장 많이 생산하는지 알아보려고 합니다. 
각 회사별 "compact" 차종 수를 내림차순으로 정렬해 출력하세요.
```

* 정답 코드

  ```python
  import numpy as np
  import pandas as pd
  
  mpg_data = pd.read_csv('mpg.txt')
  compact_df = mpg_data[mpg_data['class']=='compact']
  compact_num = compact_df['class'].groupby(compact_df['manufacturer'])
  display(compact_num.count().sort_values(ascending=False))
  
  '''
  manufacturer
  audi          15
  volkswagen    14
  toyota        12
  subaru         4
  nissan         2
  Name: class, dtype: int64
  '''
  ```
  
