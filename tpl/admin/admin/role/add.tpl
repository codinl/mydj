{% extends "../base.tpl" %}

{% block content %}
<div class="pad_10">
	<form action="" method="post" name="myform" id="myform">
		<table width="100%" cellpadding="2" cellspacing="1" class="table_form">
			<tr> 
		      <th width="60">角色名 :</th>
		      <td><input type="text" name="name" id="name" class="input-text" value="" size="25"></td>
		    </tr>
		    <tr> 
		      <th>描述 :</th>
		      <td><textarea name="remark" cols="40" rows="3"></textarea></td>
		    </tr>
		    <tr>
		      <th>状态 :</th>
		      <td><input type="radio" name="status" class="radio_style" value="1" checked> &nbsp;有效&nbsp;&nbsp;&nbsp;
		        <input type="radio" name="status" class="radio_style" value="0"> &nbsp;禁用</td>
		    </tr>
		</table>
		<input type="submit" name="dosubmit" id="dosubmit" class="dialog" value=" ">
	</form>
	<script type="text/javascript">
		$(function(){
			$.formValidator.initConfig({formid:"myform",autotip:true,onerror:function(msg,obj){window.top.art.dialog({content:msg,lock:true,width:'250',height:'50'}, function(){this.close();$(obj).focus();})}});
			$("#name").formValidator({onshow:"不能为空",onfocus:"不能为空"}).inputValidator({min:1,onerror:"请填写角色名"});
		})
	</script>
</div>
{% end %}