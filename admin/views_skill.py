# -*- coding: utf-8 -*-
from admin.account.decorators import admin_required
from admin.forms import UploadFileForm
from base import string_util
from base.page import Paginator
from card.models import General, Weapon, Shield, SecretBook, Treasure
from card.skills import Skill
from django.http import HttpResponse
from django.shortcuts.render import render_response
import config

@admin_required
def import_skill(request, template="admin/skill/import.tpl"):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            import_file  = request.FILES['import_file']
            skill_list = _init_skill_list(import_file)
            import_file.close()
            _do_import(skill_list)
        return HttpResponse("<script type='text/javascript'>alert('导入成功');</script>")
    return render_response(template)

def _do_import(import_skill_list):
    # 先清空
    Skill.clear()
    
    all_general_list = General.get_all()
    all_weapon_list = Weapon.get_all()
    all_shield_list = Shield.get_all()
    all_secretbook_list = SecretBook.get_all()
    all_treasure_list = Treasure.get_all()
    error = False
    line_number = 0
    import_count = 0
    for _skill in import_skill_list:
        line_number += 1
        skill_card_type = _skill.card_type
        if skill_card_type == "G":
            _card_names = _skill.general_names.split(",")
            _general_ids = []
            for _card_name in _card_names:
                if _card_name:
                    _general_id = _card_name_exist(_card_name,all_general_list)
                    if not _general_id:
                        _general = General.get_by_name(_card_name)
                        if not _general:
                            print line_number,_card_name,"数据库不存在"
                            error = True
                            break
                        else:
                            _general_id = _general.id
                    else:
                        _general_ids.append(_general_id)
                    if _general_ids:
                        _skill.general_ids = _long_list_2_str(_general_ids)
        elif skill_card_type == "W":
            _general_name =  _skill.general_names
            _card_name = _skill.card_names
            if _general_name:
                _general_id = _card_name_exist(_general_name,all_general_list)
                if not _general_id:
                    _general = General.get_by_name(_general_name)
                    if not _general:
                        print line_number,_general_name,"数据库不存在"
                        error = True
                        break
                    else:
                        _general_id = _general.id
                else:
                    _skill.general_ids = str(_general_id)
            if _card_name:
                _card_id = _card_name_exist(_card_name,all_weapon_list)
                if not _card_id:
                    _card = Weapon.get_by_name(_card_name)
                    if not _card:
                        print line_number,_card_name,"数据库不存在"
                        error = True
                        break
                    else:
                        _card_id = _card.id
                else:
                    _skill.card_ids = str(_card_id)
        elif skill_card_type == "S":
            _general_name =  _skill.general_names
            _card_name = _skill.card_names
            if _general_name:
                _general_id = _card_name_exist(_general_name,all_general_list)
                if not _general_id:
                    _general = General.get_by_name(_general_name)
                    if not _general:
                        print line_number,_general_name,"数据库不存在"
                        error = True
                        break
                    else:
                        _general_id = _general.id
                else:
                    _skill.general_ids = str(_general_id)
            if _card_name:
                _card_id = _card_name_exist(_card_name,all_shield_list)
                if not _card_id:
                    _card = Shield.get_by_name(_card_name)
                    if not _card:
                        print line_number,_card_name,"数据库不存在"
                        error = True
                        break
                    else:
                        _card_id = _card.id
                else:
                    _skill.card_ids = str(_card_id)
        elif skill_card_type == "SB":
            _general_name =  _skill.general_names
            _card_name = _skill.card_names
            if _general_name:
                _general_id = _card_name_exist(_general_name,all_general_list)
                if not _general_id:
                    _general = General.get_by_name(_general_name)
                    if not _general:
                        print line_number,_general_name,"数据库不存在"
                        error = True
                        break
                    else:
                        _general_id = _general.id
                else:
                    _skill.general_ids = str(_general_id)
            if _card_name:
                _card_id = _card_name_exist(_card_name,all_secretbook_list)
                if not _card_id:
                    _card = SecretBook.get_by_name(_card_name)
                    if not _card:
                        print line_number,_card_name,"数据库不存在"
                        error = True
                        break
                    else:
                        _card_id = _card.id
                else:
                    _skill.card_ids = str(_card_id)
        elif skill_card_type == "T":
            _general_name =  _skill.general_names
            _card_name = _skill.card_names
            if _general_name:
                _general_id = _card_name_exist(_general_name,all_general_list)
                if not _general_id:
                    _general = General.get_by_name(_general_name)
                    if not _general:
                        print line_number,_general_name,"数据库不存在"
                        error = True
                        break
                    else:
                        _general_id = _general.id
                else:
                    _skill.general_ids = str(_general_id)
            if _card_name:
                _card_id = _card_name_exist(_card_name,all_treasure_list)
                if not _card_id:
                    _card = Treasure.get_by_name(_card_name)
                    if not _card:
                        print line_number,_card_name,"数据库不存在"
                        error = True
                        break
                    else:
                        _card_id = _card.id
                else:
                    _skill.card_ids = str(_card_id)
        if error:
            break
        _skill.save()
        import_count += 1
    print "import_count=",import_count
    
