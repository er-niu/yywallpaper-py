# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging

from conf import read_conf

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

secret_id = 'AKIDiekPvMOFuQrBeAbpiWBVlqjRJ4eh7VBq'  # 替换为用户的 secretId
secret_key = 'fEdrulS4WErJZgugWOe6ynRubCcqz0qU'  # 替换为用户的 secretKey
region = 'ap-chengdu'  # 替换为用户的 Region
token = None  # 使用临时密钥需要传入 Token，默认为空，可不填
scheme = 'https'  # 指定使用 http/https 协议来访问 COS，默认为 https，可不填
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
# 2. 获取客户端对象
client = CosS3Client(config)


def upload_cos(path, file_name, pic_id, pic_type):
    try:
        pic_name = str(pic_id) + "_" + str(pic_type) + '.' + file_name.split('.')[1]
        with open(path + file_name, 'rb') as fp:
            response = client.put_object(
                Bucket='picture-1256975408',
                Body=fp,
                Key=pic_name,
                StorageClass='STANDARD',
                ContentType='text/html; charset=utf-8'
            )
        url = read_conf.get_conf('sys', 'address') + pic_name
        return url
    except Exception, err:
        print('failed to upload picture to cos:%s' % file_name, err)
        return 'error'
