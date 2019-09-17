# -*- coding:utf-8 -*-

import ConfigParser

conf = ConfigParser.SafeConfigParser()
print '################### read system.cfg'
# conf.read("/usr/local/src/yywallpaper-py/dist/yywallpaper-py-0.1/system.cfg")
conf.read("../system.cfg")


def get_conf(section, key):
    return conf.get(section, key)
