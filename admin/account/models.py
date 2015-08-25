# -*- coding: utf-8 -*-

from admin.account.signals import admin_logged_in
from base.util import get_client_ip
from django.contrib.auth.hashers import check_password
from django.db import models
from django.utils.translation import ugettext_lazy as _
import config
import datetime

#更新登录信息
def update_last_login(sender, request, admin, **kwargs):
    admin.last_login_time = datetime.datetime.now()
    admin.login_times += 1
    admin.last_login_ip = get_client_ip(request)
    admin.save()
    
#登录消息处理
admin_logged_in.connect(update_last_login)

#class Role(models.Model):
#    name = models.CharField(max_length=20, unique=True)
#    description = models.CharField(max_length=100)
#    create_time = models.DateTimeField(default=datetime.datetime.now())
#    update_time = models.DateTimeField(default=datetime.datetime.now())
#    is_active = models.BooleanField(default=True)

class Admin(models.Model):
    name = models.CharField(max_length=20, unique=True, help_text=_('字母、数字或下划线组成，长度小于20个字符'))
    password = models.CharField(max_length=128)
#    email = models.EmailField()
#    tel = models.CharField(max_length=20,blank=True)
#    qq = models.CharField(max_length=13,blank=True)
#    role = models.ForeignKey("Role")
    
    login_times = models.IntegerField(default=1)
    last_login_time = models.DateTimeField(default=datetime.datetime.now())
    last_login_ip = models.IPAddressField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = _('admin')
        verbose_name_plural = _('admins')

    def __unicode__(self):
        return self.name
    
    def check_password(self, raw_password):
        """
        Returns a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            self.set_password(raw_password)
            self.save()
        return check_password(raw_password, self.password, setter)
    
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the admin has been
        authenticated in templates.
        """
        return True
    
    @classmethod
    def get_admin(cls, uid):
        try:
            return cls.objects.get(pk=uid)
        except:
            return None
        
    @classmethod
    def get_count(cls):
        try:
            return cls.objects.all().count()
        except Exception,e:
            print e
        return 0
    
    @classmethod
    def get_list(cls,cur_page=1,page_size=config.default_page_size):
        try:
            return cls.objects.all()[(cur_page-1)*page_size:cur_page*page_size]
        except Exception,e:
            print e
        return None
    
     
class AnonymousAdmin(object):

    def __init__(self):
        pass

    def __unicode__(self):
        return 'AnonymousAdmin'

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __eq__(self, other):
        return isinstance(other, self.__class__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return 1 # instances always return the same hash value

    def save(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError

    def set_password(self, raw_password):
        raise NotImplementedError

    def check_password(self, raw_password):
        raise NotImplementedError

    def is_anonymous(self):
        return True

    def is_authenticated(self):
        return False
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
