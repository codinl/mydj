# -*- coding: utf-8 -*-
from admin.account.decorators import admin_required
from admin.forms import ScenarioForm, MissionGroupForm, MissionForm
from base.page import Paginator
from django.http import HttpResponse
from django.shortcuts.render import render_response
from mission.models import Scenario, MissionGroup, Mission
import config

@admin_required
def scenario_list(request, cur_page=1, template="admin/mission/scenario/list.tpl"):  
    count = Scenario.get_count()
    if count != 0:
        page = int(cur_page)
        scenario_list = Scenario.get_list(page)
        p = Paginator(page, count, page_size=config.default_page_size)
        if scenario_list:
            return render_response(template, request=request, scenario_list=scenario_list, p=p)
    return render_response(template, request=None, scenario_list=None, p=None)


@admin_required
def scenario_add(request, template="admin/mission/scenario/add.tpl"):
    if request.method == "GET":
        return render_response(template)
    elif request.method == "POST":
        form = ScenarioForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            order = form.cleaned_data['order']
            is_unlock = form.cleaned_data['is_unlock']
            try:
                scenario = Scenario.objects.create(name=name, order=order, is_unlock=is_unlock)
                scenario.save()
            except Exception, e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'scenario_add'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'scenario_add'}).close();alert('添加失败');</script>")


@admin_required
def scenario_edit(request, scenario_id=0, template="admin/mission/scenario/edit.tpl"):
    scenario = Scenario.get_by_id(scenario_id)
    if request.method == "GET":
        return render_response(template, scenario=scenario)
    elif request.method == "POST":
        form = ScenarioForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            order = form.cleaned_data['order']
            is_unlock = form.cleaned_data['is_unlock']
            try:
                scenario.name = name
                scenario.order = order
                scenario.is_unlock = is_unlock
                scenario.save()
            except Exception, e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'scenario_edit'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'scenario_edit'}).close();alert('添加失败');</script>")


@admin_required
def mission_group_list(request, cur_page=1, template="admin/mission/mission_group/list.tpl"):  
    count = MissionGroup.get_count()
    if count != 0:
        page = int(cur_page)
        mission_group_list = MissionGroup.get_list(page)
        p = Paginator(page, count, page_size=config.default_page_size)
        if mission_group_list:
            return render_response(template, request=request, mission_group_list=mission_group_list, p=p)
    return render_response(template, request=None, mission_group_list=None, p=None)


@admin_required
def mission_group_add(request, template="admin/mission/mission_group/add.tpl"):
    if request.method == "GET":
        scenario_list = Scenario.get_all()
        return render_response(template, scenario_list=scenario_list)
    elif request.method == "POST":
        form = MissionGroupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            order = form.cleaned_data['order']
            is_unlock = form.cleaned_data['is_unlock']
            scenario_id = form.cleaned_data['scenario_id']
            is_scenario_last = form.cleaned_data['is_scenario_last']
            try:
                mission_group = MissionGroup.objects.create(name=name, order=order,
                                                            is_unlock=is_unlock,
                                                            is_scenario_last=is_scenario_last,
                                                            scenario_id=scenario_id)
                mission_group.save()
            except Exception, e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'mission_group_add'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'mission_group_add'}).close();alert('添加失败');</script>")


@admin_required
def mission_group_edit(request, mission_group_id=0, template="admin/mission/mission_group/edit.tpl"):
    mission_group = MissionGroup.get_by_id(mission_group_id)
    if request.method == "GET":
        scenario_list = Scenario.get_all()
        return render_response(template, mission_group=mission_group, scenario_list=scenario_list)
    elif request.method == "POST":
        form = MissionGroupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            order = form.cleaned_data['order']
#             level = form.cleaned_data['level']
            is_unlock = form.cleaned_data['is_unlock']
            scenario_id = form.cleaned_data['scenario_id']
            is_scenario_last = form.cleaned_data['is_scenario_last']
            try:
                mission_group.name = name
                mission_group.order = order
                mission_group.is_unlock = is_unlock
