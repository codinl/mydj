{% extends "../base.tpl" %}

{% block content %}
<div class="pad_10">
	<form action="" method="post" name="myform" id="myform">
	<table width="100%" cellpadding="2" cellspacing="1" class="table_form">
		<tr> 
	      <th width="80">帐号名称 :</th>
	      <td><input type="text" name="name" id="user_name" class="input-text" value="{{admin.name}}"></td>
	    </tr>
	    <tr> 
	      <th>修改密码 :</th>
	      <td><input type="password" name="password" id="password" class="input-text"></td>
	    </tr>
	    <tr>
	      <th>确认密码 :</th>
	      <td><input type="password" name="repassword" id="repassword" class="input-text"></td>
	    </tr>
	    <!--  
	    <tr>
	      <th>所属分组 :</th>
	      <td>
	      	<select name="role_id">
	        	<option value="{$val.id}">{$val.name}</option>
	        </select>
	      </td>
	    </tr>-->
	    <tr>
	      <th>审核状态 :</th>
	      <td>
	      	<input type="radio" name="is_active" class="radio_style" value="1" {%if admin.is_active%} checked="checked"{%end%}> &nbsp;有效&nbsp;&nbsp;&nbsp;
	        <input type="radio" name="is_active" class="radio_style" value="0" {%if not admin.is_active%} checked="checked"{%end%}> &nbsp;禁用
	      </td>
	    </tr>
	</table>
	<input type="submit" name="dosubmit" id="dosubmit" class="dialog" value=" ">
	</form>
	<script type="text/javascript">
		/*$(function(){
			$.formValidator.initConfig({formid:"myform",autotip:true,onerror:function(msg,obj){window.top.art.dialog({content:msg,lock:true,width:'200',height:'50'}, function(){this.close();$(obj).focus();})}});
			$("#user_name").formValidator({onshow:"填写帐号昵称",onfocus:"填写帐号昵称"}).inputValidator({min:1,onerror:"请填写帐号昵称"}).ajaxValidator({type : "get",url : "{{config.admin_dir}}/admin/add/ajax_check_name",data :"",datatype : "html",async:'false',success : function(data){	if( data == "1" ){return true;}else{return false;}},buttons: $("#dosubmit"),onerror : "帐号已经被占用",onwait : "正在检测..."});
			$("#password").formValidator({onshow:"填写密码",onfocus:"填写6位以上密码"}).inputValidator({min:6,onerror:"请填写6位以上密码"});
			$("#repassword").formValidator({onshow:"确认密码",onfocus:"确认密码",oncorrect:"填写正确"}).compareValidator({desid:"password",operateor:"=",onerror:"两次输入密码不一致"});
		})*/
	</script>
</div>
{% end %}