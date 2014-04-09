#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

# Create your views here.
#首页
def index(request):
	t=get_template('index.html')
	html=t.render(Context())
	return HttpResponse(html)

#提问
def tiwen(request):
	t=get_template('addQuestion.html')
	html=t.render(Context())
	return HttpResponse(html)


