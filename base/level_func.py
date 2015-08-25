# -*- coding: utf-8 -*-

def gen_levelup_dict(player,award_vm,award_rm):
    _old_level = player.level
    player.xp -= player.next_xp
    player.level += 1
    _cur_level = int(player.level)
    player.next_xp = get_next_xp(_cur_level)
    _old_max_ep = player.max_ep
    player.max_ep = get_max_ep(_cur_level)
    player.ep = player.max_ep
    _old_max_sp = player.max_sp
    player.max_sp = get_max_sp(_cur_level)
    player.sp = player.max_sp
    _old_baseslot_count = player.baseslot_count
    new_baseslot_count = get_baseslot_count(player.level)
    
    _data_dict = {"player_id":player.id,
                  "name":player.name,
                  "level":[_old_level,player.level],
                  "max_ep":[_old_max_ep,player.max_ep],
                  "max_sp":[_old_max_sp,player.max_sp],
                  "baseslot_count":[_old_baseslot_count,new_baseslot_count],
                  "award":{"vm":award_vm,"rm":award_rm}
                  }
    level_up_dict = {"name":"level.up","data":_data_dict}
    return level_up_dict
    
# 级别升级经验
def get_next_xp(level):
    # LV[2,19]=上一级NEXT_XP+（INT（LV/5）+1）*10
    if level >= 2 and level <= 19:
        return get_next_xp(level - 1) + (int(level / 5) + 1) * 10
    # LV[20,999]=上一级NEXT_XP+40
    elif level >= 20 and level <= 999:
        return get_next_xp(level - 1) + 40
    return 15

def get_max_ep(level):
    # LV[1,111]=3+（级别-1）*2
    if level >= 1 and level <= 111:
        return 3 + (level - 1) * 2
    # LV[112,999]= 225
    elif level >= 112 and level <= 999:
        return 225

def get_max_sp(level):
    return 3

def get_baseslot_count(level):
    if level >= 1 and level <= 4:
        return 2 
    elif level >= 5 and level <= 9:
        return 3
    elif level >= 10 and level <= 19:
        return 4
    elif level >= 20 and level <= 29:
        return 5
    elif level >= 30 and level <= 39:
        return 6
    elif level >= 40 and level <= 49:
        return 7
    elif level >= 50 and level <= 69:
        return 8
    elif level >= 70 and level <= 99:
        return 9
    elif level >= 100 and level <= 149:
        return 10
    elif level >= 150 and level <= 199:
        return 11
    elif level >= 200 and level <= 299:
        return 12
    elif level >= 300 and level <= 499:
        return 13
    elif level >= 500 and level <= 699:
        return 14
    elif level >= 700 and level <= 998:
        return 15
    elif level >= 999:
        return 16  
    
        
#计算输入经验，获取强化增加的级别
def get_add_level(card,r_card,add_xp,card_type):
    add_level = 0
    max_level = _get_max_level(card_type,r_card.rarity,card.rebirth_count)
    cur_total_xp = get_level_xp(card.level)
    for level in range(card.level+1,max_level+1):
        #级别对应的经验
        if (cur_total_xp + card.xp + add_xp) >= get_level_xp(level):
            add_level += 1
    return add_level

# 计算到该级别需要的累计经验
def get_level_xp(level):
    return (level-1)*level/2 + 9*(level-1)
        
def _get_max_level(card_type,rarity,rebirth_count):
    if rarity < 3 or card_type == "SecretBook" or card_type == "Treasure":
        return rarity * 10
    return rarity*10*(1+rebirth_count)

# 计算吞噬卡牌产生的经验
def get_output_xp(player_card):
    if player_card:
        _level = player_card.level
        rarity = player_card.r_card.rarity
        rebirth_count = player_card.rebirth_count
        return _get_output_xp_0(_level,rarity,rebirth_count)
    
def _get_output_xp_0(level,rarity,rebirth_count):
    xp_add_total = 0
    xp_add = int((level * (level-1)/2.0 + level*10) * (0.5+rarity*0.1))
    if rarity == 5:
        if rebirth_count == 1: 
            xp_add += 1725
        elif rebirth_count == 2: 
            xp_add += 7675
    elif rarity == 4:
        if rebirth_count == 1: 
            xp_add += 1017
        elif rebirth_count == 2: 
            xp_add += 4581
    elif rarity == 3:
        if rebirth_count == 1: 
            xp_add += 588
        elif rebirth_count == 2: 
            xp_add += 2484
    xp_add_total += xp_add
    return xp_add_total


