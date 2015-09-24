{% extends "../../base.tpl" %}

{% block content %}
<div class="pad_10">
	<form action="" method="post" name="myform" id="myform">
	<table width="100%" cellpadding="2" cellspacing="1" class="table_form">
		<tr> 
	      <th width="80">名字 :</th>
	      <td><input type="text" name="name" class="input-text"></td>
	    </tr>
        <tr>
			<th>所属剧情 :</th>
			<td>
                <select name="scenario_id" id="scenario_id">
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
	      <th>序号 :</th>
	      <td>
	      	<select name="order">
	      		<option value="1">1</option>
				{% for i in range(1,10) %}
				<option value="{{i}}">{{i}}</option>
				{% end %}
			</select>
		  </td>
	    </tr>
	    <tr>
	      <th>剧组最后:</th>
	      <td>
	      	<input type="radio" name="is_scenario_last" class="radio_style" value="1" checked="checked"> &nbsp;是&nbsp;&nbsp;&nbsp;
	      	<input type="radio" name="is_scenario_last" class="radio_style" value="0"> &nbsp;否
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
{% end %}