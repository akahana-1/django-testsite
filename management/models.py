#! /usr/env/bin python
# -*-coding:utf-8-*-

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# ユーザの基礎情報を管理するデータベース
class AttributeList(models.Model):
	user = models.OneToOneField(User)
	
	GENDER_CHOICES = (
		(0,u'男性'),
		(1,u'女性'),
	)
	gender = models.IntegerField(choices = GENDER_CHOICES)
	number = models.IntegerField(max_length=6)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)

# ユーザがいつ出席したかを管理するデータベース
class AttendList(models.Model):
	user = models.OneToOneField(User)

	attendtime = models.DateField(auto_now_add = True)

	def __unicode__(self):
		return self.attendtime

