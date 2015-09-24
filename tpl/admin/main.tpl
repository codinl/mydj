{% import config %}

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" class="off">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7" />
	<link href="/statics/admin/css/style.css" rel="stylesheet" type="text/css"/>
	<link href="/statics/admin/css/dialog.css" rel="stylesheet" type="text/css" />
	<script language="javascript" type="text/javascript" src="/statics/admin/js/jquery/jquery-1.4.2.min.js"></script>
	<script language="javascript" type="text/javascript" src="/statics/admin/js/dialog.js"></script>
	<title>管理后台</title>
</head>
<body scroll="no">
<div id="header">
    <div class="logo"><a href="" title="网站名"></a></div>
    <div class="fr">
        <div class="style_but"></div>
    </div>
    <div class="col-auto" style="overflow: visible">
        <div class="log white cut_line"> {{config.lang_hello}}！{{user_name}}
            <span>|</span>
            <a href="{{config.admin_dir}}/account/logout">[{{config.lang_logout}}]</a>
        </div>            
    </div>
    <ul class="nav white" id="top_menu">
    	{% if menu_list is not None %}
    	{% for menu in menu_list %}
		<li id="_M({{menu.id}})" class="top_menu{% if menu.id == cur_menu_id %} on{% end %}">
			<a href="{{config.admin_dir}}/home/{{menu.id}}"  hidefocus="true" style="outline:none;">{{menu.name}}</a>
		</li>
        {% end %}
        {% end %}
    </ul>
</div>
<div id="content">
    <div class="left_menu fl">
        <div id="leftMain">
		{% if node_list is not None %}
			{% for node in node_list %}
			<h3 class="f14"><span class="switchs cu on" title="{{ config.lang_expand_or_contract }}"></span>{{ node.name }}</h3>
			<ul>
				{% set node_children = node.get_children() %}
				{% if node_children is not None %}
				{% for n in node_children %}
				<li id="_MP{{n.id}}" class="sub_menu"><a href="javascript:_MP({{n.id}},'{{config.admin_dir}}/{{n.url}}');" hidefocus="true" style="outline:none;">{{ n.name }}</a></li>
				{% end %}
				{% end %}
			</ul>
			{% end %}
			{% end %}
			
			<script type="text/javascript">
			$(".switchs").each(function(i){
				var ul = $(this).parent().next();
				$(this).click(
				function(){
					if(ul.is(':visible')){
						ul.hide();
						$(this).removeClass('on');
					}else{
						ul.show();
						$(this).addClass('on');
					}
				})
			});
			</script>
	</div>
    <a href="javascript:;" id="openClose" style="outline-style: none; outline-color: invert; outline-width: medium;" hideFocus="hidefocus" class="open" title="{$lang.expand_or_contract}"></a> </div>
    <div class="right_main">
    	<!--
        <div class="crumbs">
            <div class="shortcut cu-span"> <a href="{{config.admin_dir}}/index" target="right">
                <span>清除缓存</span>
                </a> <a href="javascript:Refresh();">
                <span>刷新</span>
                </a> </div>
            <span id="current_pos"></span>
        </div>-->
        <div class="rmc">
            <div class="content" style="position:relative; overflow:hidden">
                <iframe name="right" id="rightMain" src="{{config.admin_dir}}/index" frameborder="false" scrolling="auto" style="overflow-x:hidden;border:none;" width="100%" height="auto" allowtransparency="true"></iframe>
            </div>
        </div>
    </div>
</div>
<script type="text/javascript">
function windowW(){
	if($(window).width()<980){
			$('#header').css('width',980+'px');
			$('#content').css('width',980+'px');
			$('body').attr('scroll','');
			$('body').css('overflow','');
	}
}
windowW();
$(window).resize(function(){
	if($(window).width()<980){
		windowW();
	}else{
		$('#header').css('width','auto');
		$('#content').css('width','auto');
		$('body').attr('scroll','no');
		$('body').css('overflow','hidden');

	}
});
window.onresize = function(){
	var heights = document.documentElement.clientHeight-110;
	document.getElementById('rightMain').height = heights;
	var openClose = $("#rightMain").height()+9;
	$('#center_frame').height(openClose+9);
	$("#openClose").height(openClose+30);
}
window.onresize();

//左侧开关
$("#openClose").click(function(){
	if($(this).data('clicknum')==1) {
		$("html").removeClass("on");
		$(".left_menu").removeClass("left_menu_on");
		$(this).removeClass("close");
		$(this).data('clicknum', 0);
	} else {
		$(".left_menu").addClass("left_menu_on");
		$(this).addClass("close");
		$("html").addClass("on");
		$(this).data('clicknum', 1);
	}
	return false;
});

function _M(tag,targetUrl) {
	$.get("{'/statics/public/menu.tpl'}", {tag:tag}, function(data){
		$("#leftMain").html(data);
	});

	//$("#rightMain").attr('src', targetUrl);
	$('.top_menu').removeClass("on");
	$('#_M'+tag).addClass("on");

//	$.get("{:u('index/current_pos')}", {tag:tag}, function(data){
//		$("#current_pos").html(data);
//	});

	//显示左侧菜单，当点击顶部时，展开左侧
	$(".left_menu").removeClass("left_menu_on");
	$("#openClose").removeClass("close");
	$("html").removeClass("on");
	$("#openClose").data('clicknum', 0);
	$("#current_pos").data('clicknum', 1);
}

function _MP(menuid,targetUrl) {
	$("#rightMain").attr('src', targetUrl);
	$('.sub_menu').removeClass("on fb blue");
	$('#_MP'+menuid).addClass("on fb blue");
	//$("#current_pos").data('clicknum', 1);
	//$.get("{{config.admin_dir}}/menuid",function(data){
	//	$("#current_pos").html(data);
	//});
}

function Refresh() {
	var src = $("#rightMain").attr('src');
	$("#rightMain").attr('src',src);
}
</script>

</body>
</html>
