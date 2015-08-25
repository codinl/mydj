# -*- coding: utf-8 -*-
from admin.account.decorators import admin_required
from admin.forms import GeneralForm, WeaponForm, ShieldForm, SecretBookForm, \
    TreasureForm, SecretBookPartForm, TreasurePartForm
from base.page import Paginator
from card.models import Card, General, Weapon, Shield, SecretBook, Treasure, \
     TreasurePart, SecretBookPart
from conf.models import Group
from django.http import HttpResponse
from django.shortcuts.render import render_response
import config

@admin_required
def card_ajax_list(request,card_type='',template=""):  
    card_list = Card.get_card_all(card_type)
    json_str = u'<option value="">请选择...</option>'
    if card_list:
        for card in card_list:
            json_str += u'<option value="%s">%s-%s</option>' % (card.id,card.id,card.name)
    return HttpResponse(json_str)

def _add_card(card,type_name,card_type):
    rarity = 1
    if card.rarity:
        rarity = card.rarity
    try:
        c = Card.get_by_card_type_id(card_type, card.id)
        # 已经存在 则修改
        if c:
            _edit_card(card,card_type)
        else:
            c = Card.objects.create(r_card_id=card.id,type_name=type_name,
                                    card_type=card_type,rarity=rarity,
                                    card_name=card.name)
            c.save()
    except Exception,e:
        if config.debug:
            print e

def _edit_card(card,card_type):
    rarity = 1
    if card.rarity:
        rarity = card.rarity
    c = Card.get_by_card_type_id(card_type, card.id)
    if c:
        c.rarity = rarity
        c.card_name = card.name
        c.save()
        
@admin_required
def general_list(request,cur_page=1,template="admin/card/general/list.tpl"):  
    count = Card.get_card_count("General")
    if count != 0:
        page = int(cur_page)
        general_list = Card.get_card_list("General",page)
        p = Paginator(page,count,page_size=config.default_page_size)
        if general_list:
            return render_response(template,request=request,general_list=general_list,p=p)
    return render_response(template,request=None,general_list=None,p=None)

@admin_required
def general_add(request,template="admin/card/general/add.tpl"):
    group_list = Group.get_all()
    if request.method == "GET":
        return render_response(template,group_list=group_list)
    elif request.method == "POST":
        form = GeneralForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            rarity = form.cleaned_data['rarity']
            level = form.cleaned_data['level']
            group_id = form.cleaned_data['group_id']
            description = form.cleaned_data['description']
            attack = form.cleaned_data['attack']
            defence = form.cleaned_data['defence']
            rebirth_max = form.cleaned_data['rebirth_max']
            is_unlock = form.cleaned_data['is_unlock']
            image = form.cleaned_data['image']
            is_add_attack = form.cleaned_data['is_add_attack']
            is_for_init = form.cleaned_data['is_for_init']
            level_max = Card.get_level_max(rarity, 0);
            try:
                general = General.objects.create(name=name,rarity=rarity,level=level,
                                                 group_id=group_id,description=description,attack=attack,
                                                 defence=defence,rebirth_max=rebirth_max,is_unlock=is_unlock,
                                                 level_max=level_max,is_add_attack=is_add_attack,
                                                 is_for_init=is_for_init,image=image)
                general.save()
                _add_card(general,"武将","General")
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'general_add'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'general_add'}).close();alert('添加失败');</script>")

@admin_required
def general_ajax_list_group(request,group_id=0,template=""):
    general_list = General.get_by_group(group_id)
    json_str = u'<option value="">请选择...</option>'
    if general_list:
        for general in general_list:
            json_str += '<option value="%s">%s</option>' % (general.id,general.name)
    return HttpResponse(json_str)

