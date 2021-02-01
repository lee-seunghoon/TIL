[TOC]

## <Application URLConf 나누기>

### 1. project 생성(shoppingmall)

* bbs application 생성

### 2. project 설정(settings.py)

* 추가 - static 파일 설정

```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
    
# static 파일인 CSS와 JavaScript 파일 넣어주면, html 화면 제어할 수 있어.
```

### 3. 기본 table 생성 (Users, Group table)

* terminal

  ```cmd
  >>> python manage.py migrate
  >>> python manage.py createsuperuser
  ID, PW 생성
  ```

### 4. 서버 구동

```cmd
>>> python manage.py runserver
```



### 5. bbs application 개발

5)-1. model 생성 (models.py)

```python
from django.db import models

# 이 model class는 bbs_post라는 table이 만들어진다.
# class의 속성은 table의 column명을 의미한다.


class Post(models.Model):
    author = models.CharField('작성자', max_length=50)
    contents = models.CharField('글내용', max_length=200)

```



5)-2 admin site 등록 (admin.py)

```python
from django.contrib import admin
from bbs.models import Post

admin.site.register(Post)

```



5)-3 database에 변경사항 반영 & database에 적용 (cmd terminal)

```cmd
>>> (base) C:\python-Django\MyShoppingMall>python manage.py makemigrations
>>> (base) C:\python-Django\MyShoppingMall>python manage.py migrate
```



5)-4 url 경로 설정 (settings/urls.py)

```python
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url # ==> url 사용하려면 이렇게 import 필요!
from django.views.generic.base import TemplateView # ==> TemplateView 쓰기 위해!!

# url pattern 설정 시 사용할 수 있는 함수
# url(), path(), re_path()

# 1) url() : 원조 / 정규표현식을 포함해서 일반적인 설정이 가능! / 사용하기 까다로움
# 2) path() : url() 불현해서 만든 것 / 일반 문자열 형태로 url conf할 때
# 3) re_path : url() 불현해서 만든 것 / 정규 표현식으로 url conf할 때

# 정규 표현식 ==> [adh] : a 나 d 나 혹은 h (a or d or h) / []는 한 문자를 의미한다.
#               [a-z] : a 부터 z까지 이중에 한 문자 (즉, 영문자 소문자 1개)
#               [a-z]{3} : {}는 반복 의미 ==> 영문자 소문자 3개
#               ^(Caret) : 문자열의 시작을 의미 / $ : 문자열의 끝

# 메인 페이지 만들거야

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    # 문자열로 시작하면 r을 써주고 그 안에 정규표현식 넣는다. / ^$ == 공백
    # html을 로직 처리 거치지 않고 바로, view로 보여줘

    path('admin/', admin.site.urls)
]
```



5)-5 main page 제작(bootstrap 이용)

* index.html

```html

<!doctype html>
<html lang="en" class="h-100">
  <head>
    <meta charset="utf-8">
    <title>Welcome My Shopping mall</title>


    <!-- Bootstrap core CSS (CDN) -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>


    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
    </style>


    <!-- Custom styles for this template -->
    <link href="/static/css/cover.css" rel="stylesheet">


  </head>
  <body class="d-flex h-100 text-center text-white bg-dark">

<div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
  <header class="mb-auto">
    <div>
      <h3 class="float-md-start mb-0">Jway</h3>
      <nav class="nav nav-masthead justify-content-center float-md-end">
        <a class="nav-link active" aria-current="page" href="#">Home</a>
        <a class="nav-link" href="#">Intro</a>
        <a class="nav-link" href="#">Bulletin Board</a>
      </nav>
    </div>
  </header>

  <main class="px-3">
    <h1>Welcome to my Shopping-Mall</h1>
    <br>
    <p class="lead">지금은 게시판 뿐입니다. 서둘러 개발하겠습니다.</p>
    <br>
    <p class="lead">
      <a href="/bbs/list/" class="btn btn-lg btn-secondary fw-bold border-white bg-white">게시글 보기</a>
    </p>
  </main>

  <footer class="mt-auto text-white-50">
    <p>Cover template for <a href="https://getbootstrap.com/" class="text-white">Bootstrap</a>, by <a href="https://twitter.com/mdo" class="text-white">@mdo</a>.</p>
  </footer>
</div>



  </body>
</html>

```



5)-6 application urlconf 설정

* settings/urls.py

```python
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url # ==> url 사용하려면 이렇게 import 필요!
from django.views.generic.base import TemplateView # ==> TemplateView 쓰기 위해!!

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('bbs/', include('bbs.urls'))
]
```



* bbs/urls.py

```python

from django.urls import path
from bbs import views

app_name = 'bbs'

urlpatterns = [
    path('list/', views.p_list, name='p_list'),

]

```



