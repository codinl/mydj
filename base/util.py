from string import join
import random
import urllib

def get_client_ip(request):
    ip=""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_html(url):
    try:
        f = urllib.urlopen(url)
        data = f.read()
    except:
        return None
    finally:
        f.close() 
    return data

def get_jifen(jine):
    if jine <= 0:
        return 0
    return int(jine * 0.28 * 100)

def gen_random_str(size=8):
    return join(random.sample([chr(i) for i in range(97, 122)], size)).replace(" ","")

def get_num_iid_from_url(url):
    if not url:
        return None
    i = url.find("id=")
    if i< 1:
        return None
    url = url[i:i+15]
    regex = "[1-9]{1}[0-9]{8,12}"
    import re
    reobj = re.compile(regex)
    match = reobj.search(url)
    if match:
        result = match.group()
        if result:
            return result
    return None

#print get_num_iid_from_url("http://item.taobao.com/item.htm?id=19068076665&ali_refid=a3_420434_1006:1102299774:6:%BA%EC")
