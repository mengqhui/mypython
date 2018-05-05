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

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def merge_pic(n):
    """ 读取图片 """
    j = 4
    toImage = Image.new('RGBA',(80,j*25))
    jpgs = []
    for (i,ii) in zip(range(j*n,j*(n+1)),range(j)):
        jpg_n = str(i).zfill(3) + '.jpg'
        #if not os.path.exists(jpg_n):
        #    continue
        jpgs.append(jpg_n)
        fimage = Image.open(jpg_n)

        loc = (0, ii*25)
        #print(loc,jpg_n)
        toImage.paste(fimage, loc)

    toImage.save('tmp.png')
    
    return get_file_content('tmp.png'),jpgs

for n in range(0, 250):
    time.sleep(1)
    image, image_l = merge_pic(n)
    """ 调用通用文字识别（高精度版） """
    res_basicAccurate = client.basicGeneral(image)
    
    if 'words_result_num' in res_basicAccurate and res_basicAccurate['words_result_num'] is 4:
        words_result = res_basicAccurate['words_result']
        words = [n['words'] for n in words_result]
        
        for (o,n) in zip(image_l,words):
            print(o,n)
            try:
                 os.rename(o ,'[' + n + '.jpg')
            except:
                continue
            #dic.update({o :'[' + n + '.jpg'})
    else:
        print(res_basicAccurate)
        continue
