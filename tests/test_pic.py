# -*- coding:utf-8 -*-
import os
import time

from service.picture_util import img_zip


def TimeStampToTime(timestamp):

    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)

if __name__ == '__main__':
    pic_path = "/Users/songxiao/Pictures/wallpaper/dongman/《你的名字 》立花泷 宫水三叶桌面壁纸.jpg"
    t = os.path.getctime(pic_path)
    print(TimeStampToTime(t))
