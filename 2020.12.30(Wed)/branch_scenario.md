### 상황 1. fast-foward (무임승차)

> fast-foward는 feature 브랜치 생성된 이후 master 브랜치에 변경 사항이 없는 상황

1. feature/test branch 생성 및 이동

   ```bash
   $ git branch featur/test  # branch 생성
   
   $ git branch  # branch 확인
     featur/test
   * master
   
   $ git checkout featur/test  #branch 변동
   Switched to branch 'featur/test'
   (feature/test) $
   ```

   

2. 작업 완료 후 commit

   ```bash
   $ touch test.txt
   $ git add .
   $ git commit -m 'Complete test'
   [feature/test 5ff4709] Complete test
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 test.txt
   
   $ git log --oneline
   # feature/test 브랜치 이면서 지금 이 브랜치에 있다.
   7ec1c0d (HEAD -> featur/test) Complete test
   # master 브랜치라는 의미
   e68226b (master) branch
   ```

   

3. master 이동

   ```bash
   $ git checkout master
   Switched to branch 'master'
   (master) $
   ```
```
   
   


4. master에 병합

   ```bash
   $ git log --oneline
   c6f5db0 (HEAD -> master) branch # <-- master에서 이미 commit된 메시지
   $ git merge feature/test
   Updating c6f5db0..5ff4709
   # Fast-forward!!!!
   # MASTER에 변경사항 없어서 그냥 앞으로 
   # 변경사항 없다는 말은 'feature/test'branch에서 작업 후 마스터로 돌아온 후 작업X
   Fast-forward
    test.txt | 0
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 test.txt
```

   

   


5. 결과 -> fast-foward (단순히 HEAD를 이동)

   ```bash
   $ git log --oneline
   7ec1c0d (HEAD -> master, featur/test) Complete test
   e68226b branch
   
   ```

   

6. branch 삭제

   ```bash
   $ git branch -d featur/test
   Deleted branch featur/test (was 7ec1c0d).
   
   ```
   
   

---

### 상황 2. merge commit (역할 분담으로 각자 만들기)

> 서로 다른 이력(commit)을 병합(merge)하는 과정에서 다른 파일이 수정되어 있는 상황
>
> git이 auto merging을 진행하고, commit이 발생된다.

1. feature/data branch 생성 및 이동

   ```bash
   # 브랜치 만들면서 새로운 브랜치로 이동하는거 한 번에 하는 명령어
   $ git checkout -b feature/data
   Switched to a new branch 'feature/data'
   
   ```
   

   
2. 작업 완료 후 commit

   ```bash
   $ touch data.txt
   $ git add .
   $ git commit -m 'Complete data'
   [feature/data 92ef1e8] Complete data
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 data.txt
   $ git log --oneline
   92ef1e8 (HEAD -> feature/data) Complete data
   7ec1c0d (master) Complete test
   e68226b branch
   ```

   

3. master 이동

   ```bash
   $ git checkout master
   Switched to branch 'master'
   ```

   

4. *master에 추가 commit 이 발생시키기!!*

   * **다른 파일을 수정 혹은 생성하세요!**

   ```bash
   #위 1번 작업과 다른 부분. master로 돌아온 후 새로운 작업(new commit)
   $ touch hotfix.txt
   $ git add .
   $ git commit -m 'hotfix'
   [master 1ebf8b4] hotfix
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 hotfix.txt
   $ git log --oneline
   6930e34 (HEAD -> master) hotfix
   5ff4709 Complete test
   c6f5db0 Add README
   ```

   

5. master에 병합

   ```bash
   $ git merge feature/data
   
   ```

   

6. 결과 -> 자동으로 *merge commit 발생*

   * vim 편집기 화면이 나타납니다.

   * 자동으로 작성된 커밋 메시지를 확인하고, `esc`를 누른 후 `:wq`를 입력하여 저장 및 종료를 합니다.
      * `w` : write
      * `q` : quit
      
   * 커밋을  확인 해봅시다.

      ```bash
      $ git log --oneline
      34dfb67 (HEAD -> master) Merge branch 'feature/data'
      1ebf8b4 hotfix
      92ef1e8 (feature/data) Complete data
      7ec1c0d Complete test
      e68226b branch
      
      ```

      

7. 그래프 확인하기

   ```bash
   $ git log --oneline --graph
   *   34dfb67 (HEAD -> master) Merge branch 'feature/data'
   |\
   | * 92ef1e8 (feature/data) Complete data
   * | 1ebf8b4 hotfix
   |/
   * 7ec1c0d Complete test
   * e68226b branch
   
   ```

   

   

8. branch 삭제

   ```bash
   $ git branch -d feature/data
   Deleted branch feature/data (was 92ef1e8).
   
   ```

   

---

### 상황 3. merge commit 충돌 (각 part 합치기)

> 서로 다른 이력(commit)을 병합(merge)하는 과정에서 동일 파일이 수정되어 있는 상황
>
> git이 auto merging을 하지 못하고, 해당 파일의 위치에 라벨링을 해준다.
>
> 원하는 형태의 코드로 직접 수정을 하고 merge commit을 발생 시켜야 한다.

1. feature/web branch 생성 및 이동

   ```bash
   $ git checkout -b feature/web
   Switched to a new branch 'feature/web'
   
   ```

   

2. 작업 완료 후 commit

   ```bash
   # README.md 파일 수정!!
   $ touch README.md
   $ git status
   On branch feature/web
   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git restore <file>..." to discard changes in working directory)
           modified:   README.md
   
   Untracked files:
     (use "git add <file>..." to include in what will be committed)
           web.txt
   
   no changes added to commit (use "git add" and/or "git commit -a")
   $ git add .
   $ git commit -m 'Update and Complete'
   ```
   
   


3. master 이동

   ```bash
   $ git checkout master
   ```
   
   


4. *master에 추가 commit 이 발생시키기!!*

   * **동일 파일을 수정 혹은 생성하세요!**

   ```bash
   # (master에서) README 파일을 수정
   $ git status
   On branch master
   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git restore <file>..." to discard changes in working directory)
           modified:   README.md
   
   no changes added to commit (use "git add" and/or "git commit -a")
   $ git add .
   $ git commit -m 'Update README'
   ```

   

5. master에 병합

   ```bash
   $ git merge feature/web
   
   # 자동으로 병합하려고 했는데
   Auto-merging README.md
   
   # README.md 파일에서 충돌이 발생했어
   CONFLICT (content): Merge conflict in README.md
   
   # 자동 merge 실패했다 : 충돌을 고치고 결과를 커밋하라.
   Automatic merge failed; fix conflicts and then commit the result.
   
   (master|MERGING) # --> 이게 충돌된 다음 나오는 문구
   
   ```
   
   


6. 결과 -> *merge conflict발생*

   ```bash
   $ git status
   On branch master
   You have unmerged paths.
     (fix conflicts and run "git commit")
     (use "git merge --abort" to abort the merge)
   
   Changes to be committed:
           new file:   web.txt
   # 어디서 충돌 난건지 확인할 수 있다.
   Unmerged paths:
     (use "git add <file>..." to mark resolution)
           both modified:   README.md  # 각 branch에서 수정됐다.
   
   ```
   
   


7. 충돌 확인 및 해결

   ```bash
   # 충돌난 파일 들어가서 수정
   
   <<<<<<< HEAD
   # Project
   
   * data 프로젝트 blah blah
   =======
   # 프로젝트
   
   * web 개발
   >>>>>>> feature/web
   ```
   
   


8. merge commit 진행

   ```bash
   $ git add .
   $ git commit
   ```

   * vim 편집기 화면이 나타납니다.
     
   * 자동으로 작성된 커밋 메시지를 확인하고, `esc`를 누른 후 `:wq`를 입력하여 저장 및 종료를 합니다.
      
      - `w` : write
   - `q` : quit 
      
   * 커밋이  확인 해봅시다.

      

9. 그래프 확인하기

   ```bash
   
   $ git log --oneline --graph
   *   88942d7 (HEAD -> master) Merge branch 'feature/web'
   |\
   | * 81cbac1 (feature/web) Update and Complete
   * | c6c8337 Update README
   |/
   *   34dfb67 Merge branch 'feature/data'
   |\
   | * 92ef1e8 Complete data
   * | 1ebf8b4 hotfix
   |/
   * 7ec1c0d Complete test
   * e68226b branch
   ```

   


10. branch 삭제

    ```bash
    $ git branch -d feature/web
    ```
    
    
