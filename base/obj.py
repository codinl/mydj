# -*- coding: utf-8 -*-

from card.models import Card
import config
import cPickle as pickle
import random


class ProbabilityModel():
    def __init__(self,name,key,value):
        self.name = name
        self.key = key
        self.value = value


class Probability():
    def __init__(self):
        self.default_p_list = []
        self.p_list = None
        self.file_name = ""
        
    def _get_file(self):
        file_dir = config.project_dir +"/base/data/"
        return file_dir + self.file_name
        
    def dump_data(self):
        return pickle.dump(self.p_list,open(self._get_file(),"wb"))
        
    def get_p_list(self):
        try:
            self.p_list = pickle.load(open(self._get_file(),"rb"))
        except Exception,e:
            print e
            self.p_list = self.default_p_list
            self.dump_data()
        return self.p_list
    
    def set_p_value(self,name,key,value):
        p_list = self.get_p_list()
        for p in p_list:
            if key == p.key:
                p.value = value
                p.name = name
                break
        self.dump_data()
    
    def get_rand_name(self):
        p_list = self.get_p_list()
        rand_i = random.randint(1, 100)
        for i in range(0,len(p_list)):
            p = p_list[i]
            if rand_i <= self._sum_p_value(p_list,i):
                return p.key
            
    def _sum_p_value(self,p_list,i):
        _sum = 0
        for a in range(0,i+1):
            _sum += p_list[a].value
        return _sum


class MissionProbability(Probability):
    def __init__(self):
        self.default_p_list = [ProbabilityModel(u"卡牌","card",50),ProbabilityModel(u"经验","xp",20),
                               ProbabilityModel(u"银币","vm",20),ProbabilityModel(u"无","nothing",10)]
        self.file_name = "MissionProbability.pkl"


class CardModel():
    def __init__(self,card_id,card_type):
        self.card_id = card_id
        self.card_type = card_type


#随机抽选        
class FallCard():
    def __init__(self):
        self.count = 0
        self.card_list = []
        self.file_name = ""
        
    def _get_file(self):
        file_dir = config.project_dir +"/base/data/"
        return file_dir + self.file_name
        
    def _get_dict(self):
        _dict = {"count":self.count,"card_list":self.card_list}
        return _dict
    
    #初始化，从数据库导入  c_list 对应的是星级小于4的卡牌
    def init(self):
        pass
    
    def dump_data(self):
        return pickle.dump(self._get_dict(),open(self._get_file(),"wb"))
    
    def _load_data(self):
        try:
            data = pickle.load(open(self._get_file(),"rb"))
        except Exception,e:
            print e
            self.init()
            data = self._get_dict()
        return data
    
    def load_card_list(self):
        data = self._load_data()
        card_list = data['card_list']
        return card_list
    
    def get_rand_card(self):
        card_list = self.load_card_list()
        top = len(card_list) - 1
        card = card_list[0]
        if top > 0:
            rand_i = random.randint(1, top)
            card = card_list[rand_i]
        return card


#任务随机掉落卡牌        
class MisssionFallCard(FallCard):
    def __init__(self):
        FallCard.__init__(self)
        self.file_name = "MisssionFallCard.pkl"
        
    #初始化，从数据库导入  c_list 对应的是星级小于1-3的卡牌
    def init(self):
        c_list = Card.get_mission_fall_cards()
        if c_list:
            card_list = []
            for c in c_list:
                card = CardModel(c.r_card_id,c.card_type)
                card_list.append(card)
            count = len(card_list)
            mfc = MisssionFallCard()
            mfc.count = count
            mfc.card_list = card_list
            mfc.dump_data()


#战斗随机掉落卡牌        
class BattleFallCard(FallCard):
    def __init__(self):
        FallCard.__init__(self)
        self.file_name = "BattleFallCard.pkl"
        
    #初始化，从数据库导入  c_list 对应的是星级小于1-3的卡牌
    def init(self):
        c_list = Card.get_battle_fall_cards()
        if c_list:
            card_list = []
            for c in c_list:
                card = CardModel(c.r_card_id,c.card_type)
                card_list.append(card)
            count = len(card_list)
            bfc = BattleFallCard()
            bfc.count = count
            bfc.card_list = card_list
            bfc.dump_data()
    
#def test():
#    card_count = 0
#    xp_count = 0
#    vm_count = 0
#    nothing_count = 0
#    card = "card"
#    xp = "xp"
#    vm = "vm"
#    nothing = "nothing"
#    mp = MissionProbability()
##    mp.p_list = [Probability("card",50),Probability("xp",20),Probability("vm",20),Probability("nothing",10)]
##    mp.dump_data()
#    for _ in range(1,10000):
#        t = mp.get_rand_name()
#        if t == card:
#            card_count += 1
#        elif t == xp:
#            xp_count += 1
#        elif t == vm:
#            vm_count += 1
#        elif t == nothing:
#            nothing_count += 1
#    print "card_count",card_count
#    print "xp_count",xp_count
#    print "vm_count",vm_count
#    print "nothing_count",nothing_count

#test()       

#sc = MisssionFallCard()
#sc.init()
#print sc._load_data()


        
        
        
        
        
        
        
