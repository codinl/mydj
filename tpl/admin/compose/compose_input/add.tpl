{% extends "../../base.tpl" %}

{% block content %}
<div class="pad_10">
	<form action="" method="post" name="myform" id="myform">
	<table width="100%" cellpadding="2" cellspacing="1" class="table_form">
	   	<tr> 
     		<th>类型 :</th>
			<td>
				<select onclick="get_card(this,'card_id')">
					<option value="">请选择</option>
					{% if compose_input_type_list %}
					{% for compose_input_type in compose_input_type_list %}
					<option value="{{compose_input_type.id}}-{{compose_input_type.class_name}}">{{compose_input_type.id}}-{{compose_input_type.class_name}}-{{compose_input_type.name}}</option>
					{% end %}
					{% end %}
				</select>
			</td>
	    </tr>
	    <tr> 
     		<th>卡牌 :</th>
			<td>
				<select name="card_id" id="card_id">
					<option value="">请选择</option>
				</select>
			</td>
	    </tr>
	    <tr> 
	      <th>数量 :</th>
	      <td><input type="text" name="count" class="input-text" value="0"></td>
	    </tr>
	    <tr>
	      <th>is_unlock :</th>
	      <td>
	      	<input type="radio" name="is_unlock" class="radio_style" value="1" checked="checked"> &nbsp;未锁&nbsp;&nbsp;&nbsp;
	      	<input type="radio" name="is_unlock" class="radio_style" value="0"> &nbsp;锁住
	      </td>
	    </tr>
	</table>
	<input type="hidden" name="type_id" id="type_id">
	<input type="submit" name="dosubmit" id="dosubmit" class="dialog" value=" ">
	</form>
</div>
<script type="text/javascript">
function get_card(obj,to_id) {
	var val = $(obj).val();
	var val_arr = val.split('-');
	$('#type_id').val(val_arr[0]);
	var class_name = val_arr[1];
	$.get('{{config.admin_dir}}/card/ajax/list/'+class_name,function(data){
		$('#'+to_id).html(data);
	});
}
</script>
{% end %}