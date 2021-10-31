# 네이버 항공권 정보 가져오기

```python
from selenium import webdriver
browser = webdriver.Chrome()

# 브라우저 창 최대화
browser.maximize_window()

# 우리가 접속할 url
url = 'https://flight.naver.com/'

# 위 url로 이동
browser.get(url)

# 브라우저에 적혀있는 글씨로 element 선택
# 원래는 아래 text로 찾아야 하는데 오류가 나서 xpath로 도전
# browser.find_element_by_link_text('가는 날').click()
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()

# 23일을 선택하려고 하는데 23이라는 숫자가 많다.
# 그래서 전체 다 불러온다음에 인덱스로 내가 원하는 날짜 선택하자
# 원래는 아래 방식이 돼야 하지만 안되는거 보니 text로 불러 오는게 문제가 있는 듯
browser.find_elements_by_link_text('23')[0].click() # ==> 이번달
browser.find_elements_by_link_text('25')[0].click() # ==> 이번달
```

