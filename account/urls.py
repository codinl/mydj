from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^market$', 'account.views.market', name='account_market'),
    url(r'^set_rolename$', 'account.views.set_rolename', name='account_set_rolename'),
    url(r'^select_general$', 'account.views.select_general', name='account_select_general'),
    url(r'^login$', 'account.views.login', name='account_login'),
#     url(r'^register$', 'account.views.register', name='account_register'),
    url(r'^logout','account.views.logout',name="account_logout"),
#    url(r'^toinvite','account.views.toinvite',name="account_toinvite"),
    
#    url(r'^valid/email','account.views.ajax_email_valid',name="account_ajax_email_valid"),
#    url(r'^home$', 'admin.views.home', name='admin_home'),
#    url(r'^share$', 'admin.views.share_check', name='share_check'),
#    url(r'^add_cate$', 'admin.views.add_category', name='add_cate'),
)