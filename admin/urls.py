# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'admin.views.home', name='admin'),
    url(r'^home$', 'admin.views.home',name="admin_home"),
    url(r'^home/(?P<cur_menu_id>\d{1,2})$', 'admin.views.home',name="admin_home_menu"),
    url(r'^index$', 'admin.views.index', name='admin_index'), 
    
    url(r'^node/list/(?P<cur_page>\d{1,5})$', 'admin.views.node_list',name="admin_node_list"),
    url(r'^node/add$', 'admin.views.node_add',name="admin_node_add"),
    url(r'^node/edit/(?P<node_id>\d{1,5})$', 'admin.views.node_edit',name="admin_node_edit"),   
    url(r'^node/delete$', 'admin.views.node_delete',name="admin_node_delete"),
    
    url(r'^account/login$', 'admin.account.views.login',name="admin_account_login"),
    url(r'^account/logout$', 'admin.account.views.logout',name="admin_account_logout"),
    
    url(r'^admin/list/(?P<cur_page>\d{1,5})$', 'admin.account.views.admin_list',name="admin_admin_list"),
    url(r'^admin/add$', 'admin.account.views.admin_add',name="admin_admin_add"),
    url(r'^admin/edit/(?P<admin_id>\d{1,5})$', 'admin.account.views.admin_edit',name="admin_admin_edit"),
    url(r'^admin/add/ajax_check_name$', 'admin.account.views.ajax_check_name',name="admin_ajax_check_name"),
    
    url(r'^scenario/list/(?P<cur_page>\d{1,5})$', 'admin.views.scenario_list',name="admin_scenario_list"),
    url(r'^scenario/add$', 'admin.views.scenario_add',name="admin_scenario_add"),
    url(r'^scenario/edit/(?P<scenario_id>\d{1,5})$', 'admin.views.scenario_edit',name="admin_scenario_edit"),
 
    url(r'^mission_group/list/(?P<cur_page>\d{1,5})$', 'admin.views.mission_group_list',name="admin_admin_list"),
    url(r'^mission_group/add$', 'admin.views.mission_group_add',name="admin_mission_group_add"),
    url(r'^mission_group/edit/(?P<mission_group_id>\d{1,5})$', 'admin.views.mission_group_edit',name="admin_mission_group_edit"),
    url(r'^mission_group/ajax/get_list/(?P<scenario_id>\d{1,10})$', 'admin.views.ajax_group_list',name="admin_ajax_group_list"),
    
    url(r'^mission/list/(?P<cur_page>\d{1,5})$', 'admin.views.mission_list',name="admin_mission_list"),
    url(r'^mission/add$', 'admin.views.mission_add',name="admin_mission_add"),
    url(r'^mission/edit/(?P<mission_id>\d{1,5})$', 'admin.views.mission_edit',name="admin_mission_edit"),
    
    url(r'^config/group/list/(?P<cur_page>\d{1,5})$', 'admin.views.group_list',name="admin_group_list"),
    url(r'^config/group/add$', 'admin.views.group_add',name="admin_group_add"),
    url(r'^config/group/edit/(?P<group_id>\d{1,5})$', 'admin.views.group_edit',name="admin_group_edit"),
 
    url(r'^config/level/list/(?P<cur_page>\d{1,5})$', 'admin.views.config_level_list',name="admin_config_level_list"),
    url(r'^config/level/add$', 'admin.views.config_level_add',name="admin_config_level_add"),
    url(r'^config/level/edit/(?P<config_level_id>\d{1,5})$', 'admin.views.config_level_edit',name="admin_config_level_edit"),
    
    url(r'^config/mission_p/list$', 'admin.views.mission_p_list',name="admin_mission_p_list"),
    url(r'^config/mission_p/edit$', 'admin.views.mission_p_edit',name="admin_config_mission_p_edit"),
    
    url(r'^cardtype/list/(?P<cur_page>\d{1,5})$', 'admin.views.cardtype_list',name="admin_cardtype_list"),
    url(r'^cardtype/add$', 'admin.views.cardtype_add',name="admin_cardtype_add"),
    url(r'^cardtype/edit/(?P<cardtype_id>\d{1,5})$', 'admin.views.cardtype_edit',name="admin_cardtype_edit"),
    
    url(r'^card/ajax/list/(?P<card_type>\w+)$', 'admin.views.card_ajax_list',name="admin_card_ajax_list"),
    url(r'^card/update/select$', 'admin.views.select_cards_update',name="select_cards_update"),

    url(r'^general/list/(?P<cur_page>\d{1,5})$', 'admin.views.general_list',name="admin_general_list"),
    url(r'^general/add$', 'admin.views.general_add',name="admin_general_add"),
    url(r'^general/edit/(?P<general_id>\d{1,5})$', 'admin.views.general_edit',name="admin_general_edit"),
    url(r'^general/ajax/list/group/(?P<group_id>\d{1,10})$', 'admin.views.general_ajax_list_group',name="admin_general_ajax_list_group"),

    url(r'^weapon/list/(?P<cur_page>\d{1,5})$', 'admin.views.weapon_list',name="admin_weapon_list"),
    url(r'^weapon/add$', 'admin.views.weapon_add',name="admin_weapon_add"),
    url(r'^weapon/edit/(?P<weapon_id>\d{1,5})$', 'admin.views.weapon_edit',name="admin_weapon_edit"),
    
    url(r'^shield/list/(?P<cur_page>\d{1,5})$', 'admin.views.shield_list',name="admin_shield_list"),
    url(r'^shield/add$', 'admin.views.shield_add',name="admin_shield_add"),
    url(r'^shield/edit/(?P<shield_id>\d{1,5})$', 'admin.views.shield_edit',name="admin_shield_edit"),
    
    url(r'^secretbook/list/(?P<cur_page>\d{1,5})$', 'admin.views.secretbook_list',name="admin_secretbook_list"),
    url(r'^secretbook/add$', 'admin.views.secretbook_add',name="admin_secretbook_add"),
    url(r'^secretbook/edit/(?P<secretbook_id>\d{1,5})$', 'admin.views.secretbook_edit',name="admin_secretbook_edit"),
    
    url(r'^treasure/list/(?P<cur_page>\d{1,5})$', 'admin.views.treasure_list',name="admin_treasure_list"),
    url(r'^treasure/add$', 'admin.views.treasure_add',name="admin_treasure_add"),
    url(r'^treasure/edit/(?P<treasure_id>\d{1,5})$', 'admin.views.treasure_edit',name="admin_treasure_edit"),
    
    url(r'^activitycard/list/(?P<cur_page>\d{1,5})$', 'admin.views.activitycard_list',name="admin_activitycard_list"),
    url(r'^activitycard/add$', 'admin.views.activitycard_add',name="admin_activitycard_add"),
    url(r'^activitycard/edit/(?P<activitycard_id>\d{1,5})$', 'admin.views.activitycard_edit',name="admin_activitycard_edit"),
    
    url(r'^activity/list/(?P<cur_page>\d{1,5})$', 'admin.views.activity_list',name="admin_activity_list"),
    url(r'^activity/add$', 'admin.views.activity_add',name="admin_activity_add"),
    url(r'^activity/edit/(?P<activity_id>\d{1,5})$', 'admin.views.activity_edit',name="admin_activity_edit"),
    
    url(r'^compose_input_type/list/(?P<cur_page>\d{1,5})$', 'admin.views.compose_input_type_list',name="admin_compose_input_type_list"),
    url(r'^compose_input_type/add$', 'admin.views.compose_input_type_add',name="admin_compose_input_type_add"),
    url(r'^compose_input_type/edit/(?P<compose_input_type_id>\d{1,5})$', 'admin.views.compose_input_type_edit',name="admin_compose_input_type_edit"),
    
    url(r'^treasure_part/list/(?P<cur_page>\d{1,5})$', 'admin.views.treasure_part_list',name="admin_treasure_part_list"),
    url(r'^treasure_part/add$', 'admin.views.treasure_part_add',name="admin_treasure_part_add"),
    url(r'^treasure_part/edit/(?P<treasure_part_id>\d{1,5})$', 'admin.views.treasure_part_edit',name="admin_treasure_part_edit"),

    url(r'^secret_book_part/list/(?P<cur_page>\d{1,5})$', 'admin.views.secret_book_part_list',name="admin_secret_book_part_list"),
    url(r'^secret_book_part/add$', 'admin.views.secret_book_part_add',name="admin_secret_book_part_add"),
    url(r'^secret_book_part/edit/(?P<secret_book_part_id>\d{1,5})$', 'admin.views.secret_book_part_edit',name="admin_secret_book_part_edit"),

    url(r'^activity_part/list/(?P<cur_page>\d{1,5})$', 'admin.views.activity_part_list',name="admin_activity_part_list"),
    url(r'^activity_part/add$', 'admin.views.activity_part_add',name="admin_activity_part_add"),
    url(r'^activity_part/edit/(?P<activity_part_id>\d{1,5})$', 'admin.views.activity_part_edit',name="admin_activity_part_edit"),
    
    url(r'^compose_input_type/list/(?P<cur_page>\d{1,5})$', 'admin.views.compose_input_type_list',name="admin_compose_input_type_list"),
    url(r'^compose_input_type/add$', 'admin.views.compose_input_type_add',name="admin_compose_input_type_add"),
    url(r'^compose_input_type/edit/(?P<compose_input_type_id>\d{1,5})$', 'admin.views.compose_input_type_edit',name="admin_compose_input_type_edit"),
    
    url(r'^compose_input/list/(?P<cur_page>\d{1,5})$', 'admin.views.compose_input_list',name="admin_compose_input_list"),
    url(r'^compose_input/add$', 'admin.views.compose_input_add',name="admin_compose_input_add"),
    url(r'^compose_input/edit/(?P<compose_input_id>\d{1,5})$', 'admin.views.compose_input_edit',name="admin_compose_input_edit"),
    
    url(r'^skill/list/(?P<cur_page>\d{1,5})$', 'admin.views.skill_list',name="admin_skill_list"),
    url(r'^skill/import$', 'admin.views.import_skill',name="admin_skill_import"),
