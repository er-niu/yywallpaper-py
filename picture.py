# coding=gbk
# 目标：下载各目录的壁纸（大图）
import time

__author__ = 'CQC'

import urllib.request
import urllib.parse
import re
import os
import socket
import random

socket.setdefaulttimeout(30)  # 设置socket层的超时时间为20秒
# 首先创建壁纸的存放目录
path = 'D:\picture\彼岸壁纸'
if not os.path.isdir(path):
    os.makedirs(path)

# 目录
big_title = []

# 网站首页地址
url = 'http://www.netbian.com/'
headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/56.0.2924.87 Safari/537.36'}
request = urllib.request.Request(url, headers=headers)
try:
    response = urllib.request.urlopen(request).read()
except socket.timeout as e:
    print(type(e))
except Exception as err:
    print('a', str(err))
response = response.decode('gbk')  # python3

# 首页目录源代码获取
pat_menu = re.compile('<ul class="menu">(.*?)</div></li>', re.S)
code_menu = re.search(pat_menu, response)

pat_menu_title = re.compile('<a href=".*?" title=".*?">(.*?)</a>', re.S)
pat_menu_title_other = re.compile('<a href=".*?" target="_blank">(.*?)</a>', re.S)
menu_title = re.findall(pat_menu_title, code_menu.group(1))
menu_title_other = re.findall(pat_menu_title_other, code_menu.group(1))

for title in menu_title_other:
    menu_title.append(title)

for a_item in menu_title:
    big_title.append(a_item)
    print(a_item)

big_title.pop(0)
# 目录链接
pat_menu_link = re.compile('<a href="/(.*?)/".*?>', re.S)
menu_link = re.findall(pat_menu_link, code_menu.group(1))
menu_link_new = []
for link in menu_link:
    link = "/" + link + "/"
    menu_link_new.append(link)

# 去除动态壁纸目录
menu_link_new.remove('/dongtai/')
print(menu_link_new)

j = 0
#menu_link_new.pop(0)
for b_item in menu_link_new:
    # 爬取前x页
    url_page_menu = []
    url_menu = 'http://www.netbian.com/' + b_item
    url_page_menu.append(url_menu)
    page_num = 4
    if b_item == '/meinv/':
        page_num = 10

    for page in range(2, page_num):
        page_link = url_menu + '/index_' + str(page) + '.htm'
        url_page_menu.append(page_link)

    for page_index in url_page_menu:
        # 筛选出子目录代码
        pat_code_son = re.compile('<ul>(.*?)</ul>', re.S)
        middle_pattern = urllib.request.Request(page_index, headers=headers)
        try:
            middle_response = urllib.request.urlopen(middle_pattern).read()
        except socket.timeout as e:
            print(type(e))
        except Exception as err:
            print('a', str(err))
            continue
        middle_response = middle_response.decode('gbk')  # python3
        res_code_son = re.search(pat_code_son, middle_response)

        # 获得子目录链接，合成大图网页链接
        pat_link_son = re.compile('<li><a href="(.*?)" title=".*?" target="_blank"><img', re.S)
        res_link = re.findall(pat_link_son, res_code_son.group(1))

        # 显示进度
        # print(big_title[j])
        for d_item in res_link:
            # 拼接大图链接
            if d_item == 'http://www.mmmwu.com/':
                pass
            else:
                new_link = 'http://www.netbian.com/' + d_item[:-4] + '-1920x1080.htm'
                # print(new_link)
                request_real = urllib.request.Request(new_link, headers=headers)
                try:
                    response_real = urllib.request.urlopen(request_real).read()
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
                    path_final = 'D:\\picture\\彼岸壁纸' + '\\' + big_title[j] + '\\'
                    if not os.path.isdir(path_final):
                        os.makedirs(path_final)
                    path_pic = path_final + fina_title + '.jpg'
                    # print(fina_link)
                    print(path_pic)
                    f = open(path_pic, 'wb')
                    try:
                        data = urllib.request.urlopen(fina_link).read()
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
            time.sleep(random.randint(5, 20))  # 休眠随机时间
    print('One menu download OK.')
    time.sleep(random.randint(9, 30))  # 休眠随机时间
    j += 1
