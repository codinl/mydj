# -*- coding:Utf-8 -*-

from account.signals import user_logged_in
from base import time_util
from base.models_base import PageModel
from base.util import get_client_ip
from django.contrib.auth.hashers import check_password
from django.db import models
from django.utils.translation import ugettext_lazy as _
import config
import time

#更新登录信息
def update_last_login(sender, request, user, **kwargs):
    user.last_login_time = time.time()
    user.login_times += 1
    user.last_login_ip = get_client_ip(request)
    user.is_active = True
    user.save()
    
#登录消息处理
user_logged_in.connect(update_last_login)
    
class User(PageModel):
#    GENDER_CHOICES = (
#        ('M', 'Male'),
#        ('F', 'Female'),
#    )
    username = models.CharField(max_length=50, unique=True, help_text=_('字母、数字或下划线组成，长度小于20个字符'), blank=True)
    tel = models.CharField(max_length=20,blank=True)
    qq = models.CharField(max_length=13,blank=True)
    password = models.CharField(max_length=128)
    
    regist_ip = models.IPAddressField(blank=True, null=True)
    regist_time = models.PositiveIntegerField(default=time_util.get_now_second())
    invite_uid = models.IntegerField(default=0)
    login_times = models.IntegerField(default=1)
    last_login_time = models.PositiveIntegerField(default=time_util.get_now_second())
    last_login_ip = models.IPAddressField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
#    alipay = models.CharField(max_length=50,blank=True)
#    gender = models.CharField(max_length=30,choices=GENDER_CHOICES)
    
#    invite_code = models.CharField(max_length=20, blank=True)                  # 邀请码
#    invite_count = models.IntegerField(default=0)                              #共邀请人数
#    invite_shop_count = models.IntegerField(default=0)                         #邀请人购物人数

    # 应用市场用户id
    uid = models.CharField(max_length=30,unique=True,default=0)
    market = models.ForeignKey("conf.Market",null=True)
    # 应用市场用户的nickname
#     nickName = models.CharField(max_length=20,null=True,blank=True)
    # 玩家角色名 初始为空
    rolename = models.CharField(max_length=20,null=True,blank=True)
    # 是否已经有了初始武将
    has_general = models.BooleanField(default=False)
    
    tutorial_mission = models.PositiveSmallIntegerField(default=0)    # 完成任务新手导航次数
    tutorial_package = models.PositiveSmallIntegerField(default=0)    
    tutorial_battle = models.PositiveSmallIntegerField(default=0)     #
    tutorial_rob = models.PositiveSmallIntegerField(default=0)        #
    tutorial_intensify = models.PositiveSmallIntegerField(default=0)
    tutorial_mall = models.PositiveSmallIntegerField(default=0)
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __unicode__(self):
        return self.username
    
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
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True
    
    @classmethod
    def get_user(cls, uid):
        try:
            return cls.objects.get(pk=uid)
        except Exception,e:
            if config.debug:
                print e
        return None
        
    @classmethod
    def get_by_username(cls, username):
        try:
            return cls.objects.get(username=username)
        except Exception,e:
            if config.debug:
                print e
        return None
    
       
#    @classmethod
#    def get_user_email(cls,email):
#        try:
#            return cls.objects.get(email=email)
#        except:
#            return None
    
#    @classmethod
#    def get_by_invite_code(cls, invite_code):
#        try:
#            return cls.objects.get(invite_code=invite_code)
#        except:
#            return None
#        
#    def gen_invite_code(self):
#        ''' 生成邀请码 '''
#        return hex(self.id + 10000)
#    
#    @classmethod
#    def get_list(cls, page=1, page_size=15):
#        try:
#            return User.objects.order_by('-id')[(page - 1) * page_size:page * page_size]
#        except Exception, e:
#            return None
#        
#    @classmethod
#    def get_count(cls):
#        try:
#            return cls.objects.all().count()
#        except Exception, e:
#            return 0
    
     
class AnonymousUser(object):
#    uid = None
#    username = ''
#    is_staff = False

    def __init__(self):
        pass

    def __unicode__(self):
        return 'AnonymousUser'

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

#class Invite(models.Model):
#    invite_user = models.ForeignKey("User", related_name="i_invite_user")   # 邀请人
#    to_user = models.ForeignKey("User", related_name="i_to_user")           # 被邀请人
#    join_time = models.DateTimeField(default=datetime.datetime.now())      # 产生时间
#    
#    @classmethod
#    def get_invite_list(cls, invite_user, page=1, page_size=15):
#        try:
#            return cls.objects.filter(invite_user=invite_user)[(page - 1) * page_size:page * page_size]
#        except:
#            return None
#        
#    @classmethod
#    def get_invite_count(cls, invite_user):
#        try:
#            return cls.objects.filter(invite_user=invite_user).count()
#        except:
#            return 0

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
