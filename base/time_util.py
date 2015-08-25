# -*- coding: utf-8 -*-
import datetime
import time

def str_to_datetime(str_time):
    date = time.strptime(str_time, "%Y-%m-%d %H:%M:%S")
    return datetime.datetime(*date[:6])

def datetime_to_timestamp(_datetime):
    return time.mktime(_datetime.timetuple())

def datetime_to_second(_datetime):
    return time.mktime(_datetime.timetuple())

# 当前时间的秒
def get_now_second():
    return int(time.time())

# 当前时间的毫秒秒
def get_now_millisecond():
    return int(time.time() * 1000)

def seconds_to_str(second):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(second))
#     return datetime.datetime.ctime(str(seconds))

# dt = datetime.datetime.now()
# print dt
# print dt.timetuple()
# print time.mktime(dt.timetuple())
# timestamp=time.mktime(dateC.timetuple())
# print datetime_to_timestamp(dt)

# print datetime.time.microsecond()
