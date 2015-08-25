# -*- coding: utf-8 -*-

from admin.account.decorators import admin_required
from admin.forms import CardTypeForm, GroupForm, ConfigLevelForm
from base.obj import MissionProbability
from base.page import Paginator
from card.models import CardType
from conf.models import ConfigLevel, Group
from django.http import HttpResponse
from django.shortcuts.render import render_response
import config

@admin_required
def cardtype_list(request,cur_page=1,template="admin/config/cardtype/list.tpl"):  
    count = CardType.get_count()
    if count != 0:
        page = int(cur_page)
        cardtype_list = CardType.get_list(page)
        p = Paginator(page,count,page_size=config.default_page_size)
        if cardtype_list:
            return render_response(template,request=request,cardtype_list=cardtype_list,p=p)
    return render_response(template,request=None,cardtype_list=None,p=None)

@admin_required
def cardtype_add(request,template="admin/config/cardtype/add.tpl"):
    if request.method == "GET":
        return render_response(template)
    elif request.method == "POST":
        form = CardTypeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            card_type = form.cleaned_data['card_type']
            is_unlock = form.cleaned_data['is_unlock']
            try:
                cardtype = CardType.objects.create(name=name,card_type=card_type,
                                                  is_unlock=is_unlock)
                cardtype.save()
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'cardtype_add'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'cardtype_add'}).close();alert('添加失败');</script>")

@admin_required
def cardtype_edit(request,cardtype_id=0,template="admin/config/cardtype/edit.tpl"):
    cardtype = CardType.get_by_id(cardtype_id)
    if request.method == "GET":
        return render_response(template,cardtype=cardtype)
    elif request.method == "POST":
        form = CardTypeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            card_type = form.cleaned_data['card_type']
            is_unlock = form.cleaned_data['is_unlock']
            try:
                cardtype.name = name
                cardtype.card_type = card_type
                cardtype.is_unlock = is_unlock
                cardtype.save()
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'cardtype_edit'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'cardtype_edit'}).close();alert('添加失败');</script>")

@admin_required
def config_level_list(request,cur_page=1,template="admin/config/level/list.tpl"):  
    count = ConfigLevel.get_count()
    if count != 0:
        page = int(cur_page)
        config_level_list = ConfigLevel.get_list(page)
        p = Paginator(page,count,page_size=config.default_page_size)
        if config_level_list:
            return render_response(template,request=request,config_level_list=config_level_list,p=p)
    return render_response(template,request=None,config_level_list=None,p=None)

@admin_required
def config_level_add(request,template="admin/config/level/add.tpl"):
    if request.method == "GET":
        return render_response(template)
    elif request.method == "POST":
        form = ConfigLevelForm(request.POST)
        if form.is_valid():
            level = form.cleaned_data['level']
            update_need_xp = form.cleaned_data['update_need_xp']
            max_ep = form.cleaned_data['max_ep']
            max_sp = form.cleaned_data['max_sp']
            base_slot_count = form.cleaned_data['base_slot_count']
            try:
                config_level = ConfigLevel.objects.create(level=level,update_need_xp=update_need_xp,
                                                  max_ep=max_ep,max_sp=max_sp,base_slot_count=base_slot_count)
                config_level.save()
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'config_level_add'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'config_level_add'}).close();alert('添加失败');</script>")

@admin_required
def config_level_edit(request,config_level_id=0,template="admin/config/level/edit.tpl"):
    config_level = ConfigLevel.get_by_id(config_level_id)
    if request.method == "GET":
        return render_response(template,config_level=config_level)
    elif request.method == "POST":
        form = ConfigLevelForm(request.POST)
        if form.is_valid():
            level = form.cleaned_data['level']
            update_need_xp = form.cleaned_data['update_need_xp']
            max_ep = form.cleaned_data['max_ep']
            max_sp = form.cleaned_data['max_sp']
            base_slot_count = form.cleaned_data['base_slot_count']
            try:
                config_level.level = level
                config_level.update_need_xp = update_need_xp
                config_level.base_slot_count = base_slot_count
                config_level.max_ep = max_ep
                config_level.max_sp = max_sp
                config_level.save()
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'config_level_edit'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'config_level_edit'}).close();alert('添加失败');</script>")

@admin_required
def mission_p_list(request,template="admin/config/mission_p/list.tpl"):
    mp = MissionProbability()
    p_list = mp.get_p_list()
    if p_list:
        return render_response(template,p_list=p_list)
    return render_response(template,p_list=None)

@admin_required
def mission_p_edit(request,template="admin/config/mission_p/edit.tpl"):  
    mp = MissionProbability()
    p_list = mp.get_p_list()
    if request.method == "GET": 
        return render_response(template,p_list=p_list)
    elif request.method == "POST":
        try:
            for p in p_list:
                p.value = request.POST.get(p.key)
            mp.p_list = p_list
            mp.save_data()
        except Exception,e:
            if config.debug:
                print e
        else:
            return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'config_mission_p_edit'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'config_mission_p_edit'}).close();alert('添加失败');</script>")

@admin_required
def group_list(request,cur_page=1,template="admin/config/group/list.tpl"):  
    count = Group.get_count()
    if count != 0:
        page = int(cur_page)
        group_list = Group.get_list(page)
        p = Paginator(page,count,page_size=config.default_page_size)
        if group_list:
            return render_response(template,request=request,group_list=group_list,p=p)
    return render_response(template,request=None,group_list=None,p=None)

@admin_required
def group_add(request,template="admin/config/group/add.tpl"):
    if request.method == "GET":
        return render_response(template)
    elif request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            try:
                group = Group.objects.create(name=name,description=description)
                group.save()
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'group_add'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'group_add'}).close();alert('添加失败');</script>")

@admin_required
def group_edit(request,group_id=0,template="admin/config/group/edit.tpl"):
    group = Group.get_by_id(group_id)
    if request.method == "GET":
        return render_response(template,group=group)
    elif request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            try:
                group.name = name
                group.description = description
                group.save()
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'group_edit'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'group_edit'}).close();alert('添加失败');</script>")
