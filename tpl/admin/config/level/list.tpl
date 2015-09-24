{% extends "../../base.tpl" %}

{% block content %}
<div class="subnav">
	<div class="content-menu ib-a blue line-x">
		<a class="add fb"
			href="javascript:window.top.art.dialog({id:'config_level_add',iframe:'{{config.admin_dir}}/config/level/add', title:'添加级别配置', width:'480', height:'200', lock:true}, function(){var d = window.top.art.dialog({id:'config_level_add'}).data.iframe;var form = d.document.getElementById('dosubmit');form.click();return false;}, function(){window.top.art.dialog({id:'config_level_add'}).close()});void(0);">
			<em>添加级别配置</em>
		</a>
	</div>
</div>
<div class="pad-lr-10">
	<form id="myform" name="myform"
		action="{%if p%}{{config.admin_dir}}/config/level/delete/{{p.cur}}{%end%}"
		method="post" onsubmit="return check();">
		<div class="table-list">
			<table width="100%" cellspacing="0">
				<thead>
					<tr>
						<th width=10>
							<input type="checkbox" value="" id="check_box" onclick="selectall('id[]');">
						</th>
						<th width=30>编号</th>
						<th width=60>level</th>
						<th width=60>update_need_xp</th>
						<th width=60>max_ep</th>
						<th width=60>max_sp</th>
						<th width=60>base_slot_count</th>
						<th width=80>操作</th>
					</tr>
				</thead>
				<tbody>
					{% if config_level_list %}
					{% set i=0 %}
					{% for config_level in config_level_list %}
					<tr>
						<td align="center">
							<input type="checkbox" value="{$val.id}" name="id[]">
						</td>
						<td align="center">{{config_level.id}}</td>
						<td align="center">{{config_level.level}}</td>
						<td align="center">{{config_level.update_need_xp}}</td>
						<td align="center">{{config_level.max_ep}}</td>
						<td align="center">{{config_level.max_sp}}</td>
						<td align="center">{{config_level.base_slot_count}}</td>
						<td align="center">
							<a href="javascript:edit('{{config_level.id}}')">{{config.lang_edit}}</a>
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
					<a href="/{{config.admin_dir_name}}/config/level/list/1">{{config.lang_index}}</a>
					<a href="/{{config.admin_dir_name}}/config/level/list/{{p.cur-1}}">&lt;</a>
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
					<a href="/{{config.admin_dir_name}}/config/level/list/{{n}}">{{n}}</a>
					{% end %}
					{% end %}
					{% end %}
					{% if p.has_right_point() %}
					<span class="omit">...</span>
					{% end %}
					{% if p.has_next() %}
					<a href="/{{config.admin_dir_name}}/config/level/list/{{p.cur+1}}">&gt;</a>
					<a href="/{{config.admin_dir_name}}/config/level/list/{{p.get_page_count()}}">{{config.lang_last_page}}</a>
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
	window.top.art.dialog({id:'config_level_edit'}).close();
	window.top.art.dialog({title:lang_edit+'--'+name,id:'config_level_edit',iframe:'/{{config.admin_dir_name}}/config/level/edit/'+id,width:'480',height:'200'}, function(){var d = window.top.art.dialog({id:'config_level_edit'}).data.iframe;d.document.getElementById('dosubmit').click();return false;}, function(){window.top.art.dialog({id:'config_level_edit'}).close()});
}
</script>
{% end %}