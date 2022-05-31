"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [ #urls.py : 1차 url 담당 (2차 : 북마크 앱 폴더에 추가!)
    #url - 트리 타고들어감 : 1차 -> 2차 -> 3차
    #http://127.0.0.1/bookmark/? ~~~
    #ex 대학병원 /   http://127.0.0.1/중앙창구/내과  이런거
    #http://127.0.0.1/ = 로컬 호스트 주소
    path('bookmark/', include('bookmark.urls')), #bookmark앱의 .urls를 찾아가라
    path('admin/', admin.site.urls),
]
























