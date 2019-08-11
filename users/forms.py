#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/11 16:46
# @Author  : luoxiaojian
# @Site    : 
# @File    : forms.py
# @Software: PyCharm
from django import forms
from django.contrib.auth.models import Group, Permission
from .models import UserProfile
import re

# 添加用户表单验证
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # fields = "__all__"
        fields = ['username', 'name_cn', 'phone']

    def clean_phone(self):
        """
        通过正则表达式验证手机号码是否合法
        """
        phone = self.cleaned_data['phone']
        phone_regex = r'^1[34578][0-9]{9}$'
        p = re.compile(phone_regex)
        if p.match(phone):
            return phone
        else:
            # forms.ValidationError自定义表单错误
            raise forms.ValidationError('手机号码非法', code='invalid')


# 更新用户表单验证
"""
UserProfileForm会联合model判断字段是否合法，同时也会检查数据库的唯一性索引，故而更新操作不能复用。
例如，更新一个 username=aa的用户，UserProfileForm先检查字段是否合法，然后检查数据库里有没有这个
用户。如果有则任务违反了唯一性索引，验证不通过。
"""


class UserUpdateForm(forms.Form):
    username = forms.CharField(required=True, max_length=10)
    name_cn = forms.CharField(required=True, max_length=30)
    phone = forms.CharField(required=True, max_length=11)

    def clean_phone(self):
        """
        通过正则表达式验证手机号码是否合法
        """
        phone = self.cleaned_data['phone']
        phone_regex = r'^1[34578][0-9]{9}$'
        p = re.compile(phone_regex)
        if p.match(phone):
            return phone
        else:
            # forms.ValidationError自定义表单错误
            raise forms.ValidationError('手机号码非法', code='invalid')