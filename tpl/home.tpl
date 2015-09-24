{% extends base.tpl %}

{% block head_css %}
<link rel="stylesheet" type="text/css" href="/statics/game/css_min/home.css" />
{% end %}

{% block head_js %}
<script type="text/javascript" src="/statics/game/js/page_min/home.js"></script>
{% end %}

{% block body %}
<script type="text/javascript">
	MyGame.app.baseUrl = "/";
	MyGame.ajax.baseUrl = "/";
	MyGame.app.weibo.appKey = "";
	MyGame.app.weibo.officialWeiboId = "";
    MyGame.app.isNd = false;
</script>
<div id="fb-root"></div>

<script type="text/javascript">
$(function() {
	var page = new MyGame.page.Home();
	page.load();
});
</script>
{% end %}


{% block foot_js %}
<script type="text/javascript">
MyGame.gap.init({
	device : "android", 
	effectSound : MyGame.app.effectSound(),
	bgSound : MyGame.app.bgSound()
});
MyGame.app.data.userId = "";
MyGame.app.data.socialPlatform = "weibo";
MyGame.app.data.userLanguage = "zh_cn";
MyGame.app.weibo.display = "mobile";
MyGame.app.fbparams = {
	appId : "",
	channelUrl : "",
	status : true,
	cookie : true,
	xfbml : true
};
{% end %}