# -*- coding: utf-8 -*-
from admin.account.decorators import admin_required
from admin.forms import MarketForm
from base.page import Paginator
from conf.models import Market
from django.http import HttpResponse
from django.shortcuts.render import render_response
import config

@admin_required
def market_list(request,cur_page=1,template="admin/market/list.tpl"):  
    count = Market.get_count()
    if count != 0:
        page = int(cur_page)
        market_list = Market.get_list(page,config.default_page_size)
        p = Paginator(page,count,page_size=config.default_page_size)
        if market_list:
            return render_response(template,request=request,market_list=market_list,p=p)
    return render_response(template,request=None,market_list=None,p=None)

@admin_required
def market_add(request,template="admin/market/add.tpl"):
    if request.method == "GET":
        return render_response(template)
    elif request.method == "POST":
        form = MarketForm(request.POST)
        if form.is_valid():
            e_name = form.cleaned_data['e_name']
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            try:
                market = Market.objects.create(e_name=e_name,name=name,
                                                              description=description,
                                                             )
                market.save()
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'market_add'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'market_add'}).close();alert('添加失败');</script>")

@admin_required
def market_edit(request,market_id=0,template="admin/market/edit.tpl"):
    market = Market.get_by_id(market_id)
    if request.method == "GET":
        return render_response(template,market=market)
    elif request.method == "POST":
        form = MarketForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            e_name = form.cleaned_data['e_name']
            description = form.cleaned_data['description']
            try:
                market.name = name
                market.e_name = e_name
                market.description = description
                market.save()
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'market_edit'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'market_edit'}).close();alert('添加失败');</script>")
