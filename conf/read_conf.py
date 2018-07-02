# -*- coding:utf-8 -*-

import ConfigParser

conf = ConfigParser.SafeConfigParser()
conf.read("../conf/system.cfg")


def get_conf(section, key):
    return conf.get(section, key)
