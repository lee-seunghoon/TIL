# 연습문제.02



## Q1

```txt
displ(배기량)이 4 이하인 자동차와 5 이상인 자동차 중 어떤 자동차의 hwy(고속도로 연비)가 평균적으로 더 높은지 확인하세요.
```

* 정답 코드

  ```python
  class Car_data():
      
      def __init__(self, file_name, load_type):
          self.file_name = file_name
          self.load_type = load_type
          self.data = open(self.file_name, self.load_type)
          self.line = []
      
      def load(self):
          while True :
              line = self.data.readline()
              if not bool(line) :
                  break
              line = line.split(',')
              self.line.append(line)
          return self.line
      
      def close(self):
          return self.data.close
              
  
  car1 = Car_data('mpg.txt','r')
  car = car1.load()
  # print(len(car)) ==> 맨 위 매뉴 빼고 234개 data
  # print(car[0])   ==> 카테고리 보고 싶을 때
  
  
  hwy4 = 0
  n4 = 0
  hwy5 = 0
  n5 = 0
      
  for i in range(1,235):    
      if float(car[i][2]) <= 4. :
          hwy4 += float(car[i][-3])
          n4 += 1
      else :
          hwy5 += float(car[i][-3])
          n5 += 1
  
  hwy4_mean = hwy4 / n4
  hwy5_mean = hwy5 / n5
  
  # print(hwy4_mean, hwy5_mean)
  
  if hwy4_mean > hwy5_mean :
      print('배기량이 4이하인 자동차의 고속도로연비가 평균적으로 더 높습니다.')
  elif hwy4_mean < hwy5_mean:
      print('배기량이 5이상인 자동차의 고속도로연비가 평균적으로 더 높습니다.')
  
  
  ```
  
  



## Q2

```txt
자동차 제조 회사에 따라 도시 연비가 다른지 알아보려고 한다. 
"audi"와 "toyota" 중 어느 manufacturer(제조회사)의 cty(도시 연비)가 평균적으로 더 높은지 확인하세요.
```

* 정답 코드

  ```python
  class Car_data():
      
      def __init__(self, file_name, load_type):
          self.file_name = file_name
          self.load_type = load_type
          self.data = open(self.file_name, self.load_type)
          self.line = []
      
      def load(self):
          while True :
              line = self.data.readline()
              if not line :
                  break
              line = line.split(',',10)       
              self.line.append(line)
          return self.line
      
      def close(self):
          return self.data.close
      
  car = Car_data('mpg.txt', 'r')
  car2 = car.load()
  
  audi_cty = 0
  audi_num = 0
  toyota_cty = 0
  toyota_num = 0
  
  for i in range(1,235):
      if car2[i][0] == 'audi':
          audi_cty += float(car2[i][-4])
          audi_num += 1
      elif car2[i][0] == 'toyota':
          toyota_cty += float(car2[i][-4])
          toyota_num += 1
  
  audi_mean = audi_cty / audi_num
  toyota_mean = toyota_cty / toyota_num
  
  if audi_mean > toyota_mean :
      print('audi의 평균 도시연비 : {} , toyota의 평균 도시연비 : {}\
      '.format(round(audi_mean,1), round(toyota_mean,1)))
      print('audi의 평균 도시연비가 toyota보다 높습니다.')
  elif audi_mean < toyota_mean:
      print('audi의 평균 도시연비 : {} , toyota의 평균 도시연비 : {}\
      '.format(round(audi_mean,1), round(toyota_mean,1)))
      print('toyota의 평균 도시연비가 audi보다 높습니다.') 
  ```



## Q3

```txt
"chevrolet", "ford", "honda" 자동차의 고속도로 연비 평균을 알아보려고 한다. 
이 회사들의 데이터를 추출한 후 hwy(고속도로 연비) 평균을 구하세요.
```

* 정답 코드

  ```python
  class Car():
      def __init__(self, car_data):
          self.manufacturer = car_data[0]
          self.model = car_data[1]
          self.displ = float(car_data[2])
          self.year = int(car_data[3])
          self.cyl = float(car_data[4])
          self.trans = car_data[5]
          self.drv = car_data[6]
          self.cty = float(car_data[7])
          self.hwy = float(car_data[8])
          self.fl = car_data[9]
          self.car_class = car_data[10]
  
  
  def extract(file):
      line1 = file.readline()
      
      if line1 :
          car_data = line1.split(',',10)
      elif not line1 :
          car_data = list(line1)
      return car_data
  
  
  def carhwy(manufacturer):
      data = open('mpg.txt', 'r')
      data.readline()
      all_hwy = []
      while True:
          car_data = extract(data)
          if not car_data:
              break
          car = Car(car_data)
          if car.manufacturer == manufacturer :
              all_hwy.append(car.hwy)
             
      hwy_mean = sum(all_hwy)/len(all_hwy)
      all_hwy.clear()
      data.close()
      return round(hwy_mean,2)
  
  
  
  chevrolet_carhwy = carhwy('chevrolet')
  ford_carhwy = carhwy('ford')
  honda_carhwy = carhwy('honda')
  
  print('''chevrolet의 고속도로 연비 평균 : {}
  ford의 고속도로 연비 평균 : {}
  honda의 고속도로 연비 평균 : {}'''.format(chevrolet_carhwy,ford_carhwy,honda_carhwy))
  ```



## Q4

```txt
"audi"에서 생산한 자동차 중에 어떤 자동차 모델의 hwy(고속도로 연비)가 높은지 알아보려고 한다. "audi"에서 생산한 자동차 중 hwy가 1~5위에 해당하는 자동차의 데이터를 출력하세요.
```

* 정답코드

  ```python
  # 내가 생각한 알고리즘
  # audi의 hwy를 쭉 뽑은 후
  # sort로 오름차순 정렬
  # 그 정렬된 hwy리스트로 audi 차 중에서 매치되는 모델명 쭉 뽑아 (for문 써야겠네)
  # 그리고 for문으로 5개까지만 추출해
  ```
  
  ```python
  
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
  
  ```



## Q6

```txt
mpg 데이터의 class는 "suv", "compact" 등 자동차의 특징에 따라 일곱 종류로 분류한 변수입니다. 
어떤 차종의 도시 연비가 높은지 비교하려 합니다. 
class별 cty 평균을 구하고 cty 평균이 높은 순으로 정렬해 출력하세요.
```

* 정답 코드

  ```python
  
  ```
  
  

## Q7

```txt
어떤 회사 자동차의 hwy(고속도로 연비)가 가장 높은지 알아보려 합니다. 
hwy(고속도로 연비) 평균이 가장 높은 회사 세 곳을 출력하세요.
```

* 정답 코드

  ```python
  
  ```

  

## Q8

```txt
어떤 회사에서 "compact" 차종을 가장 많이 생산하는지 알아보려고 합니다. 
각 회사별 "compact" 차종 수를 내림차순으로 정렬해 출력하세요.
```

* 정답 코드

  ```python
  
  ```
  
  

## Q9

없음

* 정답 코드

  ```python
  
  ```



## Q10

없음

* 정답 코드

  ```python
  
  ```

  