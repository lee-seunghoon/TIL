## Author 수정

> - 여려 명의 작성자 ID로 글을 작성할 수 있다.
> - 개인 블로그로 진행 할 예정이어서 author 1명만 지정



- `C:\blogmaker\_data\authors.yml` 파일 수정

```yaml
sherlocky:          # 닉네임 (글 작성에 나오는 이름)
  username: ghost   # 일반 이름
  name: Ghost       # 풀네임
  url_full:         # Homepage URL
  url:
  bio: <a href="https://github.com/lee-seunghoon">Sherlocky의 Github Link</a> # 나의 SNS 링크같은거 올려도 된다 / 회사 정보 등
  picture: assets/built/images/sherlocky_logo.jpg    # author image
  facebook:         # facebook ID
  twitter:          # twitter ID
  cover: False
```





## tag 수정

> - 글의 범주를 정해주는 기능 (ex. 파이썬이냐, R이냐 등)
> - 주제로 분류하는 기능

- `C:\blogmaker\_data\tags.yml` 파일 수정

```yaml
Python:
  name: python
  description: False
  cover: assets/built/images/python.jpg  # 해당 tag 배경 이미지
AI_ML/DL:
  name: AI_ML/DL
  description: False
  cover: False
```

