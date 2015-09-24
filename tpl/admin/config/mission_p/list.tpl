{% extends "../../base.tpl" %}

{% block content %}
<div class="pad-lr-10">
	<form id="myform" name="myform">
		<div class="table-list">
			<table width="100%" cellspacing="0">
				<thead>
					<tr>
						{% if p_list %}
						{% for p in p_list %}
						<th width=60>{{p.name}}-{{p.key}}</th>
						{% end %}
						{% end %}
						<th width=80>操作</th>
					</tr>
				</thead>
				<tbody>
					<tr>
						{% if p_list %}
						{% for p in p_list %}
						<td align="center">{{p.value}}</td>
						{% end %}
						{% end %}
						<td align="center">
							<a href="javascript:edit();">{{config.lang_edit}}</a>
						</td>
					</tr>
				</tbody>
			</table>
		</div>
	</form>
</div>

<script language="javascript">
function edit() {
	var lang_edit = "{{config.lang_edit}}";
	window.top.art.dialog({title:lang_edit+'--'+name,id:'config_mission_p_edit',iframe:'/{{config.admin_dir_name}}/config/mission_p/edit',width:'480',height:'250'}, function(){var d = window.top.art.dialog({id:'config_mission_p_edit'}).data.iframe;d.document.getElementById('dosubmit').click();return false;}, function(){window.top.art.dialog({id:'config_mission_p_edit'}).close()});
}
</script>
{% end %}