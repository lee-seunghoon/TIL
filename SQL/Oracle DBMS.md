# Oracle DBMS 입문



> - 강의 : 생활코딩 (https://youtube.com/playlist?list=PLuHgQVnccGMB5q5uJIDhLlcC2V6tyXhY6)



### 키워드

> - 관계형 데이터베이스 (RDBMS)
> - 2차원 데이터 (x,y 평면좌표 / 행열 표)
> - CRUD (생성, 읽기, 수정, 삭제)
> - 스키마 : 서로 연관된 표(table)들을 그룹핑하는 상위 디렉토리
>   - 본질적 정의 : 스키마에 속하는 표(table)들을 정의하는 정보
> - 사용자 : 사용자를 만들면 스키마가 생성되고, 사용자가 스키마를 관리할 수 있다.



### Oracle 사용자 & 스키마 생성

> - Oracle 설치
> - sqlplus 실행

```sql
user-name : sys AS SYSDBA  # (== 관리자 권한으로 실행)
SQL>> CREATE USER sherlocky IDENTIFIED BY 111111;
```



### Oracle 사용자 권한 부여

```sql
SQL>> GRANT DBA TO sherlocky;  # (== DBA 즉, 모든 권한)
```



### 직접 만든 사용자로 테이블 만들기

> - `topic` 이라는 `table` 만들기

```sql
user-name : sherlocky
password : 111111

CREATE TABLE topic (
	id NUMBER NOT NULL,
    title VARCHAR2(50) NOT NULL,
    description VARCHAR2(2000) NOT NULL,
    created DATE NOT NULL
);
```



### 테이블 목록 조회

```sql
SELECT table_name FROM all_tables WHERE OWNER = 'SHERLOCKY'
```



### 데이터 행 추가

```sql
INSERT INTO topic
	(id, title, description, created)
	VALUES
	(1, 'Oracle', 'Oracle is not easy', SYSDATE);
	
# 데이터 베이스 Table 에서 데이터 CRUD 하면 꼭 commit 해야한다
commit;
```



### 데이터 행 읽기

```sql
# 모든 컬럼과 모든 행을 가져 오기
SELECT * FROM topic;

# 특정 컬럼만 불러오기
SELECT id, title, created FROM topic;

# id가 1번인 행만을 보고 싶다
SELECT * FROM topic WHERE id = 1;

# id가 1이상인 특정 컬럼만 가져오기
SELECT id, created FROM topic WHERE id > 1;
```



### 데이터 정렬하기

```sql
# id를 기준으로 내림차순 정렬
SELECT * FROM topic ORDER BY id DESC;

# id를 기준으로 오름차순 정렬
SELECT * FROM topic ORDER BY id ASC;

# title 기준으로 오름차순 정렬
SELECT * FROM topic ORDER BY title ASC;
```



### 페이지 기법

```sql
# 1번째 행부터 데이터 가져오기 (0번째 제외)
SELECT * FROM topic OFFSET 1 ROWS;

# 2번째 행부터 데이터 가져오기 (0~1번째 제외)
SELECT * FROM topic OFFSET 2 ROWS;

# FETCH == 몇개 가져올 것인가
SELECT * FROM topic
		OFFSET 0 ROWS
		FETCH NEXT 2 ROWS ONLY;
```

