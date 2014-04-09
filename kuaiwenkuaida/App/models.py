#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Question(models.Model):
	'''
	问题表
	'''
	question=models.CharField(max_length=255,db_column='question')
	answer=models.CharField(max_length=255,db_column='answer')

	class Meta:
		db_table='qa_qlist'
