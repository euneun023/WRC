from django.apps import AppConfig


class BookmarkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookmark'

#app에 대한 각자 설명들이 있음. signal 불러오는 역할 추가