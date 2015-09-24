{% extends "../base.tpl" %}

{% block content %}
<div class="pad_10">
	<form action="" method="post" name="myform" id="myform">
	<table width="100%" cellpadding="2" cellspacing="1" class="table_form">
	   	<tr> 
	      <th>名字 :</th>
	      <td><input type="text" name="name" class="input-text" value="{{skill.name}}"></td>
	    </tr>
     	<tr> 
	      <th>卡牌类型1 :</th>
	      <td>
	      	  <div style="float:left">
		  		  <select onclick="get_card(this,'card_1_id')">
					  <option value="">请选择</option>
					  {% if card_type_list %}
					  {% for card_type in card_type_list %}
					  <option value="{{card_type.card_type}}">{{card_type.id}}-{{card_type.card_type}}-{{card_type.name}}</option>
					  {% end %}
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
		  		  &nbsp;卡牌1：
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
		  		  &nbsp;卡牌1：
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
		  		  &nbsp;卡牌1：
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
		  		  &nbsp;卡牌1：
		  		  <select name="card_5_id" id="card_5_id">
					  <option value="">请选择...</option>
		  		  </select>
	  		  </div>
		  </td>
	    </tr>
    	<tr> 
	      <th>增攻/防比 :</th>
	      <td><input type="text" name="add_value_percent" class="input-text" value="{{skill.add_value_percent}}"></td>
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