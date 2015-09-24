{% extends "../../base.tpl" %}

{% block content %}
<div class="pad_10">
	<form action="" method="post" name="myform" id="myform">
	<table width="100%" cellpadding="2" cellspacing="1" class="table_form">
	   	<tr> 
	      <th>name :</th>
	      <td><input type="text" name="name" class="input-text" value="{{cardtype.name}}"></td>
	    </tr>
	    <tr> 
	      <th>card_type :</th>
	      <td><input type="text" name="card_type" class="input-text" value="{{cardtype.card_type}}"></td>
	    </tr>
	    <tr>
	      <th>is_unlock :</th>
	      <td>
	      	<input type="radio" name="is_unlock" class="radio_style" value="1" {% if cardtype.is_unlock %} checked="checked" {% end %}> &nbsp;未锁&nbsp;&nbsp;&nbsp;
	      	<input type="radio" name="is_unlock" class="radio_style" value="0" {% if not cardtype.is_unlock %} checked="checked" {% end %}> &nbsp;锁住
	      </td>
	    </tr>
	</table>
	<input type="submit" name="dosubmit" id="dosubmit" class="dialog" value=" ">
	</form>
</div>
{% end %}