{% extends "../base.tpl" %}

{% block content %}
<div class="pad_10">
	<form action="" method="post" name="myform" id="myform">
		<table width="100%" cellpadding="2" cellspacing="1" class="table_form">
			<tr>
				<th width="100">url :</th>
				<td>
					<input type="text" name="url" id="url" class="input-text">
				</td>
			</tr>
			<tr>
				<th>名称 :</th>
				<td>
					<input type="text" name="name" id="name" class="input-text">
				</td>
			</tr>
			<tr>
				<th>级别 :</th>
				<td>
					<select name="level">
						<option value="3">3-操作</option>
						<option value="1">1-菜单</option>
						<option value="2">2-分组</option>
					</select>
				</td>
			</tr>
			<tr>
				<th>分组 :</th>
				<td>
					<select name="parent">
						<option value=""></option>
						{% if level_1_list is not None %}
						{% for level_1 in level_1_list %}
						<option value="{{level_1.id}}">{{level_1.id}}-{{level_1.name}}</option>
						{% set level_2_list = level_1.get_children()%}
						{% if level_2_list is not None %}
						{% for level_2 in level_2_list%}
						<option value="{{level_2.id}}">&nbsp;&nbsp;&nbsp;&nbsp;{{level_2.id}}-{{level_2.name}}</option>
						{% end %}
						{% end %}
						{% end %}
						{% end %}
					</select>
				</td>
			</tr>
			<tr>
				<th>排序 :</th>
				<td>
					<input type="text" name="sort" id="sort" class="input-text" />
				</td>
			</tr>
			<tr>
				<th>描述 :</th>
				<td>
					<textarea name="descr" cols="40" rows="4"></textarea>
				</td>
			</tr>
			<tr>
				<th>状态 :</th>
				<td>
					<input type="radio" name="is_show" class="radio_style" value="1"
						checked="checked">
                    &nbsp;有效&nbsp;&nbsp;&nbsp;
						<input type="radio" name="status" class="radio_style" value="0">
                    &nbsp;禁用
				</td>
			</tr>
		</table>
		<input type="submit" name="dosubmit" id="dosubmit" class="dialog" value=" ">
	</form>
</div>

{% end %}