{% extends "../../base.tpl" %}

{% block content %}
<div class="pad_10">
	<form action="" method="post" name="myform" id="myform">
	<table width="100%" cellpadding="2" cellspacing="1" class="table_form">
		<!--<tr> 
	      <th width="80">名字 :</th>
	      <td><input type="text" name="name" class="input-text"></td>
	    </tr>-->
	    <tr> 
	      <th>描述 :</th>
	      <td><textarea name="description" rows="2" cols="40"></textarea></td>
	    </tr>
        <tr>
			<th>所属剧情 :</th>
			<td>
                <select name="scenario_id" onclick="get_mission_group(this,'mission_group_id');" id="scenario_id">
	                <option value="">--请选择--</option>
	                {% if scenario_list %}
	                {% for s in scenario_list %}
	                <option value="{{s.id}}">{{s.id}}-{{s.name}}</option>
	                {% end %}
	                {% end %}
                </select>
            </td>
	    </tr>
        <tr>
			<th>所属任务组 :</th>
			<td>
                <select name="mission_group_id" id="mission_group_id">
                	<option value="">--请选择--</option>
                </select>
            </td>
	    </tr>
   		<tr>
	      <th>是否关卡 :</th>
	      <td>
	      	<input type="radio" name="is_group_last" class="radio_style" value="1"> &nbsp;是&nbsp;&nbsp;&nbsp;
	      	<input type="radio" name="is_group_last" class="radio_style" value="0" checked="checked"> &nbsp;否
	      </td>
	    </tr>
	    <tr> 
	      <th>序号 :</th>
	      <td>
	      	<select name="order">
	      		<option value="1">1</option>
				{% for i in range(1,6) %}
				<option value="{{i}}">{{i}}</option>
				{% end %}
			</select>
		  </td>
	    </tr>
	   	<tr> 
	      <th>ep :</th>
	      <td><input type="text" name="ep" class="input-text" value="5"></td>
	    </tr>
	    <!--
	    <tr> 
	      <th>vm :</th>
	      <td><input type="text" name="vm" class="input-text"></td>
	    </tr>
	    <tr> 
	      <th>xp :</th>
	      <td><input type="text" name="xp" class="input-text"></td>
	    </tr>
	    <tr> 
	      <th>sum_count :</th>
	      <td><input type="text" name="sum_count" class="input-text" value="10"></td>
	    </tr>-->
	    <tr> 
	      <th>level :</th>
	      <td>
	      	<select name="level">
	      		<option value="1">1</option>
				{% for i in range(1,10) %}
				<option value="{{i}}">{{i}}</option>
				{% end %}
			</select>
		  </td>
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
function get_mission_group(obj,to_id) {
	var scenario_id = $(obj).val();
	$('#scenario_id').val(scenario_id);
	$('#cid').html( '<option value=\"\">--请选择--</option>');
	$.get('{{config.admin_dir}}/mission_group/ajax/get_list/'+scenario_id,function(data){
	$('#'+to_id).html(data);
	});
}
</script>
{% end %}