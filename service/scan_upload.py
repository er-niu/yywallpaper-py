# -*- coding:utf-8 -*-
import os
import sys
import time

import picture_util
from conf import read_conf
from dao import picture_dao
from dao.picture_dao import update_picture
from dao.upload_cos import upload_cos

reload(sys)
sys.setdefaultencoding('utf-8')
# path = "D:/picture/彼岸壁纸/"
path = read_conf.get_conf('sys', 'path')
# upath = unicode(path, 'utf-8')

dirs = os.listdir(path)
# type_id = {'美女': '0', '风景': '1', '唯美': '2', '动漫': '3', '游戏': '4', '人物': '5',
#            '动物': '6', '花卉': '7', '节日': '8', '可爱': '9', '汽车': '10', '日历': '11',
#            '设计': '12', '影视': '13', '军事': '14', '王者荣耀': '15', '鬼刀': '16',
#            '护眼': '17', '体育': '18', '其他': '19', '建筑': '20', '美食': '21', '水果': '22'}
type_id = {'meinv': '0', 'fengjing': '1', 'weimei': '2', 'dongman': '3', 'youxi': '4', 'renwu': '5',
           'dongwu': '6', 'huahui': '7', 'jieri': '8', 'keai': '9', 'qiche': '10', 'rili': '11',
           'sheji': '12', 'yingshi': '13', 'junshi': '14', 'wangzherongyao': '15', 'guidao': '16',
           'huyan': '17', 'tiyu': '18', 'qita': '19', 'jianzhu': '20', 'meishi': '21', 'shuiguo': '22'}
for type_name in dirs:
    # name = type_name.encode("utf-8")
    if '.DS_Store' == type_name:
        continue

    if 'meinv' != type_name:
        continue

    type = type_id[type_name]
    type_path = path + type_name + '/'
    all_pic = os.listdir(type_path)

    # print(all_pic)

    for file_name in all_pic:
        title = file_name.split('.')[0]
        pic_desc = title
        pic_type = type
        pic_path = type_path + file_name

        if '.DS_Store' == file_name:
            continue

        # 如果是文件夹则跳过
        if os.path.isdir(pic_path):
            continue

        count = picture_dao.check_picture(title)
        if count >= 1:
            print('picture has been exist:%s' % title)
            continue

        # 图片信息入库
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        t = os.path.getctime(pic_path)
        create_time = picture_util.TimeStampToTime(t)
        pic_id = picture_dao.insert_picture(title, pic_desc, "", "", 1920, 1080, 0, pic_type, create_time)
        print('success to insert picture id:%s title： %s', pic_id, title)

        # 上传原图到cos
        url = upload_cos(type_path, file_name, pic_id)
        if url == 'error':
            print('failed to upload_cos big picture')
            continue

        # 判断缩略图是否存在，不存在生成
        small_pic_path = type_path + 'small/' + file_name
        if os.path.exists(small_pic_path) is False:
            picture_util.img_zip(type_path, file_name)

        small_url = upload_cos(type_path + 'small/', file_name, 'small/' + str(pic_id))
        if small_url == 'error':
            print('failed to upload_cos small picture')
            continue
        # 更新db图片的url
        update_picture(url, small_url, str(pic_id))
