## User Agent



> - web site에 접속할 때, header에 담기는 정보
> - user agent를 부여해주면, 막혔던 스크래핑도 제대로 가져올 수 있다.



```python
import requests

# 내가 접속할 web site
url = 'http://nadocoding.tistory.com'

# user agent 설정
# 나의 user agent 확인하는 방법 == 구글에 user agent string 입력 후 'whatismy...'사이트로 접속
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}

# url 요청
res = requests.get(url, headers)

# request의 결과 상태를 반환
res.raise_for_status()

# 요청해서 받아온 데이터를 그대로 html 파일로 받아오기
with open('nadocoding.html', 'w', encoding='utf-8') as f:
    f.write(res.text)
```