#     url(r'^skill/add$', 'admin.views.skill_add',name="admin_skill_add"),
#     url(r'^skill/edit/(?P<skill_id>\d{1,5})$', 'admin.views.skill_edit',name="admin_skill_edit"),

    url(r'^system_message/list/(?P<cur_page>\d{1,5})$', 'admin.views.system_message_list',name="admin_system_message_list"),
    url(r'^system_message/add$', 'admin.views.system_message_add',name="admin_system_message_add"),
    url(r'^system_message/edit/(?P<system_message_id>\d{1,5})$', 'admin.views.system_message_edit',name="admin_system_message_edit"),

    url(r'^player/list/(?P<cur_page>\d{1,5})$', 'admin.views.player_list',name="admin_player_list"),
    url(r'^player/add$', 'admin.views.player_add',name="admin_player_add"),
    url(r'^player/edit/(?P<player_id>\d{1,5})$', 'admin.views.player_edit',name="admin_player_edit"),
    url(r'^player/search$', 'admin.views.player_search',name="admin_player_search"),
    
    url(r'^fall_cards/update/mission$', 'admin.views.mission_fall_cards_update',name="mission_fall_cards_update"),
    url(r'^fall_cards/update/battle$', 'admin.views.battle_fall_cards_update',name="battle_fall_cards_update"),
    url(r'^fall_cards/update/all$', 'admin.views.fall_cards_update',name="fall_cards_update"),

    url(r'^mall/good/list/(?P<cur_page>\d{1,5})$', 'admin.views.good_list',name="admin_good_list"),
    url(r'^mall/good/add$', 'admin.views.good_add',name="admin_good_add"),
    url(r'^mall/good/edit/(?P<good_id>\d{1,5})$', 'admin.views.good_edit',name="admin_good_edit"),
    
    url(r'^mall/recharge/list/(?P<cur_page>\d{1,5})$', 'admin.views.recharge_list',name="admin_recharge_list"),
    url(r'^mall/recharge/add$', 'admin.views.recharge_add',name="admin_recharge_add"),
    url(r'^mall/recharge/edit/(?P<recharge_id>\d{1,5})$', 'admin.views.recharge_edit',name="admin_recharge_edit"),

    url(r'^mall/order/list/(?P<cur_page>\d{1,5})$', 'admin.views.order_list',name="admin_order_list"),

    url(r'^market/list/(?P<cur_page>\d{1,5})$', 'admin.views.market_list',name="admin_market_list"),
    url(r'^market/add$', 'admin.views.market_add',name="admin_market_add"),
    url(r'^market/edit/(?P<market_id>\d{1,5})$', 'admin.views.market_edit',name="admin_market_edit"),

)
