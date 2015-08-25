# -*- coding: utf-8 -*-

from django import forms

class NodeForm(forms.Form):
    id = forms.IntegerField(label=(u"id"),widget=forms.HiddenInput(),required=False)
    url = forms.CharField(label=(u"url"), max_length=30, widget=forms.TextInput(attrs={'size': 30, }))  
    name = forms.CharField(label=(u""), max_length=30, widget=forms.TextInput(attrs={'size': 30, }))  
    level = forms.IntegerField(label=(u""),widget=forms.Select())
    parent = forms.IntegerField(label=(u""), widget=forms.Select(),required=False)
    is_show = forms.IntegerField(label=(u""), widget=forms.RadioSelect())
    sort = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size': 20, }))
    descr = forms.CharField(label=(u""), max_length=255, widget=forms.TextInput(attrs={'size': 255, }))

class ScenarioForm(forms.Form):
    name = forms.CharField(label=(u""), max_length=30, widget=forms.TextInput(attrs={'size': 30, }))  
    order = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    is_unlock = forms.IntegerField(label=(u"is_unlock"), widget=forms.RadioSelect())
    
class MissionGroupForm(forms.Form):
    name = forms.CharField(label=(u""), max_length=30, widget=forms.TextInput(attrs={'size': 30, }))  
    order = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    is_unlock = forms.IntegerField(label=(u"is_unlock"), widget=forms.RadioSelect())
    scenario_id = forms.IntegerField(label=(u""), widget=forms.Select())
    order = forms.IntegerField(label=(u""), widget=forms.Select())
    is_scenario_last = forms.IntegerField(label=(u"is_unlock"), widget=forms.RadioSelect())
    
class MissionForm(forms.Form):
#     name = forms.CharField(label=(u""), max_length=30, widget=forms.TextInput(attrs={'size': 30, }))  
    ep = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
#     vm = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
#     xp = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    description = forms.CharField(max_length=100,widget=forms.Textarea(),required=False)
#     sum_count = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    is_unlock = forms.IntegerField(label=(u"is_unlock"), widget=forms.RadioSelect())
    scenario_id = forms.IntegerField(label=(u""), widget=forms.Select())
    mission_group_id = forms.IntegerField(label=(u""), widget=forms.Select())
    order = forms.IntegerField(label=(u""), widget=forms.Select())
    level = forms.IntegerField(label=(u""), widget=forms.Select())
    is_group_last = forms.IntegerField(label=(u"is_unlock"), widget=forms.RadioSelect())

class ConfigLevelForm(forms.Form):
    level = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    update_need_xp = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    max_ep = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    max_sp = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    base_slot_count = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))

class ActivityForm(forms.Form):
    name = forms.CharField(label=(u""), max_length=30, widget=forms.TextInput(attrs={'size': 30, }))  
    description = forms.CharField(max_length=100,widget=forms.Textarea(),required=False)
    start_time = forms.DateTimeField()
    end_time = forms.DateTimeField()
    status = forms.IntegerField(label=(u""), widget=forms.Select())
    input_1_id = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }),required=False)
    input_2_id = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }),required=False)
    input_3_id = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }),required=False)
    input_count_1 = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }),required=False)
    input_count_2 = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }),required=False)
    input_count_3 = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }),required=False)
    output_id = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    property = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':5, }))
    success_max = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':5, }))

class GroupForm(forms.Form):
    name = forms.CharField(label=(u""), max_length=30, widget=forms.TextInput(attrs={'size': 30, }))  
    description = forms.CharField(max_length=100,widget=forms.Textarea(),required=False)

class CardTypeForm(forms.Form):
    name = forms.CharField(label=(u""), max_length=30, widget=forms.TextInput(attrs={'size': 30, }))  
    card_type = forms.CharField(max_length=100,widget=forms.TextInput(),required=False)
    is_unlock = forms.IntegerField(label=(u""), widget=forms.RadioSelect()) 

class CardForm(forms.Form):
    name = forms.CharField(label=(u""), max_length=30, widget=forms.TextInput(attrs={'size': 30, }))  
    rarity = forms.IntegerField(label=(u""), widget=forms.Select())
    description = forms.CharField(max_length=100,widget=forms.Textarea())
    level = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }),required=False)
#     level_max = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }),required=False)
    rebirth_max = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }),required=False)
    image = forms.CharField(max_length=100,widget=forms.HiddenInput(),required=False)
#    image_file = forms.FileField(required=False)
    is_unlock = forms.IntegerField(label=(u""), widget=forms.RadioSelect()) 
    
class GeneralForm(CardForm):
    group_id = forms.IntegerField(label=(u""), widget=forms.Select())
    attack = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    defence = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    is_add_attack = forms.IntegerField(label=(u""),widget=forms.Select())
    is_for_init = forms.IntegerField(label=(u""), widget=forms.RadioSelect()) 
#    skills = forms.CharField(max_length=100,widget=forms.Textarea(),required=False)

class WeaponForm(CardForm):
    attack = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    
