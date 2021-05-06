# push 충돌 상황



- 원격 저장소(github)에 가지고 있는 작업사항과 

- 로컬 저장소(내 pc 폴더)에 있는 작업 사항이
- 다르다, 즉, 버전이 다르다.
- 즉 push가 충돌



```bash
$ git push origin master
To https://github.com/edutak/practice.git
 ! [rejected]        master -> master (fetch first)
 # error!!!!!
error: failed to push some refs to 'https://github.com/edutak/practice.git'
# 거절(rejected), 왜냐하면..
# 원격저장소가 가지고 있는 작업사항
hint: Updates were rejected because the remote contains work that you do
# 너가 로컬에 가지고 있지 않다.
hint: not have locally. This is usually caused by another repository pushing
# 너는 원할거다..
# 먼저 원격저장소의 변경사항을 통합하는 것을..
# 다시 push하기 전에
# git pull .....?
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```





## 해결방법

```bash
#원격에서 pull 먼저 가져온다.
$ git pull origin master

# vim 편집기에서 나가는 방법
esc --> :wq  #입력

# 이 과정에서 merge commit이 발생한다

# 그 다음 pushㄱㄱ
$ git push origin master
```



```bash
$ git log --oneline
# merge commit 발생!
3bb716a (HEAD -> master, origin/master) Merge branch 'master' of https://github.com/edutak/practice
7822758 Update README.md
d8f1ae3 hi
e94b045 Create README.md
1ce8a44 A
3566a2b 추가작업!!
08c9f10 hi
16915c2 파워포인트
b844872 보고서
f64d131 Init
4d9c1cc First commit
```



## 상황 비교 하는 방법

* 로컬

  ```bash
  $ git log --oneline
  d8f1ae3 (HEAD -> master) hi
  1ce8a44 (origin/master) A
  3566a2b 추가작업!!
  08c9f10 hi
  16915c2 파워포인트
  b844872 보고서
  f64d131 Init
  4d9c1cc First commit
  ```

* 원격(github remote)

  ![Screen Shot 2020-12-30 at 오전 10.45](md-images/Screen%20Shot%202020-12-30%20at%20%EC%98%A4%EC%A0%84%2010.45.png)

- 로컬과 원격의 commit 내역을 비교하면서 충돌을 확인한다.