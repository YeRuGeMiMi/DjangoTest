#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2014-04-12
# @Author  : yfl <yerugemimi@gmail.com>
# @Link    : https://github.com/YeRuGeMiMi
# @Version : 1.0

from django import forms
from captcha.fields import CaptchaField


class TiwenForm(forms.Form):
	'''
		--提问表单
		--question 问题
		--answer  答案
	'''
	question=forms.CharField(required=True)
	answer=forms.CharField(required=True)
	captcha=CaptchaField()
	
	

