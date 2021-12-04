# PC 스피커 출력에 대한 실시간 자막 기능

> - 청각 장애인을 위한 스크립트 작성을 자동으로 진행
> - 카카오 OpenAPI 음성인식 사용



### `라이브러리`

```python
import speech_recognition as sr
import requests
```



### `마이크 소리 입력`

```python
recognizer = sr.Recognizer()

michrophone = sr.Microphone(sample_rate=16000)

with michrophone as source :
    recognizer.adjust_for_ambient_noise(source)
    print('소음 수치', recognizer.energy_threshold)

with michrophone as source:
    print('test')
    result = recognizer.listen(source)
    audio = result.get_raw_data()
```



### `카카오 Open API 음성 인식`

```python
url = 'https://kakaoi-newtone-openapi.kakao.com/v1/recognize'

header = {'Content-Type': 'application/octet-stream',
          #'Transfer-Encoding': 'chunked',
          'Authorization': 'KakaoAK ' + 'REST_API_KEY'}

res = requests.post(url, headers=header, data=audio)
print(res.text)
```

