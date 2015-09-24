
{% extends "../base.tpl" %}

{% block content %}
<div class="subnav">
	<div class="content-menu ib-a blue line-x">
		<a class="add fb"
			href="javascript:window.top.art.dialog({id:'admin_add',iframe:'{{config.admin_dir}}/admin/add', title:'添加管理员', width:'480', height:'250', lock:true}, function(){var d = window.top.art.dialog({id:'admin_add'}).data.iframe;var form = d.document.getElementById('dosubmit');form.click();return false;}, function(){window.top.art.dialog({id:'admin_add'}).close()});void(0);">
			<em>添加管理员</em>
		</a>
	</div>
</div>
<div class="pad-lr-10">
	<form id="myform" name="myform"
		action="{%if p%}{{config.admin_dir}}/admin/delete/{{p.cur}}{%end%}"
		method="post" onsubmit="return check();">
		<div class="table-list">
			<table width="100%" cellspacing="0">
				<thead>
					<tr>
						<th width=30>
							<input type="checkbox" value="" id="check_box" onclick="selectall('id[]');">
						</th>
						<th width=60>编号</th>
						<th width=100>帐号昵称</th>
						<th>所属分组</th>
						<th>上次登陆</th>
						<th width=60>状态</th>
						<th width=60>操作</th>
					</tr>
				</thead>
				<tbody>
					{% if admin_list %}
					{% set i=0 %}
					{% for admin in admin_list %}
					<tr>
						<td align="center">
							<input type="checkbox" value="{$val.id}" name="id[]" 
							{%if admin.name==config.val_admin %} disabled="disabled" {%end %}>
						</td>
						<td align="center">{{admin.id}}</td>
						<td align="center">{{admin.name}}</td>
						<td align="center"></td>
						<td align="center">{{admin.last_login_time}}</td>
						<td align="center" onclick="status({{admin.id}},'status')" id="status_{{i}}">
							<img src="/statics/admin/images/status_{{admin.is_active}}.gif" />
						</td>
						<td align="center">
							<a href="javascript:edit('{{admin.id}}')">{{config.lang_edit}}</a>
						</td>
					</tr>
					{% set i+=1%}
					{% end %}
					{% end %}
				</tbody>
			</table>
			<div class="btn">
				<label for="check_box" style="float:left;">{{config.lang_select_all}}/{{config.lang_cancel}}
				</label>
				<input type="submit" class="button" name="dosubmit"
					value="{{config.lang_delete}}" onclick="return confirm('{{config.lang_sure_delete}}')"
					style="float:left;margin-left:10px;" />
				{% if p %}
				<div class="pagination">
					{% if p.has_pre()%}
					<a href="/{{config.admin_dir_name}}/admin/list/1">{{config.lang_index}}</a>
					<a href="/{{config.admin_dir_name}}/admin/list/{{p.cur-1}}">&lt;</a>
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
					<a href="/{{config.admin_dir_name}}/admin/list/{{n}}">{{n}}</a>
					{% end %}
					{% end %}
					{% end %}
					{% if p.has_right_point() %}
					<span class="omit">...</span>
					{% end %}
					{% if p.has_next() %}
					<a href="/{{config.admin_dir_name}}/admin/list/{{p.cur+1}}">&gt;</a>
					<a href="/{{config.admin_dir_name}}/admin/list/{{p.get_page_count()}}">{{config.lang_last_page}}</a>
					{% end %}
				</div>
				{% end %}
			</div>
		</div>
	</form>
</div>

<script language="javascript">
function edit(id) {
	var lang_edit = "{{config.lang_edit}}";
	window.top.art.dialog({id:'admin_edit'}).close();
	window.top.art.dialog({title:lang_edit+'--'+name,id:'admin_edit',iframe:'/{{config.admin_dir_name}}/admin/edit/'+id,width:'480',height:'250'}, function(){var d = window.top.art.dialog({id:'admin_edit'}).data.iframe;d.document.getElementById('dosubmit').click();return false;}, function(){window.top.art.dialog({id:'admin_edit'}).close()});
}

/*
var lang_user_name = "帐号！";
function check(){
	var ids='';
	$("input[name='id[]']:checked").each(function(i, n){
		ids += $(n).val() + ',';
	});
	if(ids=='') {
		window.top.art.dialog({content:lang_please_select+lang_user_name,lock:true,width:'200',height:'50',time:1.5},function(){});
		return false;
	}
	return true;
}

function status(id,type){
    $.get("{:u('admin/status')}", { id: id, type: type }, function(jsondata){
		var return_data  = eval("("+jsondata+")");
		$("#"+type+"_"+id+" img").attr('src', '/statics/admin/images/status_{{admin.is_active}}.gif');
	}); 
}
*/

</script>

{% end %}