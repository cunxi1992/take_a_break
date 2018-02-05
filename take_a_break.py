# -*- coding:utf-8 -*-

# 引入time模块

import time

# 引入webbrowser模块

import webbrowser



# 设置一天需要休息几次

total_breaks = 4

# 设置循环结束变量初始值

break_count = 0

# time模块中的ctime()函数，获取当前时间

print("程序于{0}开始启动".format(time.ctime()))



while (break_count < total_breaks):

    '''

    每隔一段时间，自动打开浏览器播放最喜欢的音乐

    '''

    # 让程序等待一段时间，sleep()函数传入的是秒数

    time.sleep(2 * 60 * 60)

    # 打开指定的页面，我打开的是网易云音乐

    webbrowser.open("http://music.163.com/#/discover/toplist?id=19723756")

    # 循环结束变量递增

    break_count = break_count + 1



# 打印程序结束时间

print("程序于{0}结束，你休息了{1}次，真棒！".format(time.ctime(),total_breaks))