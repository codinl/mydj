# -*- coding:Utf-8 -*-
#
# from account import login as auth_login, logout as auth_logout, authenticate
# from account.forms import RoleNameForm
# from account.models import User
# from base import string_util
# from base.util import get_client_ip
# # from card.models import PlayerGeneral, PlayerCard
# # from conf.models import Market
# from django.contrib.auth.hashers import make_password
# from django.http import HttpResponse
# from django.shortcuts import redirect
# from django.shortcuts.render import render_response
# # from player.models import Player
# # from slot.models import BaseSlot
# import config
# import sys
# import urllib
#
# SESSION_KEY = '_auth_user_id'
# BACKEND_SESSION_KEY = '_auth_user_backend'
# REDIRECT_FIELD_NAME = 'next'
#
# # 设置角色名称
# def set_rolename(request,template='user/set_rolename.tpl'):
#     if request.method == 'POST':
#         form = RoleNameForm(request.POST)
#         if form.is_valid():
#             rolename = form.cleaned_data['rolename']
#             if not isinstance(rolename, unicode):
#                 _rolename = rolename.decode(sys.stdin.encoding).encode("utf-8")
# #                 _rolename_len = len(_rolename)
# #             if _rolename_len <= config.rolename_maxlength:
#             if _check_rolename(rolename):
#                 if _rolename_not_exists(rolename):
#                     user = request.user
#                     if user and user.is_authenticated():
#                         user.rolename = rolename
#                         try:
#                             user.save()
#                         except Exception,e:
#                             if config.debug:
#                                 print e
#                             form.errors['msg'] = u"亲～～,失败啦，请重试.."
#                         else:
#                             # 跳转到选择初始武将
#                             return select_general(request)
#                 # 角色名已经被使用
#                 else:
#                     form.errors['msg'] = u"亲，角色名已经被使用～～"
#             else:
#                 form.errors['msg'] = u"亲，角色名不正确～～"
# #             else:
# #                 form.errors['msg'] = u"亲，角色名太长啦～～"
#         else:
#             form.errors['msg'] = u"亲，角色名不正确～～"
#         if form.errors:
#             return render_response(template, form=form)
#     return render_response(template, form=None)
#
# # 选择初始武将
# def select_general(request,template='user/select_general.tpl'):
#     general_id = request.GET.get("general_id")
#     if general_id:
#         user = request.user
#         if user and user.is_authenticated():
#             if user.has_general:
#                 return user_login(request,user.username)
#             user.has_general = True
#             try:
#                 player_id = _init_player(user, general_id)
#                 if player_id:
#                     user.save()
#             except Exception, e:
#                 if config.debug:
#                     print e
#             else:
#                 return user_login(request,user.username)
#     return render_response(template)
#
# # 第三方市场账号登录
# def market(request, template=''):
#     if request.method == 'GET':
#         market_name = request.GET.get("market_name")
#         uid = request.GET.get("uid")
#         session_id = request.GET.get("session_id")
#         if not market_name or not uid or not session_id:
#             return HttpResponse(u"error，网络错误")
#         username = market_name + "-" + uid
#         user = authenticate(username=username,password="pp654321xy")
#         # 用户已经存在
#         if user and user.is_authenticated():
#             auth_login(request,user)
#             # 已经拥有角色名
#             if user.rolename:
#                 # 已经有了初始武将
#                 if user.has_general:
#                     return user_login(request, username)
#                 # 没有则跳转到武将选择页面
#                 else:
#                     return select_general(request)
#             # 没有角色名则跳转到设置角色名
#             else:
#                 return set_rolename(request)
#         # 用户不存在 “注册”一个
#         else:
#             return add_user(request, market_name, uid)
#
# def add_user(request, market_name, uid, pwd="pp654321xy"):
#     username = market_name + "-" + uid
#     if _username_not_exists(username):
#         ip = get_client_ip(request)
#         user = User.objects.create(username=username, uid=uid)
#         if market_name:
#             market = Market.get_by_ename(market_name)
#             if market:
#                 user.market = market
#         password = make_password(pwd)
#         user.password = password
#         user.regist_ip = ip
#         user.last_login_ip = ip
#         try:
#             user.save()
#         except Exception, e:
#             if config.debug:
#                 print e
#         else:
#             if request.user.is_authenticated():
#                 logout(request)
#             user = authenticate(username=username,password=pwd)
#             auth_login(request,user)
#             if not request.user or not request.user.is_authenticated():
#                 request.user = user
#             return set_rolename(request)
#
# def user_login(request,username,pwd="pp654321xy"):
#     user = authenticate(username=username, password=pwd)
#     if user and user.is_authenticated():
#         auth_login(request, user)
#         _rolename = user.rolename
#         if isinstance(_rolename, unicode):
#             _role_name = (_rolename).encode('utf-8')
#         _role_name = urllib.quote(_role_name)
#         _serverName = config.server_name
#         if isinstance(_serverName, unicode):
#             _serverName = (_serverName).encode('utf-8')
#         _serverName = urllib.quote(_serverName)
#         url = "/?playerId=%s&roleName=%s&serverName=%s" %(user.id,_role_name,_serverName)
#         if (user.tutorial_mission<2):
#             url = "/?is_new=yes&playerId=%s&roleName=%s&serverName=%s" %(user.id,_role_name,_serverName)
#         return redirect(url)
#     else:
#         return market(request)
#
# # def register(request,template='user/register.tpl'):
# #     next_url = request.GET.get("next")
# #     if request.method == 'POST':
# #         form = RegistForm(request.POST)
# #         if form.is_valid():
# #             username = form.cleaned_data['username']
# #             if len(username) > 2:
# #                 if _username_not_exists(username):
# #                     pwd = form.cleaned_data['password']
# #                     repwd = form.cleaned_data['repassword']
# #                     qq = form.cleaned_data['qq']
# #                     tel = form.cleaned_data['tel']
# #                     if len(pwd) < 5:
# #                         form.errors['msg'] = u"密码不能少于5个字符"
# #                     if pwd != repwd:
# #                         form.errors['msg'] = u"两次密码不一致！"
# #                     qq_str = str(qq)
# #                     if qq and (len(qq_str) > 13 or len(qq_str) < 5):
# #                         form.errors['msg'] = u"QQ号格式不正确！"
# #                     if tel and (len(str(tel)) != 11):
# #                         form.errors['msg'] = u"手机号格式不正确！"
# #                     if not form.errors:
# #                         ip = get_client_ip(request)
# #                         user = User.objects.create()
# #                         user.username = username
# #                         if qq:
# #                             user.qq = qq
# #                         if tel:
# #                             user.tel = tel
# #                         password = make_password(pwd)
# #                         user.password = password
# #                         user.regist_ip = ip
# #                         user.last_login_ip = ip
# #                         try:
# #                             user.save()
# # #                             _create_player(user)
# #                         except Exception,e:
# #                             if config.debug:
# #                                 print e
# #                             form.errors['msg'] = u"注册失败，请重试"
# #                         else:
# #                             if request.user.is_authenticated():
# #                                 logout(request)
# #                             user = authenticate(username=username,password=pwd)
# #                             auth_login(request,user)
# #                             if next_url:
# #                                 response = redirect(next_url)
# #                             else:
# #                                 # 跳转到设置角色名
# #                                 response = redirect("/")
# #                             #设置用户id到cookie里面，有效期6个月
# # #                            response.set_cookie("uid",user.id,max_age=60 * 60 * 24 * 30 * 12)
# #                             return response
# #                 else:
# #                     form.errors['msg'] = u"亲，用户名已经被注册～～"
# #             else:
# #                 form.errors['msg'] = u"帐号名太短，不能少于3个字符"
# #         else:
# #             form.errors['msg'] = u"输入信息不合法，请重试"
# #     else:
# #         form = RegistForm()
# #     return render_response(template,form=form,request=request,next_url=next_url)
#
# def _init_player(user, general_id):
#     player = Player.objects.create(uid=user.id, name=user.rolename)
#     player.save()
#     _init_baseslot(player.id, general_id)
#     _init_player_card_part(player.id)
#     return player.id
#
# # 添加玩家初始baseslot,然后添加初始武将
# def _init_baseslot(player_id, general_id=1):
#     baseslot_id = BaseSlot.add_init_baseslot(player_id)
#     # 再添加一个空卡槽,位置递增一个为1
#     BaseSlot.add_baseslot(player_id, 1)
#     if baseslot_id:
#         _init_generals(player_id, general_id)
#
# # 添加玩家初始武将,然后初始化player_card
# def _init_generals(player_id, general_id):
#     player_general_id = PlayerGeneral.add_init_general(player_id, general_id=general_id)
#     if player_general_id:
#         _init_player_card(player_id, "General", general_id)
#
# # 添加初始武将卡牌
# def _init_player_card(player_id, card_type, r_card_id):
#     PlayerCard.add_init_player_card(player_id, card_type, r_card_id)
#
# # 添加初始碎片
# def _init_player_card_part(player_id):
#     for _ in range(0,config.init_cardpart_count):
#         PlayerCard.add_random_player_card(player_id,"TreasurePart")
#         PlayerCard.add_random_player_card(player_id,"SecretBookPart")
#
# # #@sensitive_post_parameters()
# # #@csrf_protect
# # #@never_cache
# # def login(request,template='user/login.tpl'):
# #     next_url = request.GET.get("next")
# #     if request.method == 'POST':
# #         form = LoginForm(request.POST)
# #         if form.is_valid():
# #             username = form.cleaned_data['username']
# #             pwd = form.cleaned_data['password']
# #             user = authenticate(username=username,password=pwd)
# #             if user:
# #                 auth_login(request,user)
# #                 if next_url:
# #                     response = redirect(next_url)
# #                 else:
# #                     response = redirect("/")
# #                 #设置用户id到cookie里面，有效期6个月
# # #                response.set_cookie("uid", user.id,max_age=60 * 60 * 24 * 30 * 12)
# #                 return response
# #             else:
# #                 form.errors['msg'] = u"登录失败：用户名或密码错误"
# #         else:
# #             form.errors['msg'] = u"输入信息格式不合法，请重试"
# #     else:
# #         form = LoginForm()
# #     return render_response(template,form=form,request=request,next_url=next_url)
#
# def logout(request):
#     next_url = request.GET.get('next')
#     auth_logout(request)
#     if next_url:
#         return redirect(next_url)
#     return market(request)
#
# # @login_required
# # def toinvite(request,template="user.toinvite.tpl"):
# #    user = request.user
# #    return render_response(template,request=request,user=user)
# #
# # def ajax_email_valid(request):
# #    if request.method == "POST":
# #        form = AjaxEmailValidForm(request.POST)
# #        if form.is_valid():
# #            email = form.cleaned_data['email']
# #            json = '{"result":"error","message":"该邮箱已被注册，请重新换一个"}'
# #            if _username_not_exists(email):
# #                json = '{"result":"ok","message":"该邮箱可以注册"}'
# #            return HttpResponse(json)
#
# def _username_not_exists(username):
#     ''' username 是否已经注册 没有返回 True '''
#     try:
#         user = User.objects.get(username=username)
#     except:
#         return True
#     else:
#         if user:
#             return False
#     return False
#
# def _rolename_not_exists(rolename):
#     ''' email 是否已经注册 没有返回 True '''
#     try:
#         player = Player.objects.get(name=rolename)
#     except:
#         return True
#     else:
#         if player:
#             return False
#     return False
#
# # 是否含有非法字符
# def _check_rolename(rolename):
#     # 不能网址
#     for s in ["www.",".com",".net",".cn"]:
#         if s in rolename:
#             return False
#     # 过滤敏感字符
#     from sensor_words import sensor_words as ss
#     for s in ss:
#         if string_util.to_unicode(rolename) == string_util.to_unicode(s):
#             return False
#     return True