5)-7 p_list views에서 함수 생성

* bbs/views.py

```python
from django.shortcuts import render
from bbs.models import Post

def p_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'bbs/list.html', {'posts': posts})

```



5)-8 list.html 꾸미기 전! html에 공통적으로 사용하는 부분 따로 만들어서 관리할 수 있도록 적용

	* 전체 관리 html 생성 ==> MyShoppingMall/templates/base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
    
    <!-- jQuery CDN -->
    <script
            src="https://code.jquery.com/jquery-2.2.4.min.js"
            integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44="
            crossorigin="anonymous"></script>
    
    <!-- BootStrap CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>

</head>
<body>
    {% block container %}
    {% endblock %}
</body>
</html>
```



5)-9 base.html을 list.html에 적용

 * bbs/templates/bbs/list.html

    * list.html 

   ```html
   {% extends 'base.html' %} {# ==> base.html을 확장해서 사용할거에요. #}
   
   {% block container %} {# base.html에서 block 영역 잡혀져 있는 부분 이걸로 적용할거에요. #}
   
       <script src="/static/js/posts.js"></script>
       <div class="container"> {# <== 여기서 container는 위 block에서 잡은 naming을 의미하는가? #}
           <h1>Bulletin Board System(BBS)</h1>
           <button type="button"
                   class="btn btn-primary"  {# 부트스트랩 스타일 적용 #}
                   onclick="new_post()">새글작성</button>
           <div class="m-1"></div>  {# 부트스트랩 스타일 적용 #} / 무슨 스타일인지는 모르겠다.
   
           <div class="table-responsive">
           <table class="table table-striped table-sm">
               <thead>
                   <tr>
                       <th>#</th>
                       <th>글 작성자</th>
                       <th>글 내용</th>
                       <th>수정</th>
                       <th>삭제</th>
                   </tr>
               </thead>
               <tbody>
                   {% for post in posts %}
                   <tr>
                       <td>{{ post.id }}</td>
                       <td>{{ post.author }}</td>
                       <td>{{ post.contents }}</td>
                       <td>버튼1</td>
                       <td>버튼2</td>
                   </tr>
                   {% endfor %}
               </tbody>
           </table>
           </div>
   
       </div>
   
   
   
   {% endblock %}
   
   
   ```





## <모델 폼 적용>

### 1) 장고 부트스트랩 설치

```cmd terminal
(base) C:\python-Django\MyShoppingMall>pip install django-bootstrap4
```



### 2) 설치한 bootstrap은 우리 프로젝트 안에서 하나의 application으로 인식된다!

* `settings.py`

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bbs.apps.BbsConfig',
    'bootstrap4'  # ==> 이거 추가해줘야 한다!!
]
```



### 3) model form 만들기 ==> 내 application 안에 `forms.py` 만들기

> ==> 여기서는 ModelForm class를 정의한다!
>
> ==> ModelForm이 자동으로 Form Field(HTML tag)를 생성해준다! (input 이런거 필요없어)
>
> ==> Form 처리를 상당히 간단하게 처리할 수 있다.

* `forms.py`

```python
from django import forms
from bbs.models import Post     # ==> 내가 연결할 model class가 하나 가져온다.


class PostForm(forms.ModelForm): # 양식이 정해져 있다 / model_class명과 Form 결합
    class Meta:
        model = Post  # ==> 내가 사용할 model class가 정확히 뭔지 Meta class에서 지정해줘야 해!
        fields = ['author', 'contents']
        # ==> 어떤 속성들 이용할거냐? / Post class 안에 있는 속성 다 이용 안할수도 있다!
        # ==> field를 통해 사용할 속성 사용을 선택할 수 있다.
```



## <새글 작성 관한 새 page 만들기>



* `list.html`에서 button 클릭 누르면, 'new_post()' 실행

* 'new_post()'는 <script src="/static/js/posts.js"></script> 여기서 경로 잡아준 `posts.js`  파일에서 적용

*  `posts.js`

  ```javascript
  function new_post() {
      // 'bbs/create' ==> 상대경로 : 현재 경로를 기준으로 덧붙여서 url 생성
      //              ==> 현재 경로 : http://localhost:8000/bbs/list/
      //              ==> 저 현재경로에 상대경로가 붙어서 	  
      // 				`http://localhost:8000/bbs/list/bbs/create/` ==> 이렇게 만들어짐
      
      location.href = '/bbs/create/'
  
      // 절대경로 : http://localhost:8000/
      // 그래서 '/bbs/create/' ==> 절대경로에 저게 붙어
  ```



* url conf 설정! (`urls.py`)

  ```python
  from django.urls import path
  from bbs import views
  
  app_name = 'bbs'
  
  urlpatterns = [
      path('list/', views.p_list, name='p_list'),
      path('create/', views.p_create, name='p_create') # ==> 이 부분 추가
  ]
  ```

  

* views에서 p_create 함수 생성 (`views.py`)

  ```python
  from django.shortcuts import render
  from bbs.models import Post
  from bbs.forms import PostForm  # ==> model form에서 만들었던, PostForm import
  
  
  def p_list(request):
      posts = Post.objects.all().order_by('-id')
      return render(request, 'bbs/list.html', {'posts': posts})
  
  
  def p_create(request):
      # GET 방식 (form tag 안에서 method='POST' 인거 제외하고는 모두 GET!!)
      
      post_form = PostForm() # ==> modelform class를 객체로 가져옴
  
      return render(request, 'bbs/create.html',
                    {'post_form': post_form})
  ```

  

* `create.html` 생성

  ```html
  {% extends 'base.html' %}
  
  {# model form은 부트스트랩 적용이 안돼 있다. 그래서 django가 지원해주는 application bootstrap4을 적용시켜야함 #}
  
  {% load bootstrap4 %}
  
  
  {% block container %}
  
      <div class="container">  {# <== 이렇게 container 해주면, 전체 양식이 bootstrap적용 #}
          <h1>New Post</h1>    {# ==> 부트스트랩 스타일 #}
  
          <form method="post"> {# 여기서 작성하는 데이터가 전송은 되야 하니깐! #}
                               {# action이 없으면 현재url로 post방식으로 호출되도록 보낸다. #}
              {% csrf_token %}
  
              {% bootstrap_form post_form %}<br>   {# ==> 부트스랩을 따로 적용해주고 #}
                                                   {# 넘어온 modelform 객체 사용 #}
              <button type="submit"  {# ==> 부트스트랩 스타일 #}
                      class="btn btn-primary">등록</button>
          </form>
      </div>
  
  {% endblock %}
  ```

  

* <button type="submit"> 이 버튼을 누른다면... post 방식으로 url request!
* form method="post" 여기에 action이 없으면 현재 url로 호출!

* 여기서 현재 url == localhost:8000/bbs/create/ 
* 그럼 views.p_create 함수로 다시 넘어감 그래서 거기서 다시 처리



* `views.py`에서 p_create() 함수 수정

  ```python
  def p_create(request):
  
      # POST방식
      if request.method == 'POST':
          # 데이터베이스에 저장!
          # 사용자가 전달해준 데이터는 request.POST 안에 들어 있다.
          post_form = PostForm(request.POST)  # 데이터가 request.POST 여기에 있어서
          									# modelform에 인자로 request.POST를 줌.
  
          if post_form.is_valid():  # ==> .is_valid() ==> 이게 유효하다면
              post_form.save()  # ==> model form 안에 database가 있기 때문에 바로 저장
              return redirect('bbs:p_list')  
          	# ==> 'redirect' : client에게 접속해봐라고 응답 보내주는 숏컷함수
              # ==> 'bbs:p_list' 여기로 다시 접속해서 request 이어가
              # ==> 처음 게시판 모두 나왔던 화면으로 돌아감. (data변화 적용된 )
      
      # GET 방식
      if request.method == 'GET':
  
          # GET 방식 (form tag 안에서 method='POST' 인거 제외하고는 모두 GET!!)
          post_form = PostForm()
  
          return render(request, 'bbs/create.html',
                        {'post_form': post_form})
  
  ```

  

## <글 수정 버튼 활성화 하기>

* `p_list.html` 에서 각 버튼 활성화 및 효과 적용

```html
{% extends 'base.html' %} {# ==> base.html을 확장해서 사용할거에요. #}

{% block container %} {# base.html에서 block 영역 잡혀져 있는 부분 이걸로 적용할거에요. #}

    <script src="/static/js/posts.js"></script>
    <div class="container"> 
        <h1>Bulletin Board System(BBS)</h1>
        <button type="button"
                class="btn btn-primary"  
                onclick="new_post()">새글작성</button>
        <div class="m-1"></div>

        <div class="table-responsive">
        <table class="table table-striped table-sm">
            <thead>
                <tr>
                    <th>#</th>
                    <th>글 작성자</th>
                    <th>글 내용</th>
                    <th>수정</th>
                    <th>삭제</th>
                </tr>
            </thead>
            <tbody>
                {% for post in posts %}
                <tr>
                    <td>{{ post.id }}</td>
                    <td>{{ post.author }}</td>
                    <td>{{ post.contents }}</td>
                    <td>
                        <input type="button"
                               value="글 수정"
                               onclick="fix_post({{ post.id }})">
                    </td>
                    <td>
                        <button type="button"
                                class="btn btn-primary"
                                onclick="delete_post({{ post.id }})">글 삭제</button>

                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        </div>

    </div>



{% endblock %}


```



* '글 수정' 버튼 클릭 시 'fix_post()' ==> 함수 호출

  `posts.js` 에서 함수 추가

  ```javascript
  function fix_post(post_id) {
      location.href = '/bbs/fix/' + post_id + '/'
  ```

  

* `urls.py`에서 urlconf 추가

  ```python
  from django.urls import path
  from bbs import views
  
  app_name = 'bbs'
  
  urlpatterns = [
      path('list/', views.p_list, name='p_list'),
      path('create/', views.p_create, name='p_create'),
      path('fix/<int:post_id>/', views.p_fix, name='p_fix')  # <== 추가
  ]
  ```



* `views.py` 에서 p_fix 함수 추가!

  ```python
  from django.shortcuts import render, redirect, get_object_or_404
  from bbs.models import Post
  from bbs.forms import PostForm
  
  def p_fix(request, post_id):
      post_text = get_object_or_404(Post, pk=post_id)
  
      if request.method == 'GET':  # ==> 글 수정하는 버튼 누르면, p_fix.html에 기본값 함께 표기
          post_form = PostForm(instance=post_text) # instance 값을 주니깐 기존값이 같이 나옴
          return render(request, 'bbs/p_fix.html', 
                        {'post_text': post_text, 'post_form': post_form})
      
  ```



* `p_fix.html` 에서 화면 제어 및 `수정`버튼 구성

  ```html
  {% extends 'base.html' %}
  
  {% load bootstrap4 %}
  
  {% block container %}
      <script src="/static/js/posts.js/"></script>
      <div class="container">
          <h1>게시글을 수정해주세요.</h1><br><br><br>
          <form method="post">
              {% csrf_token %}
              {% bootstrap_form post_form %}  <!-- 이게 앞에서 modelform 형식으로 가져온--> 
              								<!-- bootsrtap_form 형식 적용해줌(modelform은 따로 해줘야해-->	
              <br>
              <button type="submit"
                      class="btn btn-primary">글 수정</button>
          </form>
          <br>
          <form method="get">
              {% csrf_token %}
              <button type="button"
                      class="btn btn-primary"
                      onclick="fix_return()">취소</button>
          </form>
  
      </div>
  {% endblock %}
  ```



* 글 수정 버튼이 있는 form tag에 action 부여 따로 없었음 그래서 현 url conf 적용

  `fix/3` ==> views.p_fix 로 다시 넘어감

  `view.py`

  ```python
  from django.shortcuts import render, redirect, get_object_or_404
  from bbs.models import Post
  from bbs.forms import PostForm
  
  def p_fix(request, post_id):
      post_text = get_object_or_404(Post, pk=post_id)
  
      if request.method == 'GET':  
          post_form = PostForm(instance=post_text) 
          return render(request, 'bbs/p_fix.html', 
                        {'post_text': post_text, 'post_form': post_form})
      
      elif request.method == 'POST':  # ==> request가 POST 방식으로 넘어왔음! 
          post_form = PostForm(request.POST)
          if post_form.is_valid(): 	# ==> 유효성 검사 먼저 해주고
              # cleaned_data가 수정해준거였어.
              # cleamed_date는 내가 바꾼 값으로 새롭게 바꿔주네
              # 원본 값인 post_text에 대입해줘야 원본 값이 바뀌네
              post_text.author = post_form.cleaned_data['author']
              post_text.contents = post_form.cleaned_data['contents']
              post_text.save()
              return redirect('bbs:p_list')
          else:
              return redirect('bbs:p_list')
  ```

  

## <글 삭제>

* 글 삭제 버튼에 `onclick="delete_post()"` 이거 적용해서 함수 만들어 줘야 함

  `posts.js`

  ```javascript
  function delete_post(post_id) {
      location.href = '/bbs/delete/' + post_id + '/'
  }
  ```



* urlconf에 이 부분 추가 해주기 ==> '/bbs/delete/' + post_id + '/' 

  `urls.py`

  ```python
  from django.urls import path
  from bbs import views
  
  app_name = 'bbs'
  
  urlpatterns = [
      path('list/', views.p_list, name='p_list'),
      path('create/', views.p_create, name='p_create'),
      path('fix/<int:post_id>/', views.p_fix, name='p_fix'),
      path('delete/<int:post_id>/', views.p_delete, name='p_delete')
  ]
  ```



* `views.py`에 `p_delete` 추가해주기

  `views.py`

  ```python
  ef p_delete(request, post_id):
      post_text = get_object_or_404(Post, pk=post_id)
      post_text.delete()  # ==> 원본값을 지워주면 됨!
      return redirect('bbs:p_list')
  ```

  

