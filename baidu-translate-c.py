# -*- coding: utf-8 -*-

import requests
import httplib, urllib
import hashlib
import random

'''
翻译API HTTP地址：
http://api.fanyi.baidu.com/api/trans/vip/translate
翻译API HTTPS地址：
https://fanyi-api.baidu.com/api/trans/vip/translate
'''

class Fanyi:

	appid = '20151113000005349'
	secretKey = 'osubCEzlGjzvw8qdQc41'

	def __init__(self, q):
		self.q=q

		myurl = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
		fromLang = 'auto'
		toLang = 'en'
		salt = random.randint(32768, 65536)
		sign = self.appid+self.q+str(salt)+self.secretKey
		m1= hashlib.md5(sign)
		sign = m1.hexdigest()
		myurl = myurl+'?appid='+self.appid+'&q='+urllib.quote(self.q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
		
		try:
			response=requests.get(myurl)
			print(response.text)
		except Exception, e:
			print e

aa=Fanyi("巨大身躯，穿着破烂短裤的浩克。还有那高举雷神之锤，一身电弧环绕的雷神索尔。更别提那美艳无双的黑寡妇了\n复仇者联盟的人物应有尽有，每个人脚下都有着相应的小星星。显示着游戏推荐程度。这是让夏天非常感兴趣的，因为，这款单机游戏，不仅仅让你可以在vr眼镜中尽情的体验虚拟现实世界，让你身临其境，过一把当超级英雄的瘾。甚至，这100多个人物大部分人都有着人物自身的相应剧情。这也就证明着，夏天可以扮演美国队长，去体验一下二战的残酷。也可以扮演钢铁侠，在现代繁华的纽约夜夜笙歌。")