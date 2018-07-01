# -*- coding:utf-8 -*-
import os, sys;


def walk(path):
    print "cd directory:" + path

    for item in os.listdir(path):
        try:
            if (item == ".DS_Store"):
                global count
                count = count + 1
                print " find file .Ds_Store"
                os.remove(path + "/" + item)
            else:
                if (os.path.isdir(path + "/" + item)):
                    print " " + path + "/" + item + " is directory"
                    walk(path + "/" + item)
            #print " " + path + "/" + item + " is file"
        except OSError, e:
            print e


if __name__ == '__main__':
    count = 0
    if (len(sys.argv) > 1):
        root_dir = sys.argv[1]
    else:
        root_dir = os.getcwd()
        walk(root_dir)
    print "\ntotal number:" + str(count)
