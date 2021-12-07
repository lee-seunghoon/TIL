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

