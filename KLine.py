# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
KLine.py  aapl.csv绘制k线
"""
import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as md


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    time = dt.datetime.strptime(dmy, '%d-%m-%Y')
    t = time.date().strftime('%Y-%m-%d')
    return t

dates, opening_prices, highest_prices, \
    lowest_prices, closing_prices = np.loadtxt(
        'aapl.csv', delimiter=',',
        usecols=(1, 3, 4, 5, 6), unpack=True,
        dtype='M8[D], f8, f8, f8, f8',
        converters={1: dmy2ymd})

# 绘制收盘价折线图
mp.figure('AAPL', facecolor='lightgray')
mp.title('AAPL', fontsize=16)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 设置x轴刻度定位器
ax = mp.gca()
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(
    md.DateFormatter('%d %b %Y'))
ax.xaxis.set_minor_locator(md.DayLocator())

# 为了日期显示合理，修改dates的dtype
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, closing_prices, alpha=0.3,
        color='dodgerblue', linewidth=2,
        linestyle='--', label='AAPL CP')


# 控制实体与影线的颜色
rise = closing_prices >= opening_prices
color = np.array(
    ['white' if x else 'green' for x in rise])
ecolor = np.array(
    ['red' if x else 'green' for x in rise])

# 绘制实体
mp.bar(dates, closing_prices - opening_prices,
       0.8, opening_prices, color=color,
       edgecolor=ecolor, zorder=3)

# 绘制影线
mp.vlines(dates, lowest_prices, highest_prices,
          color=ecolor)


mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
