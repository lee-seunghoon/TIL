# Beautiful Soup 4



## 기본1

> - 네이번 웹툰 정보를 스크래핑 해보자

```python
import requests
from bs4 import BeautifulSoup

# 네이버 웹툰 url
url = 'https://comic.naver.com/webtoon/weekday'

res = requests.get(url)
res.raise_for_status()

# 우리가 요청한 res의 웹사이트 데이터를 lxml 파서를 활용해서 뷰티풀숩 객체로 만들었다.
# 이 soup 객체가 모든 정보를 다 가지고 있다.
soup = BeautifulSoup(res.text, 'lxml')

# 우리가 요청한 웹사이트의 title을 알고싶다
print(soup.title) # ==> <title>네이버 만화 &gt; 요일별  웹툰 &gt; 전체웹툰</title>
print(soup.title.get_text()) # ==> title tag 안에 있는 text만 가지고 오고 싶을 때

# 전체 html문서 안에서 첫번째로 발견되는 a tag 불러오기
print(soup.a)

# a tag의 속성을 확인하고 싶을 때
print(soup.a.attrs)

# 내가 원하는 a tag의 속성값만 가지고 오고 싶을 때
print(soup.a['href']) # ==> #menu
```



> - `soup.find()`

```python
# 내가 스크래핑 하려는 사이트의 구성을 잘 모를 때 편하게 쓸 수 있는 방법
# soup.find('태그', attrs={속성명:값})
soup.find('a', attrs={'class':'Nbtn_upload'}) # a tag 중에서 class 속성이 Nbtn_upload 인 처음으로 발견되는 element 내용을 출력

# soup.find() 에서 tag 없이도 쓸 수 있다. (대신 이 속성이 다른 element에 없을 때)
soup.find(attrs={'class':'Nbtn_upload'})

# li tag의 class가 rank01 인 element를 가져오고 싶을 때
rank1 = soup.find('li', attrs={'class':'rank01'})

# a 링크만 필요할 때
rank1.a # ==> soup 객체처럼 사용할 수 있다.
```



## 기본2

> - 부모/형제 관계 사용

```python
# rank1의 a tag의 text 가져오기
rank1.a.get_text() # ==> 여신강림-173화

# 다음 형제 위치에 있는 element 값 가져오기
print(rank1.next_sibling) # ==> 아무것도 안뜬다.
print(rank1.next_sibling.next_sibling) # ==> 하나 더 주면 다음 element 정보를 가져온다.
									   # ==> element 사이에 개행 정보라고 해서 중간에 공백이 있을 수 있다.
    
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text()) # ==> 사신소년-113화 분열

# 이전 형제 위치에 있는 element 가져오기
rank2 = rank3.previous_sibling.previous_sibling

# 부모 elemet 가져오기
rank_parent = rank1.parent
print(rank_parent) # rank 정보를 담고 있는 li tag들을 모두 포함해서 ol tag를 출력

# 형제 가져 올 때 개행 부분이 있으면 두번씩 써야하는 게 애매하다
# 새로운 방법 == 조건을 통해 찾기
# .find_next_sibling('태그명')
# 형제 tag 중에 우리가 tag명으로 준 첫번째 tag를 찾는다.
rank2 = rank1.find_next_sibling('li')
print(rank2.a.get_text())
rank3 = rank2.find_next_sibling('li')
print(rank3.a.get_text())

# 이전 형제를 찾을 때도 똑같이 find로 찾을 수 있다.
rank2 = rank3.find_previous_sibling('li')
print(rank2.a.get_text())

# 함께 있는 형제들 모두 가져오기
rank1.find_next_siblings('li')
```



> - 특정 text를 filter로 찾기

```python
import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

# soup 전체 html elment에서 'a' tag 중 text가 '~~'인 a tag 출력
webtoon = soup.find('a', text='여신강림-173화')
print(webtoon) # ==>  <a href= ...> ... </a>
```



## 활용 1-1 (내가 좋아하는 만화 제목 스크래핑)

```python
import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

# find_all 조건에 해당하는 모든 엘리먼트를 찾는다.
# 리스트로 모든 엘리먼트를 반환해준다.
cartoons = soup.find_all('a', attrs={'class':'title'})

# 전체 a tag에서 text만 다 뽑아보자
# 그럼 우리가 가져온 웹페이지 soup 문서 안에서 웹툰 제목만 쭉 가져온다.
# 네이버 웹툰 전체 목록을 가져오게 된다.
for cartoon in cartoons:
    print(cartoon.get_text())
```



> - 윈드브레이커 각 회차 제목 가져오기

```python
import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/list?titleId=602910&weekday=mon'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

# 이 사이트의 각 회차 제목을 담고 있는 a tag는 class도 없고 td tag 밑에 있다.
# 그래서 td tag이면서 class가 title인 엘리먼트 가져와보자
cartoons = soup.find_all('td', attrs={'class': 'title'})

# 제일 위에 있는 만화 제목 가져오기
# 3부 - 128화 [마지막화] 날아라 고자현!
cartoon1_title = cartoons[0].a.get_text()
print(cartoon1_title)

# 이 제목의 링크도 가져와보자
# a tag의 속성 중 href
cartoon1_link = cartoons[0].a['href']
print(cartoon1_link) # ==> /webtoon/detail?titleId=602910&no=378&weekday=mon
					 # ==> 온전하지 않은 링크를 가져온다.
print('https://comic.naver.com' + cartoon1_link) # 잘 가져와준다.

# 이제 전체 다 가져와보자
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = 'https://comic.naver.com' + cartoon.a['href']
    print(title, link)
    
```



