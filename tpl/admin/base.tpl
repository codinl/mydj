{% import config %}

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=7" />

{% block base_css %}
<link href="/statics/admin/css/style.css" rel="stylesheet" type="text/css"/>
<link href="/statics/admin/css/dialog.css" rel="stylesheet" type="text/css" />
{% end %}

{% block head_css %}{% end %}

{% block base_js %}
<script language="javascript" type="text/javascript" src="/statics/admin/js/jquery/jquery-1.4.2.min.js"></script>
<script language="javascript" type="text/javascript" src="/statics/admin/js/jquery/plugins/formvalidator.js"></script>
<script language="javascript" type="text/javascript" src="/statics/admin/js/jquery/plugins/formvalidatorregex.js"></script>
<script language="javascript" type="text/javascript" src="/statics/admin/js/admin_common.js"></script>
<script language="javascript" type="text/javascript" src="/statics/admin/js/dialog.js"></script>
<script language="javascript" type="text/javascript" src="/statics/admin/js/iColorPicker.js"></script>
{% end %}

{% block head_js %}{% end %}

<title>管理后台</title>
</head>

<body>
{% block content %}{% end %}
</body>
</html>
