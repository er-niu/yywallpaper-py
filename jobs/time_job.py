# -*- coding:utf-8 -*-
import time

from apscheduler.schedulers.blocking import BlockingScheduler

from conf import read_conf
from service import scan_upload_day, scan_pic_day
import logging

logging.basicConfig()


def my_job():
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    # 定时任务
    # 1. 根据当前日期爬取最新图片，并保存到/分类/日期/ 文件夹 2016-07-23
    # 2. 读取文件夹图片，保存到fastfds和mysql
    #date = '2018-11-16'
    # dates = {"2019-08-08"}

    # for date in dates:
    #     scan_pic_day.scan_day_picture(date)
    #     scan_upload_day.upload_pic(date)

    scan_pic_day.scan_day_picture(date)
    scan_upload_day.upload_pic(date)


sched = BlockingScheduler()
# 定时每天 22:22:22秒执行任务
sched.add_job(my_job, 'cron', day_of_week='0-6', hour=read_conf.get_conf('job', 'hour'),
              minute=read_conf.get_conf('job', 'minute'), second=read_conf.get_conf('job', 'second'),
              end_date='2114-05-30')

sched.start()
