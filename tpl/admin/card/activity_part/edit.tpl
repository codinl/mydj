{% extends "../../base.tpl" %}

{% block content %}
<div class="pad_10">
	<form action="" method="post" name="myform" id="myform">
	<table width="100%" cellpadding="2" cellspacing="1" class="table_form">
	   	<tr> 
	      <th>名字 :</th>
	      <td><input type="text" name="name" class="input-text" value="{{activity_part.name}}"></td>
	    </tr>
	    <tr> 
	      <th>描述 :</th>
	      <td><textarea name="description" rows="2" cols="40">{{activity_part.description}}</textarea></td>
	    </tr>
   		<tr>
			<th>所属活动 :</th>
			<td>
				<select name="activity_id">
					<option value="">请选择</option>
					{% if activity_list %}
					{% for activity in activity_list %}
					<option value="{{activity.id}}">{{activity.id}}-{{activity.name}}</option>
					{% end %}
					{% end %}
				</select>
			</td>
		</tr>
		<th>图片 :</th>
	    	<td>
	    		<img id="img_show" src="/statics/game/{{activity_part.get_image()}}"><br>
	    		<input type="file" name="image_file" id="image_file" class="input-text" size="21" onchange="set_image_val(this);"/>
	    		<input type="hidden" name="image" id="image" />
	    	</td>
	    </tr>
   	    <tr>
	      <th>is_unlock :</th>
	      <td>
	      	<input type="radio" name="is_unlock" class="radio_style" value="1" {%if activity_part.is_unlock %} checked="checked" {% end %}> &nbsp;未锁&nbsp;&nbsp;&nbsp;
	      	<input type="radio" name="is_unlock" class="radio_style" value="0" {%if not activity_part.is_unlock %} checked="checked" {% end %}> &nbsp;锁住
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