# -*- coding: utf-8 -*-

from django.db import models
import config

#专门提供有翻页查询的类继承，提供常用查询函数
class PageModel(models.Model):
    #基类model不会创建数据表
    class Meta:
        abstract = True
    
    @classmethod
    def get_by_id(cls,_id):
        try:
            return cls.objects.get(pk=_id)
        except Exception,e:
            if config.debug:
                print e
            return None
    
    @classmethod
    def get_list(cls,page=1,page_size=config.default_page_size):
        page = int(page)
        page_size = int(page_size)
        try:
            return cls.objects.all()[(page-1)*page_size:page*page_size]
        except Exception,e:
            if config.debug:
                print e
        return None
    
    @classmethod
    def get_count(cls):
        try:
            return cls.objects.all().count()
        except Exception,e:
            if config.debug:
                print e
        return 0
    
    @classmethod
    def get_all(cls):
        try:
            return cls.objects.all()
        except Exception,e:
            if config.debug:
                print e
        return None
    
    def get_class_name(self):
        return self.__class__.__name__
        