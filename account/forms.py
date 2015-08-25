# -*- coding:Utf-8 -*-

from django import forms

class RegistForm(forms.Form):  
    username = forms.CharField(label=(u"用户名"), max_length=10, widget=forms.TextInput())      
    qq = forms.IntegerField(label=(u"QQ"),widget=forms.TextInput(),required=False)      
    tel = forms.IntegerField(label=(u"手机号"),widget=forms.TextInput(),required=False)      
    password = forms.CharField(label=(u"密码"), max_length=20, widget=forms.PasswordInput())  
    repassword = forms.CharField(label=(u"重复密码"), max_length=20, widget=forms.PasswordInput())  
#     market_name = forms.CharField(label=(u"应用市场"), max_length=20, widget=forms.TextInput(),required=False)  

#    username = forms.CharField(label=(u"昵称"), max_length=30, widget=forms.TextInput(attrs={'size': 20, }))  
      
#    def clean_username(self):  
#        '''''验证重复昵称'''  
#        users = User.objects.filter(username__iexact=self.cleaned_data["username"])  
#        if not users:  
#            return self.cleaned_data["username"]  
#        raise forms.ValidationError((u"该昵称已经被使用请使用其他的昵称"))  
          
#    def clean_email(self):  
#        '''验证重复email'''
#        email = self.cleaned_data["email"]
#        if email:
#            emails = UserRegist.objects.filter(email__iexact=email)  
#            if not emails:  
#                return self.cleaned_data["email"]  
#            raise forms.ValidationError((u"该邮箱已经被注册！"))
#        else:
#            raise forms.ValidationError((u"邮箱不能为空！")) 
        
#    def clean_password(self):
#        password = self.cleaned_data['password']
#        password2 =  self.cleaned_data['password2']
#        if(password == password2):
#            '''加密密码'''
#            return make_password()
#        else:
#            raise forms.ValidationError((u"两次密码输入不一致！"))   
    
class LoginForm(forms.Form):  
    username = forms.CharField(label=(u"用户名"), max_length=10, widget=forms.TextInput())      
    password = forms.CharField(label=(u"密码"), max_length=20, widget=forms.PasswordInput())  

class RoleNameForm(forms.Form):  
    rolename = forms.CharField(label=(u"角色名"), max_length=14, widget=forms.TextInput())      
    

#class AjaxEmailValidForm(forms.Form):  
#    email = forms.CharField(label=(u"email"), max_length=30, widget=forms.TextInput(attrs={'size': 20, }))  
  