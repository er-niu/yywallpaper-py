import os

from PIL import Image


def small_pic(path, name):
    small_path = path + 'small/'
    if not os.path.isdir(small_path):
        os.makedirs(small_path)
    try:
        img = Image.open(path + name)
        img = img.resize((300, 200), Image.ANTIALIAS)
        img.save(small_path + name)
    except:
        print('failed to read img file,' + small_path + name)
