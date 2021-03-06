{% extends base.tpl %}

{% block content %}
<div class="pad-10" id="home_panel">
	<div class="clearfix">
        <div class="col-2 fl">
            <h6>我的个人信息</h6>
            <div class="content">
                您好，{admin.user_name}<br>
                所属角色：{role.name} <br>
            </div>
        </div> 
        <div class="col-2 fr">
            <h6>工作提示</h6>
            <div class="content" style="color:#ff0000;">
                <volist name="security_info" id="v">
                ※{$v}<br/>
                </volist>
            </div>
        </div>               
    </div>
	<div class="clearfix">
        <div class="col-2 fl">
            <h6>系统信息</h6>
            <div class="content">
                <table class="table_panel">
                    <tbody>
                    <volist name="server_info" id="v">
                    <tr>
                        <th>{$key}：</th>
                        <td>{$v}</td>
                    </tr>
                    </volist>
                    </tbody>
                </table>
            </div>
        </div>   
    </div>
</div>
{% end %}