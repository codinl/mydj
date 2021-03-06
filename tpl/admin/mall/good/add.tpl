{% extends "../../base.tpl" %}

{% block content %}
<div class="pad_10">
	<form action="" method="post" name="myform" id="myform" enctype="multipart/form-data">
	<table width="100%" cellpadding="2" cellspacing="1" class="table_form">
	   	<tr> 
	      <th>名字 :</th>
	      <td><input type="text" name="name" class="input-text"></td>
	    </tr>
	   	<tr> 
	      <th>type_id:</th>
	      <td>
  		    <select name="type_id">
				{% for i in range(1,12) %}
				<option value="{{i}}">{{i}}</option>
				{% end %}
			</select>
	      </td>
	    </tr>
	    <tr> 
	      <th>描述 :</th>
	      <td><textarea name="description" rows="2" cols="40"></textarea></td>
	    </tr>
  	    <tr>
	    	<th>图片 :</th>
	    	<td>
	    		<img id="img_show" src=""><br>
	    		<input type="file" name="image_file" id="image_file" class="input-text" size="21" onchange="set_image_val(this);"/>
	    		<input type="hidden" name="image" id="image" />
	    	</td>
	    </tr>
	   	<tr> 
	      <th>售价银币 :</th>
	      <td><input type="text" name="vm" value="0" class="input-text"></td>
	    </tr>
	   	<tr> 
	      <th>售价元宝 :</th>
	      <td><input type="text" name="rm" value="0" class="input-text"></td>
	    </tr>
	   	<tr> 
	      <th>折扣 :</th>
	      <td><input type="text" name="discount" value="100" class="input-text"></td>
	    </tr>
   	    <tr>
	      <th>is_new :</th>
	      <td>
	      	<input type="radio" name="is_new" class="radio_style" value="1"> &nbsp;是&nbsp;&nbsp;&nbsp;
	      	<input type="radio" name="is_new" class="radio_style" value="0" checked="checked"> &nbsp;否
	      </td>
	    </tr>
   	    <tr>
	      <th>is_hot :</th>
	      <td>
	      	<input type="radio" name="is_hot" class="radio_style" value="1"> &nbsp;是&nbsp;&nbsp;&nbsp;
	      	<input type="radio" name="is_hot" class="radio_style" value="0" checked="checked"> &nbsp;否
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
function set_image_val(obj){
	url = $(obj).val();
	start = url.lastIndexOf("\\");
	start = start > 0 ? start : url.lastIndexOf("/"); 
	image_name = url.substring(start+1);
	$('#image').val(image_name);	
}
</script>
{% end %}