@admin_required
def general_edit(request,general_id=0,template="admin/card/general/edit.tpl"):
    group_list = Group.get_all()
    general = Card.get_card("General",general_id)
    if request.method == "GET":
        return render_response(template,general=general,group_list=group_list)
    elif request.method == "POST":
        form = GeneralForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            rarity = form.cleaned_data['rarity']
            level = form.cleaned_data['level']
            group_id = form.cleaned_data['group_id']
            description = form.cleaned_data['description']
            attack = form.cleaned_data['attack']
            defence = form.cleaned_data['defence']
            rebirth_max = form.cleaned_data['rebirth_max']
            is_unlock = form.cleaned_data['is_unlock']
            image = form.cleaned_data['image']
            is_add_attack = form.cleaned_data['is_add_attack']
            is_for_init = form.cleaned_data['is_for_init']
            level_max = Card.get_level_max(rarity, 0);
            try:
                edit_card = False
                if (rarity != general.rarity) or (name != general.name):
                    edit_card = True
                general.name = name
                general.rarity = rarity
                general.level = level
                general.level_max = level_max
                general.group_id = group_id
                general.description = description
                general.attack = attack
                general.defence = defence
                general.rebirth_max = rebirth_max
                general.is_unlock = is_unlock
                general.is_for_init = is_for_init
                if image:
                    general.image = image
                general.is_add_attack = is_add_attack
                general.save()
                if edit_card:
                    _edit_card(general,"General")
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'general_edit'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'general_edit'}).close();alert('添加失败');</script>")

@admin_required
def weapon_list(request,cur_page=1,template="admin/card/weapon/list.tpl"):  
    count = Card.get_card_count("Weapon")
    if count != 0:
        page = int(cur_page)
        weapon_list = Card.get_card_list("Weapon",page)
        p = Paginator(page,count,page_size=config.default_page_size)
        if weapon_list:
            return render_response(template,request=request,weapon_list=weapon_list,p=p)
    return render_response(template,request=None,weapon_list=None,p=None)

@admin_required
def weapon_add(request,template="admin/card/weapon/add.tpl"):
    if request.method == "GET":
        return render_response(template)
    elif request.method == "POST":
        form = WeaponForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            rarity = form.cleaned_data['rarity']
            description = form.cleaned_data['description']
            rebirth_max = form.cleaned_data['rebirth_max']
            is_unlock = form.cleaned_data['is_unlock']
            image = form.cleaned_data['image']
            attack = form.cleaned_data['attack']
            try:
                weapon = Weapon.objects.create(name=name,rarity=rarity,description=description,attack=attack,
                                               rebirth_max=rebirth_max,is_unlock=is_unlock,
                                               image=image)
                weapon.save()
                _add_card(weapon,"武器","Weapon")
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'weapon_add'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'weapon_add'}).close();alert('添加失败');</script>")

@admin_required
def weapon_edit(request,weapon_id=0,template="admin/card/weapon/edit.tpl"):
    weapon = Card.get_card("Weapon",weapon_id)
    if request.method == "GET":
        return render_response(template,weapon=weapon)
    elif request.method == "POST":
        form = WeaponForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            rarity = form.cleaned_data['rarity']
            description = form.cleaned_data['description']
            rebirth_max = form.cleaned_data['rebirth_max']
            is_unlock = form.cleaned_data['is_unlock']
            image = form.cleaned_data['image']
            attack = form.cleaned_data['attack']
            try:
                edit_card = False
                if (rarity != weapon.rarity) or (name != weapon.name):
                    edit_card = True
                weapon.name = name
                weapon.rarity = rarity
                weapon.description = description
                weapon.attack = attack
                weapon.rebirth_max = rebirth_max
                weapon.is_unlock = is_unlock
                if image:
                    weapon.image = image
                weapon.save()
                if edit_card:
                    _edit_card(weapon,"Weapon")
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'weapon_edit'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'weapon_edit'}).close();alert('添加失败');</script>")

