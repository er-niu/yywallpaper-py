# encoding=utf-8
import pymysql.cursors
from fdfs_client.client import *

from conf import read_conf

connection = pymysql.connect(host=read_conf.get_conf('mysql', 'host'),
                             port=int(read_conf.get_conf('mysql', 'port')),
                             user=read_conf.get_conf('mysql', 'user'),
                             password=read_conf.get_conf('mysql', 'password'),
                             db=read_conf.get_conf('mysql', 'db'),
                             charset=read_conf.get_conf('mysql', 'charset'),
                             cursorclass=pymysql.cursors.DictCursor)

# client = Fdfs_client('D:\Program Files\Python2.7\client.conf')
# client = Fdfs_client(read_conf.get_conf('fastdfs', 'client_path'))


# 保存图片
def insert_picture(title, pic_desc, big_url, small_url, length, width, like_num, pic_type, create_time):
    # 使用cursor()方法获取操作游标
    cursor = connection.cursor()
    sql = "INSERT INTO t_picture_item(title,pic_desc,big_url,small_url,length,width,like_num,pic_type,create_time) \
           VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' )" % \
          (title, pic_desc, big_url, small_url, length, width, like_num, pic_type, create_time)
    try:
        # 执行sql语句
        connection.ping(reconnect=True)
        print('excute sql:' + sql)
        cursor.execute(sql)
        id = int(connection.insert_id())
        # 向数据库提交
        connection.commit()
        return id
    except Exception, err:
        print('failed to insert picture:%s' % err)
        # 发生错误时回滚
        connection.rollback()
    connection.close()

# check 图片是否已经入库
def check_picture(title):
    # 使用cursor()方法获取操作游标
    cursor = connection.cursor()
    sql = "SELECT COUNT(*) FROM t_picture_item WHERE title = '%s'" % (title)
    try:
        # 执行sql语句
        print('excute sql========:' + sql)
        connection.ping(reconnect=True)
        cursor.execute(sql)
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        print('find the same picture:%s' % data['COUNT(*)'])
        return data['COUNT(*)']
    except Exception, err:
        print('failed to check picture:%s' % err)
        # 发生错误时回滚
        connection.rollback()
    connection.close()

def dis_connect():
    connection.close()


# def upload_picture(path):
#     try:
#         ret = client.upload_by_filename(path)
#         # http://yywallpaper.top/group1/M00/00/00/rBsABVs0Vs-AJcmtAAA_pvGSS9o605.jpg
#         url = read_conf.get_conf('sys', 'address') + ret['Remote file_id']
#         return url
#     except Exception, err:
#         print('failed to upload picture:%s' % path, err)
#         return 'error'


def update_picture(big_url, small_url, pic_id):
    # 使用cursor()方法获取操作游标
    cursor = connection.cursor()
    # SQL 更新语句
    sql = "UPDATE t_picture_item SET big_url = '%s',small_url = '%s' WHERE id = '%s'" % (big_url, small_url, pic_id)

    print(sql)
    try:
        connection.ping(reconnect=True)
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        connection.commit()
    except Exception, err:
        print('failed to update picture:%s' % err)
        # 发生错误时回滚
        connection.rollback()

    # 关闭数据库连接
    connection.close()
