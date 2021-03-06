{% extends "../../base.tpl" %}

{% block content %}
<div class="pad_10">
	<form action="" method="post" name="myform" id="myform">
	<table width="100%" cellpadding="2" cellspacing="1" class="table_form">
	   	<tr> 
	      <th>名字 :</th>
	      <td><input type="text" name="name" class="input-text" value="{{treasure.name}}"></td>
	    </tr>
   	   	<tr> 
	      <th>星级 :</th>
	      <td>
	      	<select name="rarity">
	      		<option value="{{treasure.rarity}}">{{treasure.rarity}}</option>
				{% for i in range(1,6) %}
				<option value="{{i}}">{{i}}</option>
				{% end %}
			</select>
		  </td>
	    </tr>
	    <tr> 
	      <th>描述 :</th>
	      <td><textarea name="description" rows="2" cols="40">{{treasure.description}}</textarea></td>
	    </tr>
	    <tr>
	    	<th>图片 :</th>
	    	<td>
	    		<img id="img_show" src="/statics/game/{{treasure.get_image()}}"><br>
	    		<input type="file" name="image_file" id="image_file" class="input-text" size="21" onchange="set_image_val(this);"/>
	    		<input type="hidden" name="image" id="image" />
	    	</td>
	    </tr>
	    <tr> 
	      <th>暴击概率 :</th>
	      <td><input type="text" name="crit" class="input-text" value="{{treasure.crit}}"></td>
	    </tr>
	    <tr> 
	      <th>格档概率 :</th>
	      <td><input type="text" name="block" class="input-text" value="{{treasure.block}}"></td>
	    </tr>
   	    <tr>
	      <th>is_unlock :</th>
	      <td>
	      	<input type="radio" name="is_unlock" class="radio_style" value="1" {% if treasure.is_unlock %} checked="checked"{% end %}> &nbsp;未锁&nbsp;&nbsp;&nbsp;
	      	<input type="radio" name="is_unlock" class="radio_style" value="0" {% if not treasure.is_unlock %} checked="checked"{% end %}> &nbsp;锁住
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