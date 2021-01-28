# git 기초 명령어

> 분산 버전 관리 시스템(DVCS)



## 0. 로컬 저장소(repository) 설정

```bash
$ git init
# 초기화가 되었다. in 뒤 경로에서.
Initialized empty Git repository in C:/Users/USER/Desktop/practice/.git/
(master)
```

- `.git` 폴더가 생성되고, 여기에 모든 git과 관련된 정보들이 저장된다.



## 1.기본작업 흐름

> 모든 작업은 touch로 파일을 만드는 것으로 대체



### 1. add

```bash
$ git add . 	# . : 현재 디렉토리(하위 디렉토리 포함)
$ git add a.txt # 특정 파일
$ git add my_folder/ # 특정 폴더
$ git add a.txt b.txt c.txt # 복수의 파일
```

- working directory의 변경사항(첫번째 통)을 staging area(두번째 통) 상태로 변경 시킨다.

- 커밋의 대상 파일을 관리한다.

```bash
$ touch a.txt
$ git status
On branch master

No commits yet
# 트래킹이 되고 있지 않는 파일들...
# => 새로 생성된 파일

Untracked files:
	# add 명령을 사용해!
	# 커밋이 될 것에 포함시키기 위하여..
	# => Staging area (두번째 통)으로 넣기 위해서
  (use "git add <file>..." to include in what will be committed)
        a.txt

nothing added to commit but untracked files present (use "git add" to track)
```



- add 이후

```bash
$ git status
On branch master

No commits yet

Changes to be committed:
# 커밋이 될 변경사항
# SA(두번째 통)에 넣어 있는 아이들
  (use "git rm --cached <file>..." to unstage)
        new file:   a.txt
```



### 2. commit

```bash
# 버전 하나로 
$ git commit -m 'First commit'
[master (root-commit) f414b5a] First commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a.txt

```

- `commit`은 지금 상태를 스냅샵 찍어서 버전을 확정 짓는다.
- 커밋 메시지는 지금 기록하는 이력을 충분히 잘 나타낼 수 있도록 작성한다.
- `git log` 명령어를 통해 지금까지 기록된 커밋들을 확인할 수 있다.



## 2.기타 명령어

### 1. status

> 로컬 저장소의 상태 확인

```bash
$ git status
```



### 2. log

> 커밋 히스토리 보는 방법

```bash
$ git log
commit f414b5a7d237a750dee45e8f0c65e89fee528b68 (HEAD -> master)
Author: dad0439 <dad0439@naver.com>
Date:   Tue Dec 29 14:10:59 2020 +0900

    First commit

$ git log --oneline
f414b5a (HEAD -> master) First commit

$ git log -2 # 그냥 git log랑 무슨 차이인지 모르겠네.
commit 0838a38c2608fc3e1b9d52b836a4e88498384786 (HEAD -> master, origin/master)
Author: dad0439 <dad0439@naver.com>
Date:   Tue Dec 29 14:41:51 2020 +0900


$ git log --oneline -1
```



## 3. github(원격저장소)에 업로드 하기

> 다양한 원격저장소 서비스 중에 Github를 기준으로 설명

### 준비사항

- Github에 비어 있는 저장소(repository)를 만든다.



### 기초 명령어

> **원격 저장소 설정**

```bash
$ git remote add origin https://github.com/lee-seunghoon/practice.git
# 깃, 원격저장소를(remote) 추가해줘(add) origin이라는 이름으로 URL

$ git push origin master
# origin 원격저장소의 master 브랜치로 push
```

- 이 작업 이 후 로그인

- 설정된 원격저장소를 확인하기 위해서는 아래의 명령어를 입력한다.

  ```bash
  $ git remote -v
  ```

- 다음 origin 깃을 지워줘

  ```bash
  $ git remote rm origin
  ```

- 추가 업로드

  ```bash
  $ git push origin master
  ```

  









