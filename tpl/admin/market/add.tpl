{% extends "../base.tpl" %}

{% block content %}
<div class="pad_10">
	<form action="" method="post" name="myform" id="myform" enctype="multipart/form-data">
	<table width="100%" cellpadding="2" cellspacing="1" class="table_form">
	   	<tr> 
	      <th>英文名字 :</th>
	      <td><input type="text" name="e_name" class="input-text"></td>
	    </tr>
	   	<tr> 
	      <th>名字 :</th>
	      <td><input type="text" name="name" class="input-text"></td>
	    </tr>
	    <tr> 
	      <th>描述 :</th>
	      <td><textarea name="description" rows="2" cols="40"></textarea></td>
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