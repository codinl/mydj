{% extends "../base.tpl" %}

{% block content %}
<div class="pad_10">
	<form action="" method="post" name="myform" id="myform">
	<table width="100%" cellpadding="2" cellspacing="1" class="table_form">
   		<!--<tr>
	      <th>组合类型 :</th>
	      <td>
	      	<input type="radio" name="is_cards_general" class="radio_style" value="1" checked="checked"> &nbsp;武将&nbsp;&nbsp;&nbsp;
	      	<input type="radio" name="is_cards_general" class="radio_style" value="0"> &nbsp;装备
	      </td>
	    </tr>-->
	   	<tr> 
	      <th>名字 :</th>
	      <td><input type="text" name="name" class="input-text"></td>
	    </tr>
	    <!--
	    <tr> 
	      <th>描述 :</th>
	      <td><textarea name="description" rows="2" cols="40"></textarea></td>
	    </tr>
	    -->
     	<tr> 
	      <th>卡牌类型1 :</th>
	      <td>
	      	  <div style="float:left">
		  		  <select name="card_1_type" onclick="get_card(this,'card_1_id')">
					  <option value="">请选择</option>
					  {% if card_type_list %}
					  {% set card_type = card_type_list[0] %}
					  <option value="{{card_type.card_type}}">{{card_type.id}}-{{card_type.card_type}}-{{card_type.name}}</option>
					  {% end %}
		  		  </select>
	  		  </div>
	  		  <div style="float:left">
		  		  &nbsp;卡牌1：
		  		  <select name="card_1_id" id="card_1_id">
					  <option value="">请选择...</option>
		  		  </select>
	  		  </div>
		  </td>
	    </tr>
	    <tr> 
	      <th>卡牌类型2 :</th>
	      <td>
	      	  <div style="float:left">
		  		  <select name="card_2_type" onclick="get_card(this,'card_2_id')">
					  <option value="">请选择</option>
					  {% if card_type_list %}
					  {% for card_type in card_type_list %}
					  <option value="{{card_type.card_type}}">{{card_type.id}}-{{card_type.card_type}}-{{card_type.name}}</option>
					  {% end %}
					  {% end %}
		  		  </select>
	  		  </div>
	  		  <div style="float:left">
		  		  &nbsp;卡牌2：
		  		  <select name="card_2_id" id="card_2_id">
					  <option value="">请选择...</option>
		  		  </select>
	  		  </div>
		  </td>
	    </tr>
	    <tr> 
	      <th>卡牌类型3 :</th>
	      <td>
	      	  <div style="float:left">
		  		  <select onclick="get_card(this,'card_3_id')">
					  <option value="">请选择</option>
					  {% if card_type_list %}
					  {% for card_type in card_type_list %}
					  <option value="{{card_type.card_type}}">{{card_type.id}}-{{card_type.card_type}}-{{card_type.name}}</option>
					  {% end %}
					  {% end %}
		  		  </select>
	  		  </div>
	  		  <div style="float:left">
		  		  &nbsp;卡牌3：
		  		  <select name="card_3_id" id="card_3_id">
					  <option value="">请选择...</option>
		  		  </select>
	  		  </div>
		  </td>
	    </tr>
	    <tr> 
	      <th>卡牌类型4 :</th>
	      <td>
	      	  <div style="float:left">
		  		  <select onclick="get_card(this,'card_4_id')">
					  <option value="">请选择</option>
					  {% if card_type_list %}
					  {% for card_type in card_type_list %}
					  <option value="{{card_type.card_type}}">{{card_type.id}}-{{card_type.card_type}}-{{card_type.name}}</option>
					  {% end %}
					  {% end %}
		  		  </select>
	  		  </div>
	  		  <div style="float:left">
		  		  &nbsp;卡牌4：
		  		  <select name="card_4_id" id="card_4_id">
					  <option value="">请选择...</option>
		  		  </select>
	  		  </div>
		  </td>
	    </tr>
	    <tr> 
	      <th>卡牌类型5 :</th>
	      <td>
	      	  <div style="float:left">
		  		  <select onclick="get_card(this,'card_5_id')">
					  <option value="">请选择</option>
					  {% if card_type_list %}
					  {% for card_type in card_type_list %}
					  <option value="{{card_type.card_type}}">{{card_type.id}}-{{card_type.card_type}}-{{card_type.name}}</option>
					  {% end %}
					  {% end %}
		  		  </select>
	  		  </div>
	  		  <div style="float:left">
		  		  &nbsp;卡牌5：
		  		  <select name="card_5_id" id="card_5_id">
					  <option value="">请选择...</option>
		  		  </select>
	  		  </div>
		  </td>
	    </tr>
	    <tr> 
	      <th>增攻/防比 :</th>
	      <td><input type="text" name="add_value_percent" class="input-text" value="0"></td>
	    </tr>
   	    <tr>
	      <th>is_unlock :</th>
	      <td>
	      	<input type="radio" name="is_unlock" class="radio_style" value="1" checked="checked"> &nbsp;未锁&nbsp;&nbsp;&nbsp;
	      	<input type="radio" name="is_unlock" class="radio_style" value="0"> &nbsp;锁住
	      </td>
	    </tr>
	</table>
	<input type="submit" name="dosubmit" id="dosubmit" class="dialog" value=" ">
	</form>
</div>

<script type="text/javascript">
function get_general(obj,to_id) {
	var group_id = $(obj).val();
	$.get('{{config.admin_dir}}/general/ajax/list/group/'+group_id,function(data){
		$('#'+to_id).html(data);
	});
}
function get_card(obj,to_id) {
	var card_type = $(obj).val();
	$.get('{{config.admin_dir}}/card/ajax/list/'+card_type,function(data){
		$('#'+to_id).html(data);
	});
}
</script>
{% end %}