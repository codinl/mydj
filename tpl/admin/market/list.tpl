{% extends "../base.tpl" %}

{% block content %}
<div class="subnav">
	<div class="content-menu ib-a blue line-x">
		<a class="add fb"
			href="javascript:window.top.art.dialog({id:'market_add',iframe:'{{config.admin_dir}}/market/add', title:'添加应用市场', width:'480', height:'300', lock:true}, function(){var d = window.top.art.dialog({id:'market_add'}).data.iframe;var form = d.document.getElementById('dosubmit');form.click();return false;}, function(){window.top.art.dialog({id:'market_add'}).close()});void(0);">
			<em>添加应用市场</em>
		</a>
	</div>
</div>
<div class="pad-lr-10">
	<form id="myform" name="myform"
		action="{%if p%}{{config.admin_dir}}/market/delete/{{p.cur}}{%end%}"
		method="post" onsubmit="return check();">
		<div class="table-list">
			<table width="100%" cellspacing="0">
				<thead>
					<tr>
						<th width=10>
							<input type="checkbox" value="" id="check_box" onclick="selectall('id[]');">
						</th>
						<th width=50>英文名字</th>
						<th width=50>名字</th>
						<th width=100>描述</th>
						<th width=80>操作</th>
					</tr>
				</thead>
				<tbody>
					{% if market_list %}
					{% set i=0 %}
					{% for market in market_list %}
					<tr>
						<td align="center">{{market.id}}</td>
						<td align="center">{{market.e_name}}</td>
						<td align="center">{{market.name}}</td>
						<td align="center">{{market.description}}</td>
						<td align="center">
							<a href="javascript:edit('{{market.id}}')">{{config.lang_edit}}</a>
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
					<a href="/{{config.admin_dir_name}}/market/list/1">{{config.lang_index}}</a>
					<a href="/{{config.admin_dir_name}}/market/list/{{p.cur-1}}">&lt;</a>
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
					<a href="/{{config.admin_dir_name}}/market/list/{{n}}">{{n}}</a>
					{% end %}
					{% end %}
					{% end %}
					{% if p.has_right_point() %}
					<span class="omit">...</span>
					{% end %}
					{% if p.has_next() %}
					<a href="/{{config.admin_dir_name}}/market/list/{{p.cur+1}}">&gt;</a>
					<a href="/{{config.admin_dir_name}}/market/list/{{p.get_page_count()}}">{{config.lang_last_page}}</a>
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
	window.top.art.dialog({id:'market_edit'}).close();
	window.top.art.dialog({title:lang_edit+'--'+name,id:'market_edit',iframe:'/{{config.admin_dir_name}}/market/edit/'+id,width:'480',height:'300'}, function(){var d = window.top.art.dialog({id:'market_edit'}).data.iframe;d.document.getElementById('dosubmit').click();return false;}, function(){window.top.art.dialog({id:'market_edit'}).close()});
}
</script>
{% end %}