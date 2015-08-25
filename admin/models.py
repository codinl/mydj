# -*- coding:Utf-8 -*-

from django.db import models
import config

class Node(models.Model):
    url = models.CharField(max_length=50,unique=True)
    name = models.CharField(max_length=50,db_index=True)
    level = models.PositiveSmallIntegerField(default=3)  # 级别: 1 菜单  2 组  3 操作
    parent = models.ForeignKey("Node",null=True)
    sort = models.PositiveSmallIntegerField()
    is_often = models.BooleanField(default=True)
    is_show = models.BooleanField(default=True)
    descr = models.CharField(max_length=50,blank=True)
    
    @classmethod
    def get_list(cls,page=1,page_size=20):
        try:
            return Node.objects.order_by('sort')[(page-1)*page_size:page*page_size]
        except Exception,e:
            if config.debug:
                print e
        return None
    
    @classmethod
    def get_by_id(cls,_id):
        try:
            return Node.objects.get(pk=_id)
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
    def get_level(cls,level=1):
        try:
            return cls.objects.filter(level=level).order_by('sort')
        except Exception,e:
            if config.debug:
                print e
            return 0
    
    def get_children(self):
        try:
            return Node.objects.filter(parent=self).order_by('sort')
        except Exception,e:
            if config.debug:
                print e
        return None
    
    @classmethod
    def delete_by_ids(cls,ids):
        try:
            Node.objects.extra(where=['id IN ('+ids+')']).delete()
        except Exception,e:
            if config.debug:
                print e