@admin_required
def shield_list(request,cur_page=1,template="admin/card/shield/list.tpl"):  
    count = Card.get_card_count("Shield")
    if count != 0:
        page = int(cur_page)
        shield_list = Card.get_card_list("Shield",page)
        p = Paginator(page,count,page_size=config.default_page_size)
        if shield_list:
            return render_response(template,request=request,shield_list=shield_list,p=p)
    return render_response(template,request=None,shield_list=None,p=None)

@admin_required
def shield_add(request,template="admin/card/shield/add.tpl"):
    if request.method == "GET":
        return render_response(template)
    elif request.method == "POST":
        form = ShieldForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            rarity = form.cleaned_data['rarity']
            description = form.cleaned_data['description']
            rebirth_max = form.cleaned_data['rebirth_max']
            is_unlock = form.cleaned_data['is_unlock']
            image = form.cleaned_data['image']
            defence = form.cleaned_data['defence']
            try:
                shield = Shield.objects.create(name=name,rarity=rarity,description=description,
                                                 defence=defence,rebirth_max=rebirth_max,
                                                 image=image,is_unlock=is_unlock)
                _add_card(shield,"防具","Shield")
                shield.save()
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'shield_add'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'shield_add'}).close();alert('添加失败');</script>")

@admin_required
def shield_edit(request,shield_id=0,template="admin/card/shield/edit.tpl"):
    shield = Card.get_card("Shield",shield_id)
    if request.method == "GET":
        return render_response(template,shield=shield)
    elif request.method == "POST":
        form = ShieldForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            rarity = form.cleaned_data['rarity']
            description = form.cleaned_data['description']
            rebirth_max = form.cleaned_data['rebirth_max']
            is_unlock = form.cleaned_data['is_unlock']
            image = form.cleaned_data['image']
            defence = form.cleaned_data['defence']
            try:
                edit_card = False
                if (rarity != shield.rarity) or (name != shield.name):
                    edit_card = True
                shield.name = name
                shield.rarity = rarity
                shield.description = description
                shield.rebirth_max = rebirth_max
                shield.is_unlock = is_unlock
                if image:
                    shield.image = image
                shield.defence = defence
                shield.save()
                if edit_card:
                    _edit_card(shield,"Shield")
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'shield_edit'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'shield_edit'}).close();alert('添加失败');</script>")

@admin_required
def secretbook_list(request,cur_page=1,template="admin/card/secretbook/list.tpl"):  
    count = Card.get_card_count("SecretBook")
    if count != 0:
        page = int(cur_page)
        secretbook_list = Card.get_card_list("SecretBook",page)
        p = Paginator(page,count,page_size=config.default_page_size)
        if secretbook_list:
            return render_response(template,request=request,secretbook_list=secretbook_list,p=p)
    return render_response(template,request=None,secretbook_list=None,p=None)

@admin_required
def secretbook_add(request,template="admin/card/secretbook/add.tpl"):
    if request.method == "GET":
        return render_response(template)
    elif request.method == "POST":
        form = SecretBookForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            rarity = form.cleaned_data['rarity']
            description = form.cleaned_data['description']
#             add_value_percent = form.cleaned_data['add_value_percent']
            attack_add_percent = form.cleaned_data['attack_add_percent']
            defence_add_percent = form.cleaned_data['defence_add_percent']
            is_unlock = form.cleaned_data['is_unlock']
            image = form.cleaned_data['image']
            try:
                secretbook = SecretBook.objects.create(name=name,rarity=rarity,description=description,
                                                       attack_add_percent=attack_add_percent,defence_add_percent=defence_add_percent,
                                                       image=image,is_unlock=is_unlock)
                _add_card(secretbook,"密卷","SecretBook")
                secretbook.save()
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'secretbook_add'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'secretbook_add'}).close();alert('添加失败');</script>")

