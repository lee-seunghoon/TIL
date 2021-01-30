[TOC]

## <Application URLConf 나누기>

* mysite\urls.py ==> client의 request가 첫단으로 들어오는 곳 (root urlConf)

```python
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # include 사용하려면 추가해야한다.
from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('polls/', views.index, name='index')
    # ==> 클라이언트 리퀘스트를 views로 보내서, index 함수 실행!

    path('polls/', include('polls.urls'))
    # polls라는 application 안에 urlconf를 따로 만들어서 거기서 urlconf 관리할거야
    # 'polls.urls'파일로 가라는 의미로 include로 명령
]

```



* polls\urls.py 새로 만들기
* 만든 후 입력

```python
from django.urls import path
from polls import views

urlpatterns = [
    path('', views.index, name= 'index') 
    # root urlconf에서 ==> http://localhost:8000/polls/  ==> 이 url까지 넘겨서 보내줘
    # '' ==> 공백의 의미는 저 url의 끝에 아무것도 없이 http://localhost:8000/polls/ 이 자체를 의미하고 싶을 때 사용하지
    
    # 이 url(http://localhost:8000/polls/) request할 때, view에 보내서 index함수 실행
    
    # polls라는 application 안에 urlconf를 따로 만들어서 polls application 관련 urlconf는 여기서 관리할거야
    
]
```



* `namespace` 설정

  > * 다른 appication에서 urlpattern 부여할 때, 이름 설정한 게 `중복`될 위험을 피하기 위해  설정하는거야!
  > * 한 application에서 view에서 실행할 함수의 이름을 index라고 지정했는데, 다른 application에서도 같은 이름 설정하면, 어떤 index view함수를 가져와야 하는지 알 수 없어 
  > * `협업` 때 유용하게 사용하기 위한 규칙같은 느낌
  > * namespace 부여해주고, templates에서는 예) polls:index  ==> 이런식으로 사용해서 구분할거야

  ```python
  from django.urls import path
  from . import views
  
  app_name = 'polls'
  # ==> name space를 부여해줘서, 다른 application의 중복을 미연에 방지
  
  urlpatterns = [
      path('', views.index, name= 'index') # ==> http://localhost:8000/polls/
      # polls라는 application 안에 urlconf를 따로 만들어서 거기서 urlconf 관리할거야
      # 여기서 name은 논리적인 이름이 다른 application에서 겹칠 문제를 방지하기 위해 name space 부여
  ]
  ```

  

## <root templates 설정>

> * project 전체 html을 관리할 templates가 따로 또 필요해



- mysite\settings.py 이동

```python
# TEMPLATES 로 이동
# 맨 위에 os import 해야함

import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  
        	# 'DIRS' ==> templates의 위치를 의미
        	# 'os.path.join' == templates 위치 설정 즉, 추가한다는 의미
        	# BASE_DIR == root project를 의미
        	# 새로 지정 할 templates 폴더 명시 ==> 'templates'
        
        'APP_DIRS': True,  
        # ==> application마다 templates 폴더 만들어서 사용할 수 있게끔 허용
        
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```



## <Application templates 새로 설정>

> * root의 templates가 생기면, view에서 templates 찾을 때 root의 templates에서 html을 먼저 찾는다.
> * 즉, root templates가 있는데 그 안 html 이름이 index로 똑같으면, root꺼를 먼저 찾는다.
> * 그래서 현재 내 application 안에 templates 속에 내 application 이름과 똑같은 폴더 만들어서
> * 그 안에 index.html 파일 넣어놓은다.
> * 그리고 views.py에서 render 안 html 코드를 수정한다.

* polls\views.py

```python
from django.shortcuts import render
from polls.models import Question


def index(request):
    
    question_list = Question.objects.all().order_by('-pud_date')[:5]
    context = { 'q_list' : question_list }
    
    return render(request, 'polls/index.html', context)
	# ==> 'polls/index.html'  여기서 polls는 polls\templates\polls\index.html ==> 
    # 	  여기서 templates 안에 있는 polls를 의미함 application 이름이랑 똑같이 만든 폴더!
```



## <설문조사 선택하면, 이에 맞는 항목이 나오게 하기>

> * request를 다시 요청하는거임!
> * 그럼 urlconf를 설정해야 하는데 이번에는 polls/ 안에서 진행하고 있어서
> * polls\urls.py 에서 작업해야 한다!



