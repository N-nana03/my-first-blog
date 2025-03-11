#fromやimportではじまる行は他のファイルから何かをちょこっとづつ追加する行
from django.conf import settings
from django.db import models
from django.utils import timezone

#今回のモデルを定義する　#classはオブジェクトを定義していることを、postはモデルの名前
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) #文字数が制限されたテキストを定義
    text = models.TextField() #制限のない長いテキスト用フィールド
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

#ブログを公開するメソッド #publishがメソッドの名前
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title