@admin_required
def secretbook_edit(request,secretbook_id=0,template="admin/card/secretbook/edit.tpl"):
    secretbook = Card.get_card("SecretBook",secretbook_id)
    if request.method == "GET":
        return render_response(template,secretbook=secretbook)
    elif request.method == "POST":
        form = SecretBookForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            rarity = form.cleaned_data['rarity']
            description = form.cleaned_data['description']
#             add_value_percent = form.cleaned_data['add_value_percent']
            attack_add_percent = form.cleaned_data['attack_add_percent']
            defence_add_percent = form.cleaned_data['defence_add_percent']
            is_unlock = form.cleaned_data['is_unlock']
            image = form.cleaned_data['image']
            try:
                edit_card = False
                if (rarity != secretbook.rarity) or (name != secretbook.name):
                    edit_card = True
                secretbook.name = name
                secretbook.rarity = rarity
                secretbook.description = description
                secretbook.attack_add_percent = attack_add_percent
                secretbook.defence_add_percent = defence_add_percent
                secretbook.is_unlock = is_unlock
                if image:
                    secretbook.image = image
                secretbook.save()
                if edit_card:
                    _edit_card(secretbook,"SecretBook")
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'secretbook_edit'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'secretbook_edit'}).close();alert('添加失败');</script>")

@admin_required
def treasure_list(request,cur_page=1,template="admin/card/treasure/list.tpl"):  
    count = Card.get_card_count("Treasure")
    if count != 0:
        page = int(cur_page)
        treasure_list = Card.get_card_list("Treasure",page)
        p = Paginator(page,count,page_size=config.default_page_size)
        if treasure_list:
            return render_response(template,request=request,treasure_list=treasure_list,p=p)
    return render_response(template,request=None,treasure_list=None,p=None)

@admin_required
def treasure_add(request,template="admin/card/treasure/add.tpl"):
    if request.method == "GET":
        return render_response(template)
    elif request.method == "POST":
        form = TreasureForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            rarity = form.cleaned_data['rarity']
            description = form.cleaned_data['description']
#             probability = form.cleaned_data['probability']
            block = form.cleaned_data['block']
            crit = form.cleaned_data['crit']
            is_unlock = form.cleaned_data['is_unlock']
            image = form.cleaned_data['image']
            try:
                treasure = Treasure.objects.create(name=name,rarity=rarity,description=description,
                                                   block = block,crit=crit,
                                                   image=image,is_unlock=is_unlock)
                _add_card(treasure,"宝物","Treasure")
                treasure.save()
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'treasure_add'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'treasure_add'}).close();alert('添加失败');</script>")

@admin_required
def treasure_edit(request,treasure_id=0,template="admin/card/treasure/edit.tpl"):
    treasure = Card.get_card("Treasure",treasure_id)
    if request.method == "GET":
        return render_response(template,treasure=treasure)
    elif request.method == "POST":
        form = TreasureForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            rarity = form.cleaned_data['rarity']
            description = form.cleaned_data['description']
#             probability = form.cleaned_data['probability']
            crit = form.cleaned_data['crit']
            block = form.cleaned_data['block']
            is_unlock = form.cleaned_data['is_unlock']
            image = form.cleaned_data['image']
            try:
                edit_card = False
                if (rarity != treasure.rarity) or (name != treasure.name):
                    edit_card = True
                treasure.name = name
                treasure.rarity = rarity
                treasure.description = description
#                 treasure.probability = probability
                treasure.crit = crit
                treasure.block = block
                treasure.is_unlock = is_unlock
                if image:
                    treasure.image = image
                treasure.save()
                if edit_card:
                    _edit_card(treasure,"Treasure")
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'treasure_edit'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'treasure_edit'}).close();alert('添加失败');</script>")

