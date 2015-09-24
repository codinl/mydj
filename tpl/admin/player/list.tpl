{% extends "../base.tpl" %}

{% block content %}
<div class="subnav">
	<div class="content-menu ib-a blue line-x">
		<a class="add fb"
			href="javascript:window.top.art.dialog({id:'player_add',iframe:'{{config.admin_dir}}/player/add', title:'添加级别配置', width:'480', height:'520', lock:true}, function(){var d = window.top.art.dialog({id:'player_add'}).data.iframe;var form = d.document.getElementById('dosubmit');form.click();return false;}, function(){window.top.art.dialog({id:'player_add'}).close()});void(0);">
			<em>添加玩家</em>
		</a>
	</div>
</div>
<div class="pad-lr-10">
	<form id="myform" name="myform"
		action="{%if p%}{{config.admin_dir}}/player/delete/{{p.cur}}{%end%}"
		method="post" onsubmit="return check();">
		<div class="table-list">
			<table width="100%" cellspacing="0">
				<thead>
					<tr>
						<th width=10>
							<input type="checkbox" value="" id="check_box" onclick="selectall('id[]');">
						</th>
						<th width=30>编号</th>
						<th width=50>名字</th>
						<th width=40>级别</th>
						<th width=40>攻击</th>
						<th width=40>防御</th>
						<th width=40>体力</th>
						<th width=40>军令</th>
						<th width=40>银币</th>
						<th width=40>赠送元宝</th>
						<th width=40>购买元宝</th>
						<!--  
						<th width=50>精力恢复比</th>
						<th width=50>体力恢复比</th>
						<th width=50>精力恢复时间</th>
						<th width=50>体力力恢复时间</th>
						<th width=50>精力恢复耗时</th>
						<th width=50>体力力恢复耗时</th>
						-->
						<th width=30>状态</th>
						<th width=40>操作</th>
					</tr>
				</thead>
				<tbody>
					{% if player_list %}
					{% set i=0 %}
					{% for player in player_list %}
					<tr>
						<td align="center">
							<input type="checkbox" value="{$val.id}" name="id[]">
						</td>
						<td align="center">{{player.id}}</td>
						<td align="center">{{player.name}}</td>
						<td align="center">{{player.level}}</td>
						<td align="center">{{player.attack}}</td>
						<td align="center">{{player.defence}}</td>
						<td align="center">{{player.ep}}</td>
						<td align="center">{{player.sp}}</td>
						<td align="center">{{player.vm}}</td>
						<td align="center">{{player.grm}}</td>
						<td align="center">{{player.brm}}</td>
						<td align="center" onclick="status({{player.id}},'status')" id="status_{{i}}">
							<img src="/statics/admin/images/status_{{player.is_active}}.gif" />
						</td>
						<td align="center">
							<a href="javascript:edit('{{player.id}}')">{{config.lang_edit}}</a>&nbsp;
							<a href="player/detail/{{player.id}}">{{config.lang_detail}}</a>
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
					<a href="/{{config.admin_dir_name}}/player/list/1">{{config.lang_index}}</a>
					<a href="/{{config.admin_dir_name}}/player/list/{{p.cur-1}}">&lt;</a>
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
					<a href="/{{config.admin_dir_name}}/player/list/{{n}}">{{n}}</a>
					{% end %}
					{% end %}
					{% end %}
					{% if p.has_right_point() %}
					<span class="omit">...</span>
					{% end %}
					{% if p.has_next() %}
					<a href="/{{config.admin_dir_name}}/player/list/{{p.cur+1}}">&gt;</a>
					<a href="/{{config.admin_dir_name}}/player/list/{{p.get_page_count()}}">{{config.lang_last_page}}</a>
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
	window.top.art.dialog({id:'player_edit'}).close();
	window.top.art.dialog({title:lang_edit+'--'+name,id:'player_edit',iframe:'/{{config.admin_dir_name}}/player/edit/'+id,width:'480',height:'520'}, function(){var d = window.top.art.dialog({id:'player_edit'}).data.iframe;d.document.getElementById('dosubmit').click();return false;}, function(){window.top.art.dialog({id:'player_edit'}).close()});
}
</script>
{% end %}