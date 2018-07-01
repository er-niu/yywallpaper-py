# encoding=utf-8

import pymysql.cursors
from fdfs_client.client import *

connection = pymysql.connect(host='118.24.51.89',
                             user='root',
                             password='123456',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# client = Fdfs_client('D:\Program Files\Python2.7\client.conf')
client = Fdfs_client('/Users/songxiao/work/own-web/client.conf')


# 保存图片
def insert_picture(title, pic_desc, big_url, small_url, length, width, like_num, pic_type, create_time):
    # 使用cursor()方法获取操作游标
    cursor = connection.cursor()
    sql = "INSERT INTO picture_item(title,pic_desc,big_url,small_url,length,width,like_num,pic_type,create_time) \
           VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' )" % \
          (title, pic_desc, big_url, small_url, length, width, like_num, pic_type, create_time)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 向数据库提交
        connection.commit()
    except:
        # 发生错误时回滚
        connection.rollback()


# 保存图片
def check_picture(title):
    # 使用cursor()方法获取操作游标
    cursor = connection.cursor()
    sql = "SELECT COUNT(*) FROM picture_item WHERE title = '%s'" % (title)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        print('find the same picture:%s' % data['COUNT(*)'])
        return data['COUNT(*)']
    except:
        # 发生错误时回滚
        connection.rollback()


def dis_connect():
    connection.close()


def upload_picture(path):
    try:
        ret = client.upload_by_filename(path)
        # http://yywallpaper.top/group1/M00/00/00/rBsABVs0Vs-AJcmtAAA_pvGSS9o605.jpg
        url = 'http://118.24.51.89/' + ret['Remote file_id']
        return url
    except Exception, err:
        print('failed to upload picture:%s' % path,err)
        return 'error'