* `polls\urls.py` ==>  path 추가

  ```python
  from django.urls import path
  from . import views   # ==> '.' 은 현재 폴더, 현재 application이란 의미 즉, == polls
  
  app_name = 'polls'
  # ==> application이름을 name space이름으로 부여해줘서, 다른 application의 중복을 미연에 방지
  
  urlpatterns = [
      path('', views.index, name= 'index'), # ==> http://localhost:8000/polls/
      # polls라는 application 안에 urlconf를 따로 만들어서 거기서 urlconf 관리할거야
      # 여기서 name은 논리적인 이름이 다른 application에서 겹칠 문제를 방지하기 위해 name space 부여
  	
      #####################################################################
      # ==> 아래 부분 추가
      
      path('<int:question_id>/', views.detail, name='detail')
      # <> : 변하는 값이 나온다는 의미 / int : 정수가 올거란 의미 / question_id 숫자를 의미
      # veiw의 detail함수 사용할거야.
      # 논리적인 이름은 'detail'로 설정
  ]
  ```



* `polls\views.py` ==> detail 함수 추가

```python
from django.shortcuts import render, get_object_or_404
from polls.models import Question


def index(request):
    
    question_list = Question.objects.all().order_by('-pud_date')[:5]    
    context = { 'q_list' : question_list }
   
    return render(request, 'polls/index.html', context)
   

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # get_object_or_404 
    # ==> 숏컷 함수 : 딱 1개의 객체만 들고오고 없으면 not found 404 에러 출력해!
    # ==> 'pk' : primary key를 의미하고, 
    #	         Question table의 칼럼 중에서 pk 속성 가지고 있는 값을 가져 온다.
    
    context = {'selected_question': question}
    return render(request, 'polls/detail.html', context)
```



