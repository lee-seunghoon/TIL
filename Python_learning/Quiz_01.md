# 연습문제.01



## Q1

![image-20210106171815323](md-images/image-20210106171815323.png)

* 정답 코드

  ```python
  all = 0
  
  for i in range(1,1000):
      if i%3==0 or i%5==0:
          all += i
  print('정답 :', all)
  ```

  



## Q2

![image-20210106171843155](md-images/image-20210106171843155.png)

* 정답 코드

  ```python
  n = 0
  n1 = 1
  n2 = 2
  total = 2
  
  while n <= 4000000:
      n = n1 + n2
      if n%2==0:
          total += n
          n1 = n2
          n2 = n
      else :
          n1 = n2
          n2 = n
  print('정답 :', total)    
  
  ```



## Q3

![image-20210106171909362](md-images/image-20210106171909362.png)

* 정답 코드

  ```python
  t1 = 'This is a sample Program mississippi river'
  t2 = 'abcdabcdababccddcd'
  
  def text_judge(text):
      long = 1
      text = text.upper()
      new_text = list(set(text))
      
      
      for i in new_text :
          if text.count(i) < long:
              pass
          elif text.count(i) > long :
              long = text.count(i)
              result = i
          elif text.count(i) == long :
              if i < result :
                  result = i
      return result
  
  print('정답 : "{}" =>'.format(t1), text_judge(t1))
  print('정답 : "{}" =>'.format(t2), text_judge(t2))
  ```



## Q4

![image-20210106171929012](md-images/image-20210106171929012.png)

* 정답코드

  ```python
  # 쉬운 버전
  
  import random as rd
  
  lotto = [2, 13, 16, 19, 32, 33]
  my_num = []
  n = []
  
  for i in range(5):
    l = []
    while len(l) != 6:
      new_num = rd.randint(1,46)
      if new_num not in l:
          l.append(new_num)
    my_num.append(l)
    m =0
    for j in range(5) :  
      if my_num[i][j] in lotto :
        m += 1
    if m >= 6 :
      n.append('1등')
    elif m >= 5:
      n.append('2등')
    elif m >= 4:
      n.append('3등')
    elif m >= 3:
      n.append('4등')
    elif m >= 2:
      n.append('5등')
    else :
      n.append('꽝')
  
  for i in range(1,6):
    if i <= 4 :
      grade = n.count('{}등'.format(i))
      print('{}등 {}개'.format(i, grade))
    else :
      grade = n.count('꽝')
    print('꽝 {}개'.format(grade))
  ```
  
  ```python
  # 어려운 버전
  
  import random as rd
  
  lotto = [2, 13, 16, 19, 32, 33]
  my_num = []
  n = []
  
  for i in range(5):
    l = []
    while len(l) != 7:            # l 안에 원소 개수가 6개 아니면 계속 해. --> 6개면 멈춰 
      new_num = rd.randint(1,46)
      if new_num not in l:        # 중복을 제거하기 위해 생성한 숫자가 l 안에 있는지 검사
          l.append(new_num)         # l 안에 똑같은 게 없으면 추가해버려
    my_num.append(l)
    m =0
    for j in range(6) :  
      if my_num[i][j] in lotto :
        m += 1
    if m >= 6 :
      n.append('1등')
    elif m >= 5 and my_num[i][6] in lotto :
      n.append('2등')
    elif m >= 5:
      n.append('3등')
    elif m >= 4:
      n.append('4등')
    elif m >= 3:
      n.append('5등')
    else :
      n.append('꽝')
  
  print('로또번호를 5회 생성합니다.')
  print('당신의 번호는 다음과 같습니다.')
  print('(맨 마지막 번호는 보너스 번호입니다.)')
  print('='*20)
  for x in my_num :
    print(x)
  print('='*20)
  print('결과는?')
  
  for i in range(1,7):
    if i <= 5 :
      grade = n.count('{}등'.format(i))
      print('{}등 {}개'.format(i, grade))
    else :
      grade = n.count('꽝')
    print('꽝 {}개'.format(grade))
  ```
  
  

