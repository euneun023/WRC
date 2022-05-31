from django.contrib import admin

# Register your models here.
# admin : 우리가 있는 모델을 장고의 기본으로 잇는 관리자 페이지에 집어넣기위해 등록, 관리 해주는 !
#내가 만든 모델을 관리자 페이지에서 관리할 수 있도록 등록
#모델을 등록해서 볼 수 있음

from .models import Bookmark

admin.site.register(Bookmark) #등록
#북마크를 등록하고 옵션 등록해서 보여지는 부분 조절할수있는 방법이 하나있음
#데코 사용해서 등록하는 방법도 있음




