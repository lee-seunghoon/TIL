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
