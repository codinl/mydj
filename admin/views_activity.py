# -*- coding: utf-8 -*-
from admin.account.decorators import admin_required
from admin.forms import ActivityForm
from base.page import Paginator
from card.models import CardType
from django.http import HttpResponse
from django.shortcuts.render import render_response
import config

# @admin_required
# def activity_list(request,cur_page=1,template="admin/activity/list.tpl"):  
#     count = Activity.get_count()
#     if count != 0:
#         page = int(cur_page)
#         activity_list = Activity.get_list(page)
#         p = Paginator(page,count,page_size=config.default_page_size)
#         if activity_list:
#             return render_response(template,activity_list=activity_list,p=p)
#     return render_response(template,request=None,activity_list=None,p=None)
# 
# @admin_required
# def activity_add(request,template="admin/activity/add.tpl"):
#     if request.method == "GET":
#         compose_input_type_list = ComposeInputType.get_all()
#         card_type_list = CardType.get_all()
#         return render_response(template,compose_input_type_list=compose_input_type_list,
#                                card_type_list=card_type_list)
#     elif request.method == "POST":
#         form = ActivityForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             description = form.cleaned_data['description']
#             start_time = form.cleaned_data['start_time']
#             end_time = form.cleaned_data['end_time']
#             status = form.cleaned_data['status']
#             input_1_id = form.cleaned_data['input_1_id']
#             input_2_id = form.cleaned_data['input_2_id']
#             input_3_id = form.cleaned_data['input_3_id']
#             input_count_1 = form.cleaned_data['input_count_1']
#             input_count_2 = form.cleaned_data['input_count_2']
#             input_count_3 = form.cleaned_data['input_count_3']
#             output_id = form.cleaned_data['output_id']
#             property = form.cleaned_data['property']
#             success_max = form.cleaned_data['success_max']
#             try:
#                 activity = Activity.objects.create(name=name,description=description,start_time=start_time,
#                                                    end_time=end_time,status=status,input_1_id=input_1_id,
#                                                    input_2_id=input_2_id,input_3_id=input_3_id,input_count_1=input_count_1,
#                                                    input_count_2=input_count_2,input_count_3=input_count_3,output_id=output_id,
#                                                    property=property,success_max=success_max
#                                                   )
#                 activity.save()
#             except Exception,e:
#                 print e
#             else:
#                 return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'activity_add'}).close();</script>")
#     return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'activity_add'}).close();alert('添加失败');</script>")
# 
# @admin_required
# def activity_edit(request,activity_id=0,template="admin/activity/edit.tpl"):
#     activity = Activity.get_by_id(activity_id)
#     if request.method == "GET":
#         compose_input_type_list = ComposeInputType.get_all()
#         card_type_list = CardType.get_all()
#         return render_response(template,activity=activity,card_type_list=card_type_list,
#                                compose_input_type_list=compose_input_type_list)
#     elif request.method == "POST":
#         form = ActivityForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             description = form.cleaned_data['description']
#             start_time = form.cleaned_data['start_time']
#             end_time = form.cleaned_data['end_time']
#             status = form.cleaned_data['status']
#             input_1_id = form.cleaned_data['input_1_id']
#             input_2_id = form.cleaned_data['input_2_id']
#             input_3_id = form.cleaned_data['input_3_id']
#             input_count_1 = form.cleaned_data['input_count_1']
#             input_count_2 = form.cleaned_data['input_count_2']
#             input_count_3 = form.cleaned_data['input_count_3']
#             output_id = form.cleaned_data['output_id']
#             property = form.cleaned_data['property']
#             success_max = form.cleaned_data['success_max']
#             try:
#                 activity.name = name
#                 activity.description = description
#                 activity.start_time = start_time
#                 activity.end_time = end_time
#                 activity.status = status
#                 activity.input_1_id = input_1_id
#                 activity.input_2_id = input_2_id
#                 activity.input_3_id = input_3_id
#                 activity.input_count_1 = input_count_1
#                 activity.input_count_2 = input_count_2
#                 activity.input_count_3 = input_count_3
#                 activity.output_id = output_id
#                 activity.property = property
#                 activity.success_max = success_max
#                 activity.save()
#             except Exception,e:
#                 print e
#             else:
#                 return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'activity_edit'}).close();</script>")
#     return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'activity_edit'}).close();alert('添加失败');</script>")
