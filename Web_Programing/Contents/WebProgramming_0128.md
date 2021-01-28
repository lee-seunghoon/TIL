[TOC]

# <Django WSGI 통신 흐름 정리>



* `client request` : 'http://localhost:8000/polls/'
* 우리 project안 urls.py 안 `URL_Conf`를 거쳐 View 안에 지정한 함수로 전달.
* `View`에서 다양한 로직을 처리 후 client에게 response 결과를 전송
  * 우선 `model`에게 data 요청 후 받아 옴. (data를 `객체`로 받아옴.)
  * 그리고 `templates`에게 client 화면에 어떻게 표현할건지 modeld에서 받은 data를 적용한 `html`값을 받아옴.
  * 그렇게 `request + data + html` 을 `render` 한 결과값을 `HTTPResponse` 형식으로 `View`에서  `client`에게 전달!
* client 화면에 출력



# <Application 개발>



## <Admin site 계정 만들기>

> anaconda prompt에서 내 프로젝트 디렉토리 안으로 이동한 후 
> ==> `python manage.py createsuperuser` 입력 후 id/pw 생성



## <Application 개발 시작>

### step1. Model 생성

> * Database 안에 있는 table과 연동! ==> 그래서 model을 만든다는 의미는 Database에 Table을 만든다는 의미 ==> model은 class로 만들어 진다.
> * polls/models.py ==> model을 정의하는 파일
>   그래서 model 안에 2개의 class를 만들 것!(Question, Choice) ==> 2개의 Database 생성

* model.py

  ```python
  from django.db import models
  
  class Question(models.Model):
      question_text = models.CharField(max_length=200)
      pub_date = models.DateTimeField('date published')
  
      def __str__(self):
          return self.question_text  
      	# ==> 위에 설정한 질문text를 문자열로 표현해주기 위해서!
          #     이거 없으면 메모리 주소로 출력됨
  
      	# 위에서 정의되는 class가 데이터베이스의 Table과 mapping 된다!
      	# 그럼, Table(pandas dataframe과 동일한 형식)의 column은 어떻게 정의? 
  		# ==> 속성으로 표현
      	# 컬럼명 = models.CharField(max_length=200)  <== 이게 속성을 나타내는거지
      	# models.CharField(max_length=200) 
          #	==> 문자열을 의미하는 데 최대 길이 200자로 제한!
      	# pud_date = models.DateTimeField('date published') 
          # ==> 날짜 형식, 'date published' : 그냥 설명 문자열
  
  class Choice(models.Model):
      choice_text = models.CharField(max_length=200)
      votes = models.IntegerField(default=0)
      question = models.ForeignKey(Question, on_delete=models.CASCADE)
  
      def __str__(self):
          return self.choice_text
  
      # models.IntegerField(default=0) ==> 정수 표현, 초기값을 0
      
      # ForeignKey는 종속의 의미를 갖는다!
      # ForeignKey 제약사항(constraint) : ForeignKey인 원본 data 지우고 싶으면 먼저 ForeignKey와 연결된 table에서 관련 자료 지워야 한다.
      
      # 그런데, 이렇게 하면 너무 복잡하니깐 
      #	--> 원본 지우면 링크된 data 같이 지우게 할 수 있다.
      # 'on_delete=models.CASCADE' ==> 이렇게 적용!!
  ```



### step2. admin site 등록

* admin.py (==> admin site에서 관리할 수 있도록 우리가 만든 model class 등록!)

  ```python
  from django.contrib import admin
  from polls.models import Question, Choice  
  # ==> 우리 프로젝트 아래서부터 시작 --> polls라는 패키지에서 models라는 모듈 안에 저 class들 사용할거야
  
  admin.site.register(Question)
  admin.site.register(Choice)
  ```



### step3. class로 만든 model을 database에 적용

* 새로운 Terminal 열기

  ```cmd
  Microsoft Windows [Version 10.0.18363.1316]
  (c) 2019 Microsoft Corporation. All rights reserved.
  
  (base) C:\python-Django\MyFirstWeb>python manage.py makemigrations 
  						(makemigrations ==> database 변경사항을 등록!)
  Migrations for 'polls':
    polls\migrations\0001_initial.py (==> 이렇게 새로운 변경사항이 'migrations'에 만들어진다.)
      - Create model Question
      - Create model Choice
      
  (base) C:\python-Django\MyFirstWeb>python manage.py migrate
  					(migrate ==> 등록된 변경사항을 실제 database에 적용하는 작업)
  Operations to perform:
    Apply all migrations: admin, auth, contenttypes, polls, sessions
  Running migrations:
    Applying polls.0001_initial... OK
  
  ```

  

Database 확인하는 browser tool



### step4. URL Conf에 내 application 연결 할 수 있도록 설정

* ./mysite/urls.py

  ```python
  # 아래 내용 추가
  
  from polls import views
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('polls/', views.index, name='index')
      # ==> 클라이언트 리퀘스트를 views로 보내서, index 함수 실행!
  ]
  ```



### step5. View 함수 설정

```python
from django.shortcuts import render
from polls.models import Question

# request는 client의 request를 모아서 객체로 바뀐 것 (django가 자동으로 만들어줌)
def index(request):
    # 데이터베이스를 뒤져서 설문목록을 가져온다.
    # (테이블명 : polls_question , 클래스명 : Question)

    question_list = Question.objects.all().order_by('-pub_date')[:5]
    # 우리가 불러오려는 database의 행 recorde data를 객체로 가져올거야 모두!
    # .oder_by ==> 정령해서 가져 올건데,
    # ('-pub_date') pub_date라는 column을 기준으로, 내림차순으로(마이너스)
    # q_list 안에는 객체 형태로 이뤄진 record가 리스트 안에 쭉 나열된 상태

    context = { 'q_list':question_list }
    # Data 전달용 dict 생성해서 객체 만들기

    return render(request,'index.html', context)
```



### step6. templates 만들기 

1. 'polls' 폴더 안에 'templates'폴더 만들고 (이름 정해져 있음)
2. index.html 만들기 (무조건 'templates'라는 폴더 안에 있어야 함)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <!-- templates 안에서 특별한 규칙 -->
    <!-- {%  %} + {% end... %} 이 안에는 pythjon의 함수나, 문법을 사용할 수 있다.  -->
    <!-- {{ }} 이 안에는 문자열을 집어 넣을 수 있다. -->
    {% if q_list %}
        <ul>
            {% for question in q_list %}
                <li><a href="/polls/{{ question.id }}">{{ question.question_text }} </a>></li>
            {% endfor %}
        </ul>
    {% else %}
        <h1>데이터가 없어요!</h1>
    {% endif %}
</body>
</html>
```

