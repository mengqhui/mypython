"""验证码拼接&百度OCR"""
from aip import AipOcr
from PIL import Image
import json
import time
import os

""" 你的 APPID AK SK """
APP_ID = '10033669'
API_KEY = 'FqQdAifvOsvadi5s8QEEHhXB'
SECRET_KEY = 'Y5jChkCNbSEhjdYZ4OjwGODqoMC7MBvY'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

dic = {}


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def merge_pic(n):
    """ 读取图片 """
    j = 4
    toImage = Image.new('RGBA', (80, j*25))
    jpgs = []
    for i in range(j*n, j*(n+1)):
        jpg_n = str(i).zfill(3) + '.jpg'
        jpgs.append(jpg_n)
        fimage = Image.open(jpg_n)
        loc = (0, i*25)
        print(loc)

        toImage.paste(fimage, loc)
    toImage.save('tmp.png')

    return get_file_content('tmp.png'), jpgs


image, image_l = merge_pic(0)

""" 调用表格文字识别 """
res = client.tableRecognitionAsync(image)

requestId = res['result'][0]["request_id"]
print(requestId)

""" 调用表格识别结果 
jso = client.getTableRecognitionResult(requestId)
"""
time.sleep(3)
""" 如果有可选参数 """
options = {}
options["result_type"] = "json"

""" 带参数调用表格识别结果 """
jso = client.getTableRecognitionResult(requestId, options)
print(jso)

""" 调用通用文字识别（高精度版） """
res_basicAccurate = client.basicAccurate(image)

if res_basicAccurate['words_result_num'] is 4:
    words_result = res_basicAccurate['words_result']
    words = [n['words'] for n in words_result]

    for (o, n) in zip(image_l, words):
        print(o, n)
        dic.update({o: '[' + n + '.jpg'})

for key, value in dic.items():
    print(key, value)
    os.rename(key, value)
