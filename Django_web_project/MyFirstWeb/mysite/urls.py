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


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('polls/', views.index, name='index')
    # ==> 클라이언트 리퀘스트를 views로 보내서, index 함수 실행!

    path('polls/', include('polls.urls'))
    # polls라는 application 안에 urlconf를 따로 만들어서 거기서 urlconf 관리할거야
]
