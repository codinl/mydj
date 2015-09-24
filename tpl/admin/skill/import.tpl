{% extends "../base.tpl" %}

{% block content %}
<div class="pad-lr-10">
	<form enctype="multipart/form-data" method="POST" action="{{config.admin_dir}}/skill/import">
		<br/>
		<input type="file" name="import_file" /><br/><br/>
		<input type="submit" value="导入技能" />
	</form>
</div>
{% end %}