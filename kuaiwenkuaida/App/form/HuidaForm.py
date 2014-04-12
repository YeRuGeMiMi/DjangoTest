#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2014-04-12
# @Author  : yfl <yerugemimi@gmail.com>
# @Link    : https://github.com/YeRuGeMiMi
# @Version : 1.0

from django import forms

class HuidaForm(forms.Form):
	'''
		回答表单
		answer 答案
	'''
	answer=forms.CharField(required=1)
