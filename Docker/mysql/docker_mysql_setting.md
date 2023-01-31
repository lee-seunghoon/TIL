## 1. ubuntu - docker 설치
- https://docs.docker.com/engine/install/ubuntu/   

<br>

## 2. sudo 없이 docker & docker compose 사용
```bash
# docker 그룹에 user 등록
$ sudo usermod -aG docker ${USER}

# 계정 logout 후 다시 login
$ sudo su -
$ su - shlee

# 그룹에 잘 추가 됐는지 확인 
$ groups ${USER}
```

<br>

## 3. docker-compose.yml 생성

`~/mysql/docker-compose.yml`

```yaml
version: '3'
services:
    mysql:
        image: library/mysql:5.7
        container_name: nlp-feedback
        restart: always
        ports:
            - 3306:3306
        environment:
            MYSQL_USER: shlee
            MYSQL_PASSWORD: shlee
            MYSQL_ROOT_PASSWORD: root
            TZ: Asia/Seoul
        volumes:
            - ./db/mysql/data:/var/lib/mysql
            - ./db/mysql/init:/docker-entrypoint-initdb.d
```

<br>

`~/mysql/db/mysql/data` , `~/mysql/db/mysql/init 디렉토리 생성`
```bash
mkdir db/mysql/data
mkdir db/mysql/init
```

<br>

## 4. docker image build and up

- `~/mysql`
```bash
docker compose up -d
```

<br>

- image & ps 확인
```bash
docker images
docker ps
```

<br>

## 5. mysql docker container 접속 및 root 계정 접속
```bash
docker exec -it nlp-feedback /bin/bash

mysql -u root -p  # => 이후 password 입력
```

<br>

## 6. user list 확인
```sql
use mysql;
select user, host from user;
```

<br>

## 7. 관리자 계정에 모든 권한 부여

- 처음 docker build 시 생성한 계정을 관리자 계정으로 사용 할 경우
```sql
GRANT ALL PRIVILEGES ON *.* TO 'shlee'@'%';
FLUSH PRIVILEGES;
```

<br>

- 관리자 계정을 생성하고 권한 부여할 경우
```sql
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'loalhost' IDENTIFIED BY 'adminpass' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'127.0.0.1' IDENTIFIED BY 'adminpass' WITH GRANT OPTION;
```

<br>

- 가끔 특정 버전에서의 버그 때문에 위의 명령으로도 GRANT 권한이 추가되지 않을 때가 있다.
- 이 문제를 해결하기 위해 강제로 user 테이블에 GRANT 옵션을 부여
- 마지막으로 FLUSH PRIVILEGES 명령으로 권한을 적용
```sql
UPDATE mysql.user SET grant_priv='Y' WHERE USER='admin';
FLUSH PRIVILEGES;
```

<br>

## 8. mysql 패스워드 정책 변경

- 출력이 아래와 같이 나오면 설치가 안돼 있고 결국 패스워드 정책을 설정하려고 할 때 다음과 같은 error가 발생한다
- `ERROR 1193 (HY000): Unknown system variable 'validate_password_policy'`
```sql
# password 정책을 위한 plugin 확인
select plugin_name, plugin_status from information_schema.plugins where plugin_name like 'validate%';
```

<br>

- plugin 설치 후 위 명령어 확인해보면 다음과 같은 이미지 출력
```bash
# 설치
install plugin validate_password soname 'validate_password.so';

# 재확인
select plugin_name, plugin_status from information_schema.plugins where plugin_name like 'validate%';
```

<br>

- password policy 확인
```sql
SHOW VARIABLES LIKE 'validate_password%';
```

<br>

- 기본 Default 값이 MEDIUM

    - `…check_user_name` : username(아이디)과 동일한 문자가 들어갔는지 체크 여부
    - `…length` : 최소 자리수
    - `…mixed_case_count` : 대소문자 최소 사용 횟수
    - `…special_char_count` : 특수문자 최소 사용 횟수

<br>

## 9. 기본 계정 패스워드 변경
```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'new_password';
```

<br>

## 10. 패스워드의 사용기간 및 복잡도를 기관 정책에 맞도록 설정

- 최대사용 기간 세팅
    - 확인
    0 또는 NULL 값 나오면 취약
    ```sql
    show variables like 'default_password_lifetime';
    ```
    - 수정
    ```sql
    SET GLOBAL default_password_lifetime=90;
    ```

<br>

- 복잡도 세팅
    - 확인
    0 또는 LOW 나오면 취약
    ```sql
    show variables like 'validate_password_policy';
    ```
    - 수정
    ```sql
    SET GLOBAL validate_password_policy=1
    ```

<br>

## 11. 서비스 계정, 백업 계정 세팅

- 백업 계정
    - 백업 계정의 비밀번호는 스크립트 파일에 노출될 수 밖에 없기 때문에 최소 권한을 가지도록 별도로 준비하는 것이 좋다.
    ```sql
    GRANT LOCK TABLES, RELOAD, REPLICATION CLIENT, SELECT, SHOW DATABASES, SHOW VIEW ON *.* TO 'backup'@'localhost' IDENTIFIED BY 'backuppass';
    ```

<br>

- 서비스 계정
    - 서비스용 계정을 생성하고, 그 계정에 전역적으로 부여돼야 하는 FILE이나 PROCESS와 같은 권한 부여
    ```sql
    GRANT FILE, PROCESS, RELOAD, REPLICATION CLIENT, REPLICATION SLAVE, SHOW DATABASES ON *.* TO 'nlp_user'@'localhost' IDENTIFIED BY 'svc_passwd';
    ```

    - 서비스용 계정이 접속해 쿼리를 실행해야 하는 DB별로 권한 부여
    ```sql
    GRANT ALTER, ALTER ROUTINE, CREATE, CREATE ROUTINE, CREATE VIEW, DROP, INDEX, SHOW VIEW, CREATE TEMPORARY TABLES, DELETE, EXECUTE, INSERT, LOCK TABLES, SELECT, UPDATE ON svc_db_name.* TO 'nlp_user'@'localhost';
    ```

<br>

## 12. DB 생성

- ```sql 
  create database nlp
  ```

<br>

## 13. DB 원격 접속 제한

- MySQL을 설치하면 기본적으로 로컬(localhost)에서만 접속이 가능하고 외부에서는 접속이 불가능하게 되어 있다.
- 계정의 host를 보면 허용 ip를 확인할 수 있다.
    ```sql
    select user, host from mysql.user
    ```