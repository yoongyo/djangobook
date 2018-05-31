from django.db import models

class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)


    # 객체의 title을 문자열로 반환하도록 정의
    def __str__(self):
        return self.title
