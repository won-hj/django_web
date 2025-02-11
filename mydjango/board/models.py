from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200) #글 제목
    content = models.TextField() #글 내용
    created_at = models.DateTimeField(auto_now_add=True) #작성일 자동 저장

    def __str__(self):
        return self.title #관리자 페이지에서 제목으로 표시


