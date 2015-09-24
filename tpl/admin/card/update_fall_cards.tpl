{% extends "../base.tpl" %}

{% block content %}
<div class="subnav">
	<div class="content-menu ib-a blue line-x">
		<a class="add fb" href="javascript:update_mission_fall_cards();">
			<em>更新任务掉落卡牌</em>
		</a>
	</div>
	<div class="content-menu ib-a blue line-x">
		<a class="add fb" href="javascript:update_battle_fall_cards();">
			<em>更新战斗掉落卡牌</em>
		</a>
	</div>
	<!--<div class="content-menu ib-a blue line-x">
		<a class="add fb" href="javascript:update_all_cards();">
			<em>刷新所有卡牌</em>
		</a>
	</div>-->
</div>

<script type="text/javascript">
	function update_all_cards(){
		$.ajax({
			url:"{{config.admin_dir}}/fall_cards/update/all",
			type:"post",
			success:function(data){
				if(data=="1"){
					alert("更新成功");
				}else{
					alert("更新失败");
				}
			}
		});
	}
	function update_mission_fall_cards(){
		$.ajax({
			url:"{{config.admin_dir}}/fall_cards/update/mission",
			type:"post",
			success:function(data){
				if(data=="1"){
					alert("更新成功");
				}else{
					alert("更新失败");
				}
			}
		});
	}
	function update_battle_fall_cards(){
		$.ajax({
			url:"{{config.admin_dir}}/fall_cards/update/battle",
			type:"post",
			success:function(data){
				if(data=="1"){
					alert("更新成功");
				}else{
					alert("更新失败");
				}
			}
		});
	}
</script>
{% end %}