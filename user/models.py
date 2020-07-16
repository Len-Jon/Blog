from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Article(models.Model):
    title = models.CharField(max_length=100, default="untitled")
    author_id = models.IntegerField()  # 作者id
    articleType = models.IntegerField()  # 0为markdown，1为富文本
    content = models.TextField()  # 文章内容
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
