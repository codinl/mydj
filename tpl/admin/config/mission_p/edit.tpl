{% extends "../../base.tpl" %}

{% block content %}
<div class="pad_10">
	<form action="" method="post" name="myform" id="myform">
	<table width="100%" cellpadding="2" cellspacing="1" class="table_form">
		{% if p_list %}
		{% set i=0 %}
		{% for p in  p_list %}
	   	<tr> 
	      <th>{{p.name}}-{{p.key}}:</th>
	      <td><input id="val_{{i}}" type="text" name="{{p.key}}" class="input-text" value="{{p.value}}" onblur="check_total();"></td>
	    </tr>
	    {% set i+=1 %}
	    {% end %}
	    {% end %}
	    <tr> 
	      <th>概率总和：</th>
	      <td id="total_p">100</td>
	    </tr>
	    <tr style="font-weight:bold;color:#d00;"> 
	      <th>错误提示：</th>
	      <td id="tips"></td>
	    </tr>
	</table>
	<input type="submit" name="dosubmit" id="dosubmit" class="dialog" value=" " >
	</form>
</div>

<script language="javascript">
function check_total() {
	total = get_total();
	$("#total_p").html(total);
	if(total < 100 ){
		$("#tips").html("概率总和小于100,否则会出错。请重新设置...");
	}else if(total == 100){
		$("#tips").html("");
	}else if(total > 100){
		$("#tips").html("概率总和大于100,否则会出错。请重新设置...");
	}
}
function get_total(){
	return parseInt($("#val_0").val()) + parseInt($("#val_1").val()) + 
		   parseInt($("#val_2").val()) + parseInt($("#val_3").val());
}
</script>
{% end %}