class ShieldForm(CardForm):
    defence = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    
class SecretBookForm(CardForm):
#     add_value_percent = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    attack_add_percent = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    defence_add_percent = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    
class TreasureForm(CardForm):
#     probability = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    crit = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    block = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))

class CardPartForm(forms.Form):
    name = forms.CharField(label=(u""), max_length=30, widget=forms.TextInput(attrs={'size': 30, }))  
    rarity = forms.IntegerField(label=(u""), widget=forms.Select())
    description = forms.CharField(max_length=100,widget=forms.Textarea())
    image = forms.CharField(max_length=100,widget=forms.HiddenInput(),required=False)
    is_unlock = forms.IntegerField(label=(u""), widget=forms.RadioSelect()) 
        
class ActivityCardForm(CardPartForm):
    activity_id = forms.IntegerField(label=(u""), widget=forms.Select())
    
class TreasurePartForm(CardPartForm):
    t_card_id = forms.IntegerField(label=(u""), widget=forms.Select())
    
class SecretBookPartForm(CardPartForm):
    t_card_id = forms.IntegerField(label=(u""), widget=forms.Select())
    
class ComposeInputForm(forms.Form):
    type_id = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    count = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    card_id = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    is_unlock = forms.IntegerField(label=(u""), widget=forms.RadioSelect())
 
class ComposeInputTypeForm(forms.Form):
    name = forms.CharField(label=(u""), max_length=30, widget=forms.TextInput(attrs={'size': 30, }))  
    class_name = forms.CharField(label=(u""), max_length=30, widget=forms.TextInput(attrs={'size': 30, }),required=False)  
    is_unlock = forms.IntegerField(label=(u""), widget=forms.RadioSelect())
    
class SkillForm(forms.Form):
    name = forms.CharField(label=(u""), max_length=30, widget=forms.TextInput(attrs={'size': 30, }))  
#     description = forms.CharField(max_length=100,widget=forms.Textarea(),required=False)
#     is_cards_general = forms.IntegerField(label=(u""), widget=forms.RadioSelect())
    general_id = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }),required=False)
    card_1_id = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }),required=False)
    card_2_id = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }),required=False)
    card_3_id = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }),required=False)
    card_4_id = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }),required=False)
    card_5_id = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }),required=False)
    
    card_2_type = forms.CharField(label=(u""),widget=forms.Select(),required=False)
    
    add_value_percent = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }),required=False)
#     defence_add_percent = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }),required=False)
    is_unlock = forms.IntegerField(label=(u""), widget=forms.RadioSelect())
    
    
class SystemMessageForm(forms.Form):
    title = forms.CharField(label=(u""), max_length=50, widget=forms.TextInput(attrs={'size': 50, }))  
    content = forms.CharField(max_length=200,widget=forms.Textarea())
    type = forms.IntegerField(label=(u""), widget=forms.RadioSelect())
    status = forms.IntegerField(label=(u""), widget=forms.RadioSelect())
    
class PlayerForm(forms.Form):
    name = forms.CharField(label=(u""), max_length=50, widget=forms.TextInput(attrs={'size': 50, }))  
    level = forms.IntegerField(label=(u""), widget=forms.TextInput(attrs={'size':10, }))
    ep = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    sp = forms.IntegerField(label=(u""), widget=forms.TextInput(attrs={'size':10, }))
    vm = forms.IntegerField(label=(u""), widget=forms.TextInput(attrs={'size':10, }))
    grm = forms.IntegerField(label=(u""), widget=forms.TextInput(attrs={'size':10, }))
    brm = forms.IntegerField(label=(u""), widget=forms.TextInput(attrs={'size':10, }))
    
class GoodForm(forms.Form):
    name = forms.CharField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    type_id = forms.IntegerField(label=(u""), widget=forms.Select())
    vm = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    rm = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    discount = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    description = forms.CharField(max_length=100,widget=forms.Textarea(),required=False)
    is_unlock = forms.IntegerField(label=(u""), widget=forms.RadioSelect())
    is_new = forms.IntegerField(label=(u""), widget=forms.RadioSelect())
    is_hot = forms.IntegerField(label=(u""), widget=forms.RadioSelect())
    image = forms.CharField(max_length=100,widget=forms.HiddenInput(),required=False)

class RechargeForm(forms.Form):
    name = forms.CharField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    money = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    rm = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    discount = forms.IntegerField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    description = forms.CharField(max_length=100,widget=forms.Textarea(),required=False)
#     status = forms.IntegerField(label=(u""), widget=forms.Select())
#     type_id = forms.IntegerField(label=(u""), widget=forms.Select())

class MarketForm(forms.Form):
    e_name = forms.CharField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    name = forms.CharField(label=(u""),widget=forms.TextInput(attrs={'size':10, }))
    description = forms.CharField(max_length=100,widget=forms.Textarea(),required=False)

class UploadFileForm(forms.Form):   
    import_file = forms.FileField()
    
    
    
    
    
    
    
     

    