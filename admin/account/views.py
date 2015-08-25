# -*- coding: utf-8 -*-
from admin.account import authenticate, login as auth_login, \
    logout as auth_logout
from admin.account.decorators import admin_required
from admin.account.forms import LoginForm, AddAdminForm, EditAdminForm
from admin.account.models import Admin
from base.page import Paginator
from config import admin_dir
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts.render import render_response
import config

#from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse
#from django.views.decorators.cache import never_cache
#from django.views.decorators.csrf import csrf_protect
#from django.views.decorators.debug import sensitive_post_parameters

SESSION_KEY = '_auth_admin_id'
BACKEND_SESSION_KEY = '_auth_admin_backend'
REDIRECT_FIELD_NAME = 'next'

#@sensitive_post_parameters()
#@csrf_protect
#@never_cache
def login(request,template_name='admin/admin/login.tpl'):
#    next_url = request.GET.get("next")
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            pwd = form.cleaned_data['password']
            admin = authenticate(name=name,password=pwd)
            if admin:
                auth_login(request,admin)
                return redirect(admin_dir)
            else:
                form.errors['msg'] = u"用户名或密码错误,请重试。。"
        else:
            form.errors['msg'] = u"输入信息格式不合法，请重试"
    else:
        form = LoginForm()
    return render_response(template_name,form=form)

@admin_required
def logout(request):
    next_url = request.GET.get('next')
    auth_logout(request)
    if next_url:
        return redirect(next_url)
    return redirect(config.admin_dir)    

#添加管理员帐号
@admin_required
def admin_add(request,template='admin/admin/add.tpl'):
    if request.method == 'GET':
        return render_response(template)
    elif request.method == 'POST':
        form = AddAdminForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            if len(name) > 2:
                if _name_not_exists(name):
                    pwd = form.cleaned_data['password']
                    repwd = form.cleaned_data['repassword']
                    is_active = form.cleaned_data['is_active']
#                    qq = form.cleaned_data['qq']
#                    tel = form.cleaned_data['tel']
#                    email = form.cleaned_data['email']
                    if len(pwd) < 5:
                        form.errors['msg'] = u"密码不能少于5个字符"
                    if pwd != repwd:
                        form.errors['msg'] = u"两次密码不一致！"
#                    qq_str = str(qq)
#                    if qq and (len(qq_str) > 13 or len(qq_str) < 5):
#                        form.errors['msg'] = u"QQ号格式不正确！"
#                    if tel and (len(str(tel)) != 11):
#                        form.errors['msg'] = u"手机号格式不正确！"
                    if not form.errors:
#                        ip = get_client_ip(request)
                        admin = Admin.objects.create()
                        admin.name = name
                        admin.is_active = is_active
#                        if qq:
#                            admin.qq = qq
#                        if tel:
#                            admin.tel = tel
                        password = make_password(pwd)
                        admin.password = password
#                        admin.regist_ip = ip
#                        admin.last_login_ip = ip
                        try:
                            admin.save()
                        except Exception,e:
                            print e
                        else:
                            return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'admin_add'}).close();</script>")
                return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'admin_add'}).close();alert('添加失败：');</script>")

#編輯管理员帐号
@admin_required
def admin_edit(request,admin_id=0,template='admin/admin/edit.tpl'):
    ok = True
    admin = Admin.get_admin(admin_id)
    if request.method == 'GET':
        return render_response(template,admin=admin)
    elif request.method == 'POST':
        form = EditAdminForm(request.POST)
        if not form.is_valid():
            ok = False
        if ok:
            name = form.cleaned_data['name']
            if len(name) < 3:
                ok = False
        if ok:
            pwd = form.cleaned_data['password']
            repwd = form.cleaned_data['repassword']
            is_active = form.cleaned_data['is_active']
            if pwd and repwd:
                if len(pwd) < 5:
                    form.errors['msg'] = u"密码不能少于5个字符"
                    ok = False
                if ok:
                    if pwd != repwd:
                        form.errors['msg'] = u"两次密码不一致！"
                        ok = False
        if ok:
            is_active = form.cleaned_data['is_active']
            admin.is_active = is_active
            if name != admin.name:
                admin.name = name
            if pwd:
                password = make_password(pwd)
                admin.password = password  
            try:
                admin.save()
            except Exception,e:
                ok = False
                print e
        if ok:
            return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'admin_edit'}).close();window.top.right.location.reload();</script>")
        else:
            return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'admin_edit'}).close();alert('編輯失败：');</script>")

@admin_required
def admin_list(request,cur_page=1,template='admin/admin/list.tpl'):
    count = Admin.get_count()
    if count > 0:
        cur_page = int(cur_page)
        p = Paginator(cur_page,count)
        admin_list = Admin.get_list(cur_page=cur_page)
        if admin_list:
            return render_response(template,admin_list=admin_list,p=p)
    return render_response(template,admin_list=None,p=None)

def _name_not_exists(name):
    ''' email 是否已经注册 没有返回 True '''
    try:
        admin = Admin.objects.get(name=name)
    except:
        return True
    else:
        if admin:
            return False
    return False

def ajax_check_name(request):
    name = request.GET.get("user_name")
    result = "0"
    if name:
        if _name_not_exists(name):
            result = "1"
    return HttpResponse(result)
