[TOC]

# <일반 web server>



## <Web_server>

> * 인터넷을 통해 Client의 request가 전달됐을 때, 이 request를 처리하는 Hardware & Software ==> 정적 resource를 service! (정적 resource == 이미지, 동영상 등)
> * 예) Apache, NginX



## <CGI(Common Gateway Interface)>

> * 일반 web server에서 프로그램(application) 수행시키는 규칙
> * 정적 기능하는 web server에 동적 기능 즉, program을 수행시키는 기능 부여
> * 단점 : 웹서버 내에서 프로그램까지 돌리려고 하니깐 서버 과부하 문제
> * ex) C나 Query 언어로 ??



## <WAS (web application server) 방식>

> * 일반적으로 web server와 web application을 동작시킬 수 있는 `Container(engine)`를 분리
> * 즉, WAS 안에 다시 web server를 분리하고, Container(engine) (== 프로그램의 집합체)가 프로그램을 구동시킬수 있도록!
> * 'client request' --> web server(Apache..) --> WAS(Tomcat, JBOs) 속 web server --> Container 프로그램 실행
>   동적 프로그램 실행을 request 할 때! 위와 같은 일련의 작업



---



# <파이썬 쪽 web server>



## WSGI(Web Server Gateway Interface)

> * python에 종속된 개념
> * web server가 python 프로그램을 실행시킬 수 있는 규칙 (CGI랑 비슷하네)
> * python으로 python script(web application) 실행하게끔 web server와 통신하는 규약
> * WSGI server(middle ware)가 존재하고 이게 WAS와 같은 역할 담당



## Django

> * python으로 만들어진 무료로 사용할 수 있는 web application 작성할 수 있는 Framework
> * `WSGI` 규약이 자동 적용된 Django라는 Framework를 통해 만듦!



### <Django의 특징>

> * `ORM` database 제어
> * MVT 패턴을 사용! (Design 패턴 즉, 프로그램 설계 패턴)
>   (MVC 패턴의 변형)
> * 이 패턴으로 분리해서 관리 & 생성
> * 각각 기능에 따라 코드를 분리해서 만들어야 협업과 관리 용이함.
> * 관리자 page가 자동 생성 (application level에 만들어진 'admin.py')
>   url : localhost:8000/admin ==> 통해 확인할 수 있다.
> * Elegant URL (== url 표현이 조금 더 직관적이고 쉽게 표현 가능하다)



#### MVC 패턴

> * 다양한 패턴 중 MVC 패턴!
>   M (model) : Data(Database에 있는 data를 관리할 때 쓰는 라이브러리)
>   V (view) : UI (user interface)
>   C (controller) : Business logic (사용자에게 request에 대한 결과 전송해주는 로직 처리)
> * controller가 client에게 전달할 코드, 방식 결정
> * controller가 model 쪽에 Data를 request
>   model은 Database로부터 Data를 가져와서 controller로 response
> * controller가 view 쪽에 UI 코드 (html) request
>   view는 받은 HTML을 conterller에게 response



#### MVT 패턴

> * M : model
> * V : View == MVC에서 controller 역할
> * T : Template ==UI 제어
> * web client에서 request 보내면, client가 보낸 request를 해석하는
>   `URLConf` 에서 해석한다 그리고 view로 보내준다.
> * View에서 model과 template과 소통하면서 받은 결과 client에게 response한다.



#### ORM (Objective Relational Mapping)

> * 객체 관계 맵핑
> * 데이터베이스의 변천
>   계층형DB --> Network DB --> Relational DB(관계형 DB) --> 객체 시대 도래 --> 객체 관계형 DB(ORM DB)
> * Python에서 class object(객체)를 이용해서 database를 제어
>   ==> 즉, 내부적으로 SQL 자동생성되서 사용 (SQL을 몰라도 database 제어 가능)
>   ==> 원래, Database의 제어는 무조건 SQL 언어를 사용한다.



### 용어 정리 (server-side web application)

* project : 우리가 개발하는 전체 프로그램(우리가 구현하는 site)
* application : 우리 project 내에서 module화된 단위의 program



---



# <Project 설계>



## <설문조사 project 생성>

<html 설계 _ frontend>

