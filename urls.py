# -*- coding: utf-8 -*- 

from django.conf.urls import patterns, url, include
import config

urlpatterns = patterns('',
    # url(r'^$', 'home.views.home',name="home"),
    
#     url(r'^home/', include('home.urls')),
#     url(r'^player/', include('player.urls')),
# #     url(r'^battle/', include('battle.urls')),
# #     url(r'^card/', include('card.urls')),
#     url(r'^mission/', include('mission.urls')),
#     url(r'^general/', include('general.urls')),
#     url(r'^equip/', include('equip.urls')),
#     url(r'^skill/', include('skill.urls')),

#     url(r'^intensify/', include('intensify.urls')),
#     url(r'^message/', include('message.urls')),
#     url(r'^mall/', include('mall.urls')),
#     
#     url(r'^package/', include('package.urls')),
#     url(r'^rank/', include('rank.urls')),
#     url(r'^rob/', include('rob.urls')),
#     url(r'^slot/', include('slot.urls')),
#     
#     url(r'^account/', include('account.urls')),
#     url(r'^qihoo/', include('qihoo.urls')),
#     
#     url(r'^pay/callback$', 'mall.views.pay_callback',name="mall_pay_callback"),
# 
    url(r'^backstrong/', include('admin.urls')),

    (r'^statics/(?P<path>.*)$', 'django.views.static.serve', {'document_root': config.project_statics_dir}),
)

handler404 = 'home.views.page_not_found'
handler500 = 'home.views.page_error'

