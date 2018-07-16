# -*- coding:utf-8 -*-
import os
import sys
import time

import picture_util
from conf import read_conf
from dao import picture_dao

reload(sys)
sys.setdefaultencoding('utf-8')


# path = "D:/picture/彼岸壁纸/"
# upath = unicode(path, 'utf-8')

def upload_pic(date):
    path = read_conf.get_conf('sys', 'path')
    dirs = os.listdir(path)
    type_id = {'美女': '0', '风景': '1', '唯美': '2', '动漫': '3', '游戏': '4', '人物': '5',
               '动物': '6', '花卉': '7', '节日': '8', '可爱': '9', '汽车': '10', '日历': '11',
               '设计': '12', '影视': '13', '游戏': '14', '王者荣耀': '15', '鬼刀': '16',
               '护眼': '17', '体育': '18', '其他': '19', '建筑': '20', '美食': '21', '水果': '22'}
    for type_name in dirs:
        # name = type_name.encode("utf-8")
        if '.DS_Store' == type_name:
            continue

        try:
            type = type_id[type_name]
        except:
            print('failed to get type_name:%s', type_name)
            continue

        # type = type_id[type_name]
        type_path = path + type_name + '/' + date + '/'

        print(type_path)
        if os.path.exists(type_path) is False:
            continue

        all_pic = os.listdir(type_path)
        for dr in all_pic:
            title = dr.split('.')[0]
            count = picture_dao.check_picture(title)
            if count >= 1:
                print('picture has been exist:%s' % title)
                continue

            pic_desc = title
            pic_type = type
            pic_path = type_path + dr

            if '.DS_Store' == dr:
                continue

            # 如果是文件夹则跳过
            if os.path.isdir(pic_path):
                continue

            url = picture_dao.upload_picture(pic_path)
            if url == 'error':
                print('failed to insert picture')
                continue
            # 判断缩略图是否存在，不存在生成
            small_pic_path = type_path + 'small/' + dr
            if os.path.exists(small_pic_path) is False:
                picture_util.small_pic(type_path, dr)

            small_url = picture_dao.upload_picture(small_pic_path)
            if small_url == 'error':
                print('failed to insert picture')
                continue

            # 图片信息入库
            create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            picture_dao.insert_picture(title, pic_desc, url, small_url, 1920, 1080, 0, pic_type, create_time)
            print('success to insert picture:%s' % title)
            picture_dao.dis_connect()
            # title = dr.encode("utf-8")
