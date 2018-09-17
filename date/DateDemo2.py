# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

import calendar
import time
from datetime import date, timedelta

year = time.strftime('%Y', time.localtime())
mon = time.strftime('%m', time.localtime())
day = time.strftime('%d', time.localtime())
hour = time.strftime('%H', time.localtime())
# noinspection PyShadowingBuiltins
min = time.strftime('%M', time.localtime())
sec = time.strftime('%S', time.localtime())


def today():
    return date.today()


# noinspection SpellCheckingInspection
def todaystr():
    return year + mon + day


def datetime():
    return time.strftime('%Y-%m-%d-%H:%S', time.localtime())


# noinspection SpellCheckingInspection
def datetimestr():
    return year + mon + day + hour + min + sec


def get_day_of_day(n=0):
    if n < 0:
        n = abs(n)
        return date.today() - timedelta(days=n)
    else:
        return date.today() + timedelta(days=n)


# noinspection PyShadowingNames
def get_days_of_month(year, mon):
    return calendar.monthrange(year, mon)[1]


# noinspection PyShadowingNames,SpellCheckingInspection
def get_firstdat_of_month(year, mon):
    days = '01'
    if int(mon) < 10:
        mon = '0' + str(int(mon))
        arr = (year, mon, days)
        return '-'.join('%s' % i for i in arr)


# noinspection PyShadowingNames,SpellCheckingInspection
def get_lastdat_of_month(year, mon):
    days = calendar.monthrange(year, mon)[1]
    mon = addzero(mon)
    arr = (year, mon, days)
    return '-'.join('%s' % i for i in arr)


# noinspection SpellCheckingInspection
def get_firstday_month(n=0):
    (y, m, d) = getyearandmonth(n)
    d = '01'
    arr = (y, m, d)
    return '-'.join('%s' % i for i in arr)


# noinspection SpellCheckingInspection
def get_lastday_month(n=0):
    return '-'.join('%s' % i for i in getyearandmonth(n))


# noinspection SpellCheckingInspection,PyGlobalUndefined
def getyearandmonth(n=0):
    global j, i
    thisyear = int(year)
    thismon = int(mon)
    totalmon = thismon + n
    if n >= 0:
        if totalmon <= 12:
            days = str(get_days_of_month(thisyear, totalmon))
            totalmon = addzero(totalmon)
            return year, totalmon, days
    else:
        i = totalmon // 12
        j = totalmon % 12
    if j == 0:
        i -= 1
        j = 12
        thisyear += i
        days = str(get_days_of_month(thisyear, j))
        j = addzero(j)
        return str(thisyear), str(j), days
    else:
        if 0 < totalmon < 12:
            days = str(get_days_of_month(thisyear, totalmon))
            totalmon = addzero(totalmon)
            return year, totalmon, days
        else:
            i = totalmon // 12
            j = totalmon % 12
            if j == 0:
                i -= 1
                j = 12
                thisyear += i
                days = str(get_days_of_month(thisyear, j))
                j = addzero(j)
                return str(thisyear), str(j), days


# noinspection SpellCheckingInspection
def addzero(n):
    nabs = abs(int(n))
    if nabs < 10:
        return '0' + str(nabs)
    else:
        return nabs


def get_today_month(n=0):
    (y, m, d) = getyearandmonth(n)
    # noinspection PyUnusedLocal
    arr = (y, m, d)
    if int(day) < int(d):
        arr = (y, m, day)
        return '-'.join('%s' % i for i in arr)


# noinspection PyRedeclaration,SpellCheckingInspection
def get_firstday_month(n=0):
    (y, m, d) = getyearandmonth(n)
    arr = (y, m, '01')
    return '-'.join('%s' % i for i in arr)


def main():
    print('today is:', today())
    print('today is:', todaystr())
    print('the date time is:', datetime())
    print('data time is:', datetimestr())
    print('2 days after today is:', get_day_of_day(2))
    print('2 days before today is:', get_day_of_day(-2))
    print('2 months after today is:', get_today_month(2))
    print('2 months before today is:', get_today_month(-2))
    print('2 months after this month is:', get_firstday_month(2))
    print('2 months before this month is:', get_firstday_month(-2))


if __name__ == '__main__':
    main()
