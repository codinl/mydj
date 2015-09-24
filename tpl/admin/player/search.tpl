{% extends "../base.tpl" %}

{% block content %}
<div class="pad_10">
	<form action="" method="post" name="myform" id="myform">
		<table width="100%" cellpadding="2" cellspacing="1" class="table_form">
			<tr></tr> 
		   	<tr> 
		      <th>角色名 :</th>
		      <td>
		      	<input type="text" name="player_name" class="input-text" value="">
		      	<input type="submit" value="搜索" style="font-size:14px;padding:3px 5px;">
		      </td>
		    </tr>
		</table>
	</form>
</div>
{% end %}