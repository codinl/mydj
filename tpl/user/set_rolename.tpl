{% extends "../base.tpl" %}

{% block head_css %}
<link rel="stylesheet" type="text/css" href="/statics/game/css_min/account_set_rolename.css" />
{% end %}

{% block head_js %}
{% end %}

{% block body %}
<script type="text/javascript">
MyGame.app.baseUrl = "/";
MyGame.ajax.baseUrl = "/";
MyGame.app.weibo.appKey = "";
MyGame.app.weibo.officialWeiboId = "";
MyGame.app.isNd = false;
MyGame.gap.init({
	device : 'android',
});
MyGame.app.data.facebookAppId = "";
</script>

<div id="fb-root"></div>
<script type="text/javascript">
<!--
$(function() {
	$("#page-default-register > .register > .register-title")
		.html(MyGame.utils.locale('default', 'set_nickname'));
	$('#page-default-register').find('.register-introduce')
		.html(MyGame.utils.locale('default', 'login_nickname_tip'));

	var flag = false;	//【进入】按钮只能点击一次
	new MyGame.ui.Button(undefined, {
		text : MyGame.utils.locale('default', 'enter'),
        special : "button-big-red",
		click: function() {
			if (flag == false) {
				flag = true;
				$('#mygame-default-register').submit();
			}
		}
	}).element().addClass("bind-button").appendTo($("#register-buttons"));

});
//-->
</script>

<div id="page-default-register">
	<div class="register">
		<div class="register-title"></div>
		<form accept-charset="UTF-8" id="mygame-default-register" action="/account/set_rolename" method="post">
			<div class="row">
				<div class="register-introduce"></div>
				<input name="rolename" class="rolename" type="text" width="10" maxlength="7" />			
			</div>
		</form>
		<div id="register-buttons" class="buttons"></div>
		{% if form and form.errors %}
		<div class="errorMessage" style="padding-top:8px;color:#f00;font-size:16px;text-align:center;">{{form.errors['msg']}}</div>
		{%else%}
		<div class="errorMessage" style="padding-top:8px;color:#666;font-size:16px;text-align:center;">角色名：7个字符以内,不能重复</div>
		{%end%}
	</div>
</div>

{% end %}


{% block foot_js %}

{% end %}