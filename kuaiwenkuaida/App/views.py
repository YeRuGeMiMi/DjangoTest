#-*- coding:utf-8 -*-
# @Date    : 2014-04-12
# @Author  : yfl <yerugemimi@gmail.com>
# @Link    : https://github.com/YeRuGeMiMi
# @Version : 1.0

from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from App.modules import QuestionModule as qumo
from django.utils import simplejson
from App.form.TiwenForm import TiwenForm
from App.form.HuidaForm import HuidaForm

# Create your views here.
#首页
def index(request):
	t=get_template('index.html')
	html=t.render(Context())
	return HttpResponse(html)


#Ajax查询问题
def ajaxReturn(request):
	q=qumo.queryRom()
	json_r=simplejson.dumps(q)
	return HttpResponse(json_r,mimetype="application/javascript")


#提问
def tiwen(request):
	
	if request.method == 'POST':
		form=TiwenForm(request.POST)
		if form.is_valid():
			#表单模型的非空验证
			question=form.cleaned_data['question']	
			answer=form.cleaned_data['answer']

			t=get_template('result.html')
			if  qumo.save(question,answer):
				html=t.render(Context({'result':'保存问题成功！'}))
			else :
				html=t.render(Context({'result':'未知原因，失败！'}))

			return HttpResponse(html)
				
	else:
		#get提交
		form=TiwenForm()
		t=get_template('addQuestion.html')
		html=t.render(Context({'form':form}))
		return HttpResponse(html)


#回答
def huida(request):
	
	if request.method == 'POST':
		form=HuidaForm(request.POST)
		if form.is_valid():
			#模型取值和post取值
			answer=form.cleaned_data['answer']
			qid=request.POST.get('id')
			#存数据，返回
			t=get_template('result.html')
			if qumo.regAnswer(qid,answer) :
				html=t.render(Context({'result':'回答正确！'}))
			else :
				html=t.render(Context({'result':'回答错误！'}))

			return HttpResponse(html)

	else :
		#get提交
		form=HuidaForm()
		t=get_template('answer.html')
		html=t.render(Context({'form':form}))
		return HttpResponse(html)
