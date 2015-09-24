{% extends "../base.tpl" %}

{% block head_css %}
<link rel="stylesheet" type="text/css" href="/statics/game/css_min/account.css" />
{% end %}

{% block head_js %}
<script type="text/javascript" src="/statics/game/js/page_min/select_general.js"></script>
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
</script>

<div id="fb-root"></div>

<script type="text/javascript">
$(function() {
	var page = new MyGame.page.NewPlayer();
	page.load();
});
</script>

{% end %}


{% block foot_js %}

{% end %}