# -*- coding:utf-8 -*-

# 1. 根据当前日期爬取最新图片，并保存到/分类/日期/ 文件夹
# 2. 读取文件夹图片，保存到fastfds和mysqlimport time
import time
import urllib2
import re
import os
import socket
import random
import sys

from conf import read_conf

reload(sys)
sys.setdefaultencoding('gbk')
socket.setdefaulttimeout(30)  # 设置socket层的超时时间为20秒
# 网站首页地址
url = read_conf.get_conf('http', 'url')
headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/56.0.2924.87 Safari/537.36'}


def scan_day_picture(date):
    # 首先创建壁纸的存放目录
    path = read_conf.get_conf('sys', 'path')
    if not os.path.isdir(path):
        os.makedirs(path)

    # 目录
    request = urllib2.Request(url, headers=headers)
    try:
        response = urllib2.urlopen(request).read()
    except socket.timeout as e:
        print(type(e))
    except Exception as err:
        print('a', str(err))
    response = response.decode('gbk')  # python3

    # 首页目录源代码获取
    pat_menu = re.compile('<ul class="menu">(.*?)</div></li>', re.S)
    code_menu = re.search(pat_menu, response)
    big_title = scan_pic_menu(code_menu)
    menu_link_new = scan_menu_link(code_menu)
    scan_pic_page(menu_link_new, path, big_title, date)


def scan_pic_menu(code_menu):
    big_title = []
    pat_menu_title = re.compile('<a href=".*?" title=".*?">(.*?)</a>', re.S)
    pat_menu_title_other = re.compile('<a href=".*?" target="_blank">(.*?)</a>', re.S)
    menu_title = re.findall(pat_menu_title, code_menu.group(1))
    # 爬取以上正则获取不到的目录名称
    menu_title_other = re.findall(pat_menu_title_other, code_menu.group(1))

    for title in menu_title_other:
        menu_title.append(title)

    for a_item in menu_title:
        big_title.append(a_item)
    # 去除广告4k壁纸链接
    big_title.pop(0)
    return big_title


def scan_menu_link(code_menu):
    # 目录链接
    pat_menu_link = re.compile('<a href="/(.*?)/".*?>', re.S)
    menu_link = re.findall(pat_menu_link, code_menu.group(1))
    menu_link_new = []
    for link in menu_link:
        link = "/" + link + "/"
        menu_link_new.append(link)

    # 去除动态壁纸目录
    menu_link_new.remove('/dongtai/')
    return menu_link_new


def scan_pic_page(menu_link_new, path, big_title, date):
    j = 0
    for b_item in menu_link_new:
        # 爬取前x页
        url_page_menu = []
        url_menu = url + b_item
        # 添加首页url地址
        url_page_menu.append(url_menu)
        page_num = 6
        # 组装每一页的url地址
        for page in range(2, page_num):
            page_link = url_menu + '/index_' + str(page) + '.htm'
            url_page_menu.append(page_link)

        for page_index in url_page_menu:
            # 筛选出子目录代码
            pat_code_son = re.compile('<ul>(.*?)</ul>', re.S)
            middle_pattern = urllib2.Request(page_index, headers=headers)
            try:
                middle_response = urllib2.urlopen(middle_pattern).read()
            except socket.timeout as e:
                print(type(e))
            except Exception as err:
                print('a', str(err))
                continue
            middle_response = middle_response.decode('gbk')  # python3
            res_code_son = re.search(pat_code_son, middle_response)

            # 获得子目录链接，合成大图网页链接
            #pat_link_son = re.compile('<li><a href="(.*?)" title=".*?" target="_blank"><img', re.S)
            pat_link_son = re.compile('<li><a href="(.*?)" title=".*?'+date+'".*?', re.S)

            res_link = re.findall(pat_link_son, res_code_son.group(1))
            #print(res_code_son.group(1))
            print res_link
            # print(big_title[j])
            for d_item in res_link:
                # 拼接大图链接
                if d_item == 'http://www.mmmwu.com/':
                    pass
                else:
                    new_link = url + d_item[:-4] + '-1920x1080.htm'
                    # print(new_link)
                    request_real = urllib2.Request(new_link, headers=headers)
                    try:
                        response_real = urllib2.urlopen(request_real).read()
                        response_real = response_real.decode('gbk')
                    except socket.timeout as e:
                        print(type(e))
                    except Exception as err:
                        print('a', str(err))
                        continue
                    pat_real = re.compile('<img src="(.*?)" title=".*?" alt=".*?" /></a></td></tr>')
                    link_real = re.search(pat_real, response_real)
                    # 获得子目录标题--壁纸名字
                    pat_title_real = re.compile('<img src=".*?" title=".*?" alt="(.*?)" /></a></td></tr>')
                    title_real = re.search(pat_title_real, response_real)
                    # print(response_real)
                    if link_real:
                        fina_link = link_real.group(1)
                        fina_title = title_real.group(1)
                        # 创建下载目录
                        # path_final = 'D:\\picture\\彼岸壁纸' + '\\' + big_title[j] + '\\'
                        path_final = path.decode('utf-8') + '/' + big_title[j] + '/'

                        if not os.path.isdir(path_final):
                            os.makedirs(path_final)
                        path_pic = path_final + date + '/' + fina_title + '.jpg'
                        if not os.path.isdir(path_final + date + '/'):
                            os.makedirs(path_final + date + '/')
                        # print(fina_link)
                        print(path_pic)
                        f = open(path_pic, 'wb')
                        try:
                            data = urllib2.urlopen(fina_link).read()
                        except socket.timeout as e:
                            print(type(e))
                        except Exception as err:
                            print('a', str(err))
                            continue
                        # data = data.decode('gbk')  # python3
                        f.write(data)
                        f.close()
                        if not data:
                            print("download picture failed!")

                time.sleep(random.randint(5, 6))  # 休眠随机时间
        print('One menu download OK.')
        time.sleep(random.randint(5, 6))  # 休眠随机时间
        j += 1
