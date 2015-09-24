{% import config %}

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0" />
<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
	
{%block head_base_css%}
<link rel="stylesheet" type="text/css" href="/statics/game/css_min/base.css" />
{% end %}

{% block head_css %}{% end %}

{% block head_base_js %}

<script type="text/javascript" src="/statics/game/js/lib.js"></script>
<script type="text/javascript" src="/statics/game/js/lang.js"></script>

<!--
<script type="text/javascript" src="/statics/game/js/lib/jquery1.6.4.js"></script>
<script type="text/javascript" src="/statics/game/js/lib/basefunc.js"></script>
<script type="text/javascript" src="/statics/game/js/lib/baseui.js"></script>
<script type="text/javascript" src="/statics/game/js/lib/functions.js"></script>
<script type="text/javascript" src="/statics/game/js/lib/ui.js"></script>
<script type="text/javascript" src="/statics/game/js/lang.js"></script>
-->

{% end %}
{% block head_js %}{% end %}
</head>

<body>{% block body %}{% end %}</body>
{% block foot_js %}{% end %}
</script>
</html>