## Q5

![image-20210106171945834](md-images/image-20210106171945834.png)

* 정답 코드

  ```python
  # 꼼수 써서 0.45초
  
  
  import time
  start_time = time.time()
  
  def sosu_cal(floor):
    n=1
    num = 3
    sosu = [2]
    while n < floor :
      left = []
      for i in sosu :
        left.append(int(num % i))
      if 0 not in left :
        n += 1
        sosu.append(num)
        num += 1
        left.clear
      else :
        num += 1
        left.clear
    return sosu
  
  s1 = sosu_cal(900)  # <== 소수 리스트를 미리 정해놓음
  soinsu = []
  num = 600851475143  # <== 여기 있는 숫자만 바꾸면 됨.
  for i in s1 :
    if num % i == 0 :  
      soinsu.append(i)
  print('정답 :',max(soinsu))
  
  end_time = time.time()
  proceed_time = end_time-start_time
  print('program time : {} sec'.format(round(proceed_time,2)))
  ```



## Q6

![image-20210106172000666](md-images/image-20210106172000666.png)

* 정답 코드

  ```python
  import time
  start_time = time.time()
  
  m =1
  for i in range(100,1000):
      for r in range(100,1000):
          n = str(i * r)
          if n == n[::-1] and int(n) > m:
            m = int(n)
  print('정답 :',m)
  
  end_time = time.time()
  proceed_time = end_time-start_time
  print('program time : {} sec'.format(round(proceed_time,2)))
  
  
  # 시간 소요 : 0.36 sec
  ```
  
  

## Q7

![image-20210106172011338](md-images/image-20210106172011338.png)

* 정답 코드

  ```python
  # 약 170초 ... 약 2분 50초 시간 소요...
  # 정확하게 [program time : 169.40 sec]
  
  import time
  start_time = time.time()
  
  result = 0
  num = 2
  while result == False :
  
    for i in range(1,21):
      if num % i != 0 :
        num += 1
        break
      elif num % i == 0 and i != 20 :
        pass
      elif num % i == 0 and i == 20 :
        result = num
  
  print('정답 :',result)
  
  end_time = time.time()
  proceed_time = end_time-start_time
  print('program time : {} sec'.format(round(proceed_time,2)))
  ```
  
  



  

## Q8

![image-20210106172024235](md-images/image-20210106172024235.png)

* 정답 코드

  ```python
  # 소요시간 0.0sec
  
  import time
  start_time = time.time()
  
  a = 0
  for i in range(1,101):
      a += i    
  total = a**2
  
  jcob = 0
  for i in range(1,101):
    c = i**2
      jcob += c
  
  print('정답 :', total - jcob)
  
  end_time = time.time()
  proceed_time = end_time-start_time
  print('program time : {} sec'.format(round(proceed_time,2)))
  ```
  
  

## Q9

![image-20210106172034473](md-images/image-20210106172034473.png)

* 정답 코드

  ```python
  # 성공했지만.... 10001번째 소수 구하는 데 시간이 너무 오래 걸린다.
  # program time : 71.55 sec
  
  import time
  start_time = time.time()
  
  def sosu_cal(floor):
    n=1
    num = 3
    sosu = [2]
    while n < floor :
      left = []
      for i in sosu :
        left.append(int(num % i))
      if 0 not in left :
        n += 1
        sosu.append(num)
        num += 1
        left.clear
      else :
        num += 1
        left.clear
    sosu.clear
    print('정답 :',sosu_num) 
  
  sosu_cal(10001)
  
  end_time = time.time()
  proceed_time = end_time-start_time
  print('program time : {} sec'.format(round(proceed_time,2)))
  ```



## Q10

![image-20210106172054367](md-images/image-20210106172054367.png)

* 정답 코드

  ```python
  
  ```

  

