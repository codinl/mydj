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
	      <th>星级 :</th>
	      <td>
	      	<select name="rarity">
				{% for i in range(1,6) %}
				<option value="{{i}}">{{i}}</option>
				{% end %}
			</select>
		  </td>
	    </tr>
   	    <tr> 
	      <th>级别 :</th>
	      <td><input type="text" name="level" class="input-text" value="1"></td>
	    </tr>
   		<tr>
			<th>所属阵营 :</th>
			<td>
				<select name="group_id">
					<option value="">请选择</option>
					{% if group_list %}
					{% for group in group_list %}
					<option value="{{group.id}}">{{group.id}}-{{group.name}}</option>
					{% end %}
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
			<th>是否为攻击型 :</th>
			<td>
				<select name="is_add_attack">
					<option value="1">是</option>
					<option value="0">否</option>
				</select>
			</td>
		</tr>
	    <tr> 
	      <th>攻击 :</th>
	      <td><input type="text" name="attack" class="input-text"></td>
	    </tr>
	    <tr> 
	      <th>防御 :</th>
	      <td><input type="text" name="defence" class="input-text"></td>
	    </tr>
	    <tr> 
	      <th>转生限次 :</th>
	      <td><input type="text" name="rebirth_max" class="input-text"></td>
	    </tr>
   	    <tr>
	      <th>是否初选 :</th>
	      <td>
	      	<input type="radio" name="is_for_init" class="radio_style" value="1"> &nbsp;是&nbsp;&nbsp;&nbsp;
	      	<input type="radio" name="is_for_init" class="radio_style" value="0" checked="checked"> &nbsp;否
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