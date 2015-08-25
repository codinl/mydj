# -*- coding: utf-8 -*-
from admin.account.decorators import admin_required
from admin.forms import GoodForm, RechargeForm
from base.page import Paginator
from django.http import HttpResponse
from django.shortcuts.render import render_response
from mall.models import Good, Recharge, Order
import config

@admin_required
def good_list(request,cur_page=1,template="admin/mall/good/list.tpl"):  
    count = Good.get_count()
    if count != 0:
        page = int(cur_page)
        good_list = Good.get_list(page,config.default_page_size)
        p = Paginator(page,count,page_size=config.default_page_size)
        if good_list:
            return render_response(template,request=request,good_list=good_list,p=p)
    return render_response(template,request=None,good_list=None,p=None)

@admin_required
def good_add(request,template="admin/mall/good/add.tpl"):
    if request.method == "GET":
        return render_response(template)
    elif request.method == "POST":
        form = GoodForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            type_id = form.cleaned_data['type_id']
            vm = form.cleaned_data['vm']
            rm = form.cleaned_data['rm']
            discount = form.cleaned_data['discount']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            is_new = form.cleaned_data['is_new']
            is_hot = form.cleaned_data['is_hot']
            is_unlock = form.cleaned_data['is_unlock']
            try:
                good = Good.objects.create(name=name,type_id=type_id,vm=vm,
                                         rm=rm,description=description,
                                         discount=discount,image=image,
                                         is_new=is_new,is_hot=is_hot,
                                         is_unlock=is_unlock)
                good.save()
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'good_add'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'good_add'}).close();alert('添加失败');</script>")

@admin_required
def good_edit(request,good_id=0,template="admin/mall/good/edit.tpl"):
    good = Good.get_by_id(good_id)
    if request.method == "GET":
        return render_response(template,good=good)
    elif request.method == "POST":
        form = GoodForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            type_id = form.cleaned_data['type_id']
            vm = form.cleaned_data['vm']
            rm = form.cleaned_data['rm']
            discount = form.cleaned_data['discount']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            is_new = form.cleaned_data['is_new']
            is_hot = form.cleaned_data['is_hot']
            is_unlock = form.cleaned_data['is_unlock']
            try:
                good.name = name
                good.type_id = type_id
                good.vm = vm
                good.rm = rm
                good.discount = discount
                good.description = description
                good.image = image
                good.is_new = is_new
                good.is_hot = is_hot
                good.is_unlock = is_unlock
                good.save()
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'good_edit'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'good_edit'}).close();alert('添加失败');</script>")


@admin_required
def recharge_list(request,cur_page=1,template="admin/mall/recharge/list.tpl"):  
    count = Recharge.get_count()
    if count != 0:
        page = int(cur_page)
        recharge_list = Recharge.get_list(page,config.default_page_size)
        p = Paginator(page,count,page_size=config.default_page_size)
        if recharge_list:
            return render_response(template,request=request,recharge_list=recharge_list,p=p)
    return render_response(template,request=None,recharge_list=None,p=None)

@admin_required
def recharge_add(request,template="admin/mall/recharge/add.tpl"):
    if request.method == "GET":
        return render_response(template)
    elif request.method == "POST":
        form = RechargeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
#             type_id = form.cleaned_data['type_id']
            money = form.cleaned_data['money']
            rm = form.cleaned_data['rm']
            discount = form.cleaned_data['discount']
            description = form.cleaned_data['description']
#             status = form.cleaned_data['status']
            try:
                recharge = Recharge.objects.create(name=name,money=money,
                                                 rm=rm,description=description,
                                                 discount=discount
                                                 )
                recharge.save()
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'recharge_add'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'recharge_add'}).close();alert('添加失败');</script>")

@admin_required
def recharge_edit(request,recharge_id=0,template="admin/mall/recharge/edit.tpl"):
    recharge = Recharge.get_by_id(recharge_id)
    if request.method == "GET":
        return render_response(template,recharge=recharge)
    elif request.method == "POST":
        form = RechargeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
#             type_id = form.cleaned_data['type_id']
            money = form.cleaned_data['money']
            rm = form.cleaned_data['rm']
            discount = form.cleaned_data['discount']
            description = form.cleaned_data['description']
#             status = form.cleaned_data['status']
            try:
                recharge.name = name
#                 recharge.type_id = type_id
                recharge.money = money
                recharge.rm = rm
                recharge.discount = discount
                recharge.description = description
#                 recharge.status = status
                recharge.save()
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'recharge_edit'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'recharge_edit'}).close();alert('添加失败');</script>")

@admin_required
def order_list(request,cur_page=1,template="admin/mall/order/list.tpl"):  
    count = Order.get_count()
    if count != 0:
        page = int(cur_page)
        order_list = Order.get_list(page,config.default_page_size)
        p = Paginator(page,count,page_size=config.default_page_size)
        if recharge_list:
            return render_response(template,request=request,order_list=order_list,p=p)
    return render_response(template,request=None,recharge_list=None,p=None)


