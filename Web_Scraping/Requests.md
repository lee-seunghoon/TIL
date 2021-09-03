## Requests

> - 웹 페이지 문서 정보를 가져와서 쓸 수 있도록 도와주는 파이썬 라이브러리



```python
import requests

# 웹사이트에 정보를 요청하는 방법
res = requests.get('http://google.com')

# 응답코드 확인
print('응답코드 :', res.status_code) # 200이면 정상
								   # 403이면 웹사이트에 접근할 수 없다는 미

# 응답 에러 출력 방법 1
if res.status_code == requests.codes.ok:
    print('정상입니다.')
else:
    print('문제가 생겼습니다. [에러코드 : {}]'.format(res.status_code))
    
# 응답 에러 출력 방법 2
res.raise_for_status() # 에러가 있으면 에러 출력
					   # 없으면 바로 진행
    
# 웹페이지 html 코드를 text로 가져오기
print(res.text)

# 그냥 보면 뭔지 모르니깐 html 파일로 저장해서 확인하기
with open('google.html', 'w', encoding='utf8') as f:
    f.write(res.text)
```

