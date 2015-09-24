{% extends "../base.tpl" %}

{% block content %}
<div class="pad_10">
	<form action="" method="post" name="myform" id="myform">
	<table width="100%" cellpadding="2" cellspacing="1" class="table_form">
	   	<tr> 
	      <th>标题 :</th>
	      <td><input type="text" name="title" class="input-text"></td>
	    </tr>
	    <tr> 
	      <th>内容 :</th>
	      <td><textarea name="content" rows="3" cols="50"></textarea></td>
	    </tr>
	    <tr>
	      <th>类型 :</th>
	      <td>
	      	<input type="radio" name="type" class="radio_style" value="0" checked="checked"> &nbsp;通知&nbsp;&nbsp;&nbsp;
	      	<input type="radio" name="type" class="radio_style" value="1"> &nbsp;维护
	      </td>
	    </tr>
   	    <tr>
	      <th>状态 :</th>
	      <td>
	      	<input type="radio" name="status" class="radio_style" value="0"> &nbsp;未发布&nbsp;&nbsp;&nbsp;
 		    <input type="radio" name="status" class="radio_style" value="1" checked="checked"> &nbsp;已发布&nbsp;&nbsp;&nbsp;
	      	<input type="radio" name="status" class="radio_style" value="2"> &nbsp;已过期
	      </td>
	    </tr>
	</table>
	<input type="submit" name="dosubmit" id="dosubmit" class="dialog" value=" ">
	</form>
</div>
{% end %}