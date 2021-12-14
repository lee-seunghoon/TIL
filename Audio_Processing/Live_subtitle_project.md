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



### `recognize_google` 이용하여 STT 구현

> - 마이크 인식률이 좋음
> - 아쉬운 점은 속도가 느림

```python
import speech_recognition as sr

while True :

    r = sr.Recognizer()

    try:

        # with sr.Microphone(device_index=1, sample_rate=44100) as source :
        #     r.adjust_for_ambient_noise(source)
        #     print('소음 수치', r.energy_threshold)
		
        # 마이크로 소리 데이터 입력
        with sr.Microphone(device_index=1, sample_rate=16000) as source:
            print('start')
            audio = r.listen(source)
	
    	# 입력받은 데이터 wav 파일로 저장
        with open('test.wav', 'wb') as f:
            f.write(audio.get_wav_data())
		
        # wav 파일 실행
        test_audio = sr.AudioFile('./test.wav')
		
        # 파일 음성을 record해서 google api로 STT
        with test_audio as source:
            real_audio = r.record(source)
        print(r.recognize_google(audio_data=real_audio, language='ko-KR'))
    
    except :
        continue
```



### `Kakao STT` API 이용 

> - 마이크에서 음성 인식하는 속도가 느린 듯
> - 여전히 출력 결과가 느리게 나온다.
> - 개선 방법으로 recognizer.listen(source, 10, 3) 이렇게 3초 간격을 줬음
> - 3초마다 끊기는 하는데 텍스트 출력과 마이크 인식하는 그 사이 텀에 나오는 text를 놓치는 듯

```python
import speech_recognition as sr
import requests
import json

recognizer = sr.Recognizer()

michro = sr.Microphone(sample_rate=16000)

while True:
    try:
        with michro as source :
            print('test')
            result = recognizer.listen(source, 10, 3) # ==> 3초 텀으로 제한
            audio = result.get_raw_data()

            url = 'https://kakaoi-newtone-openapi.kakao.com/v1/recognize'

            header = {'Content-Type': 'application/octet-stream',
                #'Transfer-Encoding': 'chunked',
                'Authorization': 'KakaoAK ' + REST_API_KEY}
            res = requests.post(url, headers=header, data=audio)
            print(json.loads(res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}')+1])['value'])
    
    except Exception as e :
        print(e)

```

