# -*- coding: utf-8 -*-
from admin.account.decorators import admin_required
from admin.forms import PlayerForm
from base.page import Paginator
from django.http import HttpResponse
from django.shortcuts.render import render_response
from player.models import Player
import config

@admin_required
def player_list(request,cur_page=1,template="admin/player/list.tpl"):  
    count = Player.get_count()
    if count != 0:
        page = int(cur_page)
        player_list = Player.get_list(page)
        p = Paginator(page,count,page_size=config.default_page_size)
        if player_list:
            return render_response(template,request=request,player_list=player_list,p=p)
    return render_response(template,request=None,player_list=None,p=None)

@admin_required
def player_search(request,template="admin/player/search.tpl"): 
    if request.method == "POST":
        player_name = request.POST.get('player_name')
        if player_name:
            player_list = Player.search_by_name(player_name)
            if player_list:
                count = len(player_list)
                p = Paginator(1,count,page_size=config.default_page_size)
                if player_list:
                    return render_response("admin/player/list.tpl",request=request,player_list=player_list,p=p)
    return render_response(template,request=None,player_list=None,p=None)

@admin_required
def player_add(request,template="admin/player/add.tpl"):
    if request.method == "GET":
        return render_response(template)
    elif request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            level = form.cleaned_data['level']
            update_need_xp = form.cleaned_data['update_need_xp']
            energy = form.cleaned_data['energy']
            try:
                player = Player.objects.create(level=level,update_need_xp=update_need_xp,
                                              energy=energy)
                player.save()
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'player_add'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'player_add'}).close();alert('添加失败');</script>")

@admin_required
def player_edit(request,player_id=0,template="admin/player/edit.tpl"):
    player = Player.get_by_id(player_id)
    if request.method == "GET":
        return render_response(template,player=player)
    elif request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            level = form.cleaned_data['level']
            ep = form.cleaned_data['ep']
            sp = form.cleaned_data['sp']
            vm = form.cleaned_data['vm']
            grm = form.cleaned_data['grm']
            brm = form.cleaned_data['brm']
            try:
                player.level = level
                player.ep = ep
                player.sp = sp
                player.vm = vm
                player.grm = grm
                player.brm = brm
                player.save()
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'player_edit'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'player_edit'}).close();alert('添加失败');</script>")
