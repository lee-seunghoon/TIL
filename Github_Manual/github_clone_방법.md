# 원격저장소 활용

> `Clone` 원격 저장소를 복제하여 로컬에서 활용할 수 있도록. 



# Github에 있는 commit 파일을 받아 오는 방법



```bash
$ git clone https:// ... #(<--github code url 주소)

# 없는 파일을 가져온다는 의미
# pull과는 또 다르다.
# pull은 협업 상태에서 원격 저장소에서 업데이트 된 commit을 가져오는 것.

# clone은 원격 저장소에 init 돼 있는 상태 그대로 받아온다.
# 알집으로 받아오면 그냥 파일만 받아오고 새로운 init , commit을 시작하는 것이다.
```

