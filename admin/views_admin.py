# -*- coding: utf-8 -*-

from admin.account.decorators import admin_required
from admin.forms import NodeForm
from admin.models import Node
from base.page import Paginator
import config
from django.http import HttpResponse
from django.shortcuts.render import render_response

@admin_required
def home(request,cur_menu_id=1,template="admin/main.tpl"):
    menu_list = Node.get_level(1)
    cur_menu_id = int(cur_menu_id)
    parent = Node.get_by_id(cur_menu_id)
    user_name = ""
    admin = request.admin   
    if admin:
        user_name = admin.name

    if parent:
        node_list = parent.get_children()
        return render_response(template,menu_list=menu_list,
                               node_list=node_list,cur_menu_id=cur_menu_id,
                               user_name = user_name)
    return HttpResponse("网络错误，请稍后再试...")

@admin_required
def index(request,template="admin/index.tpl"):
    return render_response(template)

@admin_required
def node_list(request,cur_page=1,template="admin/node/list.tpl"):
    count = Node.get_count()
    if count != 0:
        page = int(cur_page)
        node_list = Node.get_list(page)
        p = Paginator(page,count,page_size=config.default_page_size)
        if node_list:
            return render_response(template,request=request,node_list=node_list,p=p)
    return render_response(template,request=None,node_list=None,p=None)

@admin_required
def node_add(request,template="admin/node/add.tpl"):
    if request.method == "GET":
        level_1_list = Node.get_level(1)
        return render_response(template,level_1_list=level_1_list)
    elif request.method == "POST":
        form = NodeForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            name = form.cleaned_data['name']
            level = form.cleaned_data['level']
            parent = form.cleaned_data['parent']
            is_show = bool(form.cleaned_data['is_show'])
            sort = form.cleaned_data['sort']
            descr = form.cleaned_data['descr']
            try:
                node = Node.objects.create(url=url,name=name,level=level,parent_id=parent,is_show=is_show,sort=sort,descr=descr)
                node.save()
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'node_add'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'node_add'}).close();alert('添加失败');</script>")

@admin_required
def node_edit(request,node_id,template="admin/node/edit.tpl"):
    if request.method == "GET":
        if node_id:
            node_id = int(node_id)
            node = Node.get_by_id(node_id)
            level_1_list = Node.get_level(1)
            return render_response(template,node=node,level_1_list=level_1_list)
    elif request.method == "POST":
        form = NodeForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            url = form.cleaned_data['url']
            name = form.cleaned_data['name']
            level = form.cleaned_data['level']
            parent = form.cleaned_data['parent']
            is_show = bool(form.cleaned_data['is_show'])
            sort = form.cleaned_data['sort']
            descr = form.cleaned_data['descr']
            try:
#                node = Node.objects.get_or_create(id=id,url=url,name=name,level=level,parent_id=parent,is_show=is_show,sort=sort,descr=descr)
                node = Node.get_by_id(id)
                node.url = url
                node.name = name
                node.level = level
                node.parent_id = parent
                node.is_show = is_show
                node.sort = sort
                node.descr = descr
                node.save()
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'node_edit'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'node_edit'}).close();alert('添加失败');</script>")

@admin_required
def node_delete(request):
    if request.method == "POST":
        ids = request.POST.getlist("id")
        if ids: 
            ids_string = ','.join(ids)   
            Node.delete_by_ids(ids_string)
    return node_list(request)