# @admin_required
# def activitycard_list(request,cur_page=1,template="admin/card/activitycard/list.tpl"):  
#     count = Card.get_card_count("ActivityCard")
#     if count != 0:
#         page = int(cur_page)
#         activitycard_list = Card.get_card_list("ActivityCard",page)
#         p = Paginator(page,count,page_size=config.default_page_size)
#         if activitycard_list:
#             return render_response(template,request=request,activitycard_list=activitycard_list,p=p)
#     return render_response(template,request=None,activitycard_list=None,p=None)
# 
# @admin_required
# def activitycard_add(request,template="admin/card/activitycard/add.tpl"):
#     if request.method == "GET":
#         return render_response(template)
#     elif request.method == "POST":
#         form = ActivityCardForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             rarity = form.cleaned_data['rarity']
#             description = form.cleaned_data['description']
#             is_unlock = form.cleaned_data['is_unlock']
#             image = form.cleaned_data['image']
#             try:
#                 activitycard = ActivityCard.objects.create(name=name,rarity=rarity,description=description,
#                                                  image=image,is_unlock=is_unlock)
# #                 _add_card(activitycard,"活动卡牌","ActivityCard")
#                 activitycard.save()
#             except Exception,e:
#                 print e
#             else:
#                 return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'activitycard_add'}).close();</script>")
#     return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'activitycard_add'}).close();alert('添加失败');</script>")
# 
# @admin_required
# def activitycard_edit(request,activitycard_id=0,template="admin/card/activitycard/edit.tpl"):
#     activitycard = Card.get_card("ActivityCard",activitycard_id)
#     if request.method == "GET":
#         return render_response(template,activitycard=activitycard)
#     elif request.method == "POST":
#         form = ActivityCardForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             rarity = form.cleaned_data['rarity']
#             is_unlock = form.cleaned_data['is_unlock']
#             image = form.cleaned_data['image']
#             try:
#                 edit_card = False
#                 if (rarity != activitycard.rarity) or (name != activitycard.name):
#                     edit_card = True
#                 activitycard.name = name
#                 activitycard.rarity = rarity
#                 activitycard.is_unlock = is_unlock
#                 if image:
#                     activitycard.image = image
#                 activitycard.save()
#                 if edit_card:
#                     _edit_card(activitycard,"ActivityCard")
#             except Exception,e:
#                 print e
#             else:
#                 return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'activitycard_edit'}).close();</script>")
#     return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'activitycard_edit'}).close();alert('添加失败');</script>")
# 
# @admin_required
# def activity_part_list(request,cur_page=1,template="admin/card/activity_part/list.tpl"):  
#     count = Card.get_card_count("ActivityCard")
#     if count != 0:
#         page = int(cur_page)
#         activity_part_list = Card.get_card_list("ActivityCard",page)
#         p = Paginator(page,count,page_size=config.default_page_size)
#         if activity_part_list:
#             return render_response(template,request=request,activity_part_list=activity_part_list,p=p)
#     return render_response(template,request=None,activity_part_list=None,p=None)
# 
# @admin_required
# def activity_part_add(request,template="admin/card/activity_part/add.tpl"):
#     activity_list = Activity.get_all()
#     if request.method == "GET":
#         return render_response(template,activity_list=activity_list)
#     elif request.method == "POST":
#         form = ActivityCardForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             description = form.cleaned_data['description']
#             activity_id = form.cleaned_data['activity_id']
#             is_unlock = form.cleaned_data['is_unlock']
#             image = form.cleaned_data['image']
#             try:
#                 activity_part = ActivityCard.objects.create(name=name,description=description,
#                                                   image=image,is_unlock=is_unlock,activity_id=activity_id)
#                 activity_part.save()
#             except Exception,e:
#                 print e
#             else:
#                 return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'activity_part_add'}).close();</script>")
#     return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'activity_part_add'}).close();alert('添加失败');</script>")
# 
# @admin_required
# def activity_part_edit(request,activity_part_id=0,template="admin/card/activity_part/edit.tpl"):
#     activity_part = Card.get_card("ActivityCard",activity_part_id)
#     if request.method == "GET":
#         return render_response(template,activity_part=activity_part)
#     elif request.method == "POST":
#         form = ActivityCardForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             description = form.cleaned_data['description']
#             activity_id = form.cleaned_data['activity_id']
#             is_unlock = form.cleaned_data['is_unlock']
#             image = form.cleaned_data['image']
#             try:
#                 activity_part.name = name
#                 activity_part.description = description
#                 activity_part.is_unlock = is_unlock
#                 activity_part.activity_id = activity_id
#                 if image:
#                     activity_part.image = image
#                 activity_part.save()
#             except Exception,e:
#                 print e
#             else:
#                 return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'activity_part_edit'}).close();</script>")
#     return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'activity_part_edit'}).close();alert('添加失败');</script>")

