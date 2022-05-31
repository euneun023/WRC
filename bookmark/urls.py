from django.urls import path
#from .views import BookmarkListView, BookmarkCreateView
from .views import *

urlpatterns = [ #2차 url
    #path(어떤주소, 어떤뷰)
    # path("",), #"" = 전체가 매칭됨  -> http://127.0.0.1/bookmark/
    path("", BookmarkListView.as_view(), name='list'),
    path("add/", BookmarkCreateView.as_view(), name='add'),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'),
    path("update/<int:pk>/", BookmarkUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", BookmarkDeleteView.as_view(), name='delete'),
]

# as_view : 함수형뷰로 바꿔주는 효과가 있다.클래스형이면 이름만! (내부적으로 함수형으로 처리 대부분함..?)
# 화면 보여줄 템플릿에서 이 url을 어떻게 쓸꺼야 하며 불러다가쓸이름.  = 이 이름!
# html 태그 없어서 안보여주는것! -> 템플릿을 만들어야 한다. 어디? 앱 - template - 앱과 같은 이름 파일 - 이후 합침
# 앱이름 안에 템플릿! (이후 어떤거의 crud 인지 맞추기위함)

# 게시판 - 글번호 같은 역할 <int:pk> pk부분! pk = primary key <>=converter, vaild date <- 값에 맞는 것만 해줌
# int 없으면 문자열!
# <int:pk> - 어떤글을보겠다~ 시에 필요
