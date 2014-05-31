# -*- coding: utf-8 -*-
# Python中的time和datetime模块可以通过time.time_struct对象互相转换。
# datetime和date对象的timetuple方法会返回time_struct类型的对象。
# time的mktime方法可以将该类型对象转换为POSIX时间（秒为单位）。
# time的gmtime方法与mktime相反，将秒转换为time_struct。
# time更贴近底层的C实现，而datetime实现了对时间操作的简易封装。
# datetime.date和datetime.time分别提供了对日期和时间的访问以及算数操作。
# datetime.datetime是二者的组合。

# 遇到问题，文件命名为datetime.py导致报错，datetime没有now。
# 因为搜索模块先从当前文件夹开始，该模块屏蔽了系统内置的datetime模块。

import time
from datetime import datetime

def strptime_parser():
    now = datetime.now()
    print now
    time_iso= now.isoformat()
    print "isoformat return: type->{0} and value->{1} ".format(type(time_iso), time_iso)
    # strptime将str转换为datetime对象
    # strftime反之将datetime转换为指定格式的str
    obj_datetime = datetime.strptime(time_iso, "%Y-%m-%dT%H:%M:%S.%f")
    print obj_datetime
    # [utc]fromtimestamp将时间戳（单位秒）转换为datetime


strptime_parser()
