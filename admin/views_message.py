# -*- coding: utf-8 -*-
from admin.account.decorators import admin_required
from admin.forms import SystemMessageForm
from base import time_util
from base.page import Paginator
from django.http import HttpResponse
from django.shortcuts.render import render_response
from message.models import SystemMessage
import config

@admin_required
def system_message_list(request,cur_page=1,template="admin/system_message/list.tpl"):  
    count = SystemMessage.get_count()
    if count != 0:
        page = int(cur_page)
        system_message_list = SystemMessage.get_list(page)
        p = Paginator(page,count,page_size=config.default_page_size)
        if system_message_list:
            _system_message_list = []
            # 格式化时间
            for m in system_message_list:
                m.create_time = time_util.seconds_to_str(m.create_time)
                m.update_time = time_util.seconds_to_str(m.update_time)
                _system_message_list.append(m)
            return render_response(template,request=request,
                                   system_message_list=_system_message_list,
                                   p=p)
    return render_response(template,request=None,system_message_list=None,p=None)

@admin_required
def system_message_add(request,template="admin/system_message/add.tpl"):
    if request.method == "GET":
        return render_response(template)
    elif request.method == "POST":
        form = SystemMessageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            mtype = form.cleaned_data['type']
            content = form.cleaned_data['content']
            create_time = time_util.get_now_second()
            status = form.cleaned_data['status']
            try:
                system_message = SystemMessage.objects.create(title=title,type=mtype,
                                                  content=content,status=status,
                                                  create_time=create_time)
                system_message.save()
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'system_message_add'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'system_message_add'}).close();alert('添加失败');</script>")

@admin_required
def system_message_edit(request,system_message_id=0,template="admin/system_message/edit.tpl"):
    system_message = SystemMessage.get_by_id(system_message_id)
    if request.method == "GET":
        return render_response(template,system_message=system_message)
    elif request.method == "POST":
        form = SystemMessageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            mtype = form.cleaned_data['type']
            content = form.cleaned_data['content']
            status = form.cleaned_data['status']
            try:
                system_message.title = title
                system_message.type = mtype
                system_message.content = content
                system_message.status = status
#                 system_message.update_time = datetime.datetime.now()
                system_message.save()
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'system_message_edit'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'system_message_edit'}).close();alert('添加失败');</script>")
