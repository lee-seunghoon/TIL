# git ignore 사용법

> git 저장소 내에서 git으로 관리하고 싶지 않은 파일 있다면 `.gitignore`만들어서 관리한다.



```bash
$ touch .gitignore
```

- 이렇게 파일 만든 후
- .gitignore 에서 코드 작성하면 그 작성된거 빼고 git 관리 할 수 있음



```bash
# .gitignore 파일의 코드 입력에서 아래와 같이 입력하면 적용

1 images/ (<--폴더)
2 data.xlsx
```

- images 폴더랑 data.xlsx 파일  git 관리 에서 뺌



```bash
1	*.xlsx
2	!data.xlsx
```

- 모든 xlsx 확장자는 무시하는데 그 중 'data.xlsx'파일은 git 관리에 포함



- ignore 을 도와주는 웹 사이트

  https://www.toptal.com/developers/gitignore

  https://github.com/github/gitignore