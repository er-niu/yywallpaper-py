import os
import time

from PIL import Image
import cv2

def small_pic(path, name):
    small_path = path + 'small/'
    if not os.path.isdir(small_path):
        os.makedirs(small_path)
    try:
        img = Image.open(path + name)
        img = img.resize((450, 300), Image.ANTIALIAS)
        img.save(small_path + name)
    except:
        print('failed to read img file,' + small_path + name)


def img_zip(path, name):
    small_name = 'small/' + name
    if not os.path.isdir(path + 'small/'):
        os.makedirs(path + 'small/')

    try:
        imageBig = cv2.imread(path + name)
        res = cv2.resize(imageBig, (450, 300), interpolation=cv2.INTER_AREA)
        cv2.imwrite(path + small_name, res)
    except:
        print('failed to read img file,' + path + small_name)



def TimeStampToTime(timestamp):

    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)