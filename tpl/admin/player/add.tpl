{% extends "../base.tpl" %}

{% block content %}
<div class="pad_10">
	<form action="" method="post" name="myform" id="myform">
	<table width="100%" cellpadding="2" cellspacing="1" class="table_form">
	   	<tr> 
	      <th>ID :</th>
	      <td><input type="text" name="name" class="input-text" value=""></td>
	    </tr>
	   	<tr> 
	      <th>名字 :</th>
	      <td><input type="text" name="name" class="input-text" value=""></td>
	    </tr>
	   	<tr> 
	      <th>体力 :</th>
	      <td><input type="text" name="name" class="input-text" value=""></td>
	    </tr>
	   	<tr> 
	      <th>军令 :</th>
	      <td><input type="text" name="name" class="input-text" value=""></td>
	    </tr>
	   	<tr> 
	      <th>银币 :</th>
	      <td><input type="text" name="name" class="input-text" value=""></td>
	    </tr>	
	   	<tr> 
	      <th>赠送元宝 :</th>
	      <td><input type="text" name="name" class="input-text" value=""></td>
	    </tr>  
	   	<tr> 
	      <th>购买元宝 :</th>
	      <td><input type="text" name="name" class="input-text" value=""></td>
	    </tr>    
	</table>
	<input type="submit" name="dosubmit" id="dosubmit" class="dialog" value=" ">
	</form>
</div>
{% end %}