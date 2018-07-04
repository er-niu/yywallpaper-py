# -*- coding:utf-8 -*-
from conf import read_conf

path = read_conf.get_conf('mysql', 'host')
print(path)
