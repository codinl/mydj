# -*- coding: utf-8 -*-
from base import string_util
from card.skills import Skill

# 获取武将技能json list
def get_skills_json_array(r_general,player_on_cards):
    skills_arry = []
    skill_list = r_general.get_o_skill_list()
    if skill_list:
        for _skill in skill_list:
            on_card_ids = player_on_cards.get_on_r_cards(_skill.card_type)
            skill_description = ""
            _skill.name = "&#149 "+_skill.name
            if is_skill_active(_skill,player_on_cards):
                _skill.name = "<em>"+_skill.name +"</em>"
                skill_description = "<em>"+get_skill_description(_skill,r_general,on_card_ids) +"</em>"
            else:
                skill_description = get_skill_description(_skill,r_general,on_card_ids)
            skill_dict = {"id":_skill.id, "description":skill_description,
                          "name":_skill.name, "rebirth":""}
            skills_arry.append(skill_dict)
    return skills_arry

def is_skill_active(_skill,player_on_cards):
    if player_on_cards:
        on_cards = player_on_cards.get_on_r_cards(_skill.card_type)
        if on_cards:
            on_card_list = on_cards.split(",")
            active_card_list = Skill.get_active_card_list(_skill)
            return _is_list_in(active_card_list,on_card_list)
    return False

# _list_a 是否 in _list_b
# 类型统一转换为 str
def _is_list_in(_list_a,_list_b):
    if _list_a and _list_b:
        total = len(_list_a)
        count = 0
        for a in _list_a:
            a = string_util.to_unicode(a)
            for b in _list_b:
                b = string_util.to_unicode(b)
                if a == b:
                    count += 1
                    break
        if total == count:
            return True
    return False
    
# 只有武将显示技能
# 获取技能描述
def get_skill_description(_o_skill,r_general,on_card_ids):    
    skill_card_type = _o_skill.card_type
    card_names = ""
    if skill_card_type == "G":
        card_ids = _o_skill.general_ids
        # 去除当前武将r_id
        card_ids = string_util.exclude_something(_o_skill.general_ids,r_general.id)
        # 去除当前武将名
        card_names = string_util.exclude_something(_o_skill.general_names,r_general.name)
        card_names = _get_card_names(card_names,card_ids,on_card_ids)
    else:
        card_names = _get_card_names(_o_skill.card_names,_o_skill.card_ids,on_card_ids)
    
    card_names = string_util.clean_str(card_names)
    
    add_value_percent = _o_skill.add_value_percent
    
    add_type_name = u"防御"
    if skill_card_type == "G":
        if r_general.is_add_attack:
            add_type_name = u"攻击"
        return u"与%s同时上阵，增加%s%s%%" % (card_names, add_type_name, add_value_percent)
    elif skill_card_type == "SB":
        if r_general.is_add_attack:
            add_type_name = u"攻击"
        return u"相伴美人%s，增加%s%s%%" % (card_names, add_type_name, add_value_percent)
    else:
        if r_general.is_add_attack and skill_card_type != "S":
            add_type_name = u"攻击"
        return u"装备%s，增加%s%s%%" % (card_names, add_type_name, add_value_percent)

def _get_card_names(card_names,card_ids,on_card_ids):
    if card_names and card_ids and on_card_ids:
        card_names_list = card_names.split(",")
        card_ids_list = card_ids.split(",")
        result_card_names = []
        i = 0
        for card_name in card_names_list:
            if i >= len(card_ids_list):
                break
            card_id = card_ids_list[i]
            card_name = _get_card_name(card_name,card_id,on_card_ids)
            result_card_names.append(card_name)
            i += 1
        return ",".join(result_card_names)
    return card_names

def _get_card_name(card_name,r_card_id,on_card_ids):
    if _is_card_on(r_card_id,on_card_ids):
        return "<em>"+card_name+"</em>"
    return card_name

# 卡牌是否已上阵
def _is_card_on(r_card_id,on_card_ids):
    r_card_id = string_util.to_unicode(r_card_id)
    if on_card_ids:
        on_card_list = on_card_ids.split(',')
        for _on_card in on_card_list:
            if string_util.to_unicode(_on_card) == r_card_id:
                return True
    return False
    