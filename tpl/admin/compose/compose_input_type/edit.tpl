{% extends "../../base.tpl" %}

{% block content %}
<div class="pad_10">
	<form action="" method="post" name="myform" id="myform">
	<table width="100%" cellpadding="2" cellspacing="1" class="table_form">
	   	<tr> 
	      <th>名字 :</th>
	      <td><input type="text" name="name" class="input-text" value="{{compose_input_type.name}}"></td>
	    </tr>
	    <tr> 
	      <th>class_name :</th>
	      <td><input type="text" name="class_name" class="input-text" value="{{compose_input_type.class_name}}"></td>
	    </tr>
	    <tr>
	      <th>is_unlock :</th>
	      <td>
	      	<input type="radio" name="is_unlock" class="radio_style" value="1" {% if compose_input_type.is_unlock %}checked="checked" {% end %}> &nbsp;未锁&nbsp;&nbsp;&nbsp;
	      	<input type="radio" name="is_unlock" class="radio_style" value="0" {% if not compose_input_type.is_unlock %}checked="checked" {% end %}> &nbsp;锁住
	      </td>
	    </tr>
	</table>
	<input type="submit" name="dosubmit" id="dosubmit" class="dialog" value=" ">
	</form>
</div>
{% end %}