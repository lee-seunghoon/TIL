# Pandas 연습문제.01 

> movies.csv & ratings.csv 파일을 활용하여 작업

## Q1

```txt
사용자가 평가한 모든 영화의 전체 평균 평점
```

* 정답 코드

  ```python
  import numpy as np
  import pandas as pd
  
  df = pd.read_csv('./ml-latest-small/ratings.csv')
  display(df['rating'].mean())
  # ==> 3.501556983616962
  ```
  
  



## Q2

```txt
각 사용자별 평균 평점
```

* 정답 코드

  ```python
  import numpy as np
  import pandas as pd
  
  df = pd.read_csv('./ml-latest-small/ratings.csv')
  rating = df['rating'].groupby(df['userId'])
  print(rating.mean())
  '''
  userId
  1      4.366379
  2      3.948276
  3      2.435897
  4      3.555556
  5      3.636364
           ...   
  606    3.657399
  607    3.786096
  608    3.134176
  609    3.270270
  610    3.688556
  Name: rating, Length: 610, dtype: float64
  '''
  ```



## Q3

```txt
각 영화별 평균 평점
```

* 정답 코드

  ```python
  import numpy as np
  import pandas as pd
  
  df = pd.read_csv('./ml-latest-small/ratings.csv')
  rating = df['rating'].groupby(df['movieId'])
  rating_mean = rating.mean()
  
  
  df_movies = pd.read_csv('./ml-latest-small/movies.csv')
  df_movie_title = df_movies[['movieId','title']]
  df_merge = pd.merge(df_movie_title, rating_mean, on = 'movieId', how = 'outer')
  print(df_merge)
  '''
        movieId                                      title    rating
  0           1                           Toy Story (1995)  3.920930
  1           2                             Jumanji (1995)  3.431818
  2           3                    Grumpier Old Men (1995)  3.259615
  3           4                   Waiting to Exhale (1995)  2.357143
  4           5         Father of the Bride Part II (1995)  3.071429
  ...       ...                                        ...       ...
  9737   193581  Black Butler: Book of the Atlantic (2017)  4.000000
  9738   193583               No Game No Life: Zero (2017)  3.500000
  9739   193585                               Flint (2017)  3.500000
  9740   193587        Bungo Stray Dogs: Dead Apple (2018)  3.500000
  9741   193609        Andrew Dice Clay: Dice Rules (1991)  4.000000
  
  [9742 rows x 3 columns]
  '''
  ```



## Q4

```txt
평균 평점이 가장 높은 영화의 제목(동률이 있을 경우 모두 출력)
```

* 정답코드

  ```python
  import numpy as np
  import pandas as pd
  
  df = pd.read_csv('./ml-latest-small/ratings.csv')
  rating = df['rating'].groupby(df['movieId'])
  rating_mean = rating.mean()
  
  df_movies = pd.read_csv('./ml-latest-small/movies.csv')
  df_movie_title = df_movies[['movieId','title']]
  
  df_merge = pd.merge(df_movie_title, rating_mean, on = 'movieId', how = 'outer')
  rating_max = df_merge['rating'].max()
  result = df_merge[df_merge['rating'] == rating_max]
  print(result.sort_values(by='title'))
  '''
        movieId                             title  rating
  5690    27751               'Salem's Lot (2004)     5.0
  7332    77846               12 Angry Men (1997)     5.0
  9046   141816                  12 Chairs (1976)     5.0
  3893     5468  20 Million Miles to Earth (1957)     5.0
  5639    27373                        61* (2001)     5.0
  ...       ...                               ...     ...
  9711   187717  Won't You Be My Neighbor? (2018)     5.0
  8355   108795               Wonder Woman (2009)     5.0
  9289   158398             World of Glory (1991)     5.0
  9560   173351       Wow! A Talking Fish! (1983)     5.0
  7521    84273  Zeitgeist: Moving Forward (2011)     5.0
  
  [296 rows x 3 columns]
  '''
  ```
  
  

## Q5

```txt
Comedy영화 중 평균 평점이 가장 낮은 영화의 제목
```

* 정답 코드

  ```python
  import numpy as np
  import pandas as pd
  
  df = pd.read_csv('./ml-latest-small/ratings.csv')
  rating = df['rating'].groupby(df['movieId'])
  
  # movieId별 평점 평균
  rating_mean = rating.mean()
  
  df_movies = pd.read_csv('./ml-latest-small/movies.csv')
  
  # 데이터 결합
  df_combine = pd.merge(df_movies,rating_mean, on = 'movieId', how = 'outer')
  # rating 기준으로 정렬 (기본 오름차순)
  df_combine = df_combine.sort_values(by='rating')
  
  # 장르 중에 Comedy 있는 영화만 추출
  comedy = df_combine[df_combine['genres'].str.contains('Comedy')]
  
  # comedy 장르 중 NaN 값 지우기
  comedy.dropna(how='any', axis=0, inplace=True)
  
  # 최소값 구한 후, 그 최소값만 가지는 값 빼와서 'title'로 오름차순 정렬
  rating_min = comedy['rating'].min()
  result = comedy[comedy['rating'] == rating_min]
  display(result[['movieId','title','genres']].sort_values(by='title'))
  
  
  ```



## Q6

```txt
2015년도에 평가된 모든 Romance 영화의 평균 평점은?
```

* 정답 코드

  ```python
  import numpy as np
  import pandas as pd
  
  df = pd.read_csv('./ml-latest-small/ratings.csv')
  
  ##################################################
  # movie rating timestamp를 년도로 바꾸기
  test = df['timestamp']
  index = test.index
  
  convert_year = []
  for i in index :
      year = pd.Timestamp.fromtimestamp(test[i]).year
      convert_year.append(year)
  
  df['timestamp'] = convert_year # ==>'timestamp'라는 column값을 모두 바꾸기
  ###################################################
  
  # 2015년 영화만 뽑아오기
  rating_2015 = df.loc[df['timestamp']==2015,['movieId','rating']]
  
  movies_df = pd.read_csv('./ml-latest-small/movies.csv')
  
  # merge 하기
  df_merge = pd.merge(rating_2015,movies_df,on = 'movieId', how = 'left')
  
  # 'genres'가 romance 인 data 추출하기
  romance = df_merge[df_merge['genres'].str.contains('Romance')]
  
  # 평점 평균 구하기
  print(romance['rating'].mean())
  ```
  
