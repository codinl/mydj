# -*- coding:Utf-8 -*-

from django import forms
    
class LoginForm(forms.Form):  
    name = forms.CharField(label=(u"用户名"), max_length=10, widget=forms.TextInput())      
    password = forms.CharField(label=(u"密码"), max_length=20, widget=forms.PasswordInput())  

class AddAdminForm(forms.Form):  
    name = forms.CharField(label=(u"用户名"), max_length=10, widget=forms.TextInput())  
#    email = forms.EmailField(label=(u"email"), max_length=30, widget=forms.TextInput())    
#    qq = forms.IntegerField(label=(u"QQ"),widget=forms.TextInput(),required=False)      
#    tel = forms.IntegerField(label=(u"手机号"),widget=forms.TextInput(),required=False)      
    password = forms.CharField(label=(u"密码"), max_length=20, widget=forms.PasswordInput())  
    repassword = forms.CharField(label=(u"重复密码"), max_length=20, widget=forms.PasswordInput())
    is_active = forms.IntegerField(label=(u"is_active"), widget=forms.RadioSelect())  

class EditAdminForm(forms.Form):  
    name = forms.CharField(label=(u"用户名"), max_length=10, widget=forms.TextInput())  
#    email = forms.EmailField(label=(u"email"), max_length=30, widget=forms.TextInput())    
#    qq = forms.IntegerField(label=(u"QQ"),widget=forms.TextInput(),required=False)      
#    tel = forms.IntegerField(label=(u"手机号"),widget=forms.TextInput(),required=False)      
    password = forms.CharField(label=(u"密码"), max_length=20, widget=forms.PasswordInput(),required=False)  
    repassword = forms.CharField(label=(u"重复密码"), max_length=20, widget=forms.PasswordInput(),required=False)
    is_active = forms.IntegerField(label=(u"is_active"), widget=forms.RadioSelect())