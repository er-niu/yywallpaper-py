# -*- coding:utf-8 -*-
import time
from apscheduler.schedulers.blocking import BlockingScheduler

# 方法主体
import scan_today
import scan_upload_day
import logging


logging.basicConfig()

def my_job():
    #date =  time.strftime('%Y-%m-%d', time.localtime(time.time()))
    # 定时任务
    # 1. 根据当前日期爬取最新图片，并保存到/分类/日期/ 文件夹 2016-07-23
    # 2. 读取文件夹图片，保存到fastfds和mysql
    date = '2018-06-29'
    scan_today.scan_day_picture(date)
    scan_upload_day.upload_pic(date)


sched = BlockingScheduler()
# 定时每天 22:22:22秒执行任务
sched.add_job(my_job,'cron',day_of_week ='mon-sun',hour = 0,minute = 9,second = 05)

sched.start()