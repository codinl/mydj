{% extends "../base.tpl" %}

{% block head_css %}
<link rel="stylesheet" type="text/css" href="/statics/game/css_min/account.css" />
{% end %}

{% block head_js %}
<script type="text/javascript" src="/statics/game/js/page_min/register.js"></script>
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
MyGame.app.data.socialPlatform = "weibo";
MyGame.app.data.userLanguage = "zh_cn";

$(function() {
	$("#page-default-register > .register > .register-title").html(MyGame.utils.locale('default', 'register_title'));
    var platform = MyGame.app.getPlatform();
    if (platform == 'facebook' || MyGame.app.data.userLanguage == 'ko_kr') {
    	$('#page-default-register').find('.mobile').hide();
    	$('#findpwd-introduce').html(MyGame.utils.locale('default', 'register_findpwd_with_email'));
    }

	//关闭按钮
	$('#page-default-register').find('.button-close').click(function(){
		//新旧版本控制，跳转到选服页面或登录选择页面
		MyGame.utils.showWait();
		MyGame.app.redirect('/');//修改为返回登录选择页面
	});

	//注册按钮
	new MyGame.ui.Button(undefined, {
		text : MyGame.utils.locale('default', 'regist'),
        special : "button-big-red",
		click: function() {
			MyGame.utils.showWait();
			//MyGame.track.onEvent('02_031');	//[02][031][登陆页][账户注册][确定按钮]
			//保存登录方式为注册新账号
			//MyGame.app.saveStorage('login_method', 'regist');
			$('#mygame-default-register').submit();
		}
	}).element().addClass("bind-button").appendTo($("#register-buttons"));
		

	//返回按钮
	new MyGame.ui.Button(undefined, {
		text : MyGame.utils.locale('default', 'back'),
		classes : [],
		click: function() {
			MyGame.utils.showWait();
			MyGame.app.redirect('/');//修改为返回登录选择页面
		}
	}).element().appendTo($("#register-buttons"));

});
</script>

<div id="page-default-register">
	<div class="register">
		<div class="register-title"></div>
		<div class="mygame-ui-button button-close"></div>
		<div class="register-introduce"></div>
		<form accept-charset="UTF-8" id="mygame-default-register" action="/account/register" method="post">			
			<div class="row">
				<label for="UserRegisterForm_username" class="required">账户名 <span class="required">*</span></label> 
				<input name="username" id="UserRegisterForm_username" type="text" maxlength="10" />			
			</div>
			<div id="user-introduce" class="row tip">（账户名用于游戏登录，请务必牢记哦~）</div>
			<div class="row"><label for="UserRegisterForm_password" class="required">密码 <span class="required">*</span></label> <input name="password" id="UserRegisterForm_password" type="password" maxlength="16" /></div>
			<div class="row"><label for="UserRegisterForm_repassword" class="required">重复密码 <span class="required">*</span></label> <input name="repassword" id="UserRegisterForm_repassword" type="password" /></div>
			<div class="row mobile"><label for="UserRegisterForm_mobile">手机号</label> <input name="tel" id="UserRegisterForm_mobile" type="text" maxlength="11" />	</div>
			<div class="row"><label for="UserRegisterForm_qq">QQ</label> <input name="qq" id="UserRegisterForm_qq" type="text" /></div>
			<div id="findpwd-introduce" class="row tip">（手机和邮箱必填一项，用于找回密码）</div>
			<br/>
			<div id="register-buttons" class="buttons"></div>
			{% if form and form.errors %}<br/><div class="errorMessage" style="color:#f00;font-size:18px;text-align:center;">{{form.errors['msg']}}</div>{%end%}
		</form>	
	</div>
</div>

{% end %}
