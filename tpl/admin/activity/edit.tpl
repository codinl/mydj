{% extends "../base.tpl" %}

{% block head_css %}
<link href="/statics/admin/css/jquery-ui.css" rel="stylesheet" type="text/css" />
{% end %}

{% block base_js %}
<script language="javascript" type="text/javascript" src="/statics/admin/js/jquery/jquery-1.8.3.js"></script>
{% end %}

{% block head_js %}
<script language="javascript" type="text/javascript" src="/statics/admin/js/jquery/plugins/jquery-ui.js"></script>
{% end %}

{% block content %}

<style>
th{width:80px;}
</style>

<div class="pad_10">
	<form action="" method="post" name="myform" id="myform">
	<table width="100%" cellpadding="2" cellspacing="1" class="table_form">
	   	<tr> 
	      <th>名字 :</th>
	      <td><input type="text" name="name" value="{{activity.name}}" class="input-text"></td>
	    </tr>
     	<tr> 
	      <th>碎片类型1 :</th>
	      <td>
	      	  <div style="float:left">
		  		  <select name="input_type_1" onclick="get_card(this,'input_1_id')">
					  <option value="">请选择</option>
					  {% if compose_input_type_list %}
					  {% for compose_input_type in compose_input_type_list %}
					  <option value="{{compose_input_type.class_name}}">{{compose_input_type.id}}-{{compose_input_type.class_name}}-{{compose_input_type.name}}</option>
					  {% end %}
					  {% end %}
		  		  </select>
	  		  </div>
	  		  <div style="float:left">
		  		  &nbsp;输入碎片1：
		  		  <select name="input_1_id" id="input_1_id">
					  <option value="">请选择...</option>
		  		  </select>
	  		  </div>
	  		  <div style="float:left">
		  		  &nbsp;数量：
		  		  <input type="text" name="input_count_1" class="input-text" value="0" style="width:50px;">
	  		  </div>
		  </td>
	    </tr>   	    
	    <tr> 
	      <th>碎片类型2 :</th>
	      <td>
	      	  <div style="float:left">
		  		  <select name="input_type_1" onclick="get_card(this,'input_2_id')">
					  <option value="">请选择</option>
					  {% if compose_input_type_list %}
					  {% for compose_input_type in compose_input_type_list %}
					  <option value="{{compose_input_type.class_name}}">{{compose_input_type.id}}-{{compose_input_type.class_name}}-{{compose_input_type.name}}</option>
					  {% end %}
					  {% end %}
		  		  </select>
	  		  </div>
	  		  <div style="float:left">
		  		  &nbsp;输入碎片2：
		  		  <select name="input_2_id" id="input_2_id">
					  <option value="">请选择...</option>
		  		  </select>
	  		  </div>
	  		  <div style="float:left">
		  		  &nbsp;数量：
		  		  <input type="text" name="input_count_2" class="input-text" value="0" style="width:50px;">
	  		  </div>
		  </td>
	    </tr>
   	    <tr> 
	      <th>碎片类型3 :</th>
	      <td>
	      	  <div style="float:left">
		  		  <select name="input_type_1" onclick="get_card(this,'input_3_id')">
					  <option value="">请选择</option>
					  {% if compose_input_type_list %}
					  {% for compose_input_type in compose_input_type_list %}
					  <option value="{{compose_input_type.class_name}}">{{compose_input_type.id}}-{{compose_input_type.class_name}}-{{compose_input_type.name}}</option>
					  {% end %}
					  {% end %}
		  		  </select>
	  		  </div>
	  		  <div style="float:left">
		  		  &nbsp;输入碎片3：
		  		  <select name="input_3_id" id="input_3_id">
					  <option value="">请选择...</option>
		  		  </select>
	  		  </div>
	  		  <div style="float:left">
		  		  &nbsp;数量：
		  		  <input type="text" name="input_count_3" class="input-text" value="0" style="width:50px;">
	  		  </div>
		  </td>
	    </tr>
	    <br/>
    	<tr> 
	      <th>输出类型 :</th>
	      <td>
	  		  <select name="output_type_1" id="output_type_1" onclick="get_card(this,'output_id')">
				  <option value="0">请选择</option>
				  {% if card_type_list %}
				  {% for card_type in card_type_list %}
				  <option value="{{card_type.class_name}}">{{card_type.id}}-{{card_type.class_name}}-{{card_type.name}}</option>
				  {% end %}
				  {% end %}
	  		  </select>
	  		  <!--  
	  		  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;输出星级：
	  		  <select name="output_rarity" id="output_rarity">
				  <option value="4">4</option>
				  <option value="5">5</option>
	  		  </select>
	  		  -->
	  		  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;输出：
	  		  <select name="output_id" id="output_id">
				  <option value="0">请选择...</option>
	  		  </select>
		  </td>
	    </tr>
  	    <tr> 
	      <th>描述 :</th>
	      <td><textarea name="description" rows="3" cols="50">{{activity.description}}</textarea></td>
	    </tr>
		<tr> 
	      <th>开始时间 :</th>
	      <td><input type="text" name="start_time" value="{{activity.start_time}}" class="input-text" id="start_time"></td>
	    </tr>
	    <tr> 
	      <th>结束时间 :</th>
	      <td><input type="text" name="end_time" value="{{activity.end_time}}" class="input-text" id="end_time"></td>
	    </tr>
	    <tr> 
	      <th>合成概率 :</th>
	      <td><input type="text" name="property" value="{{activity.property}}" class="input-text"  style="width:30px;"></td>
	    </tr>
	    <tr> 
	      <th>最多次数 :</th>
	      <td><input type="text" name="success_max" value="{{activity.success_max}}" class="input-text" style="width:30px;"></td>
	    </tr>
   		<tr>
			<th>状态 :</th>
			<td>
				<select name="status">
					{% if activity.status == 1 %}
					<option value="1">1-进行中</option>
					{% elif activity.status == 0%}
					<option value="0">0-未开始</option>
					{% elif activity.status == 2%}
					<option value="2">2-已过期</option>
					{% end %}
					<option value="1">1-进行中</option>
					<option value="0">0-未开始</option>
					<option value="2">2-已过期</option>
				</select>
			</td>
		</tr>
	</table>
	<input type="submit" name="dosubmit" id="dosubmit" class="dialog" value=" ">
	</form>
</div>

<script type="text/javascript">
/*
$(function() {
	$( "#start_time" ).datepicker();
    $( "#start_time" ).datepicker("option", "dateFormat","yy-mm-dd");
    $( "#end_time" ).datepicker();
    $( "#end_time" ).datepicker("option", "dateFormat","yy-mm-dd");
});*/

function get_card(obj,to_id) {
	var class_name = $(obj).val();
	$.get('{{config.admin_dir}}/card/ajax/list/'+class_name,function(data){
		$('#'+to_id).html(data);
	});
}
</script>
{% end %}