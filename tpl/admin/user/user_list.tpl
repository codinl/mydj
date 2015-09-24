{% extends "../base.tpl" %}

{% block content %}

<div class="pad-10" >
    <form name="searchform" action="" method="get" >
    <table width="100%" cellspacing="0" class="search-form">
        <tbody>
            <tr>
            <td>
            <div class="explain-col">
				关键字 :
                <input name="keyword" type="text" class="input-text" size="25" value="{{ config.lang_keyword }}" />
                <input type="hidden" name="m" value="user" />
                <input type="submit" name="search" class="button" value="搜索" />
        	</div>
            </td>
            </tr>
        </tbody>
    </table>
    </form>
    <form id="myform" name="myform" action="{{config.admin_dir}}/user/delete" method="post" onsubmit="return check();">
    <div class="table-list">
    <table width="100%" cellspacing="0">
        <thead>
            <tr>
                <th width=15><input type="checkbox" value="" id="check_box" onclick="selectall('id');"></th>
                <th width="20">ID</th>
				<th width="150">Email</th>
                <th width="70">qq</th>
                <th width="70">电话</th>
                <th>地址</th>
                <th width=120>注册时间</th>
                <th width=120>最后登录</th>
                <th width=30>审核</th>
            </tr>
        </thead>
    	<tbody>
    	{% if user_list is not None %}
    	{% for user in user_list %}
        <tr>
           <td align="center"><input type="checkbox" value="{{user.id}}" name="id"></td>
           <td align="center">{{user.id}}</td>
           <td align="center"><a href="javascript:edit({$val.id},'{$val.name}')"><em class="blue">{{ user.email }}</em></a></td>
           <td align="center">{% if user.qq %}{{ user.qq }}{% end %}</td>
           <td align="center">{% if user.tel %}{{ user.tel }}{% end %}</td>
           <td align="center">{% if user.address %}{{ user.address }}{% end %}</td>
           <td align="center">{% if user.regist_time %}{{ user.regist_time }}{% end %}<br><font color=green>{% if user.regist_ip %}{{ user.regist_ip }}{% end %}</font></td>
		   <td align="center">{% if user.last_login_time %}{{ user.last_login_time }}{% end %}<br><font color=green>{% if user.last_login_ip %}{{ user.last_login_ip }}{% end %}</font></td>
           <td align="center" onclick="status({$val.id},'status')" id="status_{$val.id}"><img src="/statics/images/status_True.gif" /></td>
    	</tr>
    	{% end %}
    	{% end %}
    	</tbody>
    </table>
    <div class="btn">
    	<label for="check_box" style="float:left;">全选 / 取消</label>
    	<input type="submit" class="button" name="dosubmit" value="{{config.lang_delete}}" onclick="return confirm('{{ config.lang_sure_delete }}')" style="float:left;margin:0 10px 0 10px;"/>
    		{% if p is not None %}
			<div class="pagination">
				{% if p.has_pre()%}
				<a href="1">首页</a>
				<a href="{{p.cur - 1}}">&lt;</a>
				{% end %}
				{% if p.has_left_point() %}
				<span class="omit">...</span>
				{% end %}
				{% set curpage = p.cur %}
				{% if p.total > 1%}
				{% for n in range(p.get_left(),p.get_right()+1) %}
					{% if curpage==n %}
					<span class="current">{{n}}</span>
					{% else %}
					<a href="{{n}}">{{n}}</a>
					{% end %}
				{% end %}
				{% end %}
				{% if p.has_right_point() %}
				<span class="omit">...</span>
				{% end %}
				{% if p.has_next() %}
				<a href="{{p.cur + 1}}">&gt;</a>
				<a href="{{p.get_page_count()}}">尾页</a>
				{% end %}		
			</div>
			{% end %}
    </div>
    </div>
    </form>
</div>

<script language="javascript">
function edit(id, name) {
	var lang_edit = "{$Think.lang.edit}";
	window.top.art.dialog({id:'edit'}).close();
	window.top.art.dialog({title:lang_edit+'--'+name,id:'edit',iframe:'?m=user&a=edit&id='+id,width:'450',height:'500'}, 
		function(){
			var d = window.top.art.dialog({id:'edit'}).data.iframe;
			d.document.getElementById('dosubmit').click();
			return false;
		}, 
		function(){
			window.top.art.dialog({id:'edit'}).close();
		}
	);
}
function check(){
	var ids='';
	$("input[name='id']:checked").each(function(i, n){
		ids += $(n).val() + ',';
	});
	if(ids=='') {
		window.top.art.dialog({content:lang_please_select+lang_cate_name,lock:true,width:'200',height:'50',time:1.5},function(){});
		return false;
	}
	return true;
}
function status(id,type){
    $.get("{:u('user/status')}", { id: id, type: type }, function(jsondata){
		var return_data  = eval("("+jsondata+")");
		$("#"+type+"_"+id+" img").attr('src', '/statics/images/status_'+return_data.data+'.gif')
	}); 
}
</script>

{% end %}
