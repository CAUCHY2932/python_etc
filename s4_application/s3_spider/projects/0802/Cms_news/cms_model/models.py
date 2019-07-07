# -*-coding:utf-8 -*-
from django.db import models

# Create your models here.

class Test(models.Model):
    title=models.CharField(max_length=50)# 文章的标题
    date=models.DateField(max_length=30)# 文章的日期
    # content=models.CharField(max_length=10000)
    content=models.TextField()# 文章的内容
    link=models.CharField(max_length=100)# 文章的链接
    source=models.CharField(max_length=100)#文章来源