> * index.html 생성 (설문 종류 선택)
>   * '취미가 뭐에요?'
>   * '가장 좋아하는 연예인은?'
>   * '어디에 살고 있어요?'
> * detail.html 생성
>   * 각각 설문에 맞는 항목 설정
>   * ex) '가장 좋아하는 연예인은' ==> '아이유 / 김연아 / 홍길동' '투표' 버튼 활성화
> * result.html 생성
>   * '투표' 버튼 누르면 결과 창 볼 수 있도록
>   * data는 각 항목의 투표수
>   * ex) 아이유 - 5표 / 김연아 - 7표 / 홍길동 - 1표



<DataFrame 설계 _ backend>

> * 1번 테이블 : Question Table (질문 내용 담고 있는)
>   * column(`id`) (index값) => 숫자, 자동생성, Primary key, Not null
>   * column(`question`) => 문자열, Not null 
>   * column(`pubdt`) (설문만든날짜) => 날짜 형식, Not null 
> * 2번 테이블 : Choice Table (각 질문의 항목들 저장)
>   * column(`id`) => 숫자, 자동생성, Primary key, Not null
>   * column(`choice_text`) (질문항목) => 문자열, Not null
>   * column(`votes`)(투표수) => 숫자
>   * column(`votes`)(외래키, `foreign key`, Question Tabled의 id) => 각 질문 종류에 항목들을 매치하기 위해
>     (다른 table의 primary key를 가리키는 column == `foreuin key`)



---



# <Project 실습>



## Anaconda (base) 환경에서 

```cmd
conda install django
==> 장고 다운

cd .. ==> C: 으로 옮김

mkdir python-Django
==> 새로운 디렉토리 생성

cd python-Django
==> 생성한 디렉토리로 이동

django-admin startproject mysite
==> 장고 관리자 명령어로 새로운 프로젝트 만들거고 이름을 'mysite'로 

프로젝트 이름이 'mysite'이고 이 안에 이 프로젝트에 대한 설정인'mysite' 디렉토리가 또 있음
구분을 위해 ==> 'MyFirstWeb'으로 이름 바꿈

anaconda prompt로 돌아와서
cd MyFirstWeb ==> 이동

python manage.py startapp polls
==> 내가 만든 프로젝트 안에 새로운 application을 만들기 이름은 'polls'
	python 파일인 application이 만들어진다.
```



## PyCharm

`setting.py`에서 바꿀 것

```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls.apps.PollsConfig'  # ==> polls라는 application에서 설치된 class 추가 해주는 것
    
TIME_ZONE = 'Asia/Seoul'
    
Trminal 
    ==> python manage.py migrate
    ==> database 파일 만드는 것
    
    python manage.py runserver 
    # ==> WSGI서버(middle ware) 기동하는 명령어
 
localhost:8000
```



terminal 실행

```cmd
python manage.py migrate
# ==> database 파일 만드는 것
    
python manage.py runserver 
# ==>서버 기동하는 명령어


브라우저 창에서 ==> localhost:8000 입력

서버 구동 완료
```



## <Project 생성시 구조 정리>

> * 프로젝트를 처음 만들 때, 만들어지는 폴더 & 파일
>   * `'mysite'(:directory)` : 프로젝트와 똑같은 이름으로 설정파일이 들어있는 폴더가 만들어 진다.
>     * `settings.py` : 프로젝트 전체 설정
>     * `urls.py` : 프로젝트 level의 url pattern을 정의하는 `URL Conf`가 있는 파일
>     * `wsgi.py` : wsgi werver (WAS와 비슷한거) 앞에 있는 외부 web server(Apache, NginX)와 연동할 때 사용하는 파일이다. (우리는 사용 안 할 예정)
>   * `'polls'(:directory)` : 프로젝트 안 application을 의미
>     * `admin.py` : Admin site(관리자 page)에 model class를 등록 / django가 자동생성해주는 application level의 관리자 장치 ==> model class(database와 연동하는 역할?)를 등록하는 곳.
>     * `apps.py` : application의 설정, class 정의
>     * `models.py` : Database table과 연관된 model class를 정의하는 파일
>                    ==> 즉, 이곳에 class 만들면, Database table이 만들어진다.
>     * `views.py` : 로직 처리하는 view함수 정의하는 file 
>   * `'manage.py'` : 이 프로젝트에서 파이썬 시행해서 뭔가 작동하고 싶을 때 사용