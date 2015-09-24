{% extends "../base.tpl" %}

{% block content %}
<script language="javascript" type="text/javascript" src="__ROOT__/statics/js/jquery/jquery.role.js"></script>
<div class="pad-lr-10">
    <form id="myform" name="myform" action="{{config.admin_dir}}/admin/role/delete/{{p.cur}}" method="post" onsubmit="return check();">
    <div class="table-list">
	    <table width="100%" cellspacing="0">
	        <thead>
	            <tr>
	                <th width="20"><input type="checkbox" value="" id="check_box" onclick="selectall('id[]');"></th>
	                <th width="50">编号</th>
	                <th width="200">组名</th>
	                <th>描述</th>
	      			<th width="60">状态</th>
	                <th width="80">操作</th>
	            </tr>
	        </thead>
	    	<tbody>
	        {% if role_list %}
	        {% for role in role_list %}
	        <tr>
	            <td align="center"><input type="checkbox" value="{{role.id}}" name="id[]"></td>
	            <td align="center">{{role.id}}</td>
	            <td align="center">{{role.name}}</td>
	            <td align="center">{{role.description}}</td>
	            <td align="center" onclick="status({$val.id},'status')" id="status_{$val.id}"><img src="/statics/admin/images/status_{{role.is_active}}.gif".gif"</td>
	            <td align="center"><a href="role/auth/{{role.id}}">授权</a> | <a href="javascript:edit({$val.id},'{$val.name}')">{$Think.lang.edit}</a></td>
	        </tr>
	        {% end %}
	        {% end %}
	    	</tbody>
	    </table>

    	<div class="btn">
	    	<label for="check_box" style="float:left;">{{config.lang_select_all}}/{{config.lang_cancel}}</label>
	    	<input type="submit" class="button" name="dosubmit" value="{{config.lang_delete}}" onclick="return confirm('{{config.lang_sure_delete}}')" style="float:left;margin-left:10px;"/>
		    <div id="pages">
		    	 {% if p %}
				 <div class="pagination">
					{% if p.has_pre()%}
					<a href="/{{config.admin_dir_name}}/admin/role/list/1">{{config.lang_index}}</a>
					<a href="/{{config.admin_dir_name}}/admin/role/list/{{p.cur-1}}">&lt;</a>
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
						<a href="/{{config.admin_dir_name}}/admin/role/list/{{n}}">{{n}}</a>
						{% end %}
					{% end %}
					{% end %}
					{% if p.has_right_point() %}
					<span class="omit">...</span>
					{% end %}
					{% if p.has_next() %}
					<a href="/{{config.admin_dir_name}}/admin/role/list/{{p.cur+1}}">&gt;</a>
					<a href="/{{config.admin_dir_name}}/admin/role/list/{{p.get_page_count()}}">{{config.lang_last_page}}</a>
					{% end %}		
				</div>
				{% end %}
		    </div>
    	</div>
    </div>
    </form>
</div>
<script language="javascript">
function edit(id, name) {
	var lang_edit = "编辑";
	window.top.art.dialog({id:'edit'}).close();
	window.top.art.dialog({title:lang_edit+'--'+name,id:'edit',iframe:'?m=role&a=edit&id='+id,width:'400',height:'220'}, function(){var d = window.top.art.dialog({id:'edit'}).data.iframe;d.document.getElementById('dosubmit').click();return false;}, function(){window.top.art.dialog({id:'edit'}).close()});
}

function check(){
	var ids='';
	$("input[name='id[]']:checked").each(function(i, n){
		ids += $(n).val() + ',';
	});

	if(ids=='') {
		window.top.art.dialog({content:'请选择你需要操作的角色',lock:true,width:'200',height:'50',time:1.5},function(){});
		return false;
	}
	return true;
}

function status(id,type){
    $.get("{:u('role/status')}", { id: id, type: type }, function(jsondata){
		var return_data  = eval("("+jsondata+")");
		$("#"+type+"_"+id+" img").attr('src', '__ROOT__/statics/images/status_'+return_data.data+'.gif');
	}); 
}
</script>
{% end %}