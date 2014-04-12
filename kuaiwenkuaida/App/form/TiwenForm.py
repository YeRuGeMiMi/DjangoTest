#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2014-04-12
# @Author  : yfl <yerugemimi@gmail.com>
# @Link    : https://github.com/YeRuGeMiMi
# @Version : 1.0

from django import forms


class TiwenForm(forms.Form):
	question=forms.CharField(required=True)
	answer=forms.CharField(required=True)
	

