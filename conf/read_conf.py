# -*- coding:utf-8 -*-

import ConfigParser

conf = ConfigParser.SafeConfigParser()
conf.read("../system.cfg")


def get_conf(section, key):
    return conf.get(section, key)
