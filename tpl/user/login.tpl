{% extends "../base.tpl" %}

{% block head_css %}
<link rel="stylesheet" type="text/css" href="/statics/game/css_min/account.css" />
{% end %}

{% block head_js %}
<script type="text/javascript" src="/statics/game/js/page_min/login.js"></script>
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
MyGame.app.serverNode = {userRegionId: 1,regionId: 1,groupId:1,name: '太平三国'};
$(function() {
$("#page-default-login > .login > .login-title")
		.html(MyGame.utils.locale('default', 'login_title'));
		
	$("#page-default-login > .login > .button-close").click(function() {
		MyGame.utils.showWait();
		MyGame.app.redirect('/');//修改为返回登录选择页面
	});

	//登录按钮
	new MyGame.ui.Button(undefined, {
        text : MyGame.utils.locale('default', 'login'),
        special : "button-big-red",
        click: function() {
            MyGame.utils.showWait();
    		//MyGame.track.onEvent('02_022');	//[02][022][登陆页][账户登陆页][登陆按钮]
    		//保存登录方式为普通登录
			//MyGame.app.saveStorage('login_method', 'normal');
		    $('#mygame-default-login').submit();
        }
    }).element().addClass("login-button").appendTo($("#login-buttons"));

	var platform = MyGame.app.getPlatform();

	//注册
    new MyGame.ui.Button(undefined, {
        text : "注册",
        click: function() {
        	MyGame.app.redirect("/account/register");
        }
    }).element().addClass("back-button").appendTo($("#login-buttons"));

	//Init toast
	MyGame.app.toast.show('', 10, true);

});

//-->
</script>

<div id="page-default-login">
	<div class="login">
		<div class="login-title"></div>
		<div class="mygame-ui-button button-close"></div>
		<div class="separate"></div>
		<!-- 
		<div id="server" class="mygame-com-server">
			<div class="signal"></div>
			<div class="name"></div>
			<div class="flag"></div>
		</div> -->
		<form accept-charset="UTF-8" id="mygame-default-login" action="/account/login" method="post">			
			<div id="username-row" class="row username"><label for="UserLoginForm_username" class="required">账户名 <span class="required">*</span></label> <input name="username" id="UserLoginForm_username" type="text" maxlength="10" /></div>
			<div id="password-row" class="row password"><label for="UserLoginForm_password" class="required">密码 <span class="required">*</span></label> <input name="password" id="UserLoginForm_password" type="password" /></div>
			<div id="login-buttons" class="buttons"></div>
			{% if form and form.errors %}
			<div class="errorMessage" style="padding-top:8px;color:#f00;font-size:16px;text-align:center;">{{form.errors['msg']}}</div>
			{%end%}
			<script type="text/javascript">
			var nameerr = '';
			var pwderr = '';
			</script>
		</form>	
	</div>
</div>
{% end %}
