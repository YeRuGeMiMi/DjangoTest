#-*- coding:utf-8 -*-

from App.models import Question
import random

#保存
def save(question,answer):
	q=Question(question=question,answer=answer)
	q.save()
	if q.id >0 :
		return True
	else :
		return False
	
#随机查询
def queryRom():
	q=Question()
	row=q.getPks()
	count=row[random.randint(0,len(row)-1)]
	question=Question.objects.get(pk=count)
	#取出问题，和问题id
	rlist={'question':question.question,'id':question.id}
	return rlist

#验证回答
def regAnswer(qid,answer):
	question=Question.objects.get(pk=qid)
	if answer == question.answer :
		return True
	else :
		return False
