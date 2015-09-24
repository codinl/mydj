{% extends "../../base.tpl" %}

{% block content %}
<div class="pad_10">
	<form action="" method="post" name="myform" id="myform">
	<table width="100%" cellpadding="2" cellspacing="1" class="table_form">
	   	<tr> 
	      <th>level :</th>
	      <td><input type="text" name="level" class="input-text" value="{{config_level.level}}"></td>
	    </tr>
	    <tr> 
	      <th>update_need_xp :</th>
	      <td><input type="text" name="update_need_xp" class="input-text" value="{{config_level.update_need_xp}}"></td>
	    </tr>
	    <tr> 
	      <th>max_ep :</th>
	      <td><input type="text" name="max_ep" class="input-text" value="{{config_level.max_ep}}"></td>
	    </tr>
	    <tr> 
	      <th>max_sp :</th>
	      <td><input type="text" name="max_sp" class="input-text" value="{{config_level.max_sp}}"></td>
	    </tr>
   	    <tr> 
	      <th>base_slot_count :</th>
	      <td><input type="text" name="base_slot_count" class="input-text" value="{{config_level.base_slot_count}}"></td>
	    </tr>
	</table>
	<input type="submit" name="dosubmit" id="dosubmit" class="dialog" value=" ">
	</form>
</div>
{% end %}