# Pull request



## 1. 우리 작업에서 branch 만들어서 pull request 하는 방법

> 새로운 branch를 만들어서 그것을 push



### 상황

- 협업 작업으로 각자 git 작업 한 뒤 push 해야 하는 상황
- 똑같은 branch로 push하면 그냥 commit 되면서 이어지기 때문에
- manager가 검토할 수 없어
- 그래서 다른 `branch`에서 작업 한 후 push
- 그럼 `remote repository`에서 pull request 할거냐고 알림 뜸
- 클릭해서 `pull request` 보내야함
- 관리자가 보고 확인한 후 `confirm` or `reject`

```bash
$ git checkout -b new_branch_name 

# 작업 후

$ git add .
$ git commit -m '커밋메시지'

# push 할 때 기존 branch가 아니라 내가 만든 branch로 push

$ git push origin new_branch_name
```





## 2. folk로 pull request 하는 방법

> 초대 받지 않은 다른 작업에 참여 가능 (오픈 소스 참여)



