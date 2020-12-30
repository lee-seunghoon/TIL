# push 충돌 상황



- 원격 저장소(github)에 가지고 있는 작업사항과 

- 로컬 저장소(내 pc 폴더)에 있는 작업 사항이
- 다르다, 즉, 버전이 다르다.
- 즉 push가 충돌





## 해결방법

```bash
#원격에서 pull 먼저 가져온다.
$ git pull origin master

# 나가는 방법
esc --> :wq  #입력

# 이 과정에서 merge commit이 발생하단

# 그 다음 pushㄱㄱ
$ git push origin master
```



