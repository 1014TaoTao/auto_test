#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/3/20 16:40
@Author  : ZhangTAO
@File    : public_tool_time.py
@Software: PyCharm
"""
import time
from datetime import datetime
from datetime import timedelta


def countMilliseconds() -> int:
    """
    计算时间
    :return:
    """
    access_start = datetime.now()
    access_end = datetime.now()
    access_delta = (access_end - access_start).seconds * 1000
    return access_delta


def Timestamp_conversion(timeStr: str) -> int:
    """
    时间戳转换，将日期格式转换成时间戳
    :param timeStr: 时间
    :return:
    """

    try:
        datetimeFormat = datetime.strptime(str(timeStr), "%Y-%m-%d %H:%M:%S")
        timestamp = int(time.mktime(datetimeFormat.timetuple()) * 1000.0 + datetimeFormat.microsecond / 1000.0)
        return timestamp
    except ValueError:
        raise '日期格式错误, 需要传入得格式为 "%Y-%m-%d %H:%M:%S" '


def Time_conversion(timeNum: int):
    """
    时间戳转换成日期
    :param timeNum:
    :return:
    """
    if isinstance(timeNum, int):
        timeStamp = float(timeNum / 1000)
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        return otherStyleTime

    else:
        raise "请传入正确的时间戳"


def NowTime() -> str:
    """
    获取当前时间, 日期格式: 2021-12-11 12:39:25
    :return:
    """
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return localtime


def get_time_for_min(minute: int) -> int:
    """
    获取几分钟后的时间戳
    @param minute: 分钟
    @return: N分钟后的时间戳
    """
    return int(time.time() + 60 * minute) * 1000


def get_this_year() -> int:
    """
    :return: 返回今年的年份
    """
    return datetime.now().year


def get_current_month() -> int:
    """
    :return: 返回当前的月份
    """
    return datetime.now().month


def get_today() -> int:
    """
    :return: 返回当前日期
    """
    return datetime.now().day


def get_hour() -> int:
    """

    :return: 返回当前的小时数
    """
    return datetime.now().hour


def get_time():
    """
    :return: 获取当前的的年月日
    """
    return time.strftime('%Y%m%d', time.localtime(time.time()))


def get_now_timestamp() -> int:
    """
    :return: 获取当前时间戳
    """
    return int(time.time()) * 1000


def get_now_time():
    """
    :return: 当前时间
    """
    now = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
    return now


def time_cal(mode, num, time_delta=None):
    """
    :return: 返回当前时间 + n天
    "%Y-%m-%d %H:%M"
    """
    if time_delta is None:
        res = datetime.now() + timedelta(days=num)
        return res.strftime(mode)
    elif time_delta == 'hour':
        res = datetime.now() + timedelta(hours=num)
        return res.strftime(mode)
    elif time_delta == 'min':
        res = datetime.now() + timedelta(minutes=num)
        return res.strftime(mode)
    else:
        raise "time_delta参数异常！"


# if __name__ == '__main__':
#     #     print(NowTime())
#     #     Time_conversion(1547450538000)
#     print(time_cal(mode="%Y-%m-%d", num=0))
