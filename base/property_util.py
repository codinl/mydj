# -*- coding:Utf-8 -*-
import random

# 概率发生函数
def get_p_result(p_value):
    if p_value >= 1:
        return True
    if p_value <= 0:
        return False
    r_num = gen_rand_num()
    if r_num <= p_value * 100:
        return True
    return False

def gen_rand_num(min_num=1, max_num=100):
    return random.randint(min_num, max_num)

#def test():
#    is_true = 0
#    for i in range(0,1000):
#        if get_p_result(0.55):
#            is_true += 1
#    print is_true
#    
#test()
        