> - 윈드브레이커 각 회차 평점 가져오기

```python
import requests
from bs4 import BeautifulSoup

# 네이버 웹툰 윈드브레이터 웹사이트
url = 'https://comic.naver.com/webtoon/list?titleId=602910&weekday=mon'

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

# 평점 데이터를 가져오기 위해 div 태그에서 class 속성 값이 rating_type인 element를 모두 가져와
ratings = soup.find_all('div', attrs={'class':'rating_type'})

# 평점의 평균 계산하기
total_ratings = 0
for rating in ratings:
    # div tag 밑에는 strong이라는 tag에 평점 숫자 값이 있다.
    rating_score = rating.strong.get_text()
    total_ratings += float(rating_score)

print('전체 평점의 합 :', total_ratings)
print('평점의 평균은?', total_ratings/len(ratings))
```



## 활용 2-1 쿠팡

### HTTP Method
> - 서버 요청 종류중 get, post 방식에 대해 알아보자

#### GET
> - 누구나 볼 수 있게 url을 적어서 web 정보를 요청하는 방식
> - 예시) https://www.coupang.com/np/search?minPrice=1000&maxPrice=100000&page=1
> - 우리가 요청할 url 뒤에 `?` 기호와 함께 `변수=값` 형식으로 정보를 부여하고 각 정보는 `&`으로 연결한다.
> - 이 값들을 변동하면서 쉽게 접근할 수 있다.
> - get방식은 데이터를 전송할 때, 큰 데이터를 보내지 못하는 한계가 존재한다.

#### POST
> - url 아니 HTTP 메세지 바디에 숨겨서 보내는 방식
> - 보안이 필요한 데이터는 post 방식을 활용한다.
> - 데이터가 큰 경우도 가능하다
> - 회원가입과 게시글 쓰는 (개인정보 느낌이 강한) 화면은 post 방식으로 요청한다.



### 실습

```python
import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor='

# 그냥 정보를 요청하니깐 시간이 너무 오래걸리면서 뭔가 거부되는 느낌
# user agent 정보를 준다
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

# 정규식 활용
# re.compile('^search-product') == search-product 로 시작하는 모든 text를 의미함
items = soup.find_all('li', attrs={'class':re.compile('^search-product')})

# li tag 중 class가 search-product 로 시작하는 모든 엘리먼트를 가져왔는데
# 그 중 첫번째 element에서 div tag를 찾고 그 중에 class가 name인 제일 첫번째 tag를 찾아서 그 text 값을 반환 
print(items[0].find('div', attrs={'class':'name'}).get_text())
# ==> 삼성전자 2021 노트북 플러스2 15.6, 퓨어 화이트, 셀러론, 128GB, 8GB, WIN10 Pro, NT550XDA-K14AW
```



## 활용 2-2 쿠팡 상품 웹 스크래핑

> - 제품 정보에 대한 세부 항목들을 가져와본다

```python
for item in items:
    # 제품명
    name = item.find('div', attrs={'class':'name'}).get_text()
    # 가격
    price = item.find('strong', attrs={'class':'price-value'}).get_text()
    # 평점
    # 평점이 없는 데이터도 있을 수 있어서
    rating = item.find('em',attrs={'class':'rating'})
    if rating :
        rating = rating.get_text()
    else:
        rating = '평점 없음'
    # 평가개수
    rating_cnt = item.find('span', attrs={'class':'rating-total-count'}).get_text()

    print(name, price, rating, rating_cnt)
```



## 활용 2-3 쿠팡 상품 웹 스크래핑

> - 광고 상품은 제외한다.
> - Apple 맥북 상품도 제외한다.
> - 평점이 4.5 이상이고, 평가개수가 500개 이상이면서, 평점이 있는 상품만 스크래핑한다.

```python
for item in items:

    # 광고 상품을 제외하고 나머지 상품만 출력
    ad_badge = item.find('span', attrs={'class':'ad-badge-text'})
    if ad_badge:
        print('광고 상품입니다. 제외하겠습니다')
        print()
        continue

    # 제품명
    name = item.find('div', attrs={'class':'name'}).get_text()

    # Apple 맥북 상품을 안 볼거라서 제외
    if 'Apple' in name:
        print('[Apple 맥북 상품은 제외하겠습니다]')
        print()
        continue

    # 가격
    price = item.find('strong', attrs={'class':'price-value'}).get_text()
    
    # 평점
    # 평점이 없는 데이터도 있을 수 있어서
    rating = item.find('em',attrs={'class':'rating'})
    if rating :
        rating = rating.get_text()
    else:
        rating = '평점 없음'
    
    # 평가개수
    rating_cnt = item.find('span', attrs={'class':'rating-total-count'}).get_text()

    # 평점이 4.5 이상이고 평가개수가 500개 이상이면서 평점이 있는 것만 출력
    if (float(rating) >= 4.5) and (int(rating_cnt[1:-1]) >= 500) and (rating != '평점 없음'):
        print('제품이름:{}\n제품가격:{}원\n평점:{}\n평가개수:{}개'.format(name, price, rating, rating_cnt[1:-1]))
        print()
```