def _card_name_exist(_card_name,card_list):
    for _card in card_list:
        if string_util.to_unicode(_card.name) == string_util.to_unicode(_card_name):
            return _card.id
    return None
        
def _init_skill_list(_file):
    skill_list = []
    file_lines = _file.readlines()
    if file_lines:
        for file_line in file_lines:
            skill = _init_skill(file_line)
            if skill:
                skill_list.append(skill)
    return skill_list
                

def _init_skill(file_line):
    skill = None
    _str_list =  file_line.split(":")
    if len(_str_list) == 4:
        card_type = _str_list[0]
        name = _str_list[1]
        card_names = _str_list[2]
        add_value_percent = _str_list[3]
        add_value_percent = int(add_value_percent)
        if card_type == "G":
            skill = Skill(card_type=card_type,name=name,
                          general_names=card_names,
                          add_value_percent=add_value_percent)
        else:
            card_name_list = card_names.split(",")
            general_name = card_name_list[0]
            card_name = card_name_list[1]
            skill = Skill(card_type=card_type,name=name,
                          general_names=general_name,
                          card_names = card_name,
                          add_value_percent=add_value_percent)
    return skill

# 成员为long类型的list转化为str
def _long_list_2_str(_long_list):
    result = ""
    for _long in _long_list:
        result += (str(_long)+",")
    return string_util.clean_str(result)
        
# def handle_uploaded_file(f):
#     destination = open('some/file/name.txt', 'wb+')
#     for chunk in f.chunks():
#         destination.write(chunk)
#     destination.close()

@admin_required
def skill_list(request, cur_page=1, template="admin/skill/list.tpl"):  
    skill_all_list = Skill.get_all()
    if skill_all_list:
        count = len(skill_all_list)
        if count > 0:
            page = int(cur_page)
            page_start = (page-1)*config.default_page_size
            page_end = page*config.default_page_size
            if page_end > (count-1):
                page_end = (count-1)
            skill_list = skill_all_list[page_start:page_end]
            p = Paginator(page, count, page_size=config.default_page_size)
            return render_response(template, request=request, skill_list=skill_list, p=p)
    return render_response(template, request=None, skill_list=None, p=None)
