from django.db import models
from django.urls import reverse #모델 안 : reverse / 클래스형 뷰 안 -field값 쓸때 : reverse_lazy

# Create your models here.
# db 관리해주는 중간자
# model 사용 : ORM 사용이 목적.
# SQL이라는 명령 사용해서 주문해야하는데 SQL 사용하지 않고 할수있도록 하는 것 : ORM
# ORM : 데이터를 클래스, 객체화 해서 다뤄보자 하는 목적으로 나옴. => model형식의 class 만들어서 할 것.

# 모델 : 데이터베이스를 SQL 없이 다루려고 모델을 사용
# ORM 모델 만드는 이유 : 우리가 데이터를 객체화 해서 다루겠다. (sql없이보단)
# 모델 = db의 테이블  //엑셀의 한 시트
# 모델의 필드 = 테이블의 컬럼   //A열 B열
# 인스턴스 = 테이블의 레코드    //행
# 필드의 값(인스턴스의 필드값) = 레코드의 컬럼 데이터캆   //셀에 들어있는 값값

#앱에 즐찾 추가하려면? 사이트의 이름, 주소가 필요 -> 그런게 여러개 들어가야 한다. = 모델을 만든다. 라고 생각
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')  #이 이름으로 필드명을 보여주겠다.
    #필드 종류 여러개 -> 정확히 명시해야함.
    #필드의 종류가 결정하는 것
    # 1. 데이터베이스의 컬럼 종류     (글자가 들어감? 숫자가 들어감?)
    # 2. 제약 사항 (몇글자까지) 결정
    # 3. Form의 종류    //회원가입 - 전화번호 입력하세요 이런거,,,???
    # 4. Form에서 제약 사항
#모델을 만들었다 => DB에 어떤 data들을 어떤 형태로 넣을지 결정했다  //db에 넣을 준비끝X
#마이그레이션(migrate) =? 데이터베이스에 모델의 내용을 반영 (테이블 생성)
#=> 모델 수정하고도 마이그레이션 해야함 ★★ 그래야 반영이 됨
# makemigrations => 모델의 변경사항을 추적해서 기록해 놓는 것. 언제 어떤 방식으로 바뀔지 몰라서 바로기록X, migrations 폴더에 생김
#  ㄴ> 실행 : migration을 할 정보가 만들어직 ㅔ됨

# __str__
#class의 instance를 출력했을 때 나오는 내용을 만들어야 함 => 그 내용을 여기에 들어가서 보면!
    def __str__(self):  #__ __ => magic method 기본적으로 용도가 정해져있음
        return "이름 : "+self.site_name+", 주소 : "+self.url

    def get_absolute_url(self):
        return reverse('detail', args=[(self.id)]) #list 대신 pk id 그거 넣은것 / str붙여도됨

