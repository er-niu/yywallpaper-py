# -*- coding:utf-8 -*-
from conf import read_conf

path = read_conf.get_conf('sys', 'path')
print(path)