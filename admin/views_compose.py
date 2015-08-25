# -*- coding: utf-8 -*-
from admin.account.decorators import admin_required
from admin.forms import ComposeInputForm
from base.page import Paginator
import config
from django.http import HttpResponse
from django.shortcuts.render import render_response
# 
# @admin_required
# def compose_input_list(request,cur_page=1,template="admin/compose/compose_input/list.tpl"):  
#     count = ComposeInput.get_count()
#     if count != 0:
#         page = int(cur_page)
#         compose_input_list = ComposeInput.get_list(page)
#         p = Paginator(page,count,page_size=config.default_page_size)
#         if compose_input_list:
#             return render_response(template,request=request,compose_input_list=compose_input_list,p=p)
#     return render_response(template,request=None,compose_input_list=None,p=None)
# 
# @admin_required
# def compose_input_add(request,template="admin/compose/compose_input/add.tpl"):
#     compose_input_type_list = ComposeInputType.get_all()
#     if request.method == "GET":
#         return render_response(template,compose_input_type_list=compose_input_type_list)
#     elif request.method == "POST":
#         form = ComposeInputForm(request.POST)
#         if form.is_valid():
#             type_id = form.cleaned_data['type_id']
#             count = form.cleaned_data['count']
#             card_id = form.cleaned_data['card_id']
#             is_unlock = form.cleaned_data['is_unlock']
#             try:
#                 compose_input = ComposeInput.objects.create(type_id=type_id,count=count,
#                                                   card_id=card_id,is_unlock=is_unlock)
#                 compose_input.save()
#             except Exception,e:
#                 print e
#             else:
#                 return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'compose_input_add'}).close();</script>")
#     return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'compose_input_add'}).close();alert('添加失败');</script>")
# 
# @admin_required
# def compose_input_edit(request,compose_input_id=0,template="admin/compose/compose_input/edit.tpl"):
#     compose_input_type_list = ComposeInputType.get_all()
#     compose_input = ComposeInput.get_by_id(compose_input_id)
#     if request.method == "GET":
#         return render_response(template,compose_input=compose_input,
#                                compose_input_type_list=compose_input_type_list)
#     elif request.method == "POST":
#         form = ComposeInputForm(request.POST)
#         if form.is_valid():
#             type_id = form.cleaned_data['type_id']
#             count = form.cleaned_data['count']
#             card_id = form.cleaned_data['card_id']
#             is_unlock = form.cleaned_data['is_unlock']
#             try:
#                 compose_input.type_id = type_id
#                 compose_input.count = count
#                 compose_input.card_id = card_id
#                 compose_input.is_unlock = is_unlock
#                 compose_input.save()
#             except Exception,e:
#                 print e
#             else:
#                 return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'compose_input_edit'}).close();</script>")
#     return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'compose_input_edit'}).close();alert('添加失败');</script>")