* `polls\templates\polls\detail.html` 새로운 html 파일 만들고(detail.html) 작성

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <!-- selected_question이라는 객체 안에는 question_id로 선택된 Question table에서 
		한 record가 리스트 안에 있겠지. -->
    <!-- question_text 칼럼명 안에 있는 값을 제목으로 주면 질문 내용이 나오겠지 -->
    <h1>{{ selected_question.question_text }}</h1>
    
    <form action="{% url 'polls:vote' selected_question.id %}" 
          method="POST">
    {# 사용자 지정 양식!<from> / action = 서버url / method 어케 가져올거에요? #}
    {# 사실은  <form action="http://localhost:8000/polls/{{ selected_question.id }}/vote/" method="POST"> 이 표현과 같다  #}

    {# urls.py에서 가져온 request 즉, url을 의미하고 싶을 때, 'polls:vote' 이렇게 사용 #}
    {# 정확히 말하자면, view.detail도 함께 포함돼 있음! #}
    {# polls:vote 안에 변할 수 있는 값으로 ==> question_id를 사용 중 #}

        
    {%  csrf_token %}
    {#  ==> 여러 웹 상에서 보안 문제(cracking, hacking) 막아주는 
        	Django가 제시해주는 보안 코드 #}
    {#  ==> <form></form> tag 쓰면 무조건 이 보안 사용!  #}
        
        {% for choice in selected_question.choice_set.all %}
        {# selected_question과 연결된(foreign key로 연결돼 있어) 'choice' table 속에서 연결된 부분만 다(all) 가져와라 #}
        {# choice == record 객체가 list 형태로 넘어옴  #}

        <input type="radio" 
               name="my_choice" 
               id="kaka{{ forloop.counter }}">
        {# forloop.counter ==> for문이 loop 돌때, 그 index값 == counter  #}
        {#  name이 똑같이 설정돼 있으면, radio 버튼 하나만 선택할 수 있다! #}
        {#  id ==> <label for="id"> ==> 입력한 id 값을 가진 radio버튼에 label을 달아 줄 수 있다.#}
        <label for="kaka{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
        {#  가져온 choice 의 record 중에서 column명이 'choice_text'인 것을 가져오면 항목을 가져오겠네.  #}

        {% endfor%}
    
        
    </form>

</body>
</html>
```



## <투표 버튼 만든 후 투표 적용할 수 있도록>

> step1. submit 버튼을 만들고
>
> step2. 선택한 radio button의 값을 넘겨줄 때, name : value 이 쌍으로 넘겨줘서 value 값 설정해줘야 함!
>
> step3. 사용자 지정 서식(dtail.html의 <form>)에서 ==> url 적용 후 POST 방식으로 data 가져올거에요

* submit 버튼 누르면 새로운 request 요청하는 거야

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>{{ selected_question.question_text }}</h1>

    <form action="{% url 'polls:vote' selected_question.id %}" method="POST">
    
    {%  csrf_token %}
    
        {% for choice in selected_question.choice_set.all %}
        
        <input type="radio"
               name="my_choice"
               id="kaka{{ forloop.counter }}"
               value="{{ choice.id }}">            
               {#  submit 버튼을 누르면, name과 value의 쌍이 서버쪽 url로 넘어감 #}

        <label for="kaka{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
        {% endfor%}

        <br>

        {# 특수한 기능을 포함하고 있는 버튼! #}
        <input type="submit" value="투표">
        {#  이 버튼 클릭했을 때, 서버쪽으로 request 보내는 방법  ==> <form {% url 여기에 서버쪽 url 지정해줘 %}#}
    </form>

</body>
</html>
```



## <투표 버튼 누르면 Data 갱신되게 하기>

* `urls.py` 에 가서 urlconf 설정해줘야 해
  * `polls\urls.py`

```python
from django.urls import path
from . import views   # ==> '.' 은 현재 폴더, 현재 application이란 의미 즉, == polls

app_name = 'polls'


urlpatterns = [
    path('', views.index, name= 'index'),
    path('<int:question_id>/', views.detail, name='detail'),    
    path('<int:question_id>/vote/', views.vote, name='vote')  # ==> polls:vote
    # <int:question_id>/vote/ == 3/vote/
    # 사실 최종적으로 만들어지는 url request == http://localhost:8000/polls/3/vote/
]
```



* submit 버튼 누르면 form tag 안에 url로 request가 이 urlconf로 와서 'polls:vote' 이걸 찾아서 view vote 함수로 request 보내줌

  > * 그럼, 저렇게 만들고, views.py 가서 vote 함수 만들어줘야 해!

```python
from django.shortcuts import render, get_object_or_404
from polls.models import Question


def index(request):
    
    question_list = Question.objects.all().order_by('-pud_date')[:5]    
    context = { 'q_list' : question_list }
   
    return render(request, 'polls/index.html', context)
   

def detail(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)    
    context = {'selected_question': question}
    
    return render(request, 'polls/detail.html', context)

def vote(request, question_id):
    # view 쪽으로 전달되는 게 '<int:question_id>/vote/'

    question = get_object_or_404(Question, pk=question_id)
    selected_choice = question.choice_set.get(pk=request.POST['my_choice'])
    
    selected_choice.votes += 1
    selected_choice.save()  # ==> 이 객체에 대해 변경 data 내용 database에 저장해주세요
    
    # 우선 맨 처음 질문 선택 화면으로 이동해주자
    context = { 'q_list' : question_list }
    return render(request, 'polls/index.html', context)
```



## <투표 후 data에 적용된 투표 결과 출력>

* vote 함수를 수정해줘야 함!

  > step1. 우선 아무 값도 지정해주지 않으면 error 뜨기 때문에, exception 설정 필요

  * `polls\views.py`

```python
from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice  # ==> Choice 추가


def index(request):
    
    question_list = Question.objects.all().order_by('-pud_date')[:5]    
    context = { 'q_list' : question_list }
   
    return render(request, 'polls/index.html', context)
   

def detail(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)    
    context = {'selected_question': question}
    
    return render(request, 'polls/detail.html', context)

def vote(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST['my_choice'])
        # question.choice_set.get() ==> choice set과 foreign key 연결된 자료 가져올건데
        # pk=request.POST['my_choice']  ==> pk가 request.POST['my_choice']인 것을 가져올건데
        # request.POST == submit 눌렀을 때, <form> tag 안에 있는 url로 POST 방식 요청할 때,
        # 그 아래 선택 돼 있는 'name과 value' 가 쌍으로 넘어옮
        # 예를 들어 name(='my_choice') : value(="{{ choice.id }})" 이게 넘어와
        # 그래서 'my_choice'(name)를 입력하면 이건 value를 즉, choice.id 값을 준다!
        # 그래서 pk 값이 내가 선택한 choice.id 값이다.
        
    except(KeyError, Choice.DoesNotExist):
        # Key Error 오류가 나면 제외할건데
        # Choice 선택값이 존재하지 않을 때 == 즉, 아무것도 선택하지 않은거야
        # ==> Choice.DoesNotExist
        
        # 그럼, name : value 이 값이 아무것도 없겠지
        # 그럼, 위 get에서 pk 값을 아무것도 가져올 수 없겠지

        # pk가 없어서 오류가 발생할 경우를 지칭
        return render(request, 'polls/detail.html', 
                      {'selected_question': question,
                       'error_message': '아무것도 선택하지 않았어요!'})
        
    
    else: # Error가 안 뜰 경우
        selected_choice.votes += 1
    	selected_choice.save()
        
        context = { 'q_list' : question_list }
    	return render(request, 'polls/index.html', context)    
```

* detail.html에 error 날 경우 출력할 내용 if로 지정해주자.
* `detail.html`

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>{{ selected_question.question_text }}</h1>
    
    {% if error_message %}
    <div> {{ error_message }} </div><br>
    {% endif %}

    <form action="{% url 'polls:vote' selected_question.id %}" method="POST">
    
    {%  csrf_token %}
    
        {% for choice in selected_question.choice_set.all %}
        
        <input type="radio"
               name="my_choice"
               id="kaka{{ forloop.counter }}"
               value="{{ choice.id }}">            
               {#  submit 버튼을 누르면, name과 value의 쌍이 서버쪽 url로 넘어감 #}

        <label for="kaka{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
        {% endfor%}

        <br>

        {# 특수한 기능을 포함하고 있는 버튼! #}
        <input type="submit" value="투표">
        {#  이 버튼 클릭했을 때, 서버쪽으로 request 보내는 방법  ==> <form {% url 여기에 서버쪽 url 지정해줘 %}#}
    </form>

</body>
</html>
```





> ste2. 위 처럼 첫화면을 출력하는 것이 아니라 또 request를 부여해서 결과 화면 나오도록!

* `polls\views.py`

```python
from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice
from django.http import HttpResponseRedirect  # ==> 추가
from django.urls import reverse  # ==> 추가

def index(request):
    
    question_list = Question.objects.all().order_by('-pud_date')[:5]    
    context = { 'q_list' : question_list }
   
    return render(request, 'polls/index.html', context)
   

def detail(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)    
    context = {'selected_question': question}
    
    return render(request, 'polls/detail.html', context)

def vote(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST['my_choice'])
                
    except(KeyError, Choice.DoesNotExist):
        
        return render(request, 'polls/detail.html', 
                      {'selected_question': question,
                       'error_message': '아무것도 선택하지 않았어요!'})
    
    else: # Error가 안 뜰 경우
        selected_choice.votes += 1
    	selected_choice.save()
        
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        # HttpResponseRedirect() 
        # ==> client에게 url을 보내주고, 
        # ==> 그 url로 다시 request해야 원하는 결과 받을 수 있다.
        
        # reverse() 
        # ==> urlconf(urls.py)에 있는 name을 이용해서, url 형식으로 변환시켜준다.
        
        # reverse('polls:results') 
        # ==> polls의 urlconf에서 name이 results인 링크를 줘서 다시 request 하게 한다.
        
        # 'question_id'에 들어갈 인자로 args 변수 1개 줘야 하는데 '튜플 형식'으로 줘야 한다!
        # 여기서 question은 위에 detail 함수에서 생성했던 question 객체다.

        # HttpResponseRedirect() 와 reverse() 사용하기 위해서는 아래와 같이 
        # import 시켜줘야 한다.
        
        # from django.http import HttpResponseRedirect
        # from django.urls import reverse
```



> step3. 위에 HttpResponseRedirect(reverse())를 return 값으로 받아서 urlconf에 result가 name인 값이 있어야 한다.

* `polls\urls.py`

```python
from django.urls import path
from . import views   # ==> '.' 은 현재 폴더, 현재 application이란 의미 즉, == polls

app_name = 'polls'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('<int:question_id>/', views.detail, name='detail'),    
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/results/', view.results, name='results')
    # ==> view에 result 함수를 실행하도록 보낸다.
```



> step4. view로 가서 result 함수를 만들어주자 - 결과 값이 출력되도록

* `polls\views.py`

```python
from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice
from django.http import HttpResponseRedirect  # ==> 추가
from django.urls import reverse  # ==> 추가

def index(request):
    
    question_list = Question.objects.all().order_by('-pud_date')[:5]    
    context = { 'q_list' : question_list }
   
    return render(request, 'polls/index.html', context)
   

def detail(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)    
    context = {'selected_question': question}
    
    return render(request, 'polls/detail.html', context)

def vote(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST['my_choice'])
                
    except(KeyError, Choice.DoesNotExist):
        
        return render(request, 'polls/detail.html', 
                      {'selected_question': question,
                       'error_message': '아무것도 선택하지 않았어요!'})
    
    else: # Error가 안 뜰 경우
        selected_choice.votes += 1
    	selected_choice.save()
        
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        
def results(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
```



> step5. results.html을 만들자

* `polls\result.html`

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
	<h1>{{ question.question_text }}</h1>
    
    <ul>
    	{% for choice in question.choice_set.all %}
        	<li>{{ choice.choice_text }} - {{ choice.votes }}</li>
        {% endfor %}
    </ul>
    <br><br>
    <a href="{% url 'polls:detail' question.id %}">다시 투표 하기</a>
</body>
</html>
```

