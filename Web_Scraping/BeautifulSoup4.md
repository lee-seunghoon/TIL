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

