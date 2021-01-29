
from django.urls import path
from . import views   # ==> '.' 은 현재 폴더, 현재 application이란 의미 즉, == polls

app_name = 'polls'
# ==> application이름을 name space이름으로 부여해줘서, 다른 application의 중복을 미연에 방지

urlpatterns = [
    path('', views.index, name= 'index'), # ==> http://localhost:8000/polls/
    # polls라는 application 안에 urlconf를 따로 만들어서 거기서 urlconf 관리할거야
    # 여기서 name은 논리적인 이름이 다른 application에서 겹칠 문제를 방지하기 위해 name space 부여

    path('<int:question_id>/', views.detail, name='detail'),
    # <> : 변하는 값이 나온다는 의미 / int : 정수가 올거란 의미 / question_id 숫자를 의미
    # veiw의 detail함수 사용할거야.
    # 논리적인 이름은 'detail'로 설정

    path('<int:question_id>/vote/', views.vote, name='vote'),  # ==> polls:vote
    # <int:question_id>/vote/ == 3/vote/
    # 사실 최종적으로 만들어지는 url request == http://localhost:8000/polls/3/vote/

    path('<int:question_id>/results/', views.results, name='results')
]