@admin_required
def treasure_part_list(request,cur_page=1,template="admin/card/treasure_part/list.tpl"):  
    count = Card.get_card_count("TreasurePart")
    if count != 0:
        page = int(cur_page)
        treasure_part_list = Card.get_card_list("TreasurePart",page)
        p = Paginator(page,count,page_size=config.default_page_size)
        if treasure_part_list:
            return render_response(template,request=request,treasure_part_list=treasure_part_list,p=p)
    return render_response(template,request=None,treasure_part_list=None,p=None)

@admin_required
def treasure_part_add(request,template="admin/card/treasure_part/add.tpl"):
    if request.method == "GET":
        t_card_list = Card.get_card_all("Treasure")
        return render_response(template,t_card_list=t_card_list)
    elif request.method == "POST":
        form = TreasurePartForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            is_unlock = form.cleaned_data['is_unlock']
            image = form.cleaned_data['image']
            rarity = form.cleaned_data['rarity']
            t_card_id = form.cleaned_data['t_card_id']
            try:
                treasure_part = TreasurePart.objects.create(name=name,description=description,rarity=rarity,
                                                            image=image,is_unlock=is_unlock,t_card_id=t_card_id)
                treasure_part.save()
                _add_card(treasure_part,"碎片","TreasurePart")
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'treasure_part_add'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'treasure_part_add'}).close();alert('添加失败');</script>")

@admin_required
def treasure_part_edit(request,treasure_part_id=0,template="admin/card/treasure_part/edit.tpl"):
    treasure_part = Card.get_card("TreasurePart",treasure_part_id)
    if request.method == "GET":
        t_card_list = Card.get_card_all("Treasure")
        return render_response(template,treasure_part=treasure_part,
                               t_card_list=t_card_list)
    elif request.method == "POST":
        form = TreasurePartForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            is_unlock = form.cleaned_data['is_unlock']
            image = form.cleaned_data['image']
            rarity = form.cleaned_data['rarity']
            t_card_id = form.cleaned_data['t_card_id']
            try:
                treasure_part.name = name
                treasure_part.description = description
                treasure_part.is_unlock = is_unlock
                if image:
                    treasure_part.image = image
                treasure_part.t_card_id = t_card_id
                treasure_part.rarity = rarity
                treasure_part.save()
                if treasure_part:
                    _edit_card(treasure_part,"TreasurePart")
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'treasure_part_edit'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'treasure_part_edit'}).close();alert('添加失败');</script>")

@admin_required
def secret_book_part_list(request,cur_page=1,template="admin/card/secret_book_part/list.tpl"):  
    count = Card.get_card_count("SecretBookPart")
    if count != 0:
        page = int(cur_page)
        secret_book_part_list = Card.get_card_list("SecretBookPart",page)
        p = Paginator(page,count,page_size=config.default_page_size)
        if secret_book_part_list:
            return render_response(template,request=request,secret_book_part_list=secret_book_part_list,p=p)
    return render_response(template,request=None,secret_book_part_list=None,p=None)

