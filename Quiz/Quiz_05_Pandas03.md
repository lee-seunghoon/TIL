# Pandas 연습문제.03



## Q1

```txt
<성별에 따른 월급 차이>
과거에 비해 여성의 사회 진출이 활발하지만 직장에서의
위상에서는 여전히 차별이 존재하고 있는것이 사실.
실제로 그러한지 월급의 차이를 이용하여 사실을 확인해보자
```

* 정답 코드

  ```python
  import numpy as np
  import pandas as pd
  import savReaderWriter
  
  with savReaderWriter.SavReader('./data/Koweps/Koweps_hpc10_2015_beta1.sav',
                                 ioUtf8=True) as reader :
      df = pd.DataFrame(reader.all(), columns = [i for i in reader.header] )
  
  all_df = df[['h10_g3','h10_g4','h10_g10','h10_g11',
              'h10_eco9', 'p1002_8aq1', 'h10_reg7']]
  ues_df = df[['h10_g3','p1002_8aq1']]
  
  gender_payroll = use_df['p1002_8aq1'].groupby(use_df['h10_g3'])
  gender_payroll_mean = gender_payroll.mean()
  
  print('남성 평균 월급 :',round(gender_payroll_mean.iloc[0],4))
  print('여성 평균 월급 :',round(gender_payroll_mean.iloc[1],4))
  
  '''
  남성 평균 월급 : 312.2932
  여성 평균 월급 : 162.1997
  '''
  ```
  
  



## Q2

```txt
<나이와 월급의 관계>
평균적으로 몇 살 때 월급을 가장 많이 받을까? 
또 그때의 평균 월급은 얼마인가?
```

* 정답 코드

  ```python
  import numpy as np
  import pandas as pd
  import savReaderWriter
  
  with savReaderWriter.SavReader('./data/Koweps/Koweps_hpc10_2015_beta1.sav',
                                 ioUtf8=True) as reader :
      df = pd.DataFrame(reader.all(), columns = [i for i in reader.header] )
  
  all_df = df[['h10_g3','h10_g4','h10_g10','h10_g11',
              'h10_eco9', 'p1002_8aq1', 'h10_reg7']]
  ues_df = df[['h10_g4','p1002_8aq1']]
  age_wage = use_df['p1002_8aq1'].groupby(use_df['h10_g4'])
  age_wage_mean = age_wage.mean().dropna(how = 'any')
  age_wage_max = age_wage_mean.max()
  result = age_wage_mean[age_wage_mean.values == age_wage_max]
  
  print('월급을 가장 많이 받는 나이는 : {}살, 월급 : {}'\
        .format(int(2021.0-result.index[0]+1), round(result.iloc[0],4)))
  # ==> 월급을 가장 많이 받는 나이는 : 59살, 월급 : 318.6777
  ```



## Q3

```txt
<연령대에 따른 월급 차이>
30세 미만을 초년(young)
30~59세 : 중년(middle) 
60세 이상 : 노년(old)
위의 범주로 연령대에 따른 월급의 차이를 알아보자
```

* 정답 코드

  ```python
  import numpy as np
  import pandas as pd
  import savReaderWriter
  
  with savReaderWriter.SavReader('./data/Koweps/Koweps_hpc10_2015_beta1.sav',
                                 ioUtf8=True) as reader :
      df = pd.DataFrame(reader.all(), columns = [i for i in reader.header] )
  
  all_df = df[['h10_g3','h10_g4','h10_g10','h10_g11',
              'h10_eco9', 'p1002_8aq1', 'h10_reg7']]
  
  use_df = df[['h10_g4','p1002_8aq1']]
  
  new_age = []
  for i in use_df['h10_g4']:
      new_age.append(2021 - i + 1)
  use_df['h10_g4'] = new_age
  #print(use_df)
  
  age_young_mask = use_df['h10_g4']<30.0
  age_middle_mask = (use_df['h10_g4'] >= 30.0) & (use_df['h10_g4'] < 60.0)
  age_old_mask = use_df['h10_g4']>60.0
  
  young_mean = use_df.loc[age_young_mask, 'p1002_8aq1'].mean()
  middle_mean = use_df.loc[age_middle_mask, 'p1002_8aq1'].mean()
  old_mean = use_df.loc[age_old_mask, 'p1002_8aq1'].mean()
  print('초년(young) : {}\n중년(middle) : {}\n노년(old) : {}'\
        .format(round(young_mean,4),round(middle_mean,4),round(old_mean,4)))
  
  '''
  초년(young) : 125.0621
  중년(middle) : 269.0704
  노년(old) : 173.8035
  '''
  ```



## Q4

