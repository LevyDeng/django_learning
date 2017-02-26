#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    def __unicode__(self):
        return self.name

class Article(models.Model):
    title=models.CharField(u'标题',max_length=256)
    auther=models.CharField(u'作者',max_length=64)
    content=models.TextField(u'内容')
    pub_date=models.DateTimeField(u'发表时间',auto_now_add=True,editable=True)
    update_time=models.DateTimeField(u'修改时间',auto_now=True,null=True)
    def __unicode__(self):
        return self.title