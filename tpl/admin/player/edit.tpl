{% extends "../base.tpl" %}

{% block content %}
<div class="pad_10">
	<form action="" method="post" name="myform" id="myform">
	<table width="100%" cellpadding="2" cellspacing="1" class="table_form">
	   	<tr> 
	      <th>ID :</th>
	      <td><input type="text" name="id" class="input-text" value="{{player.id}}"></td>
	    </tr>
	   	<tr> 
	      <th>名字 :</th>
	      <td><input type="text" name="name" class="input-text" value="{{player.name}}"></td>
	    </tr>
	   	<tr> 
	      <th>级别 :</th>
	      <td><input type="text" name="level" class="input-text" value="{{player.level}}"></td>
	    </tr>
	   	<tr> 
	      <th>体力 :</th>
	      <td><input type="text" name="ep" class="input-text" value="{{player.ep}}"></td>
	    </tr>
	   	<tr> 
	      <th>军令 :</th>
	      <td><input type="text" name="sp" class="input-text" value="{{player.sp}}"></td>
	    </tr>
	   	<tr> 
	      <th>银币 :</th>
	      <td><input type="text" name="vm" class="input-text" value="{{player.vm}}"></td>
	    </tr>	
	   	<tr> 
	      <th>赠送元宝 :</th>
	      <td><input type="text" name="grm" class="input-text" value="{{player.grm}}"></td>
	    </tr>  
	   	<tr> 
	      <th>购买元宝 :</th>
	      <td><input type="text" name="brm" class="input-text" value="{{player.brm}}"></td>
	    </tr>    
	</table>
	<input type="submit" name="dosubmit" id="dosubmit" class="dialog" value=" ">
	</form>
</div>
{% end %}