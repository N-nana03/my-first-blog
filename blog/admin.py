from django.contrib import admin

# Register your models here.
from .models import Post
#モデルをadminページ(管理画面)上で見れるようにするためにモデルを登録登録
admin.site.register(Post)