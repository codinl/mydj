# -*- coding: utf-8 -*- 

from django.conf.urls import patterns, url, include
import config

urlpatterns = patterns('',
    # url(r'^$', 'home.views.home',name="home"),
    
#     url(r'^home/', include('home.urls')),

    url(r'^account/', include('account.urls')),

#     url(r'^pay/callback$', 'mall.views.pay_callback',name="mall_pay_callback"),
# 
    url(r'^backstrong/', include('admin.urls')),

    (r'^statics/(?P<path>.*)$', 'django.views.static.serve', {'document_root': config.project_statics_dir}),
)

handler404 = 'home.views.page_not_found'
handler500 = 'home.views.page_error'

