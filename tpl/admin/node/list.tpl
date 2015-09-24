{% extends ""../base.tpl" %}

{% block content %}

<div class="subnav">
	<div class="content-menu ib-a blue line-x">
		<a class="add fb" href="javascript:window.top.art.dialog({id:'node_add',iframe:'{{config.admin_dir}}/node/add', title:'添加菜单', width:'500', height:'480', lock:true}, function(){var d = window.top.art.dialog({id:'node_add'}).data.iframe;var form = d.document.getElementById('dosubmit');form.click();return false;}, function(){window.top.art.dialog({id:'node_add'}).close()});void(0);">
			<em>添加菜单</em>
		</a>
	</div>
</div>

<div class="pad-lr-10">
	<form name="searchform" action="" method="get">
		<table width="100%" cellspacing="0" class="search-form">
			<tbody>
				<tr>
					<td>
						<div class="explain-col">
							链接分类 :
							<!--<select name="group_id" style="width:140px;">
								<option value="" 
									<if condition="$group_id eq ''"> selected="selected" </if>
									>--所有导航--
								</option>
								<volist name="group_list" id="val">
									<option value="{$val.id}" 
										<if condition="$group_id eq $val['id']"> selected="selected" </if>
										>{$val.title}
									</option>
								</volist>
							</select>-->
							<input type="hidden" name="m" value="node" />
							<input type="submit" name="search" class="button" value="搜索" />
							<font color=red>（警告：没事非专业人员请不要操作这里，会出乱子的噢@^^@）</font>
						</div>
					</td>
				</tr>
			</tbody>
		</table>
	</form>

	<form id="myform" name="myform" action="{{ config.admin_dir }}/node/delete"
		method="post" onsubmit="return check();">
		<div class="table-list">
			<table width="100%" cellspacing="0">
				<thead>
					<tr>
						<th width="40">
							<input type="checkbox" value="" id="check_box" onclick="selectall('id');">
						</th>
						<th width="40">ID</th>
						<th width="40">名称</th>
						<th width="40">level</th>
						<th width="40">parent_id</th>
						<th width="40">parent</th>
						<th width="40">排序</th>
						<th width="40">状态</th>
						<th width="40">管理</th>
					</tr>
				</thead>
				<tbody>
					{% if node_list is not None %}
					{% set i = 1%}
					{% for node in node_list %}
					<tr>
						<td align="center">
							<input type="checkbox" value="{{ node.id }}" name="id">
						</td>
						<td align="center">{{node.id}}</td>
						<td align="center">
							<font color=blue>{{node.name}}</font>
						</td>
						<td align="center">{{node.level}}</td>
						<td align="center">
							<b>{% if node.parent %}{{node.parent.id}}{% end %}</b>
						</td>
						<td align="center">
							<b>{% if node.parent %}{{node.parent.name}}{% end %}</b>
						</td>
						<td align="center">
							<input type="text" class="input-text-c input-text" value="{{node.sort}}"
								size="4" name="listorders[{{node.id}}]">
						</td>
						<td align="center" onclick="status({{node.id}},'status')" id="status_{{node.id}}">
							<img src="/statics/admin/images/status_{{node.is_show}}.gif" />
						</td>
						<td align="center">
							<a href="javascript:edit({{node.id}},'{{node.name}}')">编辑</a>
						</td>
					</tr>
					{% end %}
					{% end %}
				</tbody>
			</table>

			<div class="btn">
				<label for="check_box">{{ config.lang_select_all }} / {{ config.lang_cancel }}</label>
				<input type="submit" class="button" name="dosubmit"
					value="{{ config.lang_delete }}" onclick="return confirm('{{ config.lang_sure_delete }}')" />
					{% if p is not None %}
					<div class="pagination">
						{% if p.has_pre()%}
						<a href="/{{config.admin_dir_name}}/node/list/1">首页</a>
						<a href="/{{config.admin_dir_name}}/node/list/{{p.cur - 1}}">&lt;</a>
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
							<a href="/{{config.admin_dir_name}}/node/list/{{n}}">{{n}}</a>
							{% end %}
						{% end %}
						{% end %}
						{% if p.has_right_point() %}
						<span class="omit">...</span>
						{% end %}
						{% if p.has_next() %}
						<a href="/{{config.admin_dir_name}}/node/list/{{p.cur + 1}}">&gt;</a>
						<a href="/{{config.admin_dir_name}}/node/list/{{p.get_page_count()}}">尾页</a>
						{% end %}		
					</div>
					{% end %}
			</div>
		</div>
	</form>
</div>

<script language="javascript">
function edit(id, name) {
	var lang_edit = "{{config.lang_edit}}";
	window.top.art.dialog({id:'node_edit'}).close();
	window.top.art.dialog({title:lang_edit+'--'+name,id:'node_edit',iframe:'{{config.admin_dir}}/node/edit/'+id,width:'500',height:'480'}, function(){var d = window.top.art.dialog({id:'node_edit'}).data.iframe;d.document.getElementById('dosubmit').click();return false;}, function(){window.top.art.dialog({id:'node_edit'}).close()});
}
function check(){
	var ids='';
	$("input[name='id']:checked").each(function(i, n){
		ids += $(n).val() + ',';
	});

	if(ids=='') {
		window.top.art.dialog({content:'请选择需要操作的菜单',lock:true,width:'200',height:'50',time:1.5},function(){});
		return false;
	}
	return true;
}
function status(id,type){
    $.get("{:u('node/status')}", { id: id, type: type }, function(jsondata){
		var return_data  = eval("("+jsondata+")");
		$("#"+type+"_"+id+" img").attr('src', '/statics/images/status_'+return_data.data+'.gif');
	}); 
}
</script>

{% end %}