```txt
<연령대 및 성별 월급 차이>
성별 월급 차이는 연령대에 따라 다른 양상을 보일 수 있습니다.
성별 월급 차이가 연령대에 따라 다른지 분석해보자
기존에는 3그룹(초년,중년,노년)이었지만 이젠 6그룹으로
그룹핑을 해야 한다.(초년남성,초년여성,..)
```

* 정답코드

  ```python
  import numpy as np
  import pandas as pd
  import savReaderWriter
  
  with savReaderWriter.SavReader('./data/Koweps/Koweps_hpc10_2015_beta1.sav',
                                 ioUtf8=True) as reader :
      df = pd.DataFrame(reader.all(), columns = [i for i in reader.header] )
  
  all_df = df[['h10_g3','h10_g4','h10_g10','h10_g11',
              'h10_eco9', 'p1002_8aq1', 'h10_reg7']]
  
  use_df = df[['h10_g3','h10_g4','p1002_8aq1']]
  
  new_age = []
  for i in use_df['h10_g4']:
      new_age.append(2021 - i + 1)
  use_df['h10_g4'] = new_age
  
  age_young_mask = use_df['h10_g4']<30.0
  age_middle_mask = (use_df['h10_g4'] >= 30.0) & (use_df['h10_g4'] < 60.0)
  age_old_mask = use_df['h10_g4']>60.0
  
  
  new_df = use_df.groupby(use_df['h10_g3'])
  
  male = new_df.get_group(1.0)
  female = new_df.get_group(2.0)
  
  male_young_mean = male.loc[age_young_mask,'p1002_8aq1'].mean()
  female_young_mean = female.loc[age_young_mask,'p1002_8aq1'].mean()
  male_middle_mean = male.loc[age_middle_mask,'p1002_8aq1'].mean()
  female_middle_mean = female.loc[age_middle_mask,'p1002_8aq1'].mean()
  male_old_mean = male.loc[age_old_mask,'p1002_8aq1'].mean()
  female_old_mean = female.loc[age_old_mask,'p1002_8aq1'].mean()
  print('# 초년 남성 : {}\n# 초년 여성 : {}\n# 중년 남성 : {}\n\
  # 중년 여성 : {}\n# 노년 남성 : {}\n# 노년 여성 : {}'\
  .format(round(male_young_mean,5),round(female_young_mean,5),\
          round(male_middle_mean,5),round(female_middle_mean,5),\
          round(male_old_mean,5),round(female_old_mean,5)))
  
  '''
  # 초년 남성 : 116.80852
  # 초년 여성 : 128.97175
  # 중년 남성 : 335.60367
  # 중년 여성 : 188.74636
  # 노년 남성 : 244.37938
  # 노년 여성 : 103.11276
  '''
  ```
  
  

## Q5

```txt
<직업별 월급 차이>
   어떤 직업이 월급을 가장 많이 받을까?
   직업별 월급을 분석해 보자
   직업코드는 제공된 Koweps_Codebook.xlsx을 이용하면 
   편하게 코드값을 이용 할 수 있습니다.
```

* 정답 코드

  ```python
  import numpy as np
  import pandas as pd
  import savReaderWriter
  
  with savReaderWriter.SavReader('./data/Koweps/Koweps_hpc10_2015_beta1.sav',
                                 ioUtf8=True) as reader :
      df = pd.DataFrame(reader.all(), columns = [i for i in reader.header] )
  
  all_df = df[['h10_g3','h10_g4','h10_g10','h10_g11',
              'h10_eco9', 'p1002_8aq1', 'h10_reg7']]
  
  jobcode = pd.read_csv('./data/Koweps/jobcode.csv', encoding='utf-8')
  jobcode = jobcode.rename({'code_job':'h10_eco9'}, axis = 1)
  
  job_wage = all_df['p1002_8aq1'].groupby(all_df['h10_eco9'])
  job_wage_mean = job_wage.mean()
  
  df_merge = pd.merge(job_wage_mean,jobcode, on = 'h10_eco9', how = 'outer')
  
  # display(job_wage_mean[job_wage_mean.values == job_wage.mean().max()])
  print(df_merge[df_merge['p1002_8aq1'] == job_wage.mean().max()])
  
  '''
        h10_eco9  p1002_8aq1                 job
  23     233.0    845.066667  금속 재료 공학 기술자 및 시험원
  '''
  ```



## Q6

```txt
<성별 직업 빈도>
   성별로 어떤 직업이 가장 많을까?
```

* 정답 코드

  ```python
  import numpy as np
  import pandas as pd
  import savReaderWriter
  
  with savReaderWriter.SavReader('./data/Koweps/Koweps_hpc10_2015_beta1.sav',
                                 ioUtf8=True) as reader :
      df = pd.DataFrame(reader.all(), columns = [i for i in reader.header] )
  
  all_df = df[['h10_g3','h10_g4','h10_g10','h10_g11',
              'h10_eco9', 'p1002_8aq1', 'h10_reg7']]
  
  jobcode = pd.read_csv('./data/Koweps/jobcode.csv', encoding='utf-8')
  jobcode = jobcode.rename({'code_job':'h10_eco9'}, axis = 1)
  
  df_merge = pd.merge(all_df, jobcode, on='h10_eco9', how = 'left')
  use_df = df_merge[['h10_g3','job']]
  
  male_job = use_df[use_df['h10_g3']==1.0]['h10_g3'].groupby(use_df['job'])
  asc_male_job = male_job.count().sort_values(ascending=False)
  
  female_job = use_df[use_df['h10_g3']==2.0]['h10_g3'].groupby(use_df['job'])
  asc_female_job = female_job.count().sort_values(ascending=False)
  
  print('남성 가장 많은 직업 :{}, {}명'.format(asc_male_job.index[0], asc_male_job[0]))
  print('여성 가장 많은 직업 :{}, {}명'.format(asc_female_job.index[0], asc_female_job[0]))
  
  '''
  남성 가장 많은 직업 :작물재배 종사자, 640명
  여성 가장 많은 직업 :작물재배 종사자, 680명
  '''
  ```
  
  

## Q7

```txt
<종교 유무에 따른 이혼율>
   종교가 있는 사람들이 이혼을 덜 할까??
```

* 정답 코드

  ```python
  import numpy as np
  import pandas as pd
  import savReaderWriter
  
  with savReaderWriter.SavReader('./data/Koweps/Koweps_hpc10_2015_beta1.sav',
                                 ioUtf8=True) as reader :
      df = pd.DataFrame(reader.all(), columns = [i for i in reader.header] )
  
  all_df = df[['h10_g3','h10_g4','h10_g10','h10_g11',
              'h10_eco9', 'p1002_8aq1', 'h10_reg7']]
  
  use_df = df[['h10_g10','h10_g11']]
  
  faith = use_df[use_df['h10_g11']==1.0]
  none_faith = use_df[use_df['h10_g11']==2.0]
  
  divorce_mask = use_df['h10_g10']==3.0
  
  faith_divorced = faith.loc[divorce_mask,:]
  none_faith_divorced = none_faith.loc[divorce_mask,:]
  
  faith_divorce_ratio = len(faith_divorced) / len(faith) * 100
  non_faith_divorce_ratio = len(none_faith_divorced) / len(none_faith) * 100
  
  print('종교 있는 사람 이혼 비율 :',round(faith_divorce_ratio,2))
  print('종교 없는 사람 이혼 비율 :', round(non_faith_divorce_ratio,2))
  '''
  종교 있는 사람 이혼 비율 : 4.08
  종교 없는 사람 이혼 비율 : 4.46
  '''
  
  if faith_divorce_ratio > non_faith_divorce_ratio :
      print('종교가 있는 사람들이 이혼을 더한다.')
  else :
      print('종교가 있는 사람들이 이혼을 덜한다.')
      
  # ==> 종교가 있는 사람들이 이혼을 덜한다.
  ```
  
  

## Q8

```txt
<지역별 연령대 비율>
   노년층이 많은 지역은 어디일까?
```

* 정답 코드

  ```python
  import numpy as np
  import pandas as pd
  import savReaderWriter
  
  with savReaderWriter.SavReader('./data/Koweps/Koweps_hpc10_2015_beta1.sav',
                                 ioUtf8=True) as reader :
      df = pd.DataFrame(reader.all(), columns = [i for i in reader.header] )
  
  all_df = df[['h10_g3','h10_g4','h10_g10','h10_g11',
              'h10_eco9', 'p1002_8aq1', 'h10_reg7']]
  
  use_df = df[['h10_g4','h10_reg7']]
  
  # 연령대 숫자로 바꾸기
  new_age = []
  for i in use_df['h10_g4']:
      new_age.append(2021 - i + 1)
  use_df['h10_g4'] = new_age
  
  # 연령층 boolean mask 만들어 놓기
  age_young_mask = use_df['h10_g4']<30.0
  age_middle_mask = (use_df['h10_g4'] >= 30.0) & (use_df['h10_g4'] < 60.0)
  age_old_mask = use_df['h10_g4']>60.0
  
  new_df = use_df.loc[age_old_mask,:]
  old_location = new_df.groupby(new_df['h10_reg7'])
  
  print(old_location.count().sort_values(by='h10_g4',ascending=False))
  print('노년층이 많은 지역은 어디일까? ==> 7번지역 : 광주/전남/전북/제주도')
  
  '''
  h10_g4
  h10_reg7        
  7.0         1389
  2.0         1333
  3.0         1307
  4.0         1051
  1.0          999
  5.0          633
  6.0          630
  '''
  # ==> 노년층이 많은 지역은 어디일까? ==> 7번지역 : 광주/전남/전북/제주도
  ```
  