# 
# @admin_required
# def skill_add(request, template="admin/skill/add.tpl"):
#     if request.method == "GET":
#         group_list = Group.get_all()
#         card_type_list = CardType.get_all()
#         return render_response(template, group_list=group_list, card_type_list=card_type_list)
#     elif request.method == "POST":
#         form = SkillForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
# #             description = form.cleaned_data['description']
# #             is_cards_general = form.cleaned_data['is_cards_general']
# #             general_id = form.cleaned_data['general_id']
#             card_ids = ''
#             card_1_id = form.cleaned_data['card_1_id']
#             if card_1_id:
#                 card_ids = card_ids + str(card_1_id) + ","
#             card_2_id = form.cleaned_data['card_2_id']
#             if card_2_id:
#                 card_ids = card_ids + str(card_2_id) + ","
#             card_3_id = form.cleaned_data['card_3_id']
#             if card_3_id:
#                 card_ids = card_ids + str(card_3_id) + ","
#             card_4_id = form.cleaned_data['card_4_id']
#             if card_4_id:
#                 card_ids = card_ids + str(card_4_id) + ","
#             card_5_id = form.cleaned_data['card_5_id']
#             if card_5_id:
#                 card_ids = card_ids + str(card_5_id)
#             add_value_percent = form.cleaned_data['add_value_percent']
# #             defence_add_percent = form.cleaned_data['defence_add_percent']
#             is_unlock = form.cleaned_data['is_unlock']
#             
#             card_2_type = form.cleaned_data['card_2_type']
#             
#             try:
# #               #武将组合，一次性添加所有相关武将的技能
#                 if card_2_type == "General":
#                     skill = Skill.objects.create(name=name, card_ids=card_ids, 
#                                                  skill_card_type="G",
#                                                  add_value_percent=add_value_percent,
#                                                  is_unlock=is_unlock)
#                     card_ids_list = card_ids.split(",")
#                     card_names = []
#                     for g_id in card_ids_list:
#                         if g_id:
#                             g_ids = []  
#                             for _g_id in card_ids_list:
#                                 if _g_id and _g_id != g_id:
#                                     g_ids.append(_g_id)
#                             general = General.get_by_id(g_id)
#                             g_ids_str = ','.join(g_ids)
#                             if general:
#                                 card_names.append(general.name)
#                                 general.o_skill_ids = add_skill(general.o_skill_ids, "G", str(skill.id), g_ids_str)
#                                 general.save()
#                     skill.card_names = ','.join(card_names)
#                     skill.save()
#                 else:
#                     if card_2_type:
#                         skill_card_type = "W"
#                         if card_2_type == "Weapon":
#                             skill_card_type = "W"
#                         elif card_2_type == "Shield":
#                             skill_card_type = "S"
#                         elif card_2_type == "SecretBook":
#                             skill_card_type = "SB"
#                         elif card_2_type == "Treasure":
#                             skill_card_type = "T"
#                         skill = Skill.objects.create(name=name,
#                                                      card_ids=card_ids, 
#                                                      skill_card_type=skill_card_type,
#                                                      add_value_percent=add_value_percent,
#                                                      is_unlock=is_unlock)
#                         general = General.get_by_id(card_1_id)
#                         if general:
#                             general.o_skill_ids = add_skill(general.o_skill_ids, skill_card_type, str(skill.id), str(card_2_id))
#                             general.save()
#                         another_card = Card.get_card(card_2_type,card_2_id)
#                         if another_card:
#                             skill.card_names = general.name+","+another_card.name
#                         skill.save()
#             except Exception, e:
#                 if config.debug:
#                     print e
#             else:
#                 return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'skill_add'}).close();window.top.right.location.reload();</script>")
#     return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'skill_add'}).close();alert('添加失败');</script>")
# 
# @admin_required
# def skill_edit(request, skill_id=0, template="admin/skill/edit.tpl"):
#     skill = Skill.get_by_id(skill_id)
#     if request.method == "GET":
#         group_list = Group.get_all()
#         card_type_list = CardType.get_all()
#         return render_response(template, skill=skill, group_list=group_list, card_type_list=card_type_list)
#     elif request.method == "POST":
#         form = SkillForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             card_ids = ''
#             card_1_id = form.cleaned_data['card_1_id']
#             if card_1_id:
#                 card_ids = card_ids + str(card_1_id) + ","
#             card_2_id = form.cleaned_data['card_2_id']
#             if card_2_id:
#                 card_ids = card_ids + str(card_2_id) + ","
#             card_3_id = form.cleaned_data['card_3_id']
#             if card_3_id:
#                 card_ids = card_ids + str(card_3_id) + ","
#             card_4_id = form.cleaned_data['card_4_id']
#             if card_4_id:
#                 card_ids = card_ids + str(card_4_id) + ","
#             card_5_id = form.cleaned_data['card_5_id']
#             if card_5_id:
#                 card_ids = card_ids + str(card_5_id) + ","
#             add_value_percent = form.cleaned_data['add_value_percent']
#             is_unlock = form.cleaned_data['is_unlock']
#             
#             card_2_type = form.cleaned_data['card_2_type']
#             
#             skill_card_type = ""
#             if card_2_type == "Weapon":
#                 skill_card_type = "W"
#             elif card_2_type == "Shield":
#                 skill_card_type = "S"
#             elif card_2_type == "SecretBook":
#                 skill_card_type = "SB"
#             elif card_2_type == "Treasure":
#                 skill_card_type = "T"
#                         
#             try:
#                 #先清空
#                 skill.card_names = ""
#                 if skill.skill_card_type == "G":
#                     card_ids_list = skill.card_ids.split(",")
#                     for g_id in card_ids_list:
#                         if g_id:
#                             general = General.get_by_id(g_id)
#                             if general:
#                                 general.o_skill_ids = remove_skill(general.o_skill_ids,"G",str(skill.id))
#                                 general.save()
#                 else:
#                     card_ids_list = skill.card_ids.split(",")
#                     general = General.get_by_id(card_ids_list[0])
#                     if general:
#                         general.o_skill_ids = remove_skill(general.o_skill_ids,skill_card_type,str(skill.id))
#                         general.save()
#                         
#                 #再添加            
#                 # 武将组合，一次性添加所有相关武将的技能
#                 if card_2_type == "General":
#                     card_ids_list = card_ids.split(",")
#                     card_names = []
#                     for g_id in card_ids_list:
#                         if g_id:
#                             g_ids = []  
#                             for _g_id in card_ids_list:
#                                 if _g_id and _g_id != g_id:
#                                     g_ids.append(_g_id)
#                             general = General.get_by_id(g_id)
#                             g_ids_str = ','.join(g_ids)
#                             if general:
#                                 card_names.append(general.name)
#                                 general.o_skill_ids = add_skill(general.o_skill_ids, "G", str(skill.id), g_ids_str)
#                                 general.save()
#                     skill.card_names = ','.join(card_names)
#                 else:
#                     skill.skill_card_type = skill_card_type
#                     
#                     general = General.get_by_id(card_1_id) 
#                     if general:
#                         #再添加
#                         general.o_skill_ids = add_skill(general.o_skill_ids, skill_card_type, str(skill.id), str(card_2_id))
#                         general.save()
#                     
#                     another_card = Card.get_card(card_2_type,card_2_id)
#                     if another_card:
#                         skill.card_names = general.name+","+another_card.name
#                                 
#                 skill.name = name
# #                 skill.description=description
# #                 skill.is_cards_general=is_cards_general
#                 skill.card_ids = card_ids
# #                 skill.general_id=general_id
#                 skill.add_value_percent = add_value_percent
#                 skill.is_unlock = is_unlock
#                 
#                 skill.save()
#                 
#             except Exception, e:
#                 if config.debug:
#                     print e
#             else:
#                 return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'skill_edit'}).close();window.top.right.location.reload();</script>")
#     return HttpResponse("<script type='text/javascript'>window.top.art.dialog({id:'skill_edit'}).close();alert('添加失败');</script>")