#                 mission_group.level = level
                mission_group.scenario_id = scenario_id
                mission_group.is_scenario_last = is_scenario_last
                mission_group.save()
            except Exception, e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'mission_group_edit'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'mission_group_edit'}).close();alert('添加失败');</script>")


@admin_required
def ajax_group_list(request, scenario_id=0):
    mission_group_list = MissionGroup.get_list_by_scenario(scenario_id)
    json_str = ''
    if mission_group_list:
        for mission_group in mission_group_list:
            json_str += '<option value="%s">%s</option>' % (mission_group.id, mission_group.name)
    return HttpResponse(json_str)


@admin_required
def mission_list(request, cur_page=1, template="admin/mission/mission/list.tpl"):  
    count = Mission.get_count()
    if count != 0:
        page = int(cur_page)
        mission_list = Mission.get_list(page)
        p = Paginator(page, count, page_size=config.default_page_size)
        if mission_list:
            return render_response(template, request=request, mission_list=mission_list, p=p)
    return render_response(template, request=None, mission_list=None, p=None)


@admin_required
def mission_add(request, template="admin/mission/mission/add.tpl"):
    if request.method == "GET":
        scenario_list = Scenario.get_all()
        return render_response(template, scenario_list=scenario_list)
    elif request.method == "POST":
        form = MissionForm(request.POST)
        if form.is_valid():
#             name = form.cleaned_data['name']
            ep = form.cleaned_data['ep']
#             vm = form.cleaned_data['vm']
#             xp = form.cleaned_data['xp']
            description = form.cleaned_data['description']
#             sum_count = form.cleaned_data['sum_count']
            is_unlock = form.cleaned_data['is_unlock']
            scenario_id = form.cleaned_data['scenario_id']
            mission_group_id = form.cleaned_data['mission_group_id']
            order = form.cleaned_data['order']
            level = form.cleaned_data['level']
            is_group_last = form.cleaned_data['is_group_last']
            vm = 35
            sum_count = 10
            if is_group_last:
                ep = 25
                vm = 180
                sum_count = 1
            xp = ep * 5
            try:
                mission = Mission.objects.create(ep=ep, vm=vm, xp=xp, sum_count=sum_count,
                                               is_unlock=is_unlock, scenario_id=scenario_id,
                                               description=description, order=order, level=level,
                                               mission_group_id=mission_group_id, is_group_last=is_group_last)
                mission.save()
            except Exception, e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'mission_add'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'mission_add'}).close();alert('添加失败');</script>")


@admin_required
def mission_edit(request, mission_id=0, template="admin/mission/mission/edit.tpl"):
    mission = Mission.get_by_id(mission_id)
    if request.method == "GET":
        scenario_list = Scenario.get_all()
        return render_response(template, scenario_list=scenario_list, mission=mission)
    elif request.method == "POST":
        form = MissionForm(request.POST)
        if form.is_valid():
#             name = form.cleaned_data['name']
            ep = form.cleaned_data['ep']
#             vm = form.cleaned_data['vm']
#             xp = form.cleaned_data['xp']
            description = form.cleaned_data['description']
#             sum_count = form.cleaned_data['sum_count']
            is_unlock = form.cleaned_data['is_unlock']
            scenario_id = form.cleaned_data['scenario_id']
            mission_group_id = form.cleaned_data['mission_group_id']
            order = form.cleaned_data['order']
            level = form.cleaned_data['level']
            is_group_last = form.cleaned_data['is_group_last']
            vm = 35
            sum_count = 10
            if is_group_last:
                ep = 25
                vm = 180
                sum_count = 1
            if scenario_id < 3:
                ep = form.cleaned_data['ep']
            xp = ep * 5
            try:
#                 mission.name = name
                mission.ep = ep
                mission.vm = vm
                mission.xp = xp
                mission.description = description
                mission.sum_count = sum_count
                mission.is_unlock = is_unlock
                mission.scenario_id = scenario_id
                mission.mission_group_id = mission_group_id
                mission.order = order
                mission.level = level
                mission.is_group_last = is_group_last
                mission.save()
            except Exception, e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'mission_edit'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'mission_edit'}).close();alert('添加失败');</script>")

