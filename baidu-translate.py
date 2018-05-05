# -*- coding: utf-8 -*-

import requests
import httplib, urllib
import md5, hashlib
import random

appid = '20151113000005349'
secretKey = 'osubCEzlGjzvw8qdQc41'

'''
翻译API HTTP地址：
http://api.fanyi.baidu.com/api/trans/vip/translate
翻译API HTTPS地址：
https://fanyi-api.baidu.com/api/trans/vip/translate
'''

myurl = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
q = "let's I see see"
fromLang = 'en'
toLang = 'zh'
salt = random.randint(32768, 65536)

sign = appid+q+str(salt)+secretKey
#m1 = md5.new()
#m1.update(sign)
m1= hashlib.md5(sign)
sign = m1.hexdigest()
myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign

try:
	response=requests.get(myurl)
	print(response.text)
except Exception, e:
	print e
