# 웹 스크래핑 실전 1

> - 링커리어 자소서 스크래핑
> - css selector를 주로 이용했음.
> - html & 웹 구조에 대한 이해 필요
> - `Selenium` & `BeautifulSoup` 사용



### `라이브러리`

```python
from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
```



### `웹 사이트 접근 & 스크래핑`

```python
# 크롬 브라우저 실행
browser = webdriver.Chrome()
# 창 키우기
browser.maximize_window()

# 접근할 url (링커리어)
url = 'https://linkareer.com/'

page_cnt = 1

# 자소서 정보 데이터 프레임 만들기
df = pd.DataFrame(columns=['기업명', '모집전형', '모집시기', '대학교', '전공', '학점', '기타스펙', '자소서'])

# 자소서 page 순서대로 가져오기
for n in range(1,5):
    start_url = url + f'cover-letter/search?page={n}&tab=all'
    browser.get(start_url)
    time.sleep(1)

    # 현재 html 웹 페이스 문서 소스 가져오기
    recent_web = bs(browser.page_source, 'lxml')

    # 현 페이지의 자소서 링크 가져오기 (원래는 div.MuiBox-root.jss167.jss168 이부분에서 jss숫자 이게 3개 인데, 맨 앞에만 달라지고, 뒤 2개가 공통분모여서 공통된 요소만 남겨둠)
    atag_list = recent_web.select('#__next > div.MuiBox-root.jss3 > div > div.MuiContainer-root.jss12.jss1.MuiContainer-disableGutters > div.MuiBox-root.jss154.jss148 > div > div.MuiBox-root.jss165.jss152 > div.MuiContainer-root.jss150.MuiContainer-disableGutters.MuiContainer-maxWidthLg > div.MuiBox-root.jss167.jss168 > div.jss174 > a')

    for atag in atag_list:

        # 자소서 링크
        new_url = url + atag.get('href')[1:] + '&simple=true'

        # 현 페이지에서 각 자소서 링크별로 접속하기
        browser.get(new_url)
        time.sleep(1)

        # 자소서 내용이 답긴 웹 페이지
        contents_soup = bs(browser.page_source, 'lxml')

        # 기업명 / 모집전형 / 모집시기
        intro1 = contents_soup.select('#__next > div.jss6.jss2 > div.MuiContainer-root.jss14.jss3.MuiContainer-disableGutters > div > div > div.MuiContainer-root.jss98.jss99.MuiContainer-maxWidthLg > div > div.MuiBox-root.jss160.jss152 > div > div > div.MuiBox-root.jss168')
        # 대학교 / 전공 / 학점 / 기타스펙
        intro2 = contents_soup.select('#__next > div.jss6.jss2 > div.MuiContainer-root.jss14.jss3.MuiContainer-disableGutters > div > div > div.MuiContainer-root.jss98.jss99.MuiContainer-maxWidthLg > div > div.MuiBox-root.jss160.jss152 > div > div > div.MuiBox-root.jss169')
        # 자기소개서
        texts = contents_soup.select('#coverLetterContent > main')

        # 양식이 안 맞는 경우가 있기에 조정

        # 기업명이 'sk텔레콤 / 5G' 이런식으로 구성돼 있는 경우가 있기에
        new_info1 = intro1[0].get_text().split(' / ')
        if len(new_info1) != 3 :
            new_info1[0] = ' '.join(new_info1[:2])
            del new_info1[1]

        # 대학교 / 전공 / 학점 까지는 공통적인데 그 뒤로 다양한 형태여서 통일
        new_info2 = intro2[0].get_text().split(' / ')
        new_info2[3] = ' '.join(new_info2[3:])
        del new_info2[4:]

        # 전체 한 리스트로 합체
        info = new_info1 + new_info2 + [texts[0].get_text()]

        # 우리의 자소서 데이터 프레임에 추가 하기
        df = df.append(pd.Series(info, index=df.columns), ignore_index=True)

# 스크래핑 다 한 후 브라우저 끄기
browser.quit()
```