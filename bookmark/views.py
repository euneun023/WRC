from django.shortcuts import render

# Create your views here.
# 실제기능
# CRUD : Create, Read, Update, Delete
# 아무리 특이한 기능이여도 이 4개안에서 다 가능
# List - 목록을 보여주는 것이므로 read에 들어감. list라는 별도의 종류가 장고에 존재한다.
#view가 동작하려면 사용자들이 이용할 수 있게 url이 필요 -> 화면보여주기 : 템플릿필요

#뷰의 종류 :
#클래스형 뷰(라이브러리를 사용하거나, 장고에서 기본적으로 만들어져 있는 웹사이트를 만들때 제일 많이쓰는 형태의 뷰들을 정리해놓음 = 제네릭뷰)
            #: 사용간편
#함수형 뷰(내멋대로 하고싶은거 할때)

#뷰 사용하려면 뷰를 먼저 불러와야함
#웹페이지에 접속한다 = 웹페이지를 본다 -> URL을 입력 => 웹서버가 (url에맞는) 뷰를 찾아서 동작시킴 -> 응답 : 화면을 봄
#여기선 어떤 url인지 지정X -> urls.py
from django.views.generic.list import ListView  #ListView 내부 소스코드 많이 보기
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark     #제네릭뷰 : 기본적으로 어떤 모델에 대한? 지정

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url']
    success_url = reverse_lazy('list') #namespace 설정안했기에 아직X #주소 불러오기? #성공하면 넘어가는곳?
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView): #내용을 보여주는 것이므로 끝
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
#    success_url = reverse_lazy('list') 대신 다른방법! -> model.py
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')















