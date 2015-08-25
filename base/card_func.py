# -*- coding: utf-8 -*-
from base import skills_func
from card.models import Card

def get_general_json_dict(general,player_on_cards,show_skills=True):
    return get_card_json_dict(general,player_on_cards,show_skills=show_skills)

def get_card_json_dict(card,player_on_cards,show_skills=True):
    r_card = card.r_card
    image = r_card.image
    card_type = r_card.get_class_name()
    baseslot_id = 0
    if card.baseslot_id:
        baseslot_id = card.baseslot_id
    data_dict = {"id":card.id,"card_type":card_type,
                 "baseslot_id":baseslot_id,
                 "player_card_id":card.id,"name":r_card.name, 
                 "description":r_card.description,   
                 "level":card.level,"is_level_max": card.is_level_max,
                 "xp":card.xp,"next_xp":card.next_xp,
                 "rarity":r_card.rarity,"rebirth_count":card.rebirth_count,
                 "large_image":Card.get_image(card_type,image,"large"),
                 "small_image":Card.get_image(card_type,image,"small")}
    # 只有武将显示技能
    if card_type == "General":
        skills_arry = []
        if show_skills and player_on_cards:
            skills_arry = skills_func.get_skills_json_array(r_card,player_on_cards)
        data_dict.update({"attack":(card.get_all_attack()),
                          "defence":(card.get_all_defence()),
                          "crit":card.treasure_crit,"block":card.treasure_block,
                          "skills":skills_arry})
    elif card_type == "Weapon":
        data_dict.update({"attack":(card.attack)})
    elif card_type == "Shield":
        data_dict.update({"defence":(card.defence)})
    elif card_type == "SecretBook":
        data_dict.update({"attack_add_percent":r_card.attack_add_percent,
                          "defence_add_percent":r_card.defence_add_percent})
    elif card_type == "Treasure":   
        data_dict.update({"crit":r_card.crit,"block":r_card.block}) 
    return data_dict

    
    