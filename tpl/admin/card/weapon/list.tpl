{% extends "../../base.tpl" %}

{% block content %}
<div class="subnav">
	<div class="content-menu ib-a blue line-x">
		<a class="add fb"
			href="javascript:window.top.art.dialog({id:'weapon_add',iframe:'{{config.admin_dir}}/weapon/add', title:'添加级别配置', width:'480', height:'400', lock:true}, function(){var d = window.top.art.dialog({id:'weapon_add'}).data.iframe;var form = d.document.getElementById('dosubmit');form.click();return false;}, function(){window.top.art.dialog({id:'weapon_add'}).close()});void(0);">
			<em>添加武器</em>
		</a>
	</div>
</div>
<div class="pad-lr-10">
	<form id="myform" name="myform"
		action="{%if p%}{{config.admin_dir}}/weapon/delete/{{p.cur}}{%end%}"
		method="post" onsubmit="return check();">
		<div class="table-list">
			<table width="100%" cellspacing="0">
				<thead>
					<tr>
						<th width=10>
							<input type="checkbox" value="" id="check_box" onclick="selectall('id[]');">
						</th>
						<th width=20>编号</th>
						<th width=40>图片</th>
						<th width=30>名字</th>
						<th width=30>星级</th>
						<th width=100>描述</th>
						<th width=30>攻击</th>
						<th width=30>转生限次</th>
						<th width=30>状态</th>
						<th width=80>操作</th>
					</tr>
				</thead>
				<tbody>
					{% if weapon_list %}
					{% set i=0 %}
					{% for weapon in weapon_list %}
					<tr>
						<td align="center">
							<input type="checkbox" value="{$val.id}" name="id[]">
						</td>
						<td align="center">{{weapon.id}}</td>
						<td align="center"><img src="/statics/game/{{weapon.get_image()}}" class="preview"></td>
						<td align="center">{{weapon.name}}</td>
						<td align="center">{{weapon.rarity}}</td>
						<td align="center">{{weapon.description}}</td>
						<td align="center">{{weapon.attack}}</td>
						<td align="center">{{weapon.rebirth_max}}</td>
						<td align="center" onclick="status({{weapon.id}},'status')" id="status_{{i}}">
							<img src="/statics/admin/images/status_{{weapon.is_unlock}}.gif" />
						</td>
						<td align="center">
							<a href="javascript:edit('{{weapon.id}}')">{{config.lang_edit}}</a>
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
					<a href="/{{config.admin_dir_name}}/weapon/list/1">{{config.lang_index}}</a>
					<a href="/{{config.admin_dir_name}}/weapon/list/{{p.cur-1}}">&lt;</a>
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
					<a href="/{{config.admin_dir_name}}/weapon/list/{{n}}">{{n}}</a>
					{% end %}
					{% end %}
					{% end %}
					{% if p.has_right_point() %}
					<span class="omit">...</span>
					{% end %}
					{% if p.has_next() %}
					<a href="/{{config.admin_dir_name}}/weapon/list/{{p.cur+1}}">&gt;</a>
					<a href="/{{config.admin_dir_name}}/weapon/list/{{p.get_page_count()}}">{{config.lang_last_page}}</a>
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
	window.top.art.dialog({id:'weapon_edit'}).close();
	window.top.art.dialog({title:lang_edit+'--'+name,id:'weapon_edit',iframe:'/{{config.admin_dir_name}}/weapon/edit/'+id,width:'480',height:'400'}, function(){var d = window.top.art.dialog({id:'weapon_edit'}).data.iframe;d.document.getElementById('dosubmit').click();return false;}, function(){window.top.art.dialog({id:'weapon_edit'}).close()});
}
</script>
{% end %}