#-*- coding:utf-8 -*-
from django.db import models
from django.db import connection
from App.units import tupleToList

# Create your models here.
class Question(models.Model):
	'''
	问题表
	'''
	question=models.CharField(max_length=255,db_column='question')
	answer=models.CharField(max_length=255,db_column='answer')

	class Meta:
		db_table='qa_qlist'

	#取得所有的主键
	def getPks(self):
		cursor=connection.cursor()
		cursor.execute("SELECT id FROM qa_qlist")
		row=cursor.fetchall()

		#关闭操作
		cursor.close()
		return tupleToList(row)

	#取得指定