@admin_required
def secret_book_part_add(request,template="admin/card/secret_book_part/add.tpl"):
    if request.method == "GET":
        t_card_list = Card.get_card_all("SecretBook")
        return render_response(template,t_card_list=t_card_list)
    elif request.method == "POST":
        form = SecretBookPartForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            is_unlock = form.cleaned_data['is_unlock']
            image = form.cleaned_data['image']
            rarity = form.cleaned_data['rarity']
            t_card_id = form.cleaned_data['t_card_id']
            try:
                secret_book_part = SecretBookPart.objects.create(name=name,description=description,
                                                                 image=image,is_unlock=is_unlock,rarity=rarity,
                                                                 t_card_id=t_card_id)
                secret_book_part.save()
                _add_card(secret_book_part,"残卷","SecretBookPart")
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'secret_book_part_add'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'secret_book_part_add'}).close();alert('添加失败');</script>")

@admin_required
def secret_book_part_edit(request,secret_book_part_id=0,template="admin/card/secret_book_part/edit.tpl"):
    secret_book_part = Card.get_card("SecretBookPart",secret_book_part_id)
    if request.method == "GET":
        t_card_list = Card.get_card_all("SecretBook")
        return render_response(template,t_card_list=t_card_list,
                               secret_book_part=secret_book_part)
    elif request.method == "POST":
        form = SecretBookPartForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            is_unlock = form.cleaned_data['is_unlock']
            image = form.cleaned_data['image']
            rarity = form.cleaned_data['rarity']
            t_card_id = form.cleaned_data['t_card_id']
            try:
                secret_book_part.name = name
                secret_book_part.description = description
                secret_book_part.is_unlock = is_unlock
                if image:
                    secret_book_part.image = image
                secret_book_part.rarity = rarity
                secret_book_part.t_card_id = t_card_id
                secret_book_part.save()
                if secret_book_part:
                    _edit_card(secret_book_part,"SecretBookPart")
            except Exception,e:
                if config.debug:
                    print e
            else:
                return HttpResponse("<script type='text/javascript'>window.top.right.location.reload();window.top.art.dialog({id:'secret_book_part_edit'}).close();</script>")
    return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'secret_book_part_edit'}).close();alert('添加失败');</script>")

@admin_required
def mission_fall_cards_update(request,template="admin/card/update_fall_cards.tpl"):
    if request.method == "GET":
        return render_response(template)
    elif request.method == "POST":
        try:
            from base.obj import MisssionFallCard
            MisssionFallCard().init()
        except Exception,e:
            if config.debug:
                print e
        else:
            return HttpResponse("1")
    return HttpResponse("0")

@admin_required
def battle_fall_cards_update(request,template="admin/card/update_fall_cards.tpl"):
    if request.method == "GET":
        return render_response(template)
    elif request.method == "POST":
        try:
            from base.obj import BattleFallCard
            BattleFallCard().init()
        except Exception,e:
            if config.debug:
                print e
        else:
            return HttpResponse("1")
    return HttpResponse("0")

#更新card_card数据表
@admin_required
def fall_cards_update(request,template="admin/card/update_fall_cards.tpl"):
    if request.method == "GET":
        return render_response(template)
    elif request.method == "POST":
        try:
            raw_sql = "TRUNCATE TABLE card_card;"
            Card.objects.raw(raw_sql)
            card_types = [["General","武将"],
                          ["Weapon","武器"],
                          ["Shield","防具"],
                          ["Treasure","宝物"],
                          ["TreasurePart","碎片"],
                          ["SecretBook","密卷"],
                          ["SecretPart","残卷"]]
            for card_type in card_types:
                card_list = Card.get_card_all(card_type[0])
                if card_list:
                    for card in card_list:
                        c = Card.objects.create(r_card_id=card.id,type_name=card_type[1],
                                                card_type=card_type[0],
                                                rarity=card.rarity,
                                                card_name=card.name)
                        c.save()
        except Exception,e:
            if config.debug:
                print e
        else:
            return HttpResponse("1")
    return HttpResponse("0")
