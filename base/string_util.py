# -*- coding:Utf-8 -*-

"""汉字处理的工具:
判断unicode是否是汉字，数字，英文，或者其他字符。
全角符号转半角符号。"""

def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'u4e00' and uchar <= u'u9fa5':
        return True
    else:
        return False
            
def is_number(uchar):
    """判断一个unicode是否是数字"""
    if uchar >= u'u0030' and uchar <= u'u0039':
        return True
    else:
        return False
    
def is_alphabet(uchar):
    """判断一个unicode是否是英文字母"""
    if (uchar >= u'u0041' and uchar <= u'u005a') or (uchar >= u'u0061' and uchar <= u'u007a'):
        return True
    else:
        return False
    
def is_other(uchar):
    """判断是否非汉字，数字和英文字符"""
    if not (is_chinese(uchar) or is_number(uchar) or is_alphabet(uchar)):
        return True
    else:
        return False
    
def B2Q(uchar):
    """半角转全角"""
    inside_code = ord(uchar)
    if inside_code < 0x0020 or inside_code > 0x7e:  # 不是半角字符就返回原来的字符
        return uchar
    if inside_code == 0x0020:  # 除了空格其他的全角半角的公式为:半角=全角-0xfee0
        inside_code = 0x3000
    else:
        inside_code += 0xfee0
    return unichr(inside_code)
    
def Q2B(uchar):
    """全角转半角"""
    inside_code = ord(uchar)
    if inside_code == 0x3000:
        inside_code = 0x0020
    else:
        inside_code -= 0xfee0
    if inside_code < 0x0020 or inside_code > 0x7e:  # 转完之后不是半角字符返回原来的字符
        return uchar
    return unichr(inside_code)
    
def stringQ2B(ustring):
    """把字符串全角转半角"""
    return "".join([Q2B(uchar) for uchar in ustring])
    
def uniform(ustring):
    """格式化字符串，完成全角转半角，大写转小写的工作"""
    return stringQ2B(ustring).lower()
    
def string2list(ustring):
    """将ustring按照中文，字母，数字分开"""
    retList = []
    utmp = []
    for uchar in ustring:
        if is_other(uchar):
            if len(utmp) == 0:
                continue
            else:
                retList.append("".join(utmp))
                utmp = []
        else:
            utmp.append(uchar)
    if len(utmp) != 0:
        retList.append("".join(utmp))
    return retList

# 去除头部 尾部 ',' ;' ':'
# 中间含有 ',,',';;','::' replace 为 ',' ;' ':'
def clean_str(stri):
    tags = [',',';',':'] 
    replace_tags = [',,',';;','::']
    if stri:
        for tag in tags:
            if stri[0] == tag:
                stri = stri[1:]
            if stri[len(stri)-1] == tag:
                # 警告 操作系统编码可能导致这里len('中文')出错
                stri = stri[0:len(stri)-1]
        i = 0
        for rt in replace_tags:
            if rt in stri:
                stri = stri.replace(rt,tags[i])
            i += 1
    return stri 

def exclude_something(things, exclude_thing):
    if things and exclude_thing:
        things = to_unicode(things)
        exclude_thing = to_unicode(exclude_thing)
        if exclude_thing in things:
            things = clean_str(things.replace(exclude_thing, ""))
    return things

# 任意字符转换为unicode
def to_unicode(s):
    if isinstance(s, unicode):
        return s
    elif isinstance(s, int) or isinstance(s, long):
        return unicode(str(s))
    elif isinstance(s, str):
        return unicode(s,'utf-8')
    
# def str_len(ustr):
#     if not ustr:
#         return 0
#     str_list = list(ustr)
#     _len = 0
#     cn_count = 0
#     for s in str_list:
#         if not is_number(s) and not is_alphabet(s):
#             cn_count += 1
#         else:
#             _len += 1
#     return int(_len + cn_count/3)
    
# if __name__ == "__main__":
    # test Q2B and B2Q
#     for i in range(0x0020, 0x007F):
#         print Q2B(B2Q(unichr(i))), B2Q(unichr(i))
    # test uniform
#     ustring = unicode('中国a','utf-8')
#     print len(ustring)
#     print str_len(ustring)
#     ustring = uniform(ustring)
#     ret = string2list(ustring)
#     print ret
    
    
    
    
