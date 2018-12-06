# -*- coding:utf-8 -*-
import os
import time

from service.picture_util import img_zip


def TimeStampToTime(timestamp):

    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)

if __name__ == '__main__':
    pic_path = "/Users/songxiao/Pictures/wallpaper/test/"
    pic_name = "111.jpg"
    img_zip(pic_path